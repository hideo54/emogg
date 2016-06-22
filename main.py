import time
import json
import RPi.GPIO as GPIO
from slackclient import SlackClient

# Slack
token = json.load(open('config.json'))['token']
print(token)
sc = SlackClient(token)

# Buttons
reactions = json.load(open('config.json'))['reactions']
GPIO.setmode(GPIO.BOARD)
GPIO.setup(list(map(int, reactions.keys())), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def add_selected_reactions(sc, channel_id, ts):
    for button in list(map(int, reactions.keys())):
        if GPIO.input(button):
            reaction = reactions[button]
            sc.api_call('reactions.add', name=reaction, channel=channel_id, timestamp=ts)

if sc.rtm_connect():
    latest_message = None
    while True:
        res = sc.rtm_read()
        for item in res:
            item_type = item.get('type')
            if item_type == 'hello':
                print('Connected successfully.')
            elif item_type == 'message':
                if latest_message != item:
                    latest_message = item
            else:
                pass
        if latest_message is not None:
            add_selected_reactions(sc, latest_message['channel'], latest_message['ts'])
        time.sleep(1)
else:
    print('Connection failed.')
