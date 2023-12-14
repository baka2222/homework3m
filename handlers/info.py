from aiogram import types, Router
from aiogram.filters import Command
info_rt = Router()


@info_rt.message(Command('info'))
async def inf(msg: types.Message):
    await msg.answer('Бот будет развиваться.')