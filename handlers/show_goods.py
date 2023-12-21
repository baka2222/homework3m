from aiogram import Router, types, F
from aiogram.filters import Command
import sqlite3
import pathlib


show_goods_rt = Router()
db_path = pathlib.Path(__file__).parent.parent / 'goods.db'
db = sqlite3.connect(db_path)
cursor = db.cursor()

@show_goods_rt.message(Command('goods'))
async def goods_func(msg: types.Message):
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[[
        types.InlineKeyboardButton(text='Скетчбук', callback_data='скетчбук'),
    ],
    [
        types.InlineKeyboardButton(text='Футболка', callback_data='футболка')
    ]])
    await msg.answer(text='Вы можете купить наш товар!', reply_markup=ikb)


@show_goods_rt.callback_query(F.data == 'скетчбук')
async def sketchbook_cb_handler(cb: types.CallbackQuery):
    cursor.execute('''SELECT * FROM goods WHERE key=5''')
    show_data = cursor.fetchall()[0]
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[[
        types.InlineKeyboardButton(text='Посмотреть', url=f'https://www.google.com/url?sa=i&url=https%3A%2F%2Fpad-me.ru%2Fsketchbuk-anime%2F&psig=AOvVaw0nQYuH3j_OxGL_2B4JUXl3&ust=1703269784984000&source=images&cd=vfe&opi=89978449&ved=0CBQQ3YkBahcKEwiYsL6xwKGDAxUAAAAAHQAAAAAQAw')
    ]])
    #Непосредственно с поля png не сумел. edit_media, edit_text, answer_photo - не работали.
    await cb.message.edit_text(text=f'{show_data[1]}. {show_data[2]}. Цена - {show_data[3]}.', reply_markup=ikb)
    await cb.answer()


@show_goods_rt.callback_query(F.data == 'футболка')
async def sketchbook_cb_handler(cb: types.CallbackQuery):
    cursor.execute('''SELECT * FROM goods WHERE key=3''')
    show_data = cursor.fetchall()[0]
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[[
        types.InlineKeyboardButton(text='Посмотреть', url=f'https://www.google.com/url?sa=i&url=https%3A%2F%2Fprom.ua%2Fp1641694046-anime-futbolka-yaponskom.html&psig=AOvVaw2FwM1Z7azqXa9v6RbGC8-_&ust=1703285243692000&source=images&cd=vfe&opi=89978449&ved=0CBQQ3YkBahcKEwig-ruSzqGDAxUAAAAAHQAAAAAQAw')
    ]])
    await cb.message.edit_text(text=f'{show_data[1]}. {show_data[2]}. Цена - {show_data[3]}.', reply_markup=ikb)
    await cb.answer()


