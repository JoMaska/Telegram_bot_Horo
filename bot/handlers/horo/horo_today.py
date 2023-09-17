from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from config.config import Config, load_config
from sqlalchemy.ext.asyncio import AsyncSession
from database import Horo

router = Router()

Config = load_config()

@router.message(F.text.startswith('🔮 Овен сегодня'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Овен',
            horo_today=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Овнов на сегодня успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Овнов на сегодня - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Телец сегодня'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Телец',
            horo_today=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Тельцов на сегодня успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Тельцов на сегодня - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Близнецы сегодня'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Близнецы',
            horo_today=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Близнецов на сегодня успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Близнецов на сегодня - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Рак сегодня'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Рак',
            horo_today=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Раков на сегодня успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Раков на сегодня - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Лев сегодня'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Лев',
            horo_today=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Львов на сегодня успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Львов на сегодня - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Дева сегодня'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Дева',
            horo_today=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Дев на сегодня успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Дев на сегодня - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Весы сегодня'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Весы',
            horo_today=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Весов на сегодня успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Весов на сегодня - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Скорпион сегодня'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Скорпион',
            horo_today=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Скорпионов на сегодня успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Скорпионов на сегодня - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Стрелец сегодня'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Стрелец',
            horo_today=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Стрельцов на сегодня успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Стрельцов на сегодня - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Козерог сегодня'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Козерог',
            horo_today=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Козерогов на сегодня успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Козерогов на сегодня - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Водолей сегодня'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Водолей',
            horo_today=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Водолеев на сегодня успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Водолеев на сегодня - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Рыбы сегодня'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Рыбы',
            horo_today=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Рыб на сегодня успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Рыб на сегодня - ошибка, данные не были занесены')
    else:
        pass