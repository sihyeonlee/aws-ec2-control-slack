from slacker import Slacker
from call_token import *
import json
import asyncio
import websockets

token = return_token('slack')               # Get Slack Token
slack = Slacker(token)

response = slack.rtm.start()                # Start RTM
message_url = response.body['url']


def filter_message(message_json):           # Filtering Message & Parsing
    message = json.loads(message_json)

    if message['type'] == 'message':
        text = message['text']

        if text == 'start':
            pass                            # Start_Instance
        elif text == 'kill':
            pass                            # Stop_Instance
        elif text == 'status':
            pass                            # Return_Instance_Status
        else:
            pass                            # Return_Nothing

    else:
        pass                                # Return_Nothing


async def get_message():
    message_ws = await websockets.connect(message_url)

    while True:
        message_json = await message_ws.recv()
        filter_message(message_json)


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
asyncio.get_event_loop().run_until_complete(get_message())
asyncio.get_event_loop().run_forever()
