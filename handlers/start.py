from aiogram import Router, types
from aiogram.filters import Command

start_rt = Router()


@start_rt.message(Command('start'))
async def start(msg: types.Message):
    ikb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Movies', callback_data='movies')],
            [types.InlineKeyboardButton(text='Anime', callback_data='anime')],
            [types.InlineKeyboardButton(text='Series', callback_data='series')]
        ])
    await msg.answer(f'Здравствуйте, {msg.from_user.first_name}, Вы попали в бота-поисковика медиатеки!',
                     reply_markup=ikb)
    types.ReplyKeyboardRemove(remove_keyboard=True)
