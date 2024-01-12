from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import F, Router, types
from bot import bot


scheduler = AsyncIOScheduler()


reminder_rt = Router()


@reminder_rt.message(F.text.startswith('напомни'))
async def reminder(msg: types.Message):
    await bot.send_message(text='Ожидайте',
                           chat_id=msg.from_user.id)
    scheduler.add_job(
        func=reminder_send,
        trigger='interval',
        seconds=5,
        kwargs={'text': msg.text,
                'chat_id': msg.from_user.id}
    )


async def reminder_send(chat_id: int, text: str):
    await bot.send_message(chat_id=chat_id,
                           text=text[8:])


