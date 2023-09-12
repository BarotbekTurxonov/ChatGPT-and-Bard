import requests

endpoint = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'


async def chatgpt(text):
    

    if not text:
        print('Please enter text parameter')
        return

    headers = {
        'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/16.3.1 hw/iPhone12_5',
        'Accept-Language': 'ar',
        'Content-Type': 'application/json; charset=UTF-8'
    }

    try:
        response = requests.post(endpoint, json={"data": {"message": text}}, headers=headers)
        result = response.json()['result']['choices'][0]['text']
        return result
    except Exception as e:
        return None


