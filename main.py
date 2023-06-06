from credentials import mobile_number
import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Hey, You can do it!',
        'key': 'textbelt'
    })
    print(resp.json())

schedule.every(5).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)