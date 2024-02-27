from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='👉 Зареєструватися в базі 👈'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Для продовження натисніть кнопку нижче 👇')
