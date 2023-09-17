from aiogram import Router, F
from aiogram.types import Message
from config.config import Config, load_config
from sqlalchemy.ext.asyncio import AsyncSession
from database import Horo
from sqlalchemy import select

router = Router()

Config = load_config()

@router.message(F.text == ('♈️ Месяц'))
async def user_horo_month_cmd(msg: Message, session: AsyncSession):
    horo_month = await session.execute(select(Horo.horo_month).where(Horo.zodiac == 'Овен'))
    await session.close()
    for horo in horo_month:
        horo_month = horo[0]
    
    await msg.answer(horo_month, parse_mode='HTML')
    
@router.message(F.text.startswith('♉️ Месяц'))
async def user_horo_month(msg: Message, session: AsyncSession):
    horo_month = await session.execute(select(Horo.horo_month).where(Horo.zodiac == 'Телец'))
    await session.close()
    for horo in horo_month:
        horo_month = horo[0]
    
    await msg.answer(horo_month, parse_mode='HTML')
    
@router.message(F.text.startswith('♊️ Месяц'))
async def user_horo_month(msg: Message, session: AsyncSession):
    horo_month = await session.execute(select(Horo.horo_month).where(Horo.zodiac == 'Близнецы'))
    await session.close()
    for horo in horo_month:
        horo_month = horo[0]
    
    await msg.answer(horo_month, parse_mode='HTML')
    
@router.message(F.text.startswith('♋️ Месяц'))
async def user_horo_month(msg: Message, session: AsyncSession):
    horo_month = await session.execute(select(Horo.horo_month).where(Horo.zodiac == 'Рак'))
    await session.close()
    for horo in horo_month:
        horo_month = horo[0]
    
    await msg.answer(horo_month, parse_mode='HTML')
    
@router.message(F.text.startswith('♌️ Месяц'))
async def user_horo_month(msg: Message, session: AsyncSession):
    horo_month = await session.execute(select(Horo.horo_month).where(Horo.zodiac == 'Лев'))
    await session.close()
    for horo in horo_month:
        horo_month = horo[0]
    
    await msg.answer(horo_month, parse_mode='HTML')
    
@router.message(F.text.startswith('♍️ Месяц'))
async def user_horo_month(msg: Message, session: AsyncSession):
    horo_month = await session.execute(select(Horo.horo_month).where(Horo.zodiac == 'Дева'))
    await session.close()
    for horo in horo_month:
        horo_month = horo[0]
    
    await msg.answer(horo_month, parse_mode='HTML')
    
@router.message(F.text.startswith('♎️ Месяц'))
async def user_horo_month(msg: Message, session: AsyncSession):
    horo_month = await session.execute(select(Horo.horo_month).where(Horo.zodiac == 'Весы'))
    await session.close()
    for horo in horo_month:
        horo_month = horo[0]
    
    await msg.answer(horo_month, parse_mode='HTML')
    
@router.message(F.text.startswith('♏️ Месяц'))
async def user_horo_month(msg: Message, session: AsyncSession):
    horo_month = await session.execute(select(Horo.horo_month).where(Horo.zodiac == 'Скорпион'))
    await session.close()
    for horo in horo_month:
        horo_month = horo[0]
    
    await msg.answer(horo_month, parse_mode='HTML')
    
@router.message(F.text.startswith('♐️ Месяц'))
async def user_horo_month(msg: Message, session: AsyncSession):
    horo_month = await session.execute(select(Horo.horo_month).where(Horo.zodiac == 'Стрелец'))
    await session.close()
    for horo in horo_month:
        horo_month = horo[0]
    
    await msg.answer(horo_month, parse_mode='HTML')
    
@router.message(F.text.startswith('♑️ Месяц'))
async def user_horo_month(msg: Message, session: AsyncSession):
    horo_month = await session.execute(select(Horo.horo_month).where(Horo.zodiac == 'Козерог'))
    await session.close()
    for horo in horo_month:
        horo_month = horo[0]
    
    await msg.answer(horo_month, parse_mode='HTML')
    
@router.message(F.text.startswith('♒️ Месяц'))
async def user_horo_month(msg: Message, session: AsyncSession):
    horo_month = await session.execute(select(Horo.horo_month).where(Horo.zodiac == 'Водолей'))
    await session.close()
    for horo in horo_month:
        horo_month = horo[0]
    
    await msg.answer(horo_month, parse_mode='HTML')
    
@router.message(F.text.startswith('♓️ Месяц'))
async def user_horo_month(msg: Message, session: AsyncSession):
    horo_month = await session.execute(select(Horo.horo_month).where(Horo.zodiac == 'Рыбы'))
    await session.close()
    for horo in horo_month:
        horo_month = horo[0]
    
    await msg.answer(horo_month, parse_mode='HTML')