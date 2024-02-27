from aiogram.utils.keyboard import ReplyKeyboardBuilder


def profile_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text='🔹 Склопакет')
    kb.button(text='🔸 Підвіконня')
    kb.button(text='🔹 Жалюзі')
    kb.button(text='🔸 Відлив')
    kb.button(text='🔹 Москітка')
    kb.button(text='🤑 Моя знижка')
    kb.button(text='📌 Статус замовлення')
    kb.button(text='📋 Мої замовлення')
    kb.adjust(2, 3, 2)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)
