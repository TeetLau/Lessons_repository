import requests
import time


api_url = 'https://api.telegram.org/bot'
api_cats_url = ' https://api.thecatapi.com/v1/images/search'
token = '7191379342:AAG_JBJ5r_hmaNN_BSiUhgcPAAcO4DGt5nw'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('

offset = -2
counter = 0
cat_response: requests.Response
cat_link: str

while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{api_url}{token}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(api_cats_url)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{api_url}{token}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1