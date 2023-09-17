import logging
import os
import random
from aiogram import Router, F, Bot, types
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from config.config import Config, load_config
from aiogram.exceptions import TelegramBadRequest
from sqlalchemy.ext.asyncio import AsyncSession
from database import Taro, NumberMagic, Compatibility, Channel, User
from sqlalchemy import select, delete
from .taro.string_taro_name import string_taro_name
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from handlers import zodiac
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from keyboards.main_keyboard import get_start_buttons, get_exit_menu_buttons
from keyboards.zodiac_keyboard import get_zodiac_buttons
from keyboards.taro_keyboard import get_inline_taro_buttons
from keyboards.vostok_horo_keyboard import get_inline_vostok_horo_buttons
from keyboards.number_keyboard import get_inline_numbers_buttons
from keyboards.compatibility_keyboard import get_inline_compatibility_buttons
from keyboards.admin_start_keyboard import get_admin_start_buttons, get_admin_buttons, get_inline_channel_admin_buttons_delete, get_choise_media, get_end_send_ras, get_nemeling_silk

router = Router()

Config = load_config()

scheduler = AsyncIOScheduler()

logger = logging.getLogger(__name__)

class CompatibilityZodiac(StatesGroup):
    first_zodiac = State()
    second_zodiac = State()
    
class CreatePosts(StatesGroup):
    text = State()
    choise = State()
    photo = State()
    video = State()
    data1 = State()
    end = State()

@router.message(Command('start'))
async def start_cmd(msg: Message):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        await msg.answer('Приветствую тебя, админ!',
                         reply_markup=get_admin_start_buttons())
    else:
        main_photo = FSInputFile(r'c:\Users\Роман\Pictures\Saved Pictures\photo_2023-01-18_01-40-17.jpg')
        await msg.answer_photo(main_photo, caption='Привет! Я - гороскоп бот ✨\n\nЯ предскажу твой день на завтра, проверю вашу совместимость с партнером, а также сделаю расклад на картах Таро 🔮',
                        reply_markup=get_start_buttons())

@router.message(Command('horo'))
async def main_cmd(msg: Message):
    await msg.answer('🔮 Выбери свой знак зодиака, чтобы узнать гороскоп на сегодня',
                     reply_markup=get_zodiac_buttons())
    
@router.message(Command('taro'))
async def main_cmd(msg: Message):
    main_photo = FSInputFile(r'c:\Users\Роман\Pictures\Saved Pictures\photo_2023-08-31_14-47-52.jpg')
    await msg.answer_photo(main_photo, caption='🀄️ Выбери карту, которая понравилась больше всего 👀',
                           reply_markup=get_inline_taro_buttons())
    
@router.message(Command('numbers'))
async def main_cmd(msg: Message):
    main_photo = FSInputFile(r'c:\Users\Роман\Pictures\Saved Pictures\617bd66a70e01e4c9c0fde5475b4e632fe9dij.jpg')
    await msg.answer_photo(main_photo, caption='🟣 Магия чисел\n\n🎲 Выберите любое число из списка ниже и получите свое предсказание',
                           reply_markup=get_inline_numbers_buttons())

@router.message(Command('eastern'))
async def main_cmd(msg: Message):
    main_photo_horo_vostok = FSInputFile(r'c:\Users\Роман\Pictures\Saved Pictures\photo_2023-09-04_14-50-59.jpg')
    await msg.answer_photo(main_photo_horo_vostok, caption='🎲 Выберете животное по году вашего рождения и получите предсказание на год',
                           reply_markup=get_inline_vostok_horo_buttons())
    
@router.message(Command('compatibility'))
async def main_cmd(msg: Message, state=FSMContext):
    main_photo = FSInputFile(r'c:\Users\Роман\Pictures\Saved Pictures\photo_2023-09-06_18-05-53.jpg')
    await msg.answer_photo(main_photo, caption='💟 Совместимость\n\nМежду ___ и ___\n\n🎲 Выберите два знака зодиака',
                           reply_markup=get_inline_compatibility_buttons())
    await state.set_state(CompatibilityZodiac.first_zodiac)
    
@router.message(Command('cancel'))
async def main_cmd(msg: Message):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        await msg.answer('🏠 Вы в главном меню',
                         reply_markup=get_admin_start_buttons())
    else:
        await msg.answer('🏠 Вы в главном меню',
                        reply_markup=get_start_buttons())

