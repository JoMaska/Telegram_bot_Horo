from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from config.config import Config, load_config
from sqlalchemy.ext.asyncio import AsyncSession
from database import Horo

router = Router()

Config = load_config()

@router.message(F.text.startswith('🔮 Овен неделя'))
async def horo_week_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Овен',
            horo_week=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Овнов на неделю успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Овнов на неделю - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Телец неделя'))
async def horo_week_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Телец',
            horo_week=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Тельцов на неделю успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Тельцов на неделю - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Близнецы неделя'))
async def horo_week_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Близнецы',
            horo_week=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Близнецов на неделю успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Близнецов на неделю - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Рак неделя'))
async def horo_week_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Рак',
            horo_week=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Раков на неделю успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Раков на неделю - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Лев неделя'))
async def horo_week_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Лев',
            horo_week=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Львов на неделю успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Львов на неделю - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Дева неделя'))
async def horo_week_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Дева',
            horo_week=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Дев на неделю успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Дев на неделю - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Весы неделя'))
async def horo_week_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Весы',
            horo_week=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Весов на неделю успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Весов на неделю - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Скорпион неделя'))
async def horo_week_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Скорпион',
            horo_week=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Скорпионов на неделю успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Скорпионов на неделю - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Стрелец неделя'))
async def horo_week_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Стрелец',
            horo_week=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Стрельцов на неделю успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Стрельцов на неделю - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Козерог неделя'))
async def horo_week_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Козерог',
            horo_week=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Козерогов на неделю успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Козерогов на неделю - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Водолей неделя'))
async def horo_week_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Водолей',
            horo_week=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Водолеев на неделю успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Водолеев на неделю - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Рыбы неделя'))
async def horo_week_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Рыбы',
            horo_week=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Рыб на неделю успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Рыб на неделю - ошибка, данные не были занесены')
    else:
        pass