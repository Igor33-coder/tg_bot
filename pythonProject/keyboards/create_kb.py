import sqlite3
import os
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.database import Database


def jalousie_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    jalousie_button = db.db_select_all('art_jalousie')
    kb = InlineKeyboardBuilder()
    for jalousie in jalousie_button:
        kb.button(text=f'{jalousie[1]}', callback_data=f'{jalousie[2]}')
    kb.adjust(2)
    return kb.as_markup()


def jalousie_hor_16_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    jalousie_button = db.db_select_all('jalousie_h16')
    kb = InlineKeyboardBuilder()
    for jalousie in jalousie_button:
        kb.button(text=f'{jalousie[1]}', callback_data=f'{jalousie[1]}')
    kb.adjust(3)
    return kb.as_markup()


def jalousie_hor_25_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    jalousie_button = db.db_select_all('jalousie_h25')
    kb = InlineKeyboardBuilder()
    for jalousie in jalousie_button:
        kb.button(text=f'{jalousie[1]}', callback_data=f'{jalousie[1]}')
    kb.adjust(3)
    return kb.as_markup()


def jalousie_vert_89_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    jalousie_button = db.db_select_all('jalousie_v89')
    kb = InlineKeyboardBuilder()
    for jalousie in jalousie_button:
        kb.button(text=f'{jalousie[1]}', callback_data=f'{jalousie[1]}')
    kb.adjust(2)
    return kb.as_markup()


def jalousie_vert_127_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    jalousie_button = db.db_select_all('jalousie_v127')
    kb = InlineKeyboardBuilder()
    for jalousie in jalousie_button:
        kb.button(text=f'{jalousie[1]}', callback_data=f'{jalousie[1]}')
    kb.adjust(2)
    return kb.as_markup()


def jalousie_hor_control():
    kb = InlineKeyboardBuilder()
    kb.button(text=f'🔹 Праве', callback_data='hor_right')
    kb.button(text=f'🔸 Ліве', callback_data='hor_left')
    kb.adjust(2)
    return kb.as_markup()


def jalousie_vert_control():
    kb = InlineKeyboardBuilder()
    kb.button(text=f'🔹 До середини', callback_data='vert_type_1')
    kb.button(text=f'🔸 В різні боки', callback_data='vert_type_2')
    kb.button(text=f'🔹 В один бік', callback_data='vert_type_3')
    kb.adjust(2)
    return kb.as_markup()


def jalousie_hor_fix():
    db = Database(os.getenv("DATABASE_NAME"))
    jalousie_button = db.db_select_all('jalousie_hor_fix')
    kb = InlineKeyboardBuilder()
    for jalousie in jalousie_button:
        kb.button(text=f'{jalousie[1]}', callback_data=f'{jalousie[1]}')
    kb.adjust(2)
    return kb.as_markup()


def jalousie_vert_fix():
    db = Database(os.getenv("DATABASE_NAME"))
    jalousie_button = db.db_select_all('jalousie_vert_fix')
    kb = InlineKeyboardBuilder()
    for jalousie in jalousie_button:
        kb.button(text=f'{jalousie[1]}', callback_data=f'{jalousie[1]}')
    kb.adjust(2)
    return kb.as_markup()


def glazing_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    glazing_button = db.db_select_all('art_glazing')
    kb = InlineKeyboardBuilder()
    for glazing in glazing_button:
        kb.button(text=f'{glazing[1]}', callback_data=f'{glazing[2]}')
    kb.adjust(2)
    return kb.as_markup()


def glazing_24_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    glazing_button = db.db_select_all('glazing_24')
    kb = InlineKeyboardBuilder()
    for glazing in glazing_button:
        kb.button(text=f'{glazing[1]}', callback_data=f'{glazing[2]}')
    kb.adjust(2)
    return kb.as_markup()


def glazing_32_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    glazing_button = db.db_select_all('glazing_32')
    kb = InlineKeyboardBuilder()
    for glazing in glazing_button:
        kb.button(text=f'{glazing[1]}', callback_data=f'{glazing[2]}')
    kb.adjust(2)
    return kb.as_markup()


