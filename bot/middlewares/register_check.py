import logging
from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, Any, Awaitable, Callable
from aiogram.types import TelegramObject
from sqlalchemy import select
from database.user import User
from sqlalchemy.engine import ScalarResult
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.row import Row, BaseRow

class RegisterCheck(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
            ) -> Any:
        
        session: AsyncSession = data['session']
        result = await session.execute(select(User).where(User.user_id == event.from_user.id))
        result: ScalarResult
        user: User = result.one_or_none()
                
        if user is not None:
            logging.info(f'\nUser: {event.from_user.username}, Id: {event.from_user.id} ALREADY in the database')
            await session.commit()
            return await handler(event, data)
        else:
            user = User(
                user_id=event.from_user.id,
                username=event.from_user.username
            )
            logging.info(f'\nUser: {event.from_user.username}, Id: {event.from_user.id} in the database')

            await session.merge(user)
            await session.commit()
        return await handler(event, data)