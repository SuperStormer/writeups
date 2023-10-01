from flask import Flask, request, send_file, make_response
import threading

app = Flask(__name__)

@app.route("/font.woff")
def font():
	resp = make_response(send_file("font.woff"))
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp

app.run(port=8000)