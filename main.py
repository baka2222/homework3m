import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from os import getenv
from handlers.start import start_rt
from handlers.movies import movies_rt
from handlers.anime import anime_rt
from handlers.series import series_rt
from handlers.info import info_rt
from handlers.survey import survey_rt
from handlers.random_message import random_message_rt
from db.db_functions import init_db
from handlers.show_goods import show_goods_rt
from handlers.reminder import reminder_rt
from bor import bot, dp
# load_dotenv()
# bot = Bot(token=getenv('BOT'))
# dp = Dispatcher()


async def on_startup(dispatcher):
    init_db()

async def main():
    await bot.set_my_commands([
        types.BotCommand(command='/start', description='Начало работы'),
        types.BotCommand(command='/info', description='О нас'),
        types.BotCommand(command='/join_team', description='Наша команда'),
        types.BotCommand(command='/goods', description='Наши товары')
    ])
    dp.include_router(reminder_rt)
    dp.include_router(anime_rt)
    dp.include_router(series_rt)
    dp.include_router(info_rt)
    dp.include_router(movies_rt)
    dp.include_router(start_rt)
    dp.include_router(survey_rt)
    dp.include_router(show_goods_rt)
    dp.startup.register(on_startup)
    dp.include_router(random_message_rt)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
