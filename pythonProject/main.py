import subprocess
from aiogram import Dispatcher, F
from aiogram.filters import Command
from dotenv import load_dotenv
from handlers.start import *
from handlers.register import *
from handlers.create import *
from handlers.send_msg import *
from handlers.user_info import *
from utils.commands import set_commands
from filters.CheckUser import CheckUser
from filters.CheckAdmin import CheckAdmin

import logging

logging.basicConfig(level=logging.INFO, filename='bot_log.log',
                    format="[%(asctime)s] - [%(levelname)s] - [%(funcName)s: %(lineno)d - %(message)s]",
                    datefmt='%d-%m-%y %H:%M:%S')

load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()


async def start_bot(bot: Bot):
    await bot.send_message(1443421597, text='👉 Бота запущено! 👈')


dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands='start'))
dp.message.register(get_help, Command(commands='help'))
dp.message.register(clear, Command(commands='clear'), CheckUser())

dp.message.register(start_register, F.text == '👉 Зареєструватися в базі 👈')
dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_phone, RegisterState.regPhone)

dp.message.register(create_jalousie, F.text == '🔹 Жалюзі', CheckUser())
dp.callback_query.register(jalousie_type, CreateState.jalousie_type)
dp.callback_query.register(jalousie_control, CreateState.jalousie_control)
dp.callback_query.register(jalousie_fix, CreateState.jalousie_fix)
dp.callback_query.register(select_jalousie, CreateState.jalousie)
dp.message.register(jalousie_number, CreateState.jalousie_number)
dp.message.register(jalousie_hor_size, CreateState.jalousie_hor_size)
dp.message.register(jalousie_vert_size, CreateState.jalousie_vert_size)
dp.callback_query.register(jalousie_order, CreateState.jalousie_order)
dp.message.register(create_windowsill, F.text == '🔸 Підвіконня', CheckUser())
dp.callback_query.register(windowsill_colour, CreateState.windowsill_colour)
dp.callback_query.register(select_windowsill, CreateState.windowsill)
dp.message.register(number_windowsills, CreateState.windowsill_number)
dp.callback_query.register(windowsill_plug, CreateState.windowsill_plug)
dp.message.register(windowsill_size, CreateState.windowsill_size)
dp.callback_query.register(windowsill_order, CreateState.windowsill_order)
dp.message.register(create_mosquito, F.text == '🔹 Москітка', CheckUser())
dp.callback_query.register(mosquito_type, CreateState.mosquito_type)
dp.callback_query.register(select_mosquito, CreateState.mosquito)
dp.message.register(number_mosquito, CreateState.mosquito_number)
dp.message.register(mosquito_hor_size, CreateState.hor_size_mosquito)
dp.message.register(mosquito_vert_size, CreateState.vert_size_mosquito)
dp.callback_query.register(mosquito_order, CreateState.mosquito_order)
dp.message.register(create_reflux, F.text == '🔸 Відлив', CheckUser())
dp.callback_query.register(reflux_type, CreateState.reflux_type)
dp.callback_query.register(select_reflux, CreateState.reflux)
dp.message.register(number_reflux, CreateState.reflux_number)
dp.message.register(reflux_size, CreateState.reflux_size)
dp.callback_query.register(reflux_order, CreateState.reflux_order)
dp.message.register(create_glazing, F.text == '🔹 Склопакет', CheckUser())
dp.callback_query.register(glazing_type, CreateState.glazing_type)
dp.callback_query.register(select_glazing, CreateState.glazing)
dp.message.register(number_glazing, CreateState.glazing_number)
dp.message.register(glazing_hor_size, CreateState.hor_size_glazing)
dp.message.register(glazing_vert_size, CreateState.vert_size_glazing)
dp.callback_query.register(glazing_order, CreateState.glazing_order)
dp.message.register(user_disc, F.text == '🤑 Моя знижка', CheckUser())
dp.message.register(select_table, F.text == '📌 Статус замовлення', CheckUser())
dp.callback_query.register(select_order, CreateState.select_table)
dp.message.register(order_info, CreateState.order_info)
dp.message.register(select_order_tables, F.text == '📋 Мої замовлення', CheckUser())
dp.callback_query.register(user_orders, CreateState.order_table)

dp.message.register(create_message, Command(commands='send'), CheckAdmin())
dp.message.register(send_all_message, CreateState.text_msg)
dp.message.register(create_message_for_one, Command(commands='send_1'), CheckAdmin())
dp.callback_query.register(select_one_user, CreateState.text_msg_one)
dp.message.register(send_message_for_one, CreateState.select_user)
dp.message.register(create_message_for_admin, Command(commands='mail'), CheckUser())
dp.message.register(send_message_for_admin, CreateState.user_text_msg)


async def get_installed_packages():
    result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').split('\n')
    with open('requirements.txt', 'w') as file:
        for line in output:
            file.write(line + '\n')


async def start():
    await set_commands(bot)
    await get_installed_packages()
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
