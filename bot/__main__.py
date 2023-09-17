import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config.config import Config, load_config
from handlers.horo import horo_tomorrow, horo_today, horo_week, horo_month, horo_year
from handlers.user import user_horo_today, user_horo_tomorrow, user_horo_week, user_horo_month, user_horo_year
from handlers.vostok_horo import vostok
from handlers import main_handler
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from middlewares import DbMiddleware, SubChecker
from middlewares import RegisterCheck
from services.serv_tomorrow import openai_cmd_tomorrow_1, openai_cmd_tomorrow_2, openai_cmd_tomorrow_3, openai_cmd_tomorrow_4
from services.serv_week import openai_cmd_week_1, openai_cmd_week_2, openai_cmd_week_3, openai_cmd_week_4
from services.serv_month import openai_cmd_month_1, openai_cmd_month_2, openai_cmd_month_3, openai_cmd_month_4
from services.serv_year import openai_cmd_year_1, openai_cmd_year_2, openai_cmd_year_3, openai_cmd_year_4
from handlers import bot_commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('\nStarting bot')
    
    Config = load_config()
    
    engine = create_async_engine(url=Config.tg_bot.url, echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    
    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    
    bot = Bot(Config.tg_bot.token)
    dp = Dispatcher()
    
    await bot.set_my_commands(commands=commands_for_bot)
    
    scheduler = AsyncIOScheduler()
    
    scheduler.add_job(openai_cmd_tomorrow_1, "cron", hour=10, minute=1, args=(bot,))
    scheduler.add_job(openai_cmd_tomorrow_2, "cron", hour=10, minute=2, args=(bot,))
    scheduler.add_job(openai_cmd_tomorrow_3, "cron", hour=10, minute=3, args=(bot,))
    scheduler.add_job(openai_cmd_tomorrow_4, "cron", hour=10, minute=4, args=(bot,))
    
    scheduler.add_job(openai_cmd_week_1, "cron", day='monday', hour=11, minute=1, args=(bot,))
    scheduler.add_job(openai_cmd_week_2, "cron", day='monday', hour=11, minute=2, args=(bot,))
    scheduler.add_job(openai_cmd_week_3, "cron", day='monday', hour=11, minute=3, args=(bot,))
    scheduler.add_job(openai_cmd_week_4, "cron", day='monday', hour=11, minute=4, args=(bot,))

    # scheduler.add_job(openai_cmd_month_1, "cron", minute=13, args=(bot,))
    # scheduler.add_job(openai_cmd_month_2, "cron", minute=14, args=(bot,))
    # scheduler.add_job(openai_cmd_month_3, "cron", minute=15, args=(bot,))
    # scheduler.add_job(openai_cmd_month_4, "cron", minute=16, args=(bot,))
    
    # scheduler.add_job(openai_cmd_year_1, "cron", minute=17, args=(bot,))
    # scheduler.add_job(openai_cmd_year_2, "cron", minute=18, args=(bot,))
    # scheduler.add_job(openai_cmd_year_3, "cron", minute=19, args=(bot,))
    # scheduler.add_job(openai_cmd_year_4, "cron", minute=20, args=(bot,))
    
    scheduler.start()
        
    dp.update.middleware(DbMiddleware(session_pool=sessionmaker))
    dp.message.middleware(RegisterCheck())
    dp.message.middleware(SubChecker())
        
    dp.include_router(main_handler.router)
    dp.include_router(user_horo_today.router)
    dp.include_router(user_horo_tomorrow.router)
    dp.include_router(user_horo_week.router)
    dp.include_router(user_horo_month.router)
    dp.include_router(user_horo_year.router)
    dp.include_router(horo_today.router)
    dp.include_router(horo_tomorrow.router)
    dp.include_router(horo_week.router)
    dp.include_router(horo_month.router)
    dp.include_router(horo_year.router)
    dp.include_router(vostok.router)
    #dp.include_router(payments.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())