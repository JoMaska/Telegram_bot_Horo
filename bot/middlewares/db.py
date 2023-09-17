import logging
from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker
from typing import Dict, Any, Awaitable, Callable
from aiogram.types import TelegramObject


class DbMiddleware(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker):
        super().__init__()
        self.session_pool = session_pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:

        async with self.session_pool() as session:
            async with session.begin():
                data["session"] = session
                
        return await handler(event, data)