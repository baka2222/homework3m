from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
survey_rt = Router()

class Survey(StatesGroup):
    name = State()
    age = State()
    bio = State()
    email = State()


@survey_rt.message(Command('stop'))
async def stop(msg: types.Message, state: FSMContext):
    kb = ReplyKeyboardRemove()
    await msg.answer('Опрос присотановлен', reply_markup=kb)
    await state.clear()


@survey_rt.message(Command('join_team'))
async def survey(msg: types.Message, state: FSMContext):
    kb = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text='/stop')]])
    await state.set_state(Survey.name)
    await msg.reply(text='Вы можете присоединиться в команду по озвучке аниме! Для этого пройдите анкету')
    await msg.answer('Нажмите стоп, чтобы остановить опрос', reply_markup=kb)
    await msg.answer('Ваше имя?')

@survey_rt.message(Survey.name)
async def name(msg: types.Message, state: FSMContext):
    def is_name_real(name_user):
        for i in name_user:
            if i.lower() in 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэяячсмитьбю':
                return True
            else:
                return False
    if ((len(msg.text) < 3) or (is_name_real(msg.text)))==False:
        await msg.answer('Вводите реальное имя')
    else:
        await state.update_data(name=msg.text)
        await state.set_state(Survey.age)
        await msg.answer(text='Хорошо. Теперь назовите число ваших полных лет')


@survey_rt.message(Survey.age)
async def age(msg: types.Message, state: FSMContext):
    if int(msg.text) < 16:
        await msg.answer('Извините, Вы слишком молоды')
    elif int(msg.text) > 80:
        await msg.answer('ХАХАХХААХА, как смешно')
    else:
        await state.update_data(age=msg.text)
        await state.set_state(Survey.bio)
        await msg.answer('Ага, а теперь кратко напишите о себе')


@survey_rt.message(Survey.bio)
async def bio(msg: types.Message, state: FSMContext):
    await state.update_data(bio=msg.text)
    await state.set_state(Survey.email)
    await msg.answer(text='Оставьте свой email, чтобы мы пересмотрели Вашу анкету')


@survey_rt.message(Survey.email)
async def email(msg: types.Message, state: FSMContext):
    await state.update_data(email=msg.text)
    await msg.answer('Все. Ваша анкета успешно сохранилась!')












