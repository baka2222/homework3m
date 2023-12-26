from aiogram import types, Router, F
from aiogram.filters import Command
import sqlite3
from pathlib import Path


show_goods_rt = Router()


@show_goods_rt.message(Command('goods'))
async def show_goods(msg: types.Message):
    db_path = Path(__file__).parent.parent / 'goods.db'
    cursor = sqlite3.connect(db_path).cursor()
    cursor.execute('SELECT name FROM categories') #Все добавил вручную, потому что через фунции были ошибки
    data_categories = cursor.fetchall()
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text=f'{data_categories[0][0]}', callback_data='clothes')],
        [types.InlineKeyboardButton(text=f'{data_categories[1][0]}', callback_data='stickers')],
        [types.InlineKeyboardButton(text=f'{data_categories[2][0]}', callback_data='sketchbooks')]
    ])
    await msg.answer(text='Вы можете приобрести нашу продукцию! Выберите категорию',
                     reply_markup=ikb)


'''У меня в таблицах по три вещей и категорий, но связь я реализовал'''
@show_goods_rt.callback_query(F.data == 'sketchbooks')
async def clothes(callback: types.CallbackQuery):
    db_path = Path(__file__).parent.parent / 'goods.db'
    cursor = sqlite3.connect(db_path).cursor()
    cursor.execute('''SELECT * FROM products AS p
    JOIN categories AS c ON p.id_categories = c.id''')
    data_tables = cursor.fetchall()
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[[
        types.InlineKeyboardButton(text=f'{data_tables[0][1]}', callback_data='Скетчбук Ханако-кун')
    ]])
    await callback.message.edit_text(text=f'Категория - {data_tables[0][7]}.\nВот список товаров',
                                     reply_markup=ikb)
    await callback.answer()


'''Дальше создаю коллбек хэндлер для хэндлера, что выше. Итак поочередно'''
@show_goods_rt.callback_query(F.data == 'Скетчбук Ханако-кун')
async def hanako_kun(callback: types.CallbackQuery):
    db_path = Path(__file__).parent.parent / 'goods.db'
    cursor = sqlite3.connect(db_path).cursor()
    cursor.execute('''SELECT * FROM products AS p
        JOIN categories AS c ON p.id_categories = c.id''')
    data_tables = cursor.fetchall()
    await callback.message.answer_photo(photo=f'{data_tables[0][4]}',
                                        caption=f'''{data_tables[0][1]}\n{data_tables[0][3]} Цена {data_tables[0][2]}.''')
    await callback.answer()


@show_goods_rt.callback_query(F.data == 'stickers')
async def clothes(callback: types.CallbackQuery):
    db_path = Path(__file__).parent.parent / 'goods.db'
    cursor = sqlite3.connect(db_path).cursor()
    cursor.execute('''SELECT * FROM products AS p
    JOIN categories AS c ON p.id_categories = c.id''')
    data_tables = cursor.fetchall()
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[[
        types.InlineKeyboardButton(text=f'{data_tables[2][1]}', callback_data='стикеры')
    ]])
    await callback.message.edit_text(text=f'Категория - {data_tables[2][7]}.\nВот список товаров',
                                     reply_markup=ikb)
    await callback.answer()


@show_goods_rt.callback_query(F.data == 'стикеры')
async def hanako_kun(callback: types.CallbackQuery):
    db_path = Path(__file__).parent.parent / 'goods.db'
    cursor = sqlite3.connect(db_path).cursor()
    cursor.execute('''SELECT * FROM products AS p
        JOIN categories AS c ON p.id_categories = c.id''')
    data_tables = cursor.fetchall()
    await callback.message.answer_photo(photo=f'{data_tables[2][4]}',
                                        caption=f'''{data_tables[2][1]}\n{data_tables[2][3]} Цена {data_tables[2][2]}.''')
    await callback.answer()


@show_goods_rt.callback_query(F.data == 'clothes')
async def clothes(callback: types.CallbackQuery):
    db_path = Path(__file__).parent.parent / 'goods.db'
    cursor = sqlite3.connect(db_path).cursor()
    cursor.execute('''SELECT * FROM products AS p
    JOIN categories AS c ON p.id_categories = c.id''')
    data_tables = cursor.fetchall()
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[[
        types.InlineKeyboardButton(text=f'{data_tables[1][1]}', callback_data='одежда')
    ]])
    await callback.message.edit_text(text=f'Категория - {data_tables[1][7]}.\nВот список товаров',
                                     reply_markup=ikb)
    await callback.answer()


@show_goods_rt.callback_query(F.data == 'одежда')
async def hanako_kun(callback: types.CallbackQuery):
    db_path = Path(__file__).parent.parent / 'goods.db'
    cursor = sqlite3.connect(db_path).cursor()
    cursor.execute('''SELECT * FROM products AS p
        JOIN categories AS c ON p.id_categories = c.id''')
    data_tables = cursor.fetchall()
    await callback.message.answer_photo(photo=f'{data_tables[1][4]}',
                                        caption=f'''{data_tables[1][1]}\n{data_tables[1][3]} Цена {data_tables[1][2]}.''')
    await callback.answer()

