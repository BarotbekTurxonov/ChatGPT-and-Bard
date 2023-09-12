from aiogram import types
from filters.group_chat import IsGroup
from filters.private_chat import IsPrivate
from loader import dp,bot
from BingImageCreator import ImageGen
from aiogram.types import InputMediaPhoto
from bardapi import Bard
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



@dp.message_handler(IsGroup(), commands=['gpt'])
async def gpt_reply(msg: types.Message):
    args = msg.get_args()
    if args:
        gpt_response = await chatgpt(args)
        if gpt_response is not None:
            await msg.reply(gpt_response)
        else:
            await msg.reply("Something went wrong!!!")
    else:
        await msg.reply("Usage:  <code>/gpt &lt;your question&gt; </code>", parse_mode='html')


@dp.message_handler(IsPrivate(), commands=['gpt'])
async def gpt_reply(msg: types.Message):
    args = msg.get_args()
    if args:
        gpt_response = await chatgpt(args)
        if gpt_response is not None:
            await msg.reply(gpt_response)
        else:
            await msg.reply("Something went wrong!!!")
    else:
        await msg.reply("Usage:  <code>/gpt &lt;your question&gt; </code>", parse_mode='html')



################### GOOOGLE BARD  ##########################

from Bard import AsyncChatbot

Secure_1PSID = "agjLcBj7DAV5x9DSmJATjKSKxsXxh5cGBGn9FrLsv8OM33nnT3mqEe93UguxYWocbzA80A."
Secure_1PSIDTS = "sidts-CjEBSAxbGQ9H9CUxH2djfRumLgF6eAOo8S1wQ-0IA382Y6slrEY2_IAg-QEGzGf_z7QiEAA"

async def bard_gpt(context):
    chatbot = await AsyncChatbot.create(Secure_1PSID, Secure_1PSIDTS)
    response = await chatbot.ask(context)
    return (response['content'])


@dp.message_handler(IsGroup(),commands=['bard'])
async def bard_api(msg: types.Message):
    args = msg.get_args()
    if args:
        try:
            result = await bard_gpt(args)
            await msg.reply(result)
        except Exception as err:
            await msg.reply(err)
    else:
        await msg.reply("Usage:  <code>/bard &lt;your question&gt; </code>", parse_mode='html')




@dp.message_handler(IsPrivate(),commands=['bard'])
async def bard_api(msg: types.Message):
    args = msg.get_args()
    if args:
        try:
            result = await bard_gpt(args)
            await msg.reply(result)
        except Exception as err:
            await msg.reply(err)
    else:
        await msg.reply("Usage:  <code>/bard &lt;your question&gt; </code>", parse_mode='html')




