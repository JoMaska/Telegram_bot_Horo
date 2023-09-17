from aiogram import Router, F
from aiogram.types import Message
from config.config import Config, load_config
from sqlalchemy.ext.asyncio import AsyncSession
from database import Horo
from sqlalchemy import select

router = Router()

Config = load_config()

@router.message(F.text == ('♈️ Неделя'))
async def user_horo_week_cmd(msg: Message, session: AsyncSession):
    horo_week = await session.execute(select(Horo.horo_week).where(Horo.zodiac == 'Овен'))
    await session.close()
    for horo in horo_week:
        horo_week = horo[0]
    
    await msg.answer(horo_week, parse_mode='HTML')
    
@router.message(F.text.startswith('♉️ Неделя'))
async def user_horo_week(msg: Message, session: AsyncSession):
    horo_week = await session.execute(select(Horo.horo_week).where(Horo.zodiac == 'Телец'))
    await session.close()
    for horo in horo_week:
        horo_week = horo[0]
    
    await msg.answer(horo_week, parse_mode='HTML')
    
@router.message(F.text.startswith('♊️ Неделя'))
async def user_horo_week(msg: Message, session: AsyncSession):
    horo_week = await session.execute(select(Horo.horo_week).where(Horo.zodiac == 'Близнецы'))
    await session.close()
    for horo in horo_week:
        horo_week = horo[0]
    
    await msg.answer(horo_week)
    
@router.message(F.text.startswith('♋️ Неделя'))
async def user_horo_week(msg: Message, session: AsyncSession):
    horo_week = await session.execute(select(Horo.horo_week).where(Horo.zodiac == 'Рак'))
    await session.close()
    for horo in horo_week:
        horo_week = horo[0]
    
    await msg.answer(horo_week, parse_mode='HTML')
    
@router.message(F.text.startswith('♌️ Неделя'))
async def user_horo_week(msg: Message, session: AsyncSession):
    horo_week = await session.execute(select(Horo.horo_week).where(Horo.zodiac == 'Лев'))
    await session.close()
    for horo in horo_week:
        horo_week = horo[0]
    
    await msg.answer(horo_week)
    
@router.message(F.text.startswith('♍️ Неделя'))
async def user_horo_week(msg: Message, session: AsyncSession):
    horo_week = await session.execute(select(Horo.horo_week).where(Horo.zodiac == 'Дева'))
    await session.close()
    for horo in horo_week:
        horo_week = horo[0]
    
    await msg.answer(horo_week, parse_mode='HTML')
    
@router.message(F.text.startswith('♎️ Неделя'))
async def user_horo_week(msg: Message, session: AsyncSession):
    horo_week = await session.execute(select(Horo.horo_week).where(Horo.zodiac == 'Весы'))
    await session.close()
    for horo in horo_week:
        horo_week = horo[0]
    
    await msg.answer(horo_week, parse_mode='HTML')
    
@router.message(F.text.startswith('♏️ Неделя'))
async def user_horo_week(msg: Message, session: AsyncSession):
    horo_week = await session.execute(select(Horo.horo_week).where(Horo.zodiac == 'Скорпион'))
    await session.close()
    for horo in horo_week:
        horo_week = horo[0]
    
    await msg.answer(horo_week, parse_mode='HTML')
    
@router.message(F.text.startswith('♐️ Неделя'))
async def user_horo_week(msg: Message, session: AsyncSession):
    horo_week = await session.execute(select(Horo.horo_week).where(Horo.zodiac == 'Стрелец'))
    await session.close()
    for horo in horo_week:
        horo_week = horo[0]
    
    await msg.answer(horo_week, parse_mode='HTML')
    
@router.message(F.text.startswith('♑️ Неделя'))
async def user_horo_week(msg: Message, session: AsyncSession):
    horo_week = await session.execute(select(Horo.horo_week).where(Horo.zodiac == 'Козерог'))
    await session.close()
    for horo in horo_week:
        horo_week = horo[0]
    
    await msg.answer(horo_week, parse_mode='HTML')
    
@router.message(F.text.startswith('♒️ Неделя'))
async def user_horo_week(msg: Message, session: AsyncSession):
    horo_week = await session.execute(select(Horo.horo_week).where(Horo.zodiac == 'Водолей'))
    await session.close()
    for horo in horo_week:
        horo_week = horo[0]
    
    await msg.answer(horo_week, parse_mode='HTML')
    
@router.message(F.text.startswith('♓️ Неделя'))
async def user_horo_week(msg: Message, session: AsyncSession):
    horo_week = await session.execute(select(Horo.horo_week).where(Horo.zodiac == 'Рыбы'))
    await session.close()
    for horo in horo_week:
        horo_week = horo[0]
    
    await msg.answer(horo_week, parse_mode='HTML')