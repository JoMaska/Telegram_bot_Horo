from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from config.config import Config, load_config
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.user import VostokHoro
from keyboards.main_keyboard import get_exit_menu_buttons

router = Router()

Config = load_config()

@router.callback_query(F.data == 'Мышь')
async def vostok_horo(callback: CallbackQuery, bot: Bot, session: AsyncSession):

    result = await session.execute(select(VostokHoro.desc).where(VostokHoro.name == 'Мышь'))
    await session.close()
    for i in result:
        result = i[0]
    
    await bot.send_message(text=result, chat_id=callback.from_user.id, reply_markup=get_exit_menu_buttons())
    
    await callback.answer()
    
@router.callback_query(F.data == 'Бык')
async def vostok_horo(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    
    result = await session.execute(select(VostokHoro.desc).where(VostokHoro.name == 'Бык'))
    await session.close()
    for i in result:
        result = i[0]
    
    await bot.send_message(text=result, chat_id=callback.from_user.id)
    
    await callback.answer()

@router.callback_query(F.data == 'Тигр')
async def vostok_horo(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    result = await session.execute(select(VostokHoro.desc).where(VostokHoro.name == 'Тигр'))
    await session.close()
    for i in result:
        result = i[0]
    
    await bot.send_message(text=result, chat_id=callback.from_user.id, reply_markup=get_exit_menu_buttons())

    await callback.answer()

@router.callback_query(F.data == 'Кролик')
async def vostok_horo(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    result = await session.execute(select(VostokHoro.desc).where(VostokHoro.name == 'Кролик'))
    await session.close()
    for i in result:
        result = i[0]
    
    await bot.send_message(text=result, chat_id=callback.from_user.id, reply_markup=get_exit_menu_buttons())

    await callback.answer()

@router.callback_query(F.data == 'Дракон')
async def vostok_horo(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    result = await session.execute(select(VostokHoro.desc).where(VostokHoro.name == 'Дракон'))
    await session.close()
    for i in result:
        result = i[0]
    
    await bot.send_message(text=result, chat_id=callback.from_user.id, reply_markup=get_exit_menu_buttons())

    await callback.answer()

@router.callback_query(F.data == 'Змея')
async def vostok_horo(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    result = await session.execute(select(VostokHoro.desc).where(VostokHoro.name == 'Змея'))
    await session.close()
    for i in result:
        result = i[0]
    
    await bot.send_message(text=result, chat_id=callback.from_user.id, reply_markup=get_exit_menu_buttons())

    await callback.answer()

@router.callback_query(F.data == 'Лошадь')
async def vostok_horo(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    result = await session.execute(select(VostokHoro.desc).where(VostokHoro.name == 'Лошадь'))
    await session.close()
    for i in result:
        result = i[0]
    
    await bot.send_message(text=result, chat_id=callback.from_user.id, reply_markup=get_exit_menu_buttons())

    await callback.answer()

@router.callback_query(F.data == 'Коза')
async def vostok_horo(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    result = await session.execute(select(VostokHoro.desc).where(VostokHoro.name == 'Коза'))
    await session.close()
    for i in result:
        result = i[0]
    
    await bot.send_message(text=result, chat_id=callback.from_user.id, reply_markup=get_exit_menu_buttons())

    await callback.answer()

@router.callback_query(F.data == 'Обезьяна')
async def vostok_horo(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    result = await session.execute(select(VostokHoro.desc).where(VostokHoro.name == 'Обезьяна'))
    await session.close()
    for i in result:
        result = i[0]
    
    await bot.send_message(text=result, chat_id=callback.from_user.id, reply_markup=get_exit_menu_buttons())

    await callback.answer()

@router.callback_query(F.data == 'Петух')
async def vostok_horo(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    result = await session.execute(select(VostokHoro.desc).where(VostokHoro.name == 'Петух'))
    await session.close()
    for i in result:
        result = i[0]
    
    await bot.send_message(text=result, chat_id=callback.from_user.id, reply_markup=get_exit_menu_buttons())

    await callback.answer()

@router.callback_query(F.data == 'Собака')
async def vostok_horo(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    result = await session.execute(select(VostokHoro.desc).where(VostokHoro.name == 'Собака'))
    await session.close()
    for i in result:
        result = i[0]
    
    await bot.send_message(text=result, chat_id=callback.from_user.id, reply_markup=get_exit_menu_buttons())

    await callback.answer()

@router.callback_query(F.data == 'Свинья')
async def vostok_horo(callback: CallbackQuery, bot: Bot, session: AsyncSession):
    result = await session.execute(select(VostokHoro.desc).where(VostokHoro.name == 'Свинья'))
    await session.close()
    for i in result:
        result = i[0]
    
    await bot.send_message(text=result, chat_id=callback.from_user.id, reply_markup=get_exit_menu_buttons())

    await callback.answer()
