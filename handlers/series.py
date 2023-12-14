from aiogram import Router, types, F

series_rt = Router()


@series_rt.callback_query(F.data == 'series')
async def srs(cb: types.CallbackQuery):
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(url='https://kinogo.biz/9957-pacany-1-1080.html', text='Пацаны')],
        [types.InlineKeyboardButton(url='https://ctc.ru/projects/serials/kukhnya/', text='Куня')]
    ])
    cb.message.edit_text('Что предпочтете смотреть?', reply_markup=ikb)
    cb.answer()
