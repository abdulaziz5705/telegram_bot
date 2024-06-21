import logging
from db import Database
from aiogram import Bot, Dispatcher, executor, types
from default_button import (menu_keyboard, menu_detail, mahsulot_button, menu_detail2, menu_detail3, menu_detail4,
                            menu_detail5, menu_detail6, menu_detail7, menu_detail8)
import asyncio


API_TOKEN = "token"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO bot_users (first_name, last_name, username, user_id) VALUES ('{first_name}', '{last_name}', '{username}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Assalomu aleykum sizni ko'rganimdan xursantman  {first_name}", reply_markup=menu_keyboard)

    else:
        await Database.connect(query, "insert")
        await message.reply(f"Xushkelibsiz {first_name}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Kitoblar")
async def show_menu(message: types.Message):
    #action = button_callback_menu.new(action=message.text)
    await message.answer("1 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=menu_detail)


@dp.message_handler(lambda message: message.text == "Kiyimlar ")
async def show_menu(message: types.Message):
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail2)


@dp.message_handler(lambda message: message.text == "Avtotovarlar ")
async def show_menu(message: types.Message):
    await message.answer("3 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail3)


@dp.message_handler(lambda message: message.text == "Texnika")
async def show_menu(message: types.Message):
    await message.answer("4 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail4)


@dp.message_handler(lambda message: message.text == "Oyoq Kiyimlar")
async def show_menu(message: types.Message):
    await message.answer("5 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail5)


@dp.message_handler(lambda message: message.text == "Akksessuar")
async def show_menu(message: types.Message):
    await message.answer("6 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail6)


@dp.message_handler(lambda message: message.text == "Remont")
async def show_menu(message: types.Message):
    await message.answer("7 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail7)


@dp.message_handler(lambda message: message.text == "Kanstovar")
async def show_menu(message: types.Message):
    await message.answer("8 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail8)


@dp.message_handler(lambda message: message.text == "Atom Habits")
async def show_menu(message: types.InlineKeyboardButton):
    keyboard: types.InlineKeyboardMarkup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="➖", callback_data="option1")
    button2 = types.InlineKeyboardButton(text="1", callback_data="option2")
    button3 = types.InlineKeyboardButton(text="➕", callback_data="option3")
    keyboard.add(button1, button2, button3)
    await message.answer("Mahsulot sonini tanlang: ", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Back")
async def show_menu(message: types.Message):
    await message.answer("Menyulardan birini tanglang:", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Mahsulot 1")
async def show_menu(message: types.Message):
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=mahsulot_button)


@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    #Pastgi kodda admin qismini qo'shishingiz mumkun listni ichiga telegram id kiritasiz
    if message.from_user.id in []:
        await message.reply("Salom admin")
        photo_path = "telegram_bot/img.png"
        await bot.send_photo(message.chat.id, photo=photo_path)
    else:
        await message.reply("Bunday buyruq turi mavjud emas")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
