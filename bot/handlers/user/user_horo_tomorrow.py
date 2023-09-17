from aiogram import Router, F
from aiogram.types import Message
from config.config import Config, load_config
from sqlalchemy.ext.asyncio import AsyncSession
from database import Horo
from sqlalchemy import select

router = Router()

Config = load_config()

@router.message(F.text == ('♈️ Завтра'))
async def user_horo_tomorrow_cmd(msg: Message, session: AsyncSession):
    horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Овен'))
    await session.close()
    for horo in horo_tomorrow:
        horo_tomorrow = horo[0]
    
    await msg.answer(horo_tomorrow, parse_mode='HTML')
    
@router.message(F.text.startswith('♉️ Завтра'))
async def user_horo_tomorrow(msg: Message, session: AsyncSession):
    horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Телец'))
    await session.close()
    for horo in horo_tomorrow:
        horo_tomorrow = horo[0]
    
    await msg.answer(horo_tomorrow, parse_mode='HTML')
    
@router.message(F.text.startswith('♊️ Завтра'))
async def user_horo_tomorrow(msg: Message, session: AsyncSession):
    horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Близнецы'))
    await session.close()
    for horo in horo_tomorrow:
        horo_tomorrow = horo[0]
    
    await msg.answer(horo_tomorrow, parse_mode='HTML')
    
@router.message(F.text.startswith('♋️ Завтра'))
async def user_horo_tomorrow(msg: Message, session: AsyncSession):
    horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Рак'))
    await session.close()
    for horo in horo_tomorrow:
        horo_tomorrow = horo[0]
    
    await msg.answer(horo_tomorrow, parse_mode='HTML')
    
@router.message(F.text.startswith('♌️ Завтра'))
async def user_horo_tomorrow(msg: Message, session: AsyncSession):
    horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Лев'))
    await session.close()
    for horo in horo_tomorrow:
        horo_tomorrow = horo[0]
    
    await msg.answer(horo_tomorrow, parse_mode='HTML')
    
@router.message(F.text.startswith('♍️ Завтра'))
async def user_horo_tomorrow(msg: Message, session: AsyncSession):
    horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Дева'))
    await session.close()
    for horo in horo_tomorrow:
        horo_tomorrow = horo[0]
    
    await msg.answer(horo_tomorrow, parse_mode='HTML')
    
@router.message(F.text.startswith('♎️ Завтра'))
async def user_horo_tomorrow(msg: Message, session: AsyncSession):
    horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Весы'))
    await session.close()
    for horo in horo_tomorrow:
        horo_tomorrow = horo[0]
    
    await msg.answer(horo_tomorrow, parse_mode='HTML')
    
@router.message(F.text.startswith('♏️ Завтра'))
async def user_horo_tomorrow(msg: Message, session: AsyncSession):
    horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Скорпион'))
    await session.close()
    for horo in horo_tomorrow:
        horo_tomorrow = horo[0]
    
    await msg.answer(horo_tomorrow, parse_mode='HTML')
    
@router.message(F.text.startswith('♐️ Завтра'))
async def user_horo_tomorrow(msg: Message, session: AsyncSession):
    horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Стрелец'))
    await session.close()
    for horo in horo_tomorrow:
        horo_tomorrow = horo[0]
    
    await msg.answer(horo_tomorrow, parse_mode='HTML')
    
@router.message(F.text.startswith('♑️ Завтра'))
async def user_horo_tomorrow(msg: Message, session: AsyncSession):
    horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Козерог'))
    await session.close()
    for horo in horo_tomorrow:
        horo_tomorrow = horo[0]
    
    await msg.answer(horo_tomorrow, parse_mode='HTML')
    
@router.message(F.text.startswith('♒️ Завтра'))
async def user_horo_tomorrow(msg: Message, session: AsyncSession):
    horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Водолей'))
    await session.close()
    for horo in horo_tomorrow:
        horo_tomorrow = horo[0]
    
    await msg.answer(horo_tomorrow, parse_mode='HTML')
    
@router.message(F.text.startswith('♓️ Завтра'))
async def user_horo_tomorrow(msg: Message, session: AsyncSession):
    horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Рыбы'))
    await session.close()
    for horo in horo_tomorrow:
        horo_tomorrow = horo[0]
    
    await msg.answer(horo_tomorrow, parse_mode='HTML')