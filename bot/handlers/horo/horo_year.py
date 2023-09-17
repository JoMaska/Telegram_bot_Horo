from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from config.config import Config, load_config
from sqlalchemy.ext.asyncio import AsyncSession
from database import Horo

router = Router()

Config = load_config()

@router.message(F.text.startswith('🔮 Овен год'))
async def horo_year_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Овен',
            horo_year=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Овнов на год успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Овнов на год - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Телец год'))
async def horo_year_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Телец',
            horo_year=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Тельцов на год успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Тельцов на год - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Близнецы год'))
async def horo_year_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Близнецы',
            horo_year=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Близнецов на год успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Близнецов на год - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Рак год'))
async def horo_year_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Рак',
            horo_year=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Раков на год успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Раков на год - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Лев год'))
async def horo_year_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Лев',
            horo_year=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Львов на год успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Львов на год - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Дева год'))
async def horo_year_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Дева',
            horo_year=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Дев на год успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Дев на год - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Весы год'))
async def horo_year_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Весы',
            horo_year=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Весов на год успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Весов на год - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Скорпион год'))
async def horo_year_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Скорпион',
            horo_year=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Скорпионов на год успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Скорпионов на год - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Стрелец год'))
async def horo_year_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Стрелец',
            horo_year=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Стрельцов на год успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Стрельцов на год - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Козерог год'))
async def horo_year_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Козерог',
            horo_year=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Козерогов на год успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Козерогов на год - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Водолей год'))
async def horo_year_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Водолей',
            horo_year=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Водолеев на год успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Водолеев на год - ошибка, данные не были занесены')
    else:
        pass
    
@router.message(F.text.startswith('🔮 Рыбы год'))
async def horo_year_cmd(msg: Message, session: AsyncSession):
    if msg.from_user.id == int(Config.tg_bot.admin_id):
        horo = Horo(
            zodiac='Рыбы',
            horo_year=msg.text
        )
        try:
            await session.merge(horo)
            await session.commit()
            await msg.answer('Гороскоп для Рыб на год успешно занесен в базу!')
        except:
            await msg.answer('Гороскоп для Рыб на год - ошибка, данные не были занесены')
    else:
        pass