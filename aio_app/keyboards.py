from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты'), KeyboardButton(text='О нас')],
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...',
)

catalog_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Футболки', callback_data='t-shirt')],
    [InlineKeyboardButton(text='Кроссовки', callback_data='sneakers')],
    [InlineKeyboardButton(text='Кепки', callback_data='cap')],
],
)

get_number_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(
        text='Отправить номер',
        request_contact=True,
    )]
],
    resize_keyboard=True,
)
