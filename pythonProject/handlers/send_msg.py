import os
import asyncio
import sqlite3
from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from state.create import CreateState
from aiogram.fsm.context import FSMContext
from keyboards.create_kb import users_kb


async def create_message(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await bot.send_message(message.from_user.id, f'Привіт адмін. Надрукуй текст ✍️')
    await state.set_state(CreateState.text_msg)


async def send_all_message(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(text_msg=message.text)
    mail_id = message.from_user.id
    user_name = message.from_user.full_name
    text = message.text
    with sqlite3.connect('tgbot_db.db') as con:
        cursor = con.cursor()
        cursor.execute('SELECT telegram_id FROM users')
        users = cursor.fetchall()
        con.commit()
    for user_id in users:
        if int(user_id[0]) != mail_id:
            await bot.send_message(int(user_id[0]), f'Від {user_name}:\n'
                                                    f'{text}')
            await asyncio.sleep(0.33)
    await state.clear()


async def create_message_for_admin(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await bot.send_message(message.from_user.id, f'Повідомлення для адміністратора ✍️')
    await state.set_state(CreateState.user_text_msg)


async def send_message_for_admin(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(user_text_msg=message.text)
    text = message.text
    user_name = message.from_user.full_name
    admin_ids_str = os.getenv('ADMIN_ID', '')
    admin_ids = admin_ids_str.split(',') if admin_ids_str else []
    for admin_id in admin_ids:
        await bot.send_message(admin_id, f'Від {user_name}:\n'
                                         f'{text}')
    await state.clear()


async def create_message_for_one(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await bot.send_message(message.from_user.id, f'Привіт адмін. Обери диллера ⬇️', reply_markup=users_kb())
    await state.set_state(CreateState.text_msg_one)


async def select_one_user(call: CallbackQuery, state: FSMContext):
    await state.update_data(select_one_user=call.data)
    await call.message.answer(f'Надрукуй текст ✍️')
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.select_user)


async def send_message_for_one(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(text_msg_one=message.text)
    create_data = await state.get_data()
    user = create_data.get('select_one_user')
    adm_name = message.from_user.full_name
    text = message.text
    with sqlite3.connect('tgbot_db.db') as con:
        cursor = con.cursor()
        cursor.execute('SELECT user_name FROM users')
        users = cursor.fetchall()
        con.commit()
    usernames = [name[0] for name in users]

    for username in usernames:
        if username == user:
            with sqlite3.connect('tgbot_db.db') as con:
                cursor = con.cursor()
                cursor.execute('SELECT telegram_id, user_name FROM users WHERE user_name == ?', (user,))
                user_id = cursor.fetchone()
                con.commit()
            await bot.send_message(int(user_id[0]), f'Від {adm_name}:\n{text}')
    await state.clear()
