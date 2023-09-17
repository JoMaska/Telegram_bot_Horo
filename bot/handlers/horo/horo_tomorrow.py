import logging
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from config.config import Config, load_config
from sqlalchemy.ext.asyncio import AsyncSession
from database import Horo
from sqlalchemy import select
from sqlalchemy.engine import ScalarResult

router = Router()

Config = load_config()

@router.message(F.text.startswith('🔮 Овен завтра'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        
        horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Овен'))
        horo_tomorrow = horo_tomorrow.one_or_none()
        horo_tomorrow = horo_tomorrow[0]
        horo_tomorrow = horo_tomorrow.replace('завтра', 'сегодня')
        horo_tomorrow = horo_tomorrow.replace('Завтра', 'Сегодня')
        
        horo_today = Horo(
                zodiac='Овен',
                horo_today=horo_tomorrow
        )
        try:
            await session.merge(horo_today)
            await session.commit()
        except:
            await msg.answer('Гороскоп для Овнов на сегодня - ошибка, данные не были занесены')
    
        horo = Horo(
            zodiac='Овен',
            horo_tomorrow=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Овнов на завтра успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Овнов на завтра - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Телец завтра'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        
        horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Телец'))
        horo_tomorrow = horo_tomorrow.one_or_none()
        horo_tomorrow = horo_tomorrow[0]
        horo_tomorrow = horo_tomorrow.replace('завтра', 'сегодня')
        horo_tomorrow = horo_tomorrow.replace('Завтра', 'Сегодня')
        
        horo_today = Horo(
                zodiac='Телец',
                horo_today=horo_tomorrow
        )
        try:
            await session.merge(horo_today)
            await session.commit()
        except:
            await msg.answer('Гороскоп для Тельцов на сегодня - ошибка, данные не были занесены')
    
        horo = Horo(
            zodiac='Телец',
            horo_tomorrow=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Тельцов на завтра успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Тельцов на завтра - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Близнецы завтра'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        
        horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Близнецы'))
        horo_tomorrow = horo_tomorrow.one_or_none()
        horo_tomorrow = horo_tomorrow[0]
        horo_tomorrow = horo_tomorrow.replace('завтра', 'сегодня')
        horo_tomorrow = horo_tomorrow.replace('Завтра', 'Сегодня')
        
        horo_today = Horo(
                zodiac='Близнецы',
                horo_today=horo_tomorrow
        )
        try:
            await session.merge(horo_today)
            await session.commit()
        except:
            await msg.answer('Гороскоп для Близнецов на сегодня - ошибка, данные не были занесены')
    
        horo = Horo(
            zodiac='Близнецы',
            horo_tomorrow=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Близнецов на завтра успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Близнецов на завтра - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Рак завтра'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        
        horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Рак'))
        horo_tomorrow = horo_tomorrow.one_or_none()
        horo_tomorrow = horo_tomorrow[0]
        horo_tomorrow = horo_tomorrow.replace('завтра', 'сегодня')
        horo_tomorrow = horo_tomorrow.replace('Завтра', 'Сегодня')
        
        horo_today = Horo(
                zodiac='Рак',
                horo_today=horo_tomorrow
        )
        try:
            await session.merge(horo_today)
            await session.commit()
        except:
            await msg.answer('Гороскоп для Раков на сегодня - ошибка, данные не были занесены')
    
        horo = Horo(
            zodiac='Рак',
            horo_tomorrow=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Раков на завтра успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Раков на завтра - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Лев завтра'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        
        horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Лев'))
        horo_tomorrow = horo_tomorrow.one_or_none()
        horo_tomorrow = horo_tomorrow[0]
        horo_tomorrow = horo_tomorrow.replace('завтра', 'сегодня')
        horo_tomorrow = horo_tomorrow.replace('Завтра', 'Сегодня')
        
        horo_today = Horo(
                zodiac='Лев',
                horo_today=horo_tomorrow
        )
        try:
            await session.merge(horo_today)
            await session.commit()
        except:
            await msg.answer('Гороскоп для Львов на сегодня - ошибка, данные не были занесены')
    
        horo = Horo(
            zodiac='Лев',
            horo_tomorrow=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Львов на завтра успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Львов на завтра - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Дева завтра'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        
        horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Дева'))
        horo_tomorrow = horo_tomorrow.one_or_none()
        horo_tomorrow = horo_tomorrow[0]
        horo_tomorrow = horo_tomorrow.replace('завтра', 'сегодня')
        horo_tomorrow = horo_tomorrow.replace('Завтра', 'Сегодня')
        
        horo_today = Horo(
                zodiac='Дева',
                horo_today=horo_tomorrow
        )
        try:
            await session.merge(horo_today)
            await session.commit()
        except:
            await msg.answer('Гороскоп для Дев на сегодня - ошибка, данные не были занесены')
    
        horo = Horo(
            zodiac='Дева',
            horo_tomorrow=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Дев на завтра успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Дев на завтра - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Весы завтра'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        
        horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Весы'))
        horo_tomorrow = horo_tomorrow.one_or_none()
        horo_tomorrow = horo_tomorrow[0]
        horo_tomorrow = horo_tomorrow.replace('завтра', 'сегодня')
        horo_tomorrow = horo_tomorrow.replace('Завтра', 'Сегодня')
        
        horo_today = Horo(
                zodiac='Весы',
                horo_today=horo_tomorrow
        )
        try:
            await session.merge(horo_today)
            await session.commit()
        except:
            await msg.answer('Гороскоп для Весов на сегодня - ошибка, данные не были занесены')
    
        horo = Horo(
            zodiac='Весы',
            horo_tomorrow=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Весов на завтра успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Весов на завтра - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Скорпион завтра'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        
        horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Скорпион'))
        horo_tomorrow = horo_tomorrow.one_or_none()
        horo_tomorrow = horo_tomorrow[0]
        horo_tomorrow = horo_tomorrow.replace('завтра', 'сегодня')
        horo_tomorrow = horo_tomorrow.replace('Завтра', 'Сегодня')
        
        horo_today = Horo(
                zodiac='Скорпион',
                horo_today=horo_tomorrow
        )
        try:
            await session.merge(horo_today)
            await session.commit()
        except:
            await msg.answer('Гороскоп для Скорпионов на сегодня - ошибка, данные не были занесены')
    
        horo = Horo(
            zodiac='Скорпион',
            horo_tomorrow=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Скорпионов на завтра успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Скорпионов на завтра - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Стрелец завтра'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        
        horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Стрелец'))
        horo_tomorrow = horo_tomorrow.one_or_none()
        horo_tomorrow = horo_tomorrow[0]
        horo_tomorrow = horo_tomorrow.replace('завтра', 'сегодня')
        horo_tomorrow = horo_tomorrow.replace('Завтра', 'Сегодня')
        
        horo_today = Horo(
                zodiac='Стрелец',
                horo_today=horo_tomorrow
        )
        try:
            await session.merge(horo_today)
            await session.commit()
        except:
            await msg.answer('Гороскоп для Стрельцов на сегодня - ошибка, данные не были занесены')
    
        horo = Horo(
            zodiac='Стрелец',
            horo_tomorrow=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Стрельцов на завтра успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Стрельцов на завтра - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Козерог завтра'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        
        horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Козерог'))
        horo_tomorrow = horo_tomorrow.one_or_none()
        horo_tomorrow = horo_tomorrow[0]
        horo_tomorrow = horo_tomorrow.replace('завтра', 'сегодня')
        horo_tomorrow = horo_tomorrow.replace('Завтра', 'Сегодня')
        
        horo_today = Horo(
                zodiac='Козерог',
                horo_today=horo_tomorrow
        )
        try:
            await session.merge(horo_today)
            await session.commit()
        except:
            await msg.answer('Гороскоп для Козерогов на сегодня - ошибка, данные не были занесены')
    
        horo = Horo(
            zodiac='Козерог',
            horo_tomorrow=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Козерогов на завтра успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Козерогов на завтра - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Водолей завтра'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        
        horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Водолей'))
        horo_tomorrow = horo_tomorrow.one_or_none()
        horo_tomorrow = horo_tomorrow[0]
        horo_tomorrow = horo_tomorrow.replace('завтра', 'сегодня')
        horo_tomorrow = horo_tomorrow.replace('Завтра', 'Сегодня')
        
        horo_today = Horo(
                zodiac='Водолей',
                horo_today=horo_tomorrow
        )
        try:
            await session.merge(horo_today)
            await session.commit()
        except:
            await msg.answer('Гороскоп для Водолеев на сегодня - ошибка, данные не были занесены')
    
        horo = Horo(
            zodiac='Водолей',
            horo_tomorrow=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Водолеев на завтра успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Водолеев на завтра - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Рыбы завтра'))
async def horo_oven_today(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        
        horo_tomorrow = await session.execute(select(Horo.horo_tomorrow).where(Horo.zodiac == 'Рыбы'))
        horo_tomorrow = horo_tomorrow.one_or_none()
        horo_tomorrow = horo_tomorrow[0]
        horo_tomorrow = horo_tomorrow.replace('завтра', 'сегодня')
        horo_tomorrow = horo_tomorrow.replace('Завтра', 'Сегодня')
        
        horo_today = Horo(
                zodiac='Рыбы',
                horo_today=horo_tomorrow
        )
        try:
            await session.merge(horo_today)
            await session.commit()
        except:
            await msg.answer('Гороскоп для Рыб на сегодня - ошибка, данные не были занесены')
    
        horo = Horo(
            zodiac='Рыбы',
            horo_tomorrow=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Рыб на завтра успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Рыб на завтра - ошибка, данные не были занесены')
    else:
        pass