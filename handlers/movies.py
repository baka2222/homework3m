from aiogram import Router, types, F

movies_rt = Router()


@movies_rt.callback_query(F.data == 'movies')
async def movies(cb: types.CallbackQuery):
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(url='https://kinogo.inc/films/784-ono-2-new-v5-lp7.html', text='Оно 2')],
        [types.InlineKeyboardButton(url='https://kinogo.inc/films/523-mstiteli-final-2019-hd-swvisiontv4-v49-sw7.html',
                                    text='Мстители: Финал')]
    ])
    await cb.message.edit_text(f'Что предпочтете смотреть?', reply_markup=ikb)
    await cb.answer()
