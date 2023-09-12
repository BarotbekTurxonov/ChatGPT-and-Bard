from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters.private_chat import IsPrivate
from loader import dp


@dp.message_handler(CommandHelp(), IsPrivate())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))