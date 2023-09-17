from aiogram import Router, F
from aiogram.types import Message
from config.config import Config, load_config
from sqlalchemy.ext.asyncio import AsyncSession
from database import Horo
from sqlalchemy import select
from keyboards.zodiac_keyboard import get_timeday_1o_buttons, get_timeday_2t_buttons, get_timeday_3b_buttons, get_timeday_4r_buttons, get_timeday_5l_buttons, get_timeday_6d_buttons, get_timeday_7v_buttons, get_timeday_8s_buttons, get_timeday_9s_buttons, get_timeday_10k_buttons, get_timeday_11v_buttons, get_timeday_12r_buttons

router = Router()

Config = load_config()

@router.message(F.text == ('♈️ Овен'))
async def user_horo_today_cmd(msg: Message, session: AsyncSession):
    horo_today = await session.execute(select(Horo.horo_today).where(Horo.zodiac == 'Овен'))
    await session.close()
    for horo in horo_today:
        horo_today = horo[0]
    
    await msg.answer(horo_today,
                     reply_markup=get_timeday_1o_buttons(), parse_mode='HTML')
    
@router.message(F.text.startswith('♉️ Телец'))
async def user_horo_today(msg: Message, session: AsyncSession):
    horo_today = await session.execute(select(Horo.horo_today).where(Horo.zodiac == 'Телец'))
    await session.close()
    for horo in horo_today:
        horo_today = horo[0]
    
    await msg.answer(horo_today,
                     reply_markup=get_timeday_2t_buttons(), parse_mode='HTML')
    
@router.message(F.text.startswith('♊️ Близнецы'))
async def user_horo_today(msg: Message, session: AsyncSession):
    horo_today = await session.execute(select(Horo.horo_today).where(Horo.zodiac == 'Близнецы'))
    await session.close()
    for horo in horo_today:
        horo_today = horo[0]
    
    await msg.answer(horo_today,
                     reply_markup=get_timeday_3b_buttons(), parse_mode='HTML')
    
@router.message(F.text.startswith('♋️ Рак'))
async def user_horo_today(msg: Message, session: AsyncSession):
    horo_today = await session.execute(select(Horo.horo_today).where(Horo.zodiac == 'Рак'))
    await session.close()
    for horo in horo_today:
        horo_today = horo[0]
    
    await msg.answer(horo_today,
                     reply_markup=get_timeday_4r_buttons(), parse_mode='HTML')
    
@router.message(F.text.startswith('♌️ Лев'))
async def user_horo_today(msg: Message, session: AsyncSession):
    horo_today = await session.execute(select(Horo.horo_today).where(Horo.zodiac == 'Лев'))
    await session.close()
    for horo in horo_today:
        horo_today = horo[0]
    
    await msg.answer(horo_today,
                     reply_markup=get_timeday_5l_buttons(), parse_mode='HTML')
    
@router.message(F.text.startswith('♍️ Дева'))
async def user_horo_today(msg: Message, session: AsyncSession):
    horo_today = await session.execute(select(Horo.horo_today).where(Horo.zodiac == 'Дева'))
    await session.close()
    for horo in horo_today:
        horo_today = horo[0]
    
    await msg.answer(horo_today,
                     reply_markup=get_timeday_6d_buttons(), parse_mode='HTML')
    
@router.message(F.text.startswith('♎️ Весы'))
async def user_horo_today(msg: Message, session: AsyncSession):
    horo_today = await session.execute(select(Horo.horo_today).where(Horo.zodiac == 'Весы'))
    await session.close()
    for horo in horo_today:
        horo_today = horo[0]
    
    await msg.answer(horo_today,
                     reply_markup=get_timeday_7v_buttons(), parse_mode='HTML')
    
@router.message(F.text.startswith('♏️ Скорпион'))
async def user_horo_today(msg: Message, session: AsyncSession):
    horo_today = await session.execute(select(Horo.horo_today).where(Horo.zodiac == 'Скорпион'))
    await session.close()
    for horo in horo_today:
        horo_today = horo[0]
    
    await msg.answer(horo_today,
                     reply_markup=get_timeday_8s_buttons(), parse_mode='HTML')
    
@router.message(F.text.startswith('♐️ Стрелец'))
async def user_horo_today(msg: Message, session: AsyncSession):
    horo_today = await session.execute(select(Horo.horo_today).where(Horo.zodiac == 'Стрелец'))
    await session.close()
    for horo in horo_today:
        horo_today = horo[0]
    
    await msg.answer(horo_today,
                     reply_markup=get_timeday_9s_buttons(), parse_mode='HTML')
    
@router.message(F.text.startswith('♑️ Козерог'))
async def user_horo_today(msg: Message, session: AsyncSession):
    horo_today = await session.execute(select(Horo.horo_today).where(Horo.zodiac == 'Козерог'))
    await session.close()
    for horo in horo_today:
        horo_today = horo[0]
    
    await msg.answer(horo_today,
                     reply_markup=get_timeday_10k_buttons(), parse_mode='HTML')
    
@router.message(F.text.startswith('♒️ Водолей'))
async def user_horo_today(msg: Message, session: AsyncSession):
    horo_today = await session.execute(select(Horo.horo_today).where(Horo.zodiac == 'Водолей'))
    await session.close()
    for horo in horo_today:
        horo_today = horo[0]
    
    await msg.answer(horo_today,
                     reply_markup=get_timeday_11v_buttons(), parse_mode='HTML')
    
@router.message(F.text.startswith('♓️ Рыбы'))
async def user_horo_today(msg: Message, session: AsyncSession):
    horo_today = await session.execute(select(Horo.horo_today).where(Horo.zodiac == 'Рыбы'))
    await session.close()
    for horo in horo_today:
        horo_today = horo[0]
    
    await msg.answer(horo_today,
                     reply_markup=get_timeday_12r_buttons(), parse_mode='HTML')