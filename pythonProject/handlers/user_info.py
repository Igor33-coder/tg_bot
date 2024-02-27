import sqlite3

from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from state.create import CreateState
from keyboards.create_kb import tables_kb
from keyboards.profile_kb import profile_kb


async def user_disc(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    user_id = message.from_user.id
    with sqlite3.connect('tgbot_db.db') as con:
        cursor = con.cursor()
        cursor.execute('SELECT discount, telegram_id FROM users WHERE telegram_id == ?', (user_id,))
        disc = cursor.fetchone()
        con.commit()
    await bot.send_message(message.from_user.id, f'На даний час Ваша знижка становить - {int(disc[0])}% 📊',
                           reply_markup=profile_kb())


async def select_table(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    await bot.send_message(message.from_user.id, f'Що Ви замовляли? ⬇️', reply_markup=tables_kb())
    await state.set_state(CreateState.select_table)


async def select_order(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Вкажіть номер замовлення ⬇️')
    await state.update_data(select_table=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.order_info)


async def order_info(message: Message, state: FSMContext, bot: Bot):
    user_id = message.from_user.id
    order = message.text

    async def process_order(table_name):
        with sqlite3.connect('orders_db.db') as con:
            cursor = con.cursor()
            cursor.execute(f'SELECT id, В_роботі, telegram_id FROM {table_name} WHERE id = ?', (order,))
            status = cursor.fetchone()
            con.commit()
        if status is not None:
            if int(status[2]) == user_id:
                if status[1] == 0:
                    await bot.send_message(message.from_user.id, '🔴 Замовлення в опрацюванні 🔴',
                                           reply_markup=profile_kb())
                    await state.clear()
                elif status[1] == 1:
                    await bot.send_message(message.from_user.id, '🟡 Замовлення в роботі 🟡', reply_markup=profile_kb())
                    await state.clear()
                elif status[1] == 2:
                    await bot.send_message(message.from_user.id, '🟢 Замовлення готове 🟢', reply_markup=profile_kb())
                    await state.clear()
            else:
                await bot.send_message(message.from_user.id, f'❌ Це не Ваше замовлення ❌')

    tables = ['ПІДВІКОННЯ', 'ВІДЛИВ', 'МОСКІТКА', 'ОСТЕКЛЕННЯ', 'ЖАЛЮЗІ']
    if order.isdigit() and 1 <= int(order) <= 1000:
        data_base = await state.get_data()
        table = data_base.get('select_table')
        if table in tables:
            await process_order(table)
        else:
            await bot.send_message(message.from_user.id, f'❌ Неправильна таблиця ❌')
    else:
        await bot.send_message(message.from_user.id, '❌ Невірно введено дані! ❌')


async def select_order_tables(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    await bot.send_message(message.from_user.id, f'Що Ви замовляли? ⬇️', reply_markup=tables_kb())
    await state.set_state(CreateState.order_table)


async def user_orders(call: CallbackQuery, state: FSMContext):
    await state.update_data(order_table=call.data)
    user_id = call.from_user.id
    data_base = await state.get_data()
    table = data_base.get('order_table')
    if table == 'ПІДВІКОННЯ':
        with sqlite3.connect('orders_db.db') as con:
            cursor = con.cursor()
            cursor.execute('SELECT id, telegram_id FROM ПІДВІКОННЯ WHERE telegram_id = ?', (user_id,))
            orders = cursor.fetchall()
            con.commit()
        first_elements = [tpl[0] for tpl in orders]
        user_list = ', '.join(map(str, first_elements[-10:]))
        await call.message.answer(f'Номери Ваших замовлень: {user_list}')
    elif table == 'ВІДЛИВ':
        with sqlite3.connect('orders_db.db') as con:
            cursor = con.cursor()
            cursor.execute('SELECT id, telegram_id FROM ВІДЛИВ WHERE telegram_id = ?', (user_id,))
            orders = cursor.fetchall()
            con.commit()
        first_elements = [tpl[0] for tpl in orders]
        user_list = ', '.join(map(str, first_elements[-10:]))
        await call.message.answer(f'Номери Ваших замовлень: {user_list}', reply_markup=profile_kb())
    elif table == 'МОСКІТКА':
        with sqlite3.connect('orders_db.db') as con:
            cursor = con.cursor()
            cursor.execute('SELECT id, telegram_id FROM МОСКІТКА WHERE telegram_id = ?', (user_id,))
            orders = cursor.fetchall()
            con.commit()
        first_elements = [tpl[0] for tpl in orders]
        user_list = ', '.join(map(str, first_elements[-10:]))
        await call.message.answer(f'Номери Ваших замовлень: {user_list}', reply_markup=profile_kb())
    elif table == 'ОСТЕКЛЕННЯ':
        with sqlite3.connect('orders_db.db') as con:
            cursor = con.cursor()
            cursor.execute('SELECT id, telegram_id FROM ОСТЕКЛЕННЯ WHERE telegram_id = ?', (user_id,))
            orders = cursor.fetchall()
            con.commit()
        first_elements = [tpl[0] for tpl in orders]
        user_list = ', '.join(map(str, first_elements[-10:]))
        await call.message.answer(f'Номери Ваших замовлень: {user_list}', reply_markup=profile_kb())
    elif table == 'ЖАЛЮЗІ':
        with sqlite3.connect('orders_db.db') as con:
            cursor = con.cursor()
            cursor.execute('SELECT id, telegram_id FROM ЖАЛЮЗІ WHERE telegram_id = ?', (user_id,))
            orders = cursor.fetchall()
            con.commit()
        first_elements = [tpl[0] for tpl in orders]
        user_list = ', '.join(map(str, first_elements[-10:]))
        await call.message.answer(f'Номери Ваших замовлень: {user_list}', reply_markup=profile_kb())
