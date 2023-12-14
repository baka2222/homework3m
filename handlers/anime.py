from aiogram import types, Router, F

anime_rt = Router()


@anime_rt.callback_query(F.data == 'anime')
async def anm(cb: types.CallbackQuery):
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(url='https://jut.su/naruuto/', text='Наруто')],
        [types.InlineKeyboardButton(url='https://jut.su/kime-no-yaiba/', text='КРД')]
    ])
    await cb.message.edit_text('Что предпочтете смотреть?', reply_markup=ikb)
    await cb.answer()
