from aiogram import Bot
from aiogram.types import Message
from keyboards.register_kb import register_keyboard
from keyboards.profile_kb import profile_kb
from utils.database import Database
import os


async def get_start(message: Message, bot: Bot):
    dp = Database(os.getenv('DATABASE_NAME'))
    users = dp.select_user_id(message.from_user.id)
    if users:
        await bot.send_message(message.from_user.id, f'Доброго дня {users[1]} 👋\n', reply_markup=profile_kb())
    else:
        await bot.send_message(message.from_user.id, f'Привіт 👋!\n'
                                                     f'Я Бот фірми ВікнаСвіт 🤖', reply_markup=register_keyboard())


async def get_help(message: Message, bot: Bot):
    dp = Database(os.getenv('DATABASE_NAME'))
    users = dp.select_user_id(message.from_user.id)
    if users:
        await bot.send_message(message.from_user.id, f'Доброго дня {users[1]} 👋\n'
                                                     f'Графік роботи фірми:\n'
                                                     f'🆚ПН-ПТ: 8.00 - 18.00\n🆚СБ-НД: 9.00 - 13.00\n'
                                                     f'Телефони для довідок:\n🆚 0666907733\n🆚 0968827844\n🆚 0503044108',
                               reply_markup=profile_kb())
    else:
        await bot.send_message(message.from_user.id, f'Привіт 👋!\n'
                                                     f'Я Бот фірми ВікнаСвіт 🤖', reply_markup=register_keyboard())
