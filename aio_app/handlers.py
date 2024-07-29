from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import aio_app.keyboards as kb

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main_kb)
    await message.reply('Как дела?')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи')


# Обработчик конкретного входящего текста
# @router.message(F.text == 'У меня всё хорошо')
# async def txt_all_right(message: Message):
#     await message.answer('Я очень рад')

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара', reply_markup=kb.catalog_kb)


@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали категорию футболок')


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возраст')


@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Отправьте номер телефона', reply_markup=kb.get_number_kb)


@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Ваши имя: {data["name"]}\nвозраст: {data["age"]}\nномер: {data["number"]}')
    await state.clear()