@router.message(F.text == '✍🏻 Изменить каналы')
async def edit_channel_cmd(msg: Message):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        await msg.answer('Выберите действие',
                         reply_markup=get_admin_buttons())
        
@router.message(F.text == '✍🏻 Добавить рассылку')
async def edit_message_echo_cmd(msg: Message, state=FSMContext):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        await msg.answer('Напишите текст рассылки')
        await state.set_state(CreatePosts.text)
        
@router.message(F.text == '🗑 Удалить канал')
async def edit_channel_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
       
        silk1 = await session.execute(select(Channel.silk).where(Channel.id == 1))
        silk2 = await session.execute(select(Channel.silk).where(Channel.id == 2))
        silk3 = await session.execute(select(Channel.silk).where(Channel.id == 3))
        silk4 = await session.execute(select(Channel.silk).where(Channel.id == 4))
        silk5 = await session.execute(select(Channel.silk).where(Channel.id == 5))
        
        for silk in silk1:
            silk1 = silk[0]
        for silk in silk2:
            silk2 = silk[0]
        for silk in silk3:
            silk3 = silk[0]
        for silk in silk4:
            silk4 = silk[0]
        for silk in silk5:
            silk5 = silk[0]
        
        if str(silk1).startswith('<sqlalchemy.engine.result'):
            silk1 = 'Пусто'
        else:
            pass
        if str(silk2).startswith('<sqlalchemy.engine.result'):
            silk2 = 'Пусто'
        else:
            pass
        if str(silk3).startswith('<sqlalchemy.engine.result'):
            silk3 = 'Пусто'
        else:
            pass
        if str(silk4).startswith('<sqlalchemy.engine.result'):
            silk4 = 'Пусто'
        else:
            pass
        if str(silk5).startswith('<sqlalchemy.engine.result'):
            silk5 = 'Пусто'
        else:
            pass
        await session.commit()
        await msg.answer(text='Выберите канал для удаления', reply_markup=get_exit_menu_buttons())
        await msg.answer(f'1. {silk1}\n2. {silk2}\n3. {silk3}\n4. {silk4}\n5. {silk5}',
                         reply_markup=get_inline_channel_admin_buttons_delete())
        

@router.message(F.text == '➕ Мои каналы')
async def edit_channel_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        silk1 = await session.execute(select(Channel.silk).where(Channel.id == 1))
        silk2 = await session.execute(select(Channel.silk).where(Channel.id == 2))
        silk3 = await session.execute(select(Channel.silk).where(Channel.id == 3))
        silk4 = await session.execute(select(Channel.silk).where(Channel.id == 4))
        silk5 = await session.execute(select(Channel.silk).where(Channel.id == 5))
        
        for silk in silk1:
            silk1 = silk[0]
        for silk in silk2:
            silk2 = silk[0]
        for silk in silk3:
            silk3 = silk[0]
        for silk in silk4:
            silk4 = silk[0]
        for silk in silk5:
            silk5 = silk[0]
        
        if str(silk1).startswith('<sqlalchemy.engine.result'):
            silk1 = 'Пусто'
        else:
            pass
        if str(silk2).startswith('<sqlalchemy.engine.result'):
            silk2 = 'Пусто'
        else:
            pass
        if str(silk3).startswith('<sqlalchemy.engine.result'):
            silk3 = 'Пусто'
        else:
            pass
        if str(silk4).startswith('<sqlalchemy.engine.result'):
            silk4 = 'Пусто'
        else:
            pass
        if str(silk5).startswith('<sqlalchemy.engine.result'):
            silk5 = 'Пусто'
        else:
            pass
        await session.commit()
        await msg.answer(f'Порядок каналов\n1. {silk1}\n2. {silk2}\n3. {silk3}\n4. {silk4}\n5. {silk5}')
        await msg.answer("Отправь мне сообщение с командой 'Добавить канал', с указанием порядкового номера канала, ссылки, айди - через пробелы\nНапример: Добавить канал 1 https://t.me/channel_jomaska -1001726045986",
                         reply_markup=get_exit_menu_buttons())
        await msg.answer("Отправь мне сообщение с командой 'Добавить рекламный канал', с указанием ссылки\nНапример: Добавить рекламный канал https://t.me/channel_jomaska",
                         reply_markup=get_exit_menu_buttons())

