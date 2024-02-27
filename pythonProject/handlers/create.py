from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.create_kb import *
from keyboards.profile_kb import profile_kb
from state.create import CreateState


async def create_jalousie(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    await bot.send_message(message.from_user.id, f'⬇️ Оберіть тип жалюзі ⬇️', reply_markup=jalousie_kb())
    await state.set_state(CreateState.jalousie_type)


async def jalousie_type(call: CallbackQuery, state: FSMContext):
    jalousie_options = {
        'hor_16': jalousie_hor_16_kb(),
        'hor_25': jalousie_hor_25_kb(),
        'vert_89': jalousie_vert_89_kb(),
        'vert_127': jalousie_vert_127_kb()
    }

    await state.update_data(jalousie_type=call.data)
    create_data = await state.get_data()
    user_table = create_data.get('jalousie_type')

    if user_table in jalousie_options:
        await call.message.answer(f'⬇️ Оберіть колір ⬇️', reply_markup=jalousie_options[user_table])
        await call.message.edit_reply_markup(reply_markup=None)
        await call.answer()
        await state.set_state(CreateState.jalousie_control)
    else:
        await call.message.answer("❌ Неправильний вибір! ❌")


async def jalousie_control(call: CallbackQuery, state: FSMContext):
    jalousie_control_options = {
        'hor_16': jalousie_hor_control(),
        'hor_25': jalousie_hor_control(),
        'vert_89': jalousie_vert_control(),
        'vert_127': jalousie_vert_control()
    }

    await state.update_data(jalousie_colour=call.data)
    create_data = await state.get_data()
    user_table = create_data.get('jalousie_type')

    if user_table in jalousie_control_options:
        await call.message.answer(f'⬇️ Оберіть тип керування ⬇️', reply_markup=jalousie_control_options[user_table])
        await call.message.edit_reply_markup(reply_markup=None)
        await call.answer()
        await state.set_state(CreateState.jalousie_fix)
    else:
        await call.message.answer("❌ Неправильний вибір! ❌")


async def jalousie_fix(call: CallbackQuery, state: FSMContext):
    jalousie_fix_options = {
        'hor_16': jalousie_hor_fix(),
        'hor_25': jalousie_hor_fix(),
        'vert_89': jalousie_vert_fix(),
        'vert_127': jalousie_vert_fix()
    }

    await state.update_data(jalousie_control=call.data)
    create_data = await state.get_data()
    user_table = create_data.get('jalousie_type')

    if user_table in jalousie_fix_options:
        await call.message.answer(f'⬇️ Оберіть тип фіксації ⬇️', reply_markup=jalousie_fix_options[user_table])
        await call.message.edit_reply_markup(reply_markup=None)
        await call.answer()
        await state.set_state(CreateState.jalousie)
    else:
        await call.message.answer("❌ Неправильний вибір! ❌")


async def select_jalousie(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Вкажіть кількість (до 20 штук) ⚠️')
    await state.update_data(jalousie_fix=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.jalousie_number)


async def jalousie_number(message: Message, state: FSMContext, bot: Bot):
    if message.text.isdigit() and 1 <= int(message.text) <= 20:
        await bot.send_message(message.from_user.id, f'Вкажіть ширину в мм ⚠️')
        await state.update_data(jalousie_number=message.text)
        await state.set_state(CreateState.jalousie_hor_size)
    else:
        await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')


async def jalousie_hor_size(message: Message, state: FSMContext, bot: Bot):
    jalousie_vert_size_options = {
        'hor_16': (280, 2021),
        'hor_25': (280, 2021),
        'vert_89': (450, 4500),
        'vert_127': (450, 4500)
    }

    create_data = await state.get_data()
    user_table = create_data.get('jalousie_type')

    if user_table in jalousie_vert_size_options:
        min_value, max_value = jalousie_vert_size_options[user_table]
        if message.text.isdigit() and min_value <= int(message.text) <= max_value:
            await bot.send_message(message.from_user.id, 'Тепер вкажіть висоту в мм ⚠️️')
            await state.update_data(jalousie_hor_size=message.text)
            await state.set_state(CreateState.jalousie_vert_size)
        else:
            await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')
    else:
        await bot.send_message(message.from_user.id, "❌ Неправильний вибір! ❌")


async def jalousie_vert_size(message: Message, state: FSMContext, bot: Bot):
    furniture_type_ua = {
        'hor_16': 'Горизонтальні 16 мм',
        'hor_25': 'Горизонтальні 25 мм',
        'vert_89': 'Вертикальні 89 мм',
        'vert_127': 'Вертикальні 127 мм'
    }

    control_ua_map = {
        'hor_left': 'Ліве',
        'hor_right': 'Праве',
        'vert_type_1': 'До середини',
        'vert_type_2': 'В різні боки',
        'vert_type_3': 'В один бік'
    }
    create_data = await state.get_data()
    user_table = create_data.get('jalousie_type')
    colour = create_data.get('jalousie_colour')
    control = create_data.get('jalousie_control')
    fix = create_data.get('jalousie_fix')
    num = create_data.get('jalousie_number')
    hor_size = create_data.get('jalousie_hor_size')

    user_table_ua = furniture_type_ua.get(user_table, '')

    control_ua = control_ua_map.get(control, '')

    user_id = message.from_user.id

    if user_table in ['hor_16', 'hor_25']:
        size_range = (100, 2800)
        if message.text.isdigit() and size_range[0] <= int(message.text) <= size_range[1]:
            await state.update_data(jalousie_vert_size=message.text)
            create_data = await state.get_data()
            vert_size = create_data.get('jalousie_vert_size')
            square = round(((int(hor_size) / 1000) * (int(vert_size) / 1000)), 3)

            message_text = (f'🔹 Ви обрали - {user_table_ua}\n'
                            f'🔸 Колір - {colour}\n'
                            f'🔹 Тип управління - {control_ua}\n'
                            f'🔸 Тип фіксації - {fix}\n'
                            f'🔹 Кількість - {num} шт\n'
                            f'🔸 Ширина - {hor_size} мм\n'
                            f'🔹 Висота - {vert_size} мм\n')

            if user_table == 'hor_16':
                with sqlite3.connect('tgbot_db.db') as con:
                    cursor = con.cursor()
                    cursor.execute('SELECT price, art FROM jalousie_h16 WHERE art == ?', (colour,))
                    table_1 = cursor.fetchone()
                    con.commit()
            elif user_table == 'hor_25':
                with sqlite3.connect('tgbot_db.db') as con:
                    cursor = con.cursor()
                    cursor.execute('SELECT price, art FROM jalousie_h25 WHERE art == ?', (colour,))
                    table_1 = cursor.fetchone()
                    con.commit()
            with sqlite3.connect('tgbot_db.db') as con:
                cursor.execute('SELECT price, art FROM jalousie_hor_fix WHERE art == ?', (fix,))
                table_2 = cursor.fetchone()
                con.commit()

            if square <= 0.6:
                price = ((table_1[0] * 0.6) + table_2[0]) * int(num)
                price = round(price, 2)
            else:
                price = ((square * table_1[0]) + table_2[0]) * int(num)
                price = round(price, 2)

            with sqlite3.connect('tgbot_db.db') as con:
                cursor = con.cursor()
                cursor.execute('SELECT discount, telegram_id FROM users WHERE telegram_id == ?', (user_id,))
                res = cursor.fetchone()
                con.commit()

            disc_price = price - ((int(res[0]) / 100) * price)
            disc_price = round(disc_price, 2)

            await bot.send_message(message.from_user.id, message_text)
            await bot.send_message(message.from_user.id, f'💰 Ціна - {price}💰')
            await bot.send_message(message.from_user.id, f'💰 Ваша ціна - {disc_price} 💰', reply_markup=profile_kb())
            await bot.send_message(message.from_user.id, f'👇 Натисніть для підтвердження 👇',
                                   reply_markup=confirm_button_kb())
            await state.set_state(CreateState.jalousie_order)
        else:
            await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')
    elif user_table in ['vert_89', 'vert_127']:
        size_range = (200, 4500)
        if message.text.isdigit() and size_range[0] <= int(message.text) <= size_range[1]:
            await state.update_data(jalousie_vert_size=message.text)
            create_data = await state.get_data()
            vert_size = create_data.get('jalousie_vert_size')
            square = ((int(hor_size) / 1000) * (int(vert_size) / 1000))

            message_text = (f'🔹 Ви обрали - {user_table_ua}\n'
                            f'🔸 Колір - {colour}\n'
                            f'🔹 Тип управління - {control_ua}\n'
                            f'🔸 Тип фіксації - {fix}\n'
                            f'🔹 Кількість - {num} шт\n'
                            f'🔸 Ширина - {hor_size} мм\n'
                            f'🔹 Висота - {vert_size} мм\n')

            if user_table == 'vert_89':
                with sqlite3.connect('tgbot_db.db') as con:
                    cursor = con.cursor()
                    cursor.execute('SELECT price, art FROM jalousie_v89 WHERE art == ?', (colour,))
                    table_1 = cursor.fetchone()
                    con.commit()
            elif user_table == 'vert_127':
                with sqlite3.connect('tgbot_db.db') as con:
                    cursor = con.cursor()
                    cursor.execute('SELECT price, art FROM jalousie_v127 WHERE art == ?', (colour,))
                    table_1 = cursor.fetchone()
                    con.commit()
            with sqlite3.connect('tgbot_db.db') as con:
                cursor.execute('SELECT price, art FROM jalousie_vert_fix WHERE art == ?', (fix,))
                table_2 = cursor.fetchone()
                con.commit()

            if square <= 1.5:
                price = (table_1[0] + table_2[0]) * int(num)
                price = round(price, 2)
            else:
                price = (((square * table_1[0]) / 1.5) + table_2[0]) * int(num)
                price = round(price, 2)

            with sqlite3.connect('tgbot_db.db') as con:
                cursor = con.cursor()
                cursor.execute('SELECT discount, telegram_id FROM users WHERE telegram_id == ?', (user_id,))
                res = cursor.fetchone()
                con.commit()

            disc_price = price - ((int(res[0]) / 100) * price)
            disc_price = round(disc_price, 2)

            await bot.send_message(message.from_user.id, message_text)
            await bot.send_message(message.from_user.id, f'💰 Ціна - {price}💰')
            await bot.send_message(message.from_user.id, f'💰 Ваша ціна - {disc_price} 💰', reply_markup=profile_kb())
            await bot.send_message(message.from_user.id, f'👇 Натисніть для підтвердження 👇',
                                   reply_markup=confirm_button_kb())
            await state.set_state(CreateState.jalousie_order)
        else:
            await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')


async def jalousie_order(call: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(confirm_order=call.data)
    create_data = await state.get_data()
    user_table = create_data.get('jalousie_type')
    user_table_ua = {
        'hor_16': 'Горизонтальні 16 мм',
        'hor_25': 'Горизонтальні 25 мм',
        'vert_89': 'Вертикальні 89 мм',
        'vert_127': 'Вертикальні 127 мм'
    }.get(user_table, '')

    colour = create_data.get('jalousie_colour')
    control = create_data.get('jalousie_control')
    control_ua = {
        'hor_left': 'Ліве',
        'hor_right': 'Праве',
        'vert_type_1': 'До середини',
        'vert_type_2': 'В різні боки',
        'vert_type_3': 'В один бік'
    }.get(control, '')

    fix = create_data.get('jalousie_fix')
    num = create_data.get('jalousie_number')
    hor_size = create_data.get('jalousie_hor_size')
    vert_size = create_data.get('jalousie_vert_size')
    user_id = call.from_user.id

    with sqlite3.connect('tgbot_db.db') as con:
        cursor1 = con.cursor()
        with sqlite3.connect('orders_db.db') as conn:
            cursor2 = conn.cursor()
            cursor1.execute('SELECT telegram_id, user_name, user_phone FROM users')
            data = cursor1.fetchall()
            ids = [int(item[0]) for item in data]
            if user_id in ids:
                cursor1.execute('SELECT user_name, user_phone FROM users WHERE telegram_id == ?', (user_id,))
                data = cursor1.fetchone()
                user_name = data[0]
                user_phone = data[1]
                try:
                    cursor2.execute(
                        'INSERT INTO ЖАЛЮЗІ (Телефон, Імя, Тип, Колір, Управління, Фіксація, Кількість, Ширина,'
                        'Довжина, В_роботі, telegram_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?)',
                        (user_phone, user_name, user_table_ua, colour, control_ua, fix, num, hor_size,
                         vert_size, user_id))
                    order_id = cursor2.lastrowid
                except Exception as e:
                    print(f"Помилка при додаванні замовлення: {e}")
    conn.commit()
    await call.message.answer(f'👍 Ваше замовлення підтверджено! 👍\n'
                              f'Номер замовлення - {order_id}', reply_markup=profile_kb())
    admin_ids_str = os.getenv('ADMIN_ID', '')
    admin_ids = admin_ids_str.split(',') if admin_ids_str else []
    for admin_id in admin_ids:
        await bot.send_message(admin_id, f'💰 Надійшло нове замовлення на 👉 ЖАЛЮЗІ 👈 від {user_name} 💰')
    await state.clear()


async def create_glazing(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    await bot.send_message(message.from_user.id, f'⬇️ Оберіть товщину склопакета ⬇️',
                           reply_markup=glazing_kb())
    await state.set_state(CreateState.glazing_type)


async def glazing_type(call: CallbackQuery, state: FSMContext):
    await state.update_data(glazing_type=call.data)
    create_data = await state.get_data()
    user_table = create_data.get('glazing_type')

    if user_table in ['glazing_24', 'glazing_32', 'glazing_40']:
        await call.message.answer(f'⬇️ Оберіть тип ⬇️', reply_markup=globals()[f'glazing_{user_table[-2:]}_kb']())
        await call.message.edit_reply_markup(reply_markup=None)
        await call.answer()
        await state.set_state(CreateState.glazing)
    elif user_table == 'gl_4':
        await call.message.answer(f'Вкажіть кількість (до 20 штук) ⚠️')
        await call.message.edit_reply_markup(reply_markup=None)
        await call.answer()
        await state.set_state(CreateState.glazing_number)


async def select_glazing(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Вкажіть кількість (до 20 штук) ⚠️')
    await state.update_data(glazing=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.glazing_number)


async def number_glazing(message: Message, state: FSMContext, bot: Bot):
    if message.text.isdigit() and 1 <= int(message.text) <= 20:
        await bot.send_message(message.from_user.id, f'Вкажіть ширину в мм ⚠️')
        await state.update_data(glazing_number=message.text)
        await state.set_state(CreateState.hor_size_glazing)
    else:
        await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')


async def glazing_hor_size(message: Message, state: FSMContext, bot: Bot):
    if message.text.isdigit() and 150 <= int(message.text) <= 2500:
        await bot.send_message(message.from_user.id, 'Тепер вкажіть висоту в мм ⚠️')
        await state.update_data(hor_size_glazing=message.text)
        await state.set_state(CreateState.vert_size_glazing)
    else:
        await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')


async def glazing_vert_size(message: Message, state: FSMContext, bot: Bot):
    if message.text.isdigit():
        vert_size = int(message.text)
        if 150 <= vert_size <= 2500:
            await state.update_data(vert_size_glazing=message.text)
            create_data = await state.get_data()
            glazing = create_data.get('glazing')
            if glazing is None:
                glazing = 'gl_4'
            glazing_dict = {
                'gl_4': 'Скло 4 мм',
                'sp_24': '24 мм',
                'sp_24_en': '24 мм ЕНЕРГО',
                'sp_24_sat': '24 мм САТІН',
                'sp_24_sil': '24 мм БРОНЗА-СРІБЛО',
                'sp_24_br': '24 мм КОРИЧНЕВИЙ МАТ',
                'pvh_24_wh': 'ПВХ БІЛЕ 24 мм',
                'pvh_24_gold': 'ПВХ ЗОЛ. ДУБ 24 мм',
                'pvh_24_nut': 'ПВХ ГОРІХ 24 мм',
                'sp_32': '32 мм',
                'sp_32_en': '32 мм 1 ЕНЕРГО',
                'sp_32_en_2': '32 мм 2 ЕНЕРГО',
                'sp_32_arg': '32 мм + АРГ',
                'sp_32_en_arg': '32 мм 1 ЕНЕРГО + АРГ',
                'sp_32_sat': '32 мм САТІН',
                'sp_32_sil': '32 мм БРОНЗА-СРІБЛО',
                'sp_32_br': '32 мм КОРИЧНЕВИЙ МАТ',
                'pvh_32_wh': 'ПВХ БІЛЕ 32 мм',
                'pvh_32_gold': 'ПВХ ЗОЛ. ДУБ 32 мм',
                'pvh_32_nut': 'ПВХ ГОРІХ 32 мм',
                'sp_40': '40 мм',
                'sp_40_en': '40 мм 1 ЕНЕРГО',
                'sp_40_en_2': '40 мм 2 ЕНЕРГО',
                'sp_40_arg': '40 мм + АРГ',
                'sp_40_en_arg': '40 мм 1 ЕНЕРГО + АРГ',
                'sp_40_sat': '40 мм САТІН',
                'sp_40_sil': '40 мм БРОНЗА-СРІБЛО',
                'sp_40_br': '40 мм КОРИЧНЕВИЙ МАТ',
                'pvh_40_wh': 'ПВХ БІЛЕ 40 мм'
            }
            glazing_ua = glazing_dict.get(glazing, '')
            hor_size = create_data.get('hor_size_glazing')
            vert_size = create_data.get('vert_size_glazing')
            nums = create_data.get('glazing_number')
            square = ((int(hor_size) / 1000) * (int(vert_size) / 1000))
            per = (int(vert_size) / 500) + (int(hor_size) / 500)
            if square < 2.5:
                await bot.send_message(message.from_user.id, f'🔹 Ви обрали - {glazing_ua}\n'
                                                             f'🔸 Кількість - {nums} шт\n'
                                                             f'🔹 Ширина - {hor_size} мм\n'
                                                             f'🔸 Висота - {vert_size} мм\n')

                with sqlite3.connect('tgbot_db.db') as con:
                    cursor_1 = con.cursor()
                    cursor_2 = con.cursor()
                    cursor_1.execute('SELECT price FROM glazing_price')
                    cursor_2.execute('SELECT price FROM profit_work_waste')
                    tab_1 = cursor_1.fetchall()
                    tab_2 = cursor_2.fetchall()
                    con.commit()
                price = 0
                if glazing == 'gl_4':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    work = round(square * tab_2[13][0])
                    price = (sqw_glaz + work) * tab_2[24][0]
                elif glazing == 'sp_24':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    dist_ram = round((per * tab_2[19][0]) * tab_1[10][0], 2)
                    corn = tab_1[13][0] * 4
                    sel_gel = round((per * 0.066) * tab_1[7][0], 2)
                    germ = round((per * 0.072) * tab_1[5][0], 2)
                    byt = round((per * 0.0015) * tab_1[6][0], 2)
                    work = round(tab_2[11][0] + tab_2[12][0] + (tab_2[13][0] * 2), 2)
                    price = ((sqw_glaz * 2) + dist_ram + corn + sel_gel + germ + byt + work) * tab_2[24][0]
                elif glazing == 'sp_24_en':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_en = round((square * tab_2[17][0]) * tab_1[1][0], 2)
                    dist_ram = round((per * tab_2[19][0]) * tab_1[10][0], 2)
                    corn = tab_1[13][0] * 4
                    sel_gel = round((per * 0.066) * tab_1[7][0], 2)
                    germ = round((per * 0.072) * tab_1[5][0], 2)
                    byt = round((per * 0.0015) * tab_1[6][0], 2)
                    work = round(tab_2[11][0] + tab_2[12][0] + ((tab_2[13][0] * 2) + tab_2[14][0]),
                                 2)
                    price = (sqw_glaz + sqw_glaz_en + dist_ram + corn + sel_gel + germ + byt + work) * tab_2[24][0]
                elif glazing == 'sp_24_sat':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_sat = round((square * tab_2[18][0]) * tab_1[2][0], 2)
                    dist_ram = round((per * tab_2[19][0]) * tab_1[10][0], 2)
                    corn = tab_1[13][0] * 4
                    sel_gel = round((per * 0.066) * tab_1[7][0], 2)
                    germ = round((per * 0.072) * tab_1[5][0], 2)
                    byt = round((per * 0.0015) * tab_1[6][0], 2)
                    work = round(tab_2[11][0] + tab_2[12][0] + (tab_2[13][0] * 2), 2)
                    price = (sqw_glaz + sqw_glaz_sat + dist_ram + corn + sel_gel + germ + byt + work) * tab_2[24][0]
                elif glazing == 'sp_24_sil':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_sil = round((square * tab_2[18][0]) * tab_1[3][0], 2)
                    dist_ram = round((per * tab_2[19][0]) * tab_1[10][0], 2)
                    corn = tab_1[13][0] * 4
                    sel_gel = round((per * 0.066) * tab_1[7][0], 2)
                    germ = round((per * 0.072) * tab_1[5][0], 2)
                    byt = round((per * 0.0015) * tab_1[6][0], 2)
                    work = round(tab_2[11][0] + tab_2[12][0] + (tab_2[13][0] * 2), 2)
                    price = (sqw_glaz + sqw_glaz_sil + dist_ram + corn + sel_gel + germ + byt + work) * tab_2[24][0]
                elif glazing == 'sp_24_br':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_br = round((square * tab_2[18][0]) * tab_1[4][0], 2)
                    dist_ram = round((per * tab_2[19][0]) * tab_1[10][0], 2)
                    corn = tab_1[13][0] * 4
                    sel_gel = round((per * 0.066) * tab_1[7][0], 2)
                    germ = round((per * 0.072) * tab_1[5][0], 2)
                    byt = round((per * 0.0015) * tab_1[6][0], 2)
                    work = round(tab_2[11][0] + tab_2[12][0] + (tab_2[13][0] * 2), 2)
                    price = (sqw_glaz + sqw_glaz_br + dist_ram + corn + sel_gel + germ + byt + work) * tab_2[24][0]
                elif glazing == 'pvh_24_wh':
                    sqw_glaz = round((square * tab_2[20][0]) * tab_1[16][0], 2)
                    work = tab_2[26][0]
                    price = (sqw_glaz + work) * tab_2[24][0]
                elif glazing == 'pvh_24_gold':
                    sqw_glaz = round((square * tab_2[23][0]) * tab_1[17][0], 2)
                    work = tab_2[26][0] * 4
                    price = (sqw_glaz + work) * tab_2[24][0]
                elif glazing == 'pvh_24_nut':
                    sqw_glaz = round((square * tab_2[23][0]) * tab_1[18][0], 2)
                    work = tab_2[26][0] * 4
                    price = (sqw_glaz + work) * tab_2[24][0]

                elif glazing == 'sp_32':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[8][0]) * 2, 2)
                    corn = tab_1[11][0] * 8
                    sel_gel = round(((per * 0.08) * tab_1[7][0]), 2)
                    germ = round((per * 0.09) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + (tab_2[13][0] * 3), 2)
                    price = ((sqw_glaz * 3) + dist_ram + corn + sel_gel + germ + byt + work) * tab_2[24][0]
                elif glazing == 'sp_32_en':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_en = round((square * tab_2[17][0]) * tab_1[1][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[8][0]) * 2, 2)
                    corn = tab_1[11][0] * 8
                    sel_gel = round(((per * 0.08) * tab_1[7][0]), 2)
                    germ = round((per * 0.09) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0]) * 2, 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + (tab_2[13][0] * 3) + tab_2[14][0], 2)
                    price = (((sqw_glaz * 2) + sqw_glaz_en + dist_ram + corn + sel_gel + germ + byt + work) *
                             tab_2[24][0])
                elif glazing == 'sp_32_en_2':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_en = round((square * tab_2[17][0]) * tab_1[1][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[8][0] * 2), 2)
                    corn = tab_1[11][0] * 8
                    sel_gel = round(((per * 0.08) * tab_1[7][0]), 2)
                    germ = round((per * 0.09) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + ((tab_2[13][0] * 3) + (tab_2[14][0] * 2)), 2)
                    price = ((sqw_glaz + (sqw_glaz_en * 2) + dist_ram + corn + sel_gel + germ + byt + work) *
                             tab_2[24][0])
                elif glazing == 'sp_32_arg':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[8][0] * 2), 2)
                    corn = round(tab_1[11][0] * 4, 2)
                    corn_arg = round((tab_1[14][0] + tab_1[15][0]) * 4, 2)
                    sel_gel = round((per * 0.08) * tab_1[7][0], 2)
                    germ = round((per * 0.09) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + (tab_2[13][0] * 3) + (tab_2[15][0] * 2),
                                 2)
                    price = ((((sqw_glaz * 3) + dist_ram + corn + corn_arg + sel_gel + germ + byt + work) *
                             tab_2[24][0]) - 45.5)
                elif glazing == 'sp_32_en_arg':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_en = round((square * tab_2[17][0]) * tab_1[1][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[8][0]) * 2, 2)
                    corn = round(tab_1[11][0] * 4, 2)
                    corn_arg = round((tab_1[14][0] + tab_1[15][0]) * 4, 2)
                    sel_gel = round(((per * 0.08) * tab_1[7][0]), 2)
                    germ = round((per * 0.09) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + ((tab_2[13][0] * 3) + tab_2[14][0]) +
                                 (tab_2[15][0] * 2), 2)
                    price = ((((sqw_glaz * 2) + sqw_glaz_en + dist_ram + corn + corn_arg + sel_gel + germ + byt + work)
                              * tab_2[24][0]) - 45.5)
                elif glazing == 'sp_32_sat':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_sat = round((square * tab_2[18][0]) * tab_1[2][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[8][0]) * 2, 2)
                    corn = tab_1[11][0] * 8
                    sel_gel = round((per * 0.08) * tab_1[7][0], 2)
                    germ = round((per * 0.09) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + (tab_2[13][0] * 3), 2)
                    price = (((sqw_glaz * 2) + sqw_glaz_sat + dist_ram + corn + sel_gel + germ + byt + work) *
                             tab_2[24][0])
                elif glazing == 'sp_32_sil':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_sil = round((square * tab_2[18][0]) * tab_1[3][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[8][0]) * 2, 2)
                    corn = tab_1[11][0] * 8
                    sel_gel = round((per * 0.08) * tab_1[7][0], 2)
                    germ = round((per * 0.09) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + (tab_2[13][0] * 3), 2)
                    price = (((sqw_glaz * 2) + sqw_glaz_sil + dist_ram + corn + sel_gel + germ + byt + work) *
                             tab_2[24][0])
                elif glazing == 'sp_32_br':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_br = round((square * tab_2[18][0]) * tab_1[4][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[8][0]) * 2, 2)
                    corn = tab_1[11][0] * 8
                    sel_gel = round((per * 0.08) * tab_1[7][0], 2)
                    germ = round((per * 0.09) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + (tab_2[13][0] * 3), 2)
                    price = (((sqw_glaz * 2) + sqw_glaz_br + dist_ram + corn + sel_gel + germ + byt + work) *
                             tab_2[24][0])
                elif glazing == 'pvh_32_wh':
                    sqw_glaz = round((square * tab_2[21][0]) * tab_1[19][0], 2)
                    work = tab_2[26][0]
                    price = (sqw_glaz + work) * tab_2[24][0]
                elif glazing == 'pvh_32_gold':
                    sqw_glaz = round((square * tab_2[23][0]) * tab_1[20][0], 2)
                    # work = round((square * tab_2[26][0] * 4), 2)
                    price = sqw_glaz * tab_2[24][0]
                elif glazing == 'pvh_32_nut':
                    sqw_glaz = round((square * tab_2[23][0]) * tab_1[21][0], 2)
                    # work = round((square * tab_2[26][0] * 4), 2)
                    price = sqw_glaz * tab_2[24][0]

                elif glazing == 'sp_40':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[9][0]) * 2, 2)
                    corn = tab_1[12][0] * 8
                    sel_gel = round(((per * 0.132) * tab_1[7][0]), 2)
                    germ = round((per * 0.126) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + (tab_2[13][0] * 3), 2)
                    elit = tab_2[25][0] * square
                    price = ((sqw_glaz * 3) + dist_ram + corn + sel_gel + germ + byt + work + elit) * tab_2[24][0]
                elif glazing == 'sp_40_en':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_en = round((square * tab_2[17][0]) * tab_1[1][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[9][0]) * 2, 2)
                    corn = tab_1[12][0] * 8
                    sel_gel = round(((per * 0.132) * tab_1[7][0]), 2)
                    germ = round((per * 0.126) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0]) * 2, 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + ((tab_2[13][0] * 3) + (tab_2[14][0]) * 2), 2)
                    elit = tab_2[25][0] * square
                    price = (((sqw_glaz * 2) + sqw_glaz_en + dist_ram + corn + sel_gel + germ + byt + work + elit) *
                             tab_2[24][0])
                elif glazing == 'sp_40_en_2':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_en = round((square * tab_2[17][0]) * tab_1[1][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[9][0] * 2), 2)
                    corn = tab_1[12][0] * 8
                    sel_gel = round(((per * 0.132) * tab_1[7][0]), 2)
                    germ = round((per * 0.126) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + ((tab_2[13][0] * 3) + (tab_2[14][0] * 2)), 2)
                    elit = tab_2[25][0] * square
                    price = ((sqw_glaz + (sqw_glaz_en * 2) + dist_ram + corn + sel_gel + germ + byt + work + elit) *
                             tab_2[24][0])
                elif glazing == 'sp_40_arg':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[9][0] * 2), 2)
                    corn = round(tab_1[12][0] * 4, 2)
                    corn_arg = round((tab_1[14][0] + tab_1[15][0]) * 4, 2)
                    sel_gel = round((per * 0.132) * tab_1[7][0], 2)
                    germ = round((per * 0.126) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + (tab_2[13][0] * 3) + (tab_2[15][0] * 2),
                                 2)
                    elit = tab_2[25][0] * square
                    price = ((((sqw_glaz * 3) + dist_ram + corn + corn_arg + sel_gel + germ + byt + work + elit) *
                             tab_2[24][0]) - 45.5)
                elif glazing == 'sp_40_en_arg':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_en = round((square * tab_2[17][0]) * tab_1[1][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[9][0]) * 2, 2)
                    corn = round(tab_1[11][0] * 4, 2)
                    corn_arg = round((tab_1[14][0] + tab_1[15][0]) * 4, 2)
                    sel_gel = round(((per * 0.132) * tab_1[7][0]), 2)
                    germ = round((per * 0.126) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + ((tab_2[13][0] * 3) + tab_2[14][0]) +
                                 (tab_2[15][0] * 2), 2)
                    elit = tab_2[25][0] * square
                    price = ((((sqw_glaz * 2) + sqw_glaz_en + dist_ram + corn + corn_arg + sel_gel + germ + byt + work +
                              elit) * tab_2[24][0]) - 45.5)
                elif glazing == 'sp_40_sat':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_sat = round((square * tab_2[18][0]) * tab_1[2][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[9][0]) * 2, 2)
                    corn = tab_1[12][0] * 8
                    sel_gel = round((per * 0.132) * tab_1[7][0], 2)
                    germ = round((per * 0.126) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + (tab_2[13][0] * 3), 2)
                    elit = tab_2[25][0] * square
                    price = (((sqw_glaz * 2) + sqw_glaz_sat + dist_ram + corn + sel_gel + germ + byt + work + elit) *
                             tab_2[24][0])
                elif glazing == 'sp_40_sil':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_sil = round((square * tab_2[18][0]) * tab_1[3][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[9][0]) * 2, 2)
                    corn = tab_1[12][0] * 8
                    sel_gel = round((per * 0.132) * tab_1[7][0], 2)
                    germ = round((per * 0.126) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + (tab_2[13][0] * 3), 2)
                    elit = tab_2[25][0] * square
                    price = (((sqw_glaz * 2) + sqw_glaz_sil + dist_ram + corn + sel_gel + germ + byt + work + elit) *
                             tab_2[24][0])
                elif glazing == 'sp_40_br':
                    sqw_glaz = round((square * tab_2[16][0]) * tab_1[0][0], 2)
                    sqw_glaz_br = round((square * tab_2[18][0]) * tab_1[4][0], 2)
                    dist_ram = round(((per * tab_2[19][0]) * tab_1[9][0]) * 2, 2)
                    corn = tab_1[12][0] * 8
                    sel_gel = round((per * 0.132) * tab_1[7][0], 2)
                    germ = round((per * 0.126) * tab_1[5][0], 2)
                    byt = round(((per * 0.0015) * tab_1[6][0] * 2), 2)
                    work = round(tab_2[11][0] + (tab_2[12][0] * 2) + (tab_2[13][0] * 3), 2)
                    elit = tab_2[25][0] * square
                    price = (((sqw_glaz * 2) + sqw_glaz_br + dist_ram + corn + sel_gel + germ + byt + work + elit) *
                             tab_2[24][0])
                elif glazing == 'pvh_40_wh':
                    sqw_glaz = round((square * tab_2[22][0]) * tab_1[22][0], 2)
                    work = tab_2[26][0]
                    price = (sqw_glaz + work) * tab_2[24][0]
                price = round(price, 2)

                await bot.send_message(message.from_user.id, f'💰 Ціна - {price} 💰', reply_markup=profile_kb())
                await bot.send_message(message.from_user.id, f'👇 Натисніть для підтвердження 👇',
                                       reply_markup=confirm_button_kb())
                await state.set_state(CreateState.glazing_order)
            else:
                await bot.send_message(message.from_user.id, '❌ Занадто великий склоппакет! ❌')
        else:
            await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')
    else:
        await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')