def glazing_40_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    glazing_button = db.db_select_all('glazing_40')
    kb = InlineKeyboardBuilder()
    for glazing in glazing_button:
        kb.button(text=f'{glazing[1]}', callback_data=f'{glazing[2]}')
    kb.adjust(2)
    return kb.as_markup()


def windowsill_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    windowsill_button = db.db_select_all('art_windowsill')
    kb = InlineKeyboardBuilder()
    for windowsill in windowsill_button:
        kb.button(text=f'{windowsill[1]}', callback_data=f'{windowsill[2]}')
    kb.adjust(1)
    return kb.as_markup()


def windowsill_white_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    windowsill_button = db.db_select_all('windowsill_white')
    kb = InlineKeyboardBuilder()
    for windowsill in windowsill_button:
        kb.button(text=f'{windowsill[1]}', callback_data=f'{windowsill[1]}')
    kb.adjust(3)
    return kb.as_markup()


def windowsill_gold_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    windowsill_button = db.db_select_all('windowsill_gold')
    kb = InlineKeyboardBuilder()
    for windowsill in windowsill_button:
        kb.button(text=f'{windowsill[1]}', callback_data=f'{windowsill[1]}')
    kb.adjust(3)
    return kb.as_markup()


def windowsill_plug_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    windowsill_plug_button = db.db_select_all('windowsill_plug_white')
    kb = InlineKeyboardBuilder()
    for windowsill_plug in windowsill_plug_button:
        kb.button(text=f'{windowsill_plug[1]}', callback_data=f'{windowsill_plug[1]}')
    kb.adjust(3)
    return kb.as_markup()


def reflux_type_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    reflux_button = db.db_select_all('art_reflux')
    kb = InlineKeyboardBuilder()
    for reflux in reflux_button:
        kb.button(text=f'{reflux[1]}', callback_data=f'{reflux[2]}')
    kb.adjust(2)
    return kb.as_markup()


def reflux_kb():
    kb = InlineKeyboardBuilder()
    for i in range(50, 471, 10):
        kb.button(text=f'{str(i)} мм', callback_data=f'{i}')
    kb.adjust(5)
    return kb.as_markup()


def mosquito_type_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text=f'🔹 Внутрішня', callback_data='inside')
    kb.button(text=f'🔸 Зовнішня', callback_data='outside')
    kb.adjust(2)
    return kb.as_markup()


def mosquito_inside_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    mosquito_button = db.db_select_all('art_mosquito_inside')
    kb = InlineKeyboardBuilder()
    for mosquito in mosquito_button:
        kb.button(text=f'{mosquito[1]}', callback_data=f'{mosquito[2]}')
    kb.adjust(2)
    return kb.as_markup()


def mosquito_outside_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    mosquito_button = db.db_select_all('art_mosquito_outside')
    kb = InlineKeyboardBuilder()
    for mosquito in mosquito_button:
        kb.button(text=f'{mosquito[1]}', callback_data=f'{mosquito[2]}')
    kb.adjust(2)
    return kb.as_markup()


def confirm_button_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='✅ Підтвердити ✅', callback_data='confirm_order')
    kb.adjust()
    return kb.as_markup()


def users_kb():
    db = Database(os.getenv("DATABASE_NAME"))
    users_button = db.db_select_all('users')
    kb = InlineKeyboardBuilder()
    for user in users_button:
        kb.button(text=f'{user[1]}', callback_data=f'{user[1]}')
    kb.adjust(3)
    return kb.as_markup()


def tables_kb():
    conn = sqlite3.connect('orders_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    conn.commit()
    table_names = cursor.fetchall()
    kb = InlineKeyboardBuilder()
    for table in table_names:
        kb.button(text=f'{table[0]}', callback_data=f'{table[0]}')
    kb.adjust(3, 2)
    return kb.as_markup()
