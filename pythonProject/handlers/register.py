import re
import os
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.profile_kb import profile_kb
from state.register import RegisterState
from utils.database import Database


async def start_register(message: Message, state: FSMContext, bot: Bot):
    dp = Database(os.getenv('DATABASE_NAME'))
    users = dp.select_user_id(message.from_user.id)
    if users:
        await bot.send_message(message.from_user.id, f'☝️ {users[1]}\n'
                                                     f'Ви вже зареєстровані! ☝️')
    else:
        await bot.send_message(message.from_user.id, f'Давай знайомитися! 🖖\n'
                                                     f"Для початку вкажіть ім'я та прізвище 👇")
        await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Приємно познайомитися {message.text}! ✌️\n'
                                                 f'Тепер вкажіть номер 📱 у форматі +380xxxxxxxxx\n'
                                                 f'⚠️ Обережно!⚠️ Я чутливий до формату!')

    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regPhone)


async def register_phone(message: Message, state: FSMContext, bot: Bot):
    pattern = re.compile(r'^\+\d{12}$')
    if re.match(pattern, message.text.replace(' ', '')) and message.text.replace('+', '').isdigit():
        await state.update_data(regphone=message.text)
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')
        msg = (f'Приємно познайомитися {reg_name} 👋!\n'
               f'Ваш телефон: {reg_phone} ☎️\n'
               f'Для початку Ваша знижка 5% 🤑. Вона буде відкоригована на протязі дня.')
        await bot.send_message(message.from_user.id, msg, reply_markup=profile_kb())
        db = Database(os.getenv('DATABASE_NAME'))
        db.add_user(reg_name, reg_phone, message.from_user.id)
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, f'❗️Невірно вказаний номер!❗️')