async def glazing_order(call: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(confirm_order=call.data)
    create_data = await state.get_data()
    glazing_tp = create_data.get('glazing_type')
    glazing_tp_ua = {'glazing_24': 'Склопакет 24 мм',
                     'glazing_32': 'Склопакет 32 мм',
                     'glazing_40': 'Склопакет 40 мм'}.get(glazing_tp, '')

    glazing = create_data.get('glazing')
    glazing_dict = {
        'gl_4': 'Скло 4 мм',
        'sp_24': 'С/П 24 мм',
        'sp_24_en': 'С/П 24 мм ЕНЕРГО',
        'sp_24_sat': 'С/П 24 мм САТІН',
        'sp_24_sil': 'С/П 24 мм БРОНЗА-СРІБЛО',
        'sp_24_br': 'С/П 24 мм КОРИЧНЕВИЙ МАТ',
        'pvh_24_wh': 'ПВХ БІЛЕ 24 мм',
        'pvh_24_gold': 'ПВХ ЗОЛ. ДУБ 24 мм',
        'pvh_24_nut': 'ПВХ ГОРІХ 24 мм',
        'sp_32': 'С/П 32 мм',
        'sp_32_en': 'С/П 32 мм 1 ЕНЕРГО',
        'sp_32_en_2': 'С/П 32 мм 2 ЕНЕРГО',
        'sp_32_arg': 'С/П 32 мм + АРГ',
        'sp_32_en_arg': 'С/П 32 мм 1 ЕНЕРГО + АРГ',
        'sp_32_sat': 'С/П 32 мм САТІН',
        'sp_32_sil': 'С/П 32 мм БРОНЗА-СРІБЛО',
        'sp_32_br': 'С/П 32 мм КОРИЧНЕВИЙ МАТ',
        'pvh_32_wh': 'ПВХ БІЛЕ 32 мм',
        'pvh_32_gold': 'ПВХ ЗОЛ. ДУБ 32 мм',
        'pvh_32_nut': 'ПВХ ГОРІХ 32 мм',
        'sp_40': 'С/П 40 мм',
        'sp_40_en': 'С/П 40 мм 1 ЕНЕРГО',
        'sp_40_en_2': 'С/П 40 мм 2 ЕНЕРГО',
        'sp_40_arg': 'С/П 40 мм + АРГ',
        'sp_40_en_arg': 'С/П 40 мм 1 ЕНЕРГО + АРГ',
        'sp_40_sat': 'С/П 40 мм САТІН',
        'sp_40_sil': 'С/П 40 мм БРОНЗА-СРІБЛО',
        'sp_40_br': 'С/П 40 мм КОРИЧНЕВИЙ МАТ',
        'pvh_40_wh': 'ПВХ БІЛЕ 40 мм'
    }
    glazing_ua = glazing_dict.get(glazing, '')
    hor_size = create_data.get('hor_size_glazing')
    vert_size = create_data.get('vert_size_glazing')
    nums = create_data.get('glazing_number')
    user_id = call.from_user.id
    with sqlite3.connect('tgbot_db.db') as con:
        cursor1 = con.cursor()
        with sqlite3.connect('orders_db.db') as conn:
            cursor2 = conn.cursor()
            cursor1.execute('SELECT telegram_id, user_name, user_phone FROM users')
            data = cursor1.fetchall()
            ids = [int(item[0]) for item in data]
            if user_id in ids:
                cursor1.execute('SELECT user_name, user_phone FROM users WHERE telegram_id == ?', (user_id,))
                data = cursor1.fetchone()
                user_name = data[0]
                user_phone = data[1]
                try:
                    cursor2.execute('INSERT INTO ОСТЕКЛЕННЯ (Телефон, Імя, Товщина, Тип, Кількість, Ширина, Довжина,'
                                    'В_роботі, telegram_id) VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?)',
                                    (user_phone, user_name, glazing_tp_ua, glazing_ua, nums, hor_size,
                                     vert_size, user_id))
                    order_id = cursor2.lastrowid
                except Exception as e:
                    print(f"Помилка при додаванні замовлення: {e}")
    conn.commit()
    await call.message.answer(f'👍 Ваше замовлення підтверджено! 👍\n'
                              f'Номер замовлення - {order_id}', reply_markup=profile_kb())
    admin_ids_str = os.getenv('ADMIN_ID', '')
    admin_ids = admin_ids_str.split(',') if admin_ids_str else []
    for admin_id in admin_ids:
        await bot.send_message(admin_id, f' 💰Надійшло нове замовлення на 👉 ОСТЕКЛЕННЯ 👈 від {user_name} 💰')
    await state.clear()


async def create_windowsill(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    await bot.send_message(message.from_user.id, f'⬇️ Оберіть підвіконня ⬇️',
                           reply_markup=windowsill_kb())
    await state.set_state(CreateState.windowsill_colour)


async def windowsill_colour(call: CallbackQuery, state: FSMContext):
    await state.update_data(windowsill_colour=call.data)
    create_data = await state.get_data()
    user_table = create_data.get('windowsill_colour')

    if user_table in ['win_white', 'win_gold']:
        markup = windowsill_white_kb() if user_table == 'win_white' else windowsill_gold_kb()
        await call.message.answer(f'⬇️ Вкажіть ширину ⬇️', reply_markup=markup)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.answer()
        await state.set_state(CreateState.windowsill)


async def select_windowsill(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'⬇️ Вкажіть заглушку ⬇️', reply_markup=windowsill_plug_kb())
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.update_data(windowsill=call.data)
    await state.set_state(CreateState.windowsill_plug)


async def windowsill_plug(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Вкажіть кількість (до 20 штук) ⚠️')
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.update_data(windowsill_plug=call.data)
    await state.set_state(CreateState.windowsill_number)


async def number_windowsills(message: Message, state: FSMContext, bot: Bot):
    if message.text.isdigit() and 1 <= int(message.text) <= 20:
        await bot.send_message(message.from_user.id, f'Вкажіть довжину в мм ⚠️')
        await state.update_data(windowsill_number=message.text)
        await state.set_state(CreateState.windowsill_size)
    else:
        await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')


async def windowsill_size(message: Message, state: FSMContext, bot: Bot):
    if message.text.isdigit() and 250 <= int(message.text) <= 6000:
        user_id = message.from_user.id
        await state.update_data(windowsill_size=message.text)
        create_data = await state.get_data()
        colour = create_data.get('windowsill_colour')
        colour_ua = 'Білий' if colour == 'win_white' else 'Золотий дуб'
        user_table = create_data.get('windowsill')
        plug = create_data.get('windowsill_plug')
        nums = create_data.get('windowsill_number')
        size = create_data.get('windowsill_size')

        await bot.send_message(message.from_user.id, f'🔹 Ви обрали - {user_table}\n'
                                                     f'🔸 Колір - {colour_ua}\n'
                                                     f'🔹 Заглушка - {plug}\n'
                                                     f'🔸 Кількість - {nums} шт\n'
                                                     f'🔹 Довжина - {size}\n')

        table = 'windowsill_white' if colour == 'win_white' else 'windowsill_gold'
        table_plug = 'windowsill_plug_white' if colour == 'win_white' else 'windowsill_plug_gold'
        with sqlite3.connect('tgbot_db.db') as con:
            cursor = con.cursor()
            cursor.execute(f'SELECT price FROM {table} WHERE art == ?', (user_table,))
            table_1 = cursor.fetchone()
            cursor.execute(f'SELECT price FROM profit_work_waste')
            waste = cursor.fetchall()
            cursor.execute(f'SELECT price FROM profit_work_waste')
            income = cursor.fetchall()
            cursor.execute(f'SELECT price, art FROM {table_plug} WHERE art == ?', (plug,))
            table_2 = cursor.fetchone()
            con.commit()
        colour_income = {'win_white': 10, 'win_gold': 9}
        income = income[colour_income.get(colour)]
        price = round(((((table_1[0] * int(size)) * round(waste[8][0], 3) / 1000) + table_2[0]) * income[0]) *
                      int(nums), 2)
        await bot.send_message(message.from_user.id, f'💰 Ціна - {price} 💰')

        with sqlite3.connect('tgbot_db.db') as con:
            cursor = con.cursor()
            cursor.execute('SELECT discount, telegram_id FROM users WHERE telegram_id == ?', (user_id,))
            res = cursor.fetchone()
            con.commit()

        disc_price = round(price - ((int(res[0]) / 100) * price), 2)

        await bot.send_message(message.from_user.id, f'💰 Ваша ціна - {disc_price} 💰', reply_markup=profile_kb())
        await bot.send_message(message.from_user.id, f'👇 Натисніть для підтвердження 👇',
                               reply_markup=confirm_button_kb())
        await state.set_state(CreateState.windowsill_order)
    else:
        await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')


async def windowsill_order(call: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(confirm_order=call.data)
    create_data = await state.get_data()
    user_table = create_data.get('windowsill')
    colour = create_data.get('windowsill_colour')
    colour_ua = 'Білий' if colour == 'win_white' else 'Золотий дуб'
    plug = create_data.get('windowsill_plug')
    nums = create_data.get('windowsill_number')
    length = create_data.get('windowsill_size')

    user_id = call.from_user.id
    with sqlite3.connect('tgbot_db.db') as con:
        cursor1 = con.cursor()
        with sqlite3.connect('orders_db.db') as conn:
            cursor2 = conn.cursor()
            cursor1.execute('SELECT telegram_id, user_name, user_phone FROM users')
            data = cursor1.fetchall()
            ids = [int(item[0]) for item in data]
            if user_id in ids:
                cursor1.execute('SELECT user_name, user_phone FROM users WHERE telegram_id == ?', (user_id,))
                data = cursor1.fetchone()
                user_name = data[0]
                user_phone = data[1]
                try:
                    cursor2.execute(
                        'INSERT INTO ПІДВІКОННЯ (Телефон, Імя, Підвіконня, Колір, Заглушка, Кількість, Довжина, '
                        'В_роботі, telegram_id) VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?)',
                        (user_phone, user_name, user_table, colour_ua, plug, nums, length, user_id))
                    order_id = cursor2.lastrowid
                except Exception as e:
                    print(f"Помилка при додаванні замовлення: {e}")
    conn.commit()
    await call.message.answer(f'👍 Ваше замовлення підтверджено! 👍\n'
                              f'Номер замовлення - {order_id}', reply_markup=profile_kb())
    admin_ids_str = os.getenv('ADMIN_ID', '')
    admin_ids = admin_ids_str.split(',') if admin_ids_str else []
    for admin_id in admin_ids:
        await bot.send_message(admin_id, f'💰 Надійшло нове замовлення на 👉 ПІДВІКОННЯ 👈 від {user_name} 💰')
    await state.clear()


async def create_reflux(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    await bot.send_message(message.from_user.id, f'⬇️ Оберіть колір відливу ⬇️',
                           reply_markup=reflux_type_kb())
    await state.set_state(CreateState.reflux_type)


async def reflux_type(call: CallbackQuery, state: FSMContext):
    await state.update_data(reflux_type=call.data)
    await call.message.answer(f'⬇️ Оберіть ширину відливу ⬇️', reply_markup=reflux_kb())
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.reflux)


async def select_reflux(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Вкажіть кількість (до 20 штук) ⚠️')
    await state.update_data(reflux=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.reflux_number)


async def number_reflux(message: Message, state: FSMContext, bot: Bot):
    if message.text.isdigit() and 1 <= int(message.text) <= 20:
        await bot.send_message(message.from_user.id, f'Вкажіть довжину в мм ⚠️')
        await state.update_data(reflux_number=message.text)
        await state.set_state(CreateState.reflux_size)
    else:
        await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')


async def reflux_size(message: Message, state: FSMContext, bot: Bot):
    if message.text.isdigit() and 250 <= int(message.text) <= 3000:
        user_id = message.from_user.id
        await state.update_data(reflux_size=message.text)
        create_data = await state.get_data()
        reflux_tp = create_data.get('reflux_type')
        colour_map = {
            'reflux_white': 'Білий',
            'reflux_br': 'Коричневий',
            'reflux_ant': 'Антрацит'
        }
        colour_ua = colour_map.get(reflux_tp, '')

        user_table = create_data.get('reflux')
        nums = create_data.get('reflux_number')
        size = create_data.get('reflux_size')

        reflux_tp = create_data.get('reflux_type')

        await bot.send_message(message.from_user.id, f'🔹 Ви обрали відлив - {user_table} мм\n'
                                                     f'🔸 Колір - {colour_ua}\n'
                                                     f'🔹 Кількісь - {nums} шт\n'
                                                     f'🔸 Довжина - {size} мм\n')

        with sqlite3.connect('tgbot_db.db') as con:
            cursor = con.cursor()
            cursor.execute('SELECT price FROM reflux_price')
            table_1 = cursor.fetchall()
            cursor.execute('SELECT price FROM profit_work_waste')
            table_2 = cursor.fetchall()
            con.commit()

        square_factor = table_2[6][0] if reflux_tp == 'reflux_white' else table_2[7][0]
        square = round((int(size) / 1000) * ((int(user_table) + 50) / 1000) * square_factor, 3)

        col_price = table_1[0][0] if reflux_tp == 'reflux_white' else table_1[1][0] if reflux_tp == 'reflux_br' else (
            table_1)[2][0]
        price = round((((col_price * square + table_2[4][0]) * int(nums)) * table_2[5][0]), 2)

        await bot.send_message(message.from_user.id, f'💰 Ціна - {price} 💰')

        with sqlite3.connect('tgbot_db.db') as con:
            cursor = con.cursor()
            cursor.execute('SELECT discount, telegram_id FROM users WHERE telegram_id == ?', (user_id,))
            res = cursor.fetchone()
            con.commit()

        disc_price = round(price - ((int(res[0]) / 100) * price), 2)

        await bot.send_message(message.from_user.id, f'💰 Ваша ціна - {disc_price} 💰', reply_markup=profile_kb())
        await bot.send_message(message.from_user.id, f'👇 Натисніть для підтвердження 👇',
                               reply_markup=confirm_button_kb())
        await state.set_state(CreateState.reflux_order)
    else:
        await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')


async def reflux_order(call: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(confirm_order=call.data)
    create_data = await state.get_data()
    user_table = create_data.get('reflux')
    colour = create_data.get('reflux_type')
    colour_map = {
        'reflux_white': 'Білий',
        'reflux_br': 'Коричневий',
        'reflux_ant': 'Антрацит'
    }
    colour_ua = colour_map.get(colour, '')
    nums = create_data.get('reflux_number')
    length = create_data.get('reflux_size')
    user_id = call.from_user.id

    with sqlite3.connect('tgbot_db.db') as con:
        cursor1 = con.cursor()
        with sqlite3.connect('orders_db.db') as conn:
            cursor2 = conn.cursor()
            cursor1.execute('SELECT telegram_id, user_name, user_phone FROM users')
            data = cursor1.fetchall()
            ids = [int(item[0]) for item in data]
            if user_id in ids:
                cursor1.execute('SELECT user_name, user_phone FROM users WHERE telegram_id == ?', (user_id,))
                data = cursor1.fetchone()
                user_name = data[0]
                user_phone = data[1]
                try:
                    cursor2.execute('INSERT INTO ВІДЛИВ (Телефон, Імя, Відлив, Колір, Кількість, Довжина, В_роботі, '
                                    'telegram_id) VALUES (?, ?, ?, ?, ?, ?, 0, ?)',
                                    (user_phone, user_name, user_table, colour_ua, nums, length, user_id))
                    order_id = cursor2.lastrowid
                except Exception as e:
                    print(f"Помилка при додаванні замовлення: {e}")
    conn.commit()
    await call.message.answer(f'👍 Ваше замовлення підтверджено! 👍\n'
                              f'Номер замовлення - {order_id}', reply_markup=profile_kb())
    admin_ids_str = os.getenv('ADMIN_ID', '')
    admin_ids = admin_ids_str.split(',') if admin_ids_str else []
    for admin_id in admin_ids:
        await bot.send_message(admin_id, f'💰 Надійшло нове замовлення на 👉 ВІДЛИВ 👈 від {user_name} 💰')
    await state.clear()


async def create_mosquito(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    await bot.send_message(message.from_user.id, f'⬇️ Оберіть тип москітної сітки ⬇️',
                           reply_markup=mosquito_type_kb())
    await state.set_state(CreateState.mosquito_type)


async def mosquito_type(call: CallbackQuery, state: FSMContext):
    await state.update_data(mosquito_type=call.data)
    create_data = await state.get_data()
    user_table = create_data.get('mosquito_type')

    reply_markup_map = {
        'inside': mosquito_inside_kb(),
        'outside': mosquito_outside_kb()
    }

    state_transition_map = {
        'inside': CreateState.mosquito,
        'outside': CreateState.mosquito
    }

    if user_table in reply_markup_map:
        await call.message.answer(f'⬇️ Оберіть колір ⬇️', reply_markup=reply_markup_map[user_table])
        await call.message.edit_reply_markup(reply_markup=None)
        await call.answer()
        await state.set_state(state_transition_map[user_table])


async def select_mosquito(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Вкажіть кількість (до 20 штук) ⚠️')
    await state.update_data(mosquito=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.mosquito_number)


async def number_mosquito(message: Message, state: FSMContext, bot: Bot):
    if message.text.isdigit() and 1 <= int(message.text) <= 20:
        await bot.send_message(message.from_user.id, f'Вкажіть ширину в мм ⚠️')
        await state.update_data(mosquito_number=message.text)
        await state.set_state(CreateState.hor_size_mosquito)
    else:
        await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')


async def mosquito_hor_size(message: Message, state: FSMContext, bot: Bot):
    if message.text.isdigit() and 250 <= int(message.text) <= 2500:
        await bot.send_message(message.from_user.id, 'Тепер вкажіть висоту в мм ⚠️')
        await state.update_data(hor_size_mosquito=message.text)
        await state.set_state(CreateState.vert_size_mosquito)
    else:
        await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')


async def mosquito_vert_size(message: Message, state: FSMContext, bot: Bot):
    if not message.text.isdigit() or not 250 <= int(message.text) <= 2500:
        await bot.send_message(message.from_user.id, '❌ Невірно введено дані! Повторіть ввід! ❌')
        return

    await state.update_data(vert_size_mosquito=message.text)
    create_data = await state.get_data()
    mosquito_tp = create_data.get('mosquito_type')
    mosquito_tp_ua = 'Внутрішня' if mosquito_tp == 'inside' else 'Зовнішня'

    colour = create_data.get('mosquito')
    colour_map = {
        'inside_white': 'Білий', 'outside_white': 'Білий',
        'inside_brown': 'Коричневий', 'outside_brown': 'Коричневий',
        'inside_anthracite': 'Антрацит'
    }
    colour_ua = colour_map.get(colour, '')

    hor_size = create_data.get('hor_size_mosquito')
    vert_size = create_data.get('vert_size_mosquito')
    nums = create_data.get('mosquito_number')
    square = ((int(hor_size) / 1000) * (int(vert_size) / 1000))

    if square >= 3:
        await bot.send_message(message.from_user.id, '❌ Занадто велика москітка! ❌')

    await bot.send_message(message.from_user.id, f'🔹 Тип сітки - {mosquito_tp_ua}\n'
                                                 f'🔸 Колір - {colour_ua}\n'
                                                 f'🔹 Кількісь - {nums} шт\n'
                                                 f'🔸 Ширина - {hor_size} мм\n'
                                                 f'🔹 Висота - {vert_size} мм\n')

    table_name = f'mosquito_{mosquito_tp}_{colour.split("_")[1]}'
    with sqlite3.connect('tgbot_db.db') as con:
        cursor = con.cursor()
        cursor.execute(f'SELECT price FROM {table_name}')
        table_1 = cursor.fetchall()
        cursor.execute(f'SELECT price FROM profit_work_waste')
        table_2 = cursor.fetchall()
        con.commit()
    per = ((int(vert_size) + int(hor_size)) / 500)
    ch_1 = round(per * table_1[0][0], 1)
    ch_2 = round(table_1[1][0] * 18, 2)
    ch_3 = table_1[2][0]
    ch_4 = 0
    if mosquito_tp == 'inside':
        ch_4 = round(((per - 0.252) * table_2[3][0]) * table_1[3][0], 2)
    elif mosquito_tp == 'outside':
        waste = 0
        if colour == 'outside_white':
            waste = table_2[3][0]
        elif colour == 'outside_brown':
            waste = table_2[27][0]
        ch_4 = round(((per - 0.176) * waste) * table_1[3][0], 2)
    ch_5 = round(table_1[4][0] * 2, 2)
    ch_6 = round(((square * table_2[2][0]) * table_1[5][0]), 3)
    ch_7 = round(table_1[6][0] * 4, 2)
    work = table_2[0][0]
    profit = table_2[1][0]

    price = (ch_1 + ch_2 + ch_3 + ch_4 + ch_5 + ch_6 + ch_7 + work) * profit
    price = round(price, 2)

    await bot.send_message(message.from_user.id, f'💰 Ціна - {price} 💰', reply_markup=profile_kb())
    await bot.send_message(message.from_user.id, f'👇 Натисніть для підтвердження 👇',
                           reply_markup=confirm_button_kb())
    await state.set_state(CreateState.mosquito_order)


async def mosquito_order(call: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(confirm_order=call.data)
    create_data = await state.get_data()
    mos_type = create_data.get('mosquito_type')
    type_ua = 'Внутрішня' if mos_type == 'inside' else 'Зовнішня'
    colour = create_data.get('mosquito')
    hor_size = create_data.get('hor_size_mosquito')
    vert_size = create_data.get('vert_size_mosquito')
    nums = create_data.get('mosquito_number')
    user_id = call.from_user.id
    with sqlite3.connect('tgbot_db.db') as con:
        cursor1 = con.cursor()
        with sqlite3.connect('orders_db.db') as conn:
            cursor2 = conn.cursor()
            cursor1.execute('SELECT telegram_id, user_name, user_phone FROM users')
            data = cursor1.fetchall()
            ids = [int(item[0]) for item in data]
            if user_id in ids:
                cursor1.execute('SELECT user_name, user_phone FROM users WHERE telegram_id == ?', (user_id,))
                data = cursor1.fetchone()
                user_name = data[0]
                user_phone = data[1]
                try:
                    cursor2.execute('INSERT INTO МОСКІТКА (Телефон, Імя, Тип, Колір, Кількість, Ширина, Довжина,'
                                    'В_роботі, telegram_id) VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?)',
                                    (user_phone, user_name, type_ua, colour, nums, hor_size, vert_size, user_id))
                    order_id = cursor2.lastrowid
                except Exception as e:
                    print(f"Помилка при додаванні замовлення: {e}")
    conn.commit()
    await call.message.answer(f'👍 Ваше замовлення підтверджено! 👍\n'
                              f'Номер замовлення - {order_id}', reply_markup=profile_kb())
    admin_ids_str = os.getenv('ADMIN_ID', '')
    admin_ids = admin_ids_str.split(',') if admin_ids_str else []
    for admin_id in admin_ids:
        await bot.send_message(admin_id, f'💰 Надійшло нове замовлення на 👉 МОСКІТКУ 👈 від {user_name} 💰')
    await state.clear()


async def clear(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    await bot.send_message(message.from_user.id, f'🚮 Введені дані очищено!', reply_markup=profile_kb())
