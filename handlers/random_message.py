from aiogram import Router, types
random_message_rt = Router()


@random_message_rt.message()
async def rndm_msg(msg: types.Message):
    if msg.text.lower() == 'привет' or msg.text.lower() == 'здравствуй':
        await msg.answer('Привет привет')
    elif msg.text.lower() in ('как дела', 'как дела?', 'как ты', 'как ты?'):
        await msg.answer('Все отлично!')
    elif msg.text.lower() == 'пока':
        await msg.answer('Пока пока')
    else:
        await msg.answer(text='Очень интересно...')