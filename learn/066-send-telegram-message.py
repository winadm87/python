# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import requests

def send_to_telegram(message):

    apiToken = 'place_bot_id_here' # create a bot with botfather and copy bot id here
    chatID = '-place_tg_group_id_here' # create a group in tg, add to group https://t.me/RawDataBot, on the connect it will show group id
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram("Hello from Python!")

def send_to_telegram_image(image):

    apiToken = 'place_bot_id_here'
    chatID = '-place_tg_group_id_here'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendPhoto'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'photo': image})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram_image("https://en.wikipedia.org/static/images/project-logos/enwiki.png")