@router.message(F.text.startswith('Добавить канал'))
async def edit_channel_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        text = msg.text
        text = text.replace("Добавить канал", '')
        text = text.split(' ')
        await msg.answer(f'Номер канала: {text[1]}\nСсылка на канал: {text[2]}\nАйди канала: {text[3]}')
        try:
            channel = Channel(
            id=int(text[1]),
            silk=str(text[2]),
            id_channel=str(text[3])
            )
            await session.merge(channel)
            await session.commit()
        except:
            await msg.answer('Ошибка!')
        await msg.answer(f'Добавлено!')
    
@router.message(F.text.startswith('Добавить рекламный канал'))
async def edit_channel_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        text = msg.text
        text = text.replace("Добавить рекламный канал", '')
        text = text.split(' ')
        await msg.answer(f'Номер канала: 6\nСсылка на канал: {text[1]}')
        try:
            channel = Channel(
            id=6,
            silk=str(text[1])
            )
            await session.merge(channel)
            await session.commit()
        except:
            await msg.answer('Ошибка!')
        await msg.answer(f'Добавлено!')
    
@router.message(F.text == '🔮 Гороскоп')
async def horo_cmd(msg: Message):
    await msg.answer('🔮 Выбери свой знак зодиака, чтобы узнать гороскоп на сегодня',
                     reply_markup=get_zodiac_buttons())

@router.message(F.text == '🕯 ОСОБЫЕ ВОЗМОЖНОСТИ')
async def horo_cmd(msg: Message):
    await msg.answer('🕯 <b>Желаешь нечто большее?</b>', parse_mode='HTML',
                     reply_markup=get_exit_menu_buttons())
    await msg.answer('🕯 Тогда нажми на кнопку ниже и получи уникальные возможности, которые доступны только здесь',
                     reply_markup=get_nemeling_silk())
    #await msg.answer('Без этого сообщения кнопка выхода в меню не может появиться', reply_markup=get_exit_menu_buttons())

@router.message(F.text == '🏠 Выйти в меню')
async def exit_cmd(msg: Message):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        await msg.answer('🏠 Вы в главном меню',
                         reply_markup=get_admin_start_buttons())
    else:
        await msg.answer('🏠 Вы в главном меню',
                        reply_markup=get_start_buttons())

@router.message(F.text == '🏵 Восточный гороскоп')
async def vostok_horo_cmd(msg: Message):
    main_photo_horo_vostok = FSInputFile(r'c:\Users\Роман\Pictures\Saved Pictures\photo_2023-09-04_14-50-59.jpg')
    await msg.answer_photo(main_photo_horo_vostok, caption='🎲 Выберете животное по году вашего рождения и получите предсказание на год',
                           reply_markup=get_inline_vostok_horo_buttons())

@router.message(F.text == '🀄️ Карты таро')
async def taro_cmd_main(msg: Message):
    main_photo = FSInputFile(r'c:\Users\Роман\Pictures\Saved Pictures\photo_2023-08-31_14-47-52.jpg')
    await msg.answer_photo(main_photo, caption='🀄️ Выбери карту, которая понравилась больше всего 👀',
                           reply_markup=get_inline_taro_buttons())

@router.message(F.text == '🟣 Магия чисел')
async def taro_cmd_main(msg: Message):
    main_photo = FSInputFile(r'c:\Users\Роман\Pictures\Saved Pictures\617bd66a70e01e4c9c0fde5475b4e632fe9dij.jpg')
    await msg.answer_photo(main_photo, caption='🟣 Магия чисел\n\n🎲 Выберите любое число из списка ниже и получите свое предсказание',
                           reply_markup=get_inline_numbers_buttons())

@router.message(F.text == '💟 Совместимость')
async def taro_cmd_main(msg: Message, state=FSMContext):
    main_photo = FSInputFile(r'c:\Users\Роман\Pictures\Saved Pictures\photo_2023-09-06_18-05-53.jpg')
    await msg.answer_photo(main_photo, caption='💟 Совместимость\n\nМежду ___ и ___\n\n🎲 Выберите два знака зодиака',
                           reply_markup=get_inline_compatibility_buttons())
    await state.set_state(CompatibilityZodiac.first_zodiac)

