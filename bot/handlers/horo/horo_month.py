from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from config.config import Config, load_config
from sqlalchemy.ext.asyncio import AsyncSession
from database import Horo

router = Router()

Config = load_config()

@router.message(F.text.startswith('🔮 Овен месяц'))
async def horo_month_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Овен',
            horo_month=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Овнов на месяц успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Овнов на месяц - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Телец месяц'))
async def horo_month_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Телец',
            horo_month=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Тельцов на месяц успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Тельцов на месяц - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Близнецы месяц'))
async def horo_month_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Близнецы',
            horo_month=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Близнецов на месяц успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Близнецов на месяц - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Рак месяц'))
async def horo_month_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Рак',
            horo_month=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Раков на месяц успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Раков на месяц - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Лев месяц'))
async def horo_month_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Лев',
            horo_month=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Львов на месяц успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Львов на месяц - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Дева месяц'))
async def horo_month_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Дева',
            horo_month=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Дев на месяц успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Дев на месяц - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Весы месяц'))
async def horo_month_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Весы',
            horo_month=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Весов на месяц успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Весов на месяц - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Скорпион месяц'))
async def horo_month_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Скорпион',
            horo_month=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Скорпионов на месяц успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Скорпионов на месяц - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Стрелец месяц'))
async def horo_month_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Стрелец',
            horo_month=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Стрельцов на месяц успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Стрельцов на месяц - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Козерог месяц'))
async def horo_month_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Козерог',
            horo_month=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Козерогов на месяц успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Козерогов на месяц - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Водолей месяц'))
async def horo_month_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Водолей',
            horo_month=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Водолеев на месяц успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Водолеев на месяц - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Рыбы месяц'))
async def horo_month_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Рыбы',
            horo_month=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Рыб на месяц успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Рыб на месяц - ошибка, данные не были занесены')
    else:
        pass