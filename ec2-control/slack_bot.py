from slacker import Slacker
from call_token import *
from aws_control import *
import json
import asyncio
import websockets
import os


token = return_token('slack')
slack = Slacker(token)

response = slack.rtm.start()
message_url = response.body['url']


def filter_message(message_json):
    message = json.loads(message_json)
    return_message = False

    if message['type'] == 'message' and not('subtype' in message):
        text = message['text']

        if text == 'start':
            return_message = server_start()
        elif text == 'stop':
            return_message = server_stop()
        elif text == 'status':
            return_message = server_status()
        else:
            pass

    else:
        pass

    return return_message


async def get_message():
    message_ws = await websockets.connect(message_url)

    while True:
        message_json = await message_ws.recv()
        return_message = filter_message(message_json)
        if return_message:
            slack.chat.post_message('#general', return_message, as_user=True)

try:
    slack.chat.post_message('#general', 'Hello, There!', as_user=True)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.get_event_loop().run_until_complete(get_message())
    asyncio.get_event_loop().run_forever()

except:
    slack.chat.post_message('#general', 'WARNING!', as_user=True)
    slack.chat.post_message('#general', 'Server will reboot', as_user=True)
    os.system('sudo reboot now')
