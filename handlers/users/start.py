from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.private_chat import IsPrivate
from loader import dp
from utils.db_api.baza import send_ex
from aiogram.dispatcher import FSMContext
import sqlite3

@dp.message_handler(IsPrivate(),CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.from_user.full_name

    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        user_id INTEGER UNIQUE,
        full_name TEXT
    )
    """
    send_ex(create_table_query)
    
    try:	
        insert_user_query = f"INSERT INTO users (user_id, full_name) VALUES ({user_id}, '{full_name}')"
        send_ex(insert_user_query)
        await message.answer(f"Hello, {full_name}. Ask your questions\n\n<b>@UZ_CHATGPT</b>")
                            
        await state.finish()
    except Exception as err:
        print(err)
        await message.answer(f"Hello, {full_name}. Ask your questions\n\n<b>@UZ_CHATGPT</b>")
        await state.finish()