@router.callback_query(F.data == 'delete')
async def delete_inl(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    
    async def check_sub(channel_id: int) -> bool:
        try:
            channel = await session.execute(select(Channel.id_channel).where(Channel.id == channel_id))
            text = ''.join(str(c[0]) for c in channel)
            user = await bot.get_chat_member(chat_id=text, user_id=callback.from_user.id)
            return user.status != "left"
        except TelegramBadRequest:
            if text == '':
                return True
            return False
        
    sub1 = await check_sub(1)
    sub2 = await check_sub(2)
    sub3 = await check_sub(3)
    sub4 = await check_sub(4)
    sub5 = await check_sub(5)
    
    if all([sub1, sub2, sub3, sub4, sub5]): 
        await callback.message.delete()
        await callback.message.answer('Теперь со мной можно работать')
        if callback.from_user.id == int(Config.tg_bot.admin_id):
            await bot.send_message('Приветствую тебя, админ!',
                         reply_markup=get_admin_start_buttons(), chat_id=callback.from_user.id)
        else:
            main_photo = FSInputFile(r'c:\Users\Роман\Pictures\Saved Pictures\photo_2023-01-18_01-40-17.jpg')
            await bot.send_photo(photo=main_photo, caption='Привет! Я - гороскоп бот ✨\n\nЯ предскажу твой день на завтра, проверю вашу совместимость с партнером, а также сделаю расклад на картах Таро 🔮',
                        reply_markup=get_start_buttons(), chat_id=callback.from_user.id)
    else:
        await callback.answer("Ты не подписался!", show_alert=True)
        
@router.callback_query(F.data == 'taro_random')
async def taro_send(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    
    random_taro_name = random.choice(string_taro_name)
    
    photo_silk = await session.execute(select(Taro.silk).where(Taro.name == random_taro_name))
    desc_photo = await session.execute(select(Taro.desc).where(Taro.name == random_taro_name))
    name_photo = await session.execute(select(Taro.name).where(Taro.name == random_taro_name))
    
    await session.commit()
    
    for silk in photo_silk:
        photo_silk = silk[0]

    for desc in desc_photo:
        desc_photo = desc[0]    
        
    for name in name_photo:
        name_photo = name[0]    

    photo = FSInputFile(photo_silk)
    await bot.send_photo(photo=photo, caption=desc[0], chat_id=callback.from_user.id,
                         reply_markup=get_exit_menu_buttons())
    await callback.answer()

@router.callback_query(F.data == 'numb_random')
async def numb_send(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    
    random_numb_id = random.randint(1, 50)
    
    desc_numb = await session.execute(select(NumberMagic.desc).where(NumberMagic.id == random_numb_id))
    
    # add_number1 = "Древняя мудрость глубоко скрыта в твоей ДНК, раскрой ее и обретешь невероятную силу."
    # add_number2 = "Символ на твоей руке станет источником твоей защиты и удачи на пути к успеху."
    # add_number3 = "В ближайшее время ты получишь письмо, которое изменит твою жизнь навсегда."
    # add_number4 = "Получишь неожиданный подарок, который откроет дверь к большому успеху."
    # add_number5 = "Встреча с незнакомцем приведет к важному повороту в твоей жизни."
    # add_number6 = "Находка на улице принесет тебе не только материальное благополучие, но и душевное удовлетворение."
    # add_number7 = "Тебя ждет настоящая любовь, которая озарит твою жизнь и принесет гармонию."
    # add_number8 = "Ты скоро найдешь потерянное, что даст тебе ответы на многие вопросы."
    # add_number9 = "Загадка, с которой ты столкнешься, поможет разгадать секретную тайну твоей семьи."
    # add_number10 = "Ты скоро осуществишь долгожданную мечту, благодаря неожиданной помощи из неожиданного источника."


    # number1 = NumberMagic(
    #     id=41,
    #     desc=add_number1
    # )
    # number2 = NumberMagic(
    #     id=42,
    #     desc=add_number2
    # )
    # number3 = NumberMagic(
    #     id=3,
    #     desc=add_number3
    # )
    # number4 = NumberMagic(
    #     id=4,
    #     desc=add_number4
    # )
    # number5 = NumberMagic(
    #     id=5,
    #     desc=add_number5
    # )
    # number6 = NumberMagic(
    #     id=6,
    #     desc=add_number6
    # )
    # number7 = NumberMagic(
    #     id=7,
    #     desc=add_number7
    # )
    # number8 = NumberMagic(
    #     id=8,
    #     desc=add_number8
    # )
    # number9 = NumberMagic(
    #     id=9,
    #     desc=add_number9
    # )
    # number10 = NumberMagic(
    #     id=10,
    #     desc=add_number10
    # )
    
    # # await session.merge(number1)
    # # await session.merge(number2)
    # await session.merge(number3)
    # await session.merge(number4)
    # await session.merge(number5)
    # await session.merge(number6)
    # await session.merge(number7)
    # await session.merge(number8)
    # await session.merge(number9)
    # await session.merge(number10)
    # await session.commit()
    
    
    
    await session.commit()
    
    for desc in desc_numb:
        desc_numb = desc[0]    
    dop = '🔮 Ваше предсказание\n\n💬 '
    await bot.send_message(text=dop+desc[0], chat_id=callback.from_user.id,
                         reply_markup=get_exit_menu_buttons())
    await callback.answer()
       
@router.callback_query(CompatibilityZodiac.first_zodiac, F.data.in_(zodiac))
async def compatibility(callback: CallbackQuery, state=FSMContext):
    
    await state.update_data(first_zodiac=callback.data)
    await callback.answer('✅ Добавлено')
    await callback.message.edit_caption(caption=f'💟 Совместимость\n\nМежду {callback.data} и ___\n\n🎲 Выберите два знака зодиака',
                                        reply_markup=get_inline_compatibility_buttons())
    # await bot.edit_message_text(text="Теперь, выберите второй знак зодиака",
    #                     chat_id=callback.message.chat.id,
    #                     reply_markup=get_inline_compatibility_buttons())
    # await bot.send_message(text="Теперь, выберите второй знак зодиака",
    #                        chat_id=callback.from_user.id,
    #                        reply_markup=get_inline_compatibility_buttons())
    
    await state.set_state(CompatibilityZodiac.second_zodiac)
    # photo_silk = await session.execute(select(Taro.silk).where(Taro.name == random_taro_name))
    # desc_photo = await session.execute(select(Taro.desc).where(Taro.name == random_taro_name))
    # name_photo = await session.execute(select(Taro.name).where(Taro.name == random_taro_name))
    
    # await session.close()
    
    # for silk in photo_silk:
    #     photo_silk = silk[0]

    # for desc in desc_photo:
    #     desc_photo = desc[0]    
        
    # for name in name_photo:
    #     name_photo = name[0]    

    # photo = FSInputFile(photo_silk)
    # main_photo = FSInputFile(r'c:\Users\Роман\Pictures\Saved Pictures\photo_2023-09-06_18-05-53.jpg')
    
    # await callback.message.delete()
    # await bot.send_photo(photo=main_photo, caption='💟 Совместимость\n\nМежду Овен и ___\n\n🎲 Выберите два знака зодиака')
    # number = 1
    # await bot.send_photo(photo=photo, caption=desc[0], chat_id=callback.from_user.id)
    # await callback.answer()

@router.callback_query(CompatibilityZodiac.second_zodiac, F.data.in_(zodiac))
async def compatibility(callback: CallbackQuery, session: AsyncSession, state=FSMContext):
    user_data = await state.get_data()
    first = user_data['first_zodiac']
    second = callback.data

    id = await session.execute(select(Compatibility.id).where(Compatibility.first_zodiac == first, Compatibility.second_zodiac == second))
    desc = await session.execute(select(Compatibility.desc).where(Compatibility.first_zodiac == first, Compatibility.second_zodiac == second))
    channel = await session.execute(select(Channel.silk).where(Channel.id == 6))
    
    text = ''.join(str(c[0]) for c in channel)
    
    for id1 in id:
        id = id1[0]
        
    for desc1 in desc:
        desc = desc1[0]
        
    if str(desc).startswith('<sqlalchemy.engine.result'):
        id = await session.execute(select(Compatibility.id).where(Compatibility.first_zodiac == second, Compatibility.second_zodiac == first))
        desc = await session.execute(select(Compatibility.desc).where(Compatibility.first_zodiac == second, Compatibility.second_zodiac == first))

        for id1 in id:
            id = id1[0]
        for desc1 in desc:
            desc = desc1[0]
    else:
        pass
    await session.commit()
    await callback.answer('✅ Добавлено')
    await callback.message.edit_caption(caption=f'💟 Совместимость\n\nМежду {first} и {callback.data}\n\n{id}. {desc}')
    await callback.message.answer(f'Подпишись на <a href="{text}">канал</a>', parse_mode='HTML',reply_markup=get_exit_menu_buttons())
    await state.clear()

@router.callback_query(F.data == 'delete_silk_and_id_1')
async def taro_send(callback: CallbackQuery, session: AsyncSession):
    
    delt = delete(Channel).where(Channel.id == 1)
    
    await session.execute(delt)

    await session.commit()
    await callback.answer(f'Успешно удален 1 канал')
    
@router.callback_query(F.data == 'delete_silk_and_id_2')
async def taro_send(callback: CallbackQuery, session: AsyncSession):
    
    delt = delete(Channel).where(Channel.id == 2)
    
    await session.execute(delt)

    await session.commit()
    await callback.answer(f'Успешно удален 2 канал')
    
@router.callback_query(F.data == 'delete_silk_and_id_3')
async def taro_send(callback: CallbackQuery, session: AsyncSession):
    
    delt = delete(Channel).where(Channel.id == 3)
    
    await session.execute(delt)

    await session.commit()
    await callback.answer(f'Успешно удален 3 канал')
    
@router.callback_query(F.data == 'delete_silk_and_id_4')
async def taro_send(callback: CallbackQuery, session: AsyncSession):
    
    delt = delete(Channel).where(Channel.id == 4)
    
    await session.execute(delt)

    await session.commit()
    await callback.answer(f'Успешно удален 4 канал')
    
@router.callback_query(F.data == 'delete_silk_and_id_5')
async def taro_send(callback: CallbackQuery, session: AsyncSession):
    
    delt = delete(Channel).where(Channel.id == 5)
    
    await session.execute(delt)

    await session.commit()
    await callback.answer(f'Успешно удален 5 канал')
    
@router.message(CreatePosts.text)
async def compatibility(msg: Message, state=FSMContext):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        await state.update_data(text=msg.text)
        await state.set_state(CreatePosts.choise)
        await msg.answer('Выберите, какое медиа будет использовано', reply_markup=get_choise_media())
        
@router.callback_query(CreatePosts.choise, F.data == 'photo_media')
async def compatibility(callback: CallbackQuery, state=FSMContext):
    if callback.from_user.id == int(Config.tg_bot.admin_id):
        await callback.answer('Отправьте фото', show_alert=True)
        await state.set_state(CreatePosts.photo)

@router.callback_query(CreatePosts.choise, F.data == 'video_media')
async def compatibility(callback: CallbackQuery, state=FSMContext):
    if callback.from_user.id == int(Config.tg_bot.admin_id):
        await callback.answer('Отправьте видео', show_alert=True)
        await state.set_state(CreatePosts.video)
        
@router.callback_query(CreatePosts.choise, F.data == 'none_media')
async def compatibility(callback: CallbackQuery, state=FSMContext):
    if callback.from_user.id == int(Config.tg_bot.admin_id):
        await callback.answer('Напишите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ', show_alert=True)
        await state.set_state(CreatePosts.data1)
        
@router.message(CreatePosts.photo)
async def compatibility(msg: Message, bot: Bot, state=FSMContext):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        await state.update_data(photo=msg.text)

        photo = msg.photo[-1].file_id
        file = await bot.get_file(photo)
        file_path = file.file_path
        saved_file_path = rf"c:\Users\Роман\Pictures\Saved Pictures/{photo}.jpg"
        
        await state.update_data(photo=saved_file_path)
        await bot.download_file(file_path, saved_file_path)
        await state.set_state(CreatePosts.data1)
        await msg.answer('Напишите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ')
        
@router.message(CreatePosts.video)
async def compatibility(msg: Message, bot: Bot, state=FSMContext):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        await state.update_data(video=msg.text)
        video = msg.video.file_id
        
        file = await bot.get_file(video)
        file_path = file.file_path
        saved_file_path = rf"c:\Users\Роман\Pictures\Saved Pictures/{video}.mp4"
        
        await state.update_data(video=saved_file_path)
        await bot.download_file(file_path, saved_file_path)
        await state.set_state(CreatePosts.data1)
        await msg.answer('Напишите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ')
            
@router.message(CreatePosts.data1)
async def compatibility(msg: Message, bot: Bot, session: AsyncSession, state=FSMContext):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        await state.update_data(data1=msg.text)
        user_data = await state.get_data()
        try:
            video = user_data['video']
        except:
            video = ''
        try:
            photo = user_data['photo']
        except:
            photo = ''
        text = user_data['text']
        data1 = user_data['data1']
        #date = datetime.strptime(data1, '%d.%m.%Y %H:%M')
        #scheduler.add_job(send_broadcast_message, 'date', run_date=date, args=[text, session, bot, photo, video])
        
        # await msg.answer('Рассылка запланирована на указанную дату.')
        # try:
        #     scheduler.start()
        # except:
        #     pass
        n = '\n\n'
        create = 'Создать рассылку?'
        if photo != '':
            file1 = FSInputFile(photo)
            await bot.send_photo(photo=file1, caption=text, chat_id=Config.tg_bot.admin_id, parse_mode='HTML')
            await bot.send_message(text=data1 + n + create, chat_id=Config.tg_bot.admin_id, reply_markup=get_end_send_ras())
        if video != '':
            file1 = FSInputFile(video)
            await bot.send_video(video=file1, caption=text, chat_id=Config.tg_bot.admin_id, parse_mode='HTML')
            await bot.send_message(text=data1 + n + create, chat_id=Config.tg_bot.admin_id, reply_markup=get_end_send_ras())
        if photo == '' and video == '':
            await bot.send_message(text=text, chat_id=Config.tg_bot.admin_id, parse_mode='HTML')
            await bot.send_message(text=data1 + n + create, chat_id=Config.tg_bot.admin_id, reply_markup=get_end_send_ras())
        #await bot.send_message()
        
        await state.set_state(CreatePosts.end)

@router.callback_query(CreatePosts.end, F.data == 'end_ras_yes')
async def compatibility(callback: CallbackQuery, bot: Bot, session: AsyncSession, state=FSMContext):        
    if callback.from_user.id == int(Config.tg_bot.admin_id):
        user_data = await state.get_data()
        try:
            video = user_data['video']
        except:
            video = ''
        try:
            photo = user_data['photo']
        except:
            photo = ''
        text = user_data['text']
        data1 = user_data['data1']
        date = datetime.strptime(data1, '%d.%m.%Y %H:%M')
        scheduler.add_job(send_broadcast_message, 'date', run_date=date, args=[text, session, bot, photo, video])
        
        await callback.message.edit_text('Рассылка запланирована на указанную дату')
        #await callback.answer('Рассылка запланирована на указанную дату', show_alert=True)
        try:
            scheduler.start()
        except:
            pass
        await state.clear()
        
@router.callback_query(CreatePosts.end, F.data == 'end_ras_no')
async def compatibility(callback: CallbackQuery, bot: Bot, session: AsyncSession, state=FSMContext):        
    if callback.from_user.id == int(Config.tg_bot.admin_id):
        await callback.message.edit_text('Рассылка отменена')
        #await callback.answer('Рассылка отменена.', show_alert=True)
        await state.clear()
    
async def send_broadcast_message(text, session, bot, photo, video):
    users = (await session.scalars(select(User.user_id))).fetchall()
    session: AsyncSession
    await session.close()
    for user in users:
        try:
            if photo != '':
                file1 = FSInputFile(photo)
                await bot.send_photo(photo=file1, caption=text, chat_id=user, parse_mode='HTML')
            if video != '':
                file1 = FSInputFile(video)
                await bot.send_video(video=file1, caption=text, chat_id=user, parse_mode='HTML')
            if photo == '' and video == '':
                await bot.send_message(text=text, chat_id=user, parse_mode='HTML')
        except:
            logging.info(f'\n\nError {user} send message\n')
    try:
        os.remove(photo)
    except:
        pass
    try:
        os.remove(video)
    except:
        pass