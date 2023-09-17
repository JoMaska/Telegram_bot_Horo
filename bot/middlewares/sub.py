import logging
from sqlalchemy import select
from config.config import Config, load_config
from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, Any, Awaitable, Callable, List
from aiogram.types import TelegramObject
from aiogram.exceptions import TelegramBadRequest
from keyboards.channel_sub_keyboard import get_inline_buttons
from database import Channel

Config = load_config()


class SubChecker(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
            
    ) -> Any:
        session: AsyncSession = data['session']
        if event.from_user.id == int(Config.tg_bot.admin_id):
            return await handler(event, data)
        
        async def check_sub(channel_id: int) -> bool:
            try:
                session: AsyncSession = data['session']
                channel = await session.execute(select(Channel.id_channel).where(Channel.id == channel_id))
                text = ''.join(str(c[0]) for c in channel)
                user = await data['bot'].get_chat_member(chat_id=text, user_id=event.from_user.id)
                return user.status != "left"
            except TelegramBadRequest:
                if text == '':
                    return True
                return False
            
        sub1 = await check_sub(1)
        sub2 = await check_sub(2)
        sub3 = await check_sub(3)
        sub4 = await check_sub(4)
        sub5 = await check_sub(5)
        
        
        
        
        
        # async def check_sub(channel_ids: List[int]) -> List[bool]:
        #     # try:
        #         session: AsyncSession = data['session']
        #         channels = await session.execute(select(Channel.id_channel).where(Channel.id.in_(channel_ids)))
        #         channel_ids = [str(c[0]) for c in channels]
        #         logging.info(f'\n\nДЛИНА СПИСКА {len(channel_ids)}\n\n')
        #         users = []
        #         for channel_id in channel_ids:
        #             try:
        #                 user = await data['bot'].get_chat_member(chat_id=channel_id, user_id=event.from_user.id)
        #                 if channel_id == '':
        #                     users.append(user.status != 'left')
        #                 users.append(user)
        #                 logging.info(f'\n\n{users}\n\n')
        #             except TelegramBadRequest:
        #                 if user == '':
        #                     logging.info(f'\n\nОШИБКААААААААААААААААААААААА\n\n')
        #                     users.append(user.status != 'left')
        #                 users.append(user.status == 'left')
        #         result = []
        #         for i in channel_ids:
        #             logging.info(f'\n\n{i}\n\n')
        #             result.append(True)
        #         return [user.status != "left" for user in users]
        #     # except TelegramBadRequest:
        #     #     result = []
        #     #     for i in channel_ids:
        #     #         if i == '':
        #     #             result.append(True)
        #     #         logging.info(f'\n\n{i}\n\n')
        #     #         result.append(False)
        #     #         return result
        #     #     return [True] * len(channel_ids)
        # sub_results = await check_sub([1, 2, 3, 4, 5])
        
        # logging.info(f'\n\n{sub_results}\n\n')
        # sub1, sub2, sub3, sub4, sub5 = sub_results
        
        
        
        
        if all([sub1, sub2, sub3, sub4, sub5]):
            return await handler(event, data)
        else:
            channels = []
            for i in range(1, 6):     
                channel = await session.execute(select(Channel.silk).where(Channel.id == i))
                text = ''
                for c in channel:
                    text += str(c[0])
                channels.append(text)
                
            if sub1 == True:
                channels[0] = 'Подписан'
            if sub2 == True:
                channels[1] = 'Подписан'
            if sub3 == True:
                channels[2] = 'Подписан'
            if sub4 == True:
                channels[3] = 'Подписан'
            if sub5 == True:
                channels[4] = 'Подписан'
            
            await event.answer('Чтобы пользоваться всеми возможностями бота бесплатно, подпишись на каналы ниже и нажми «✅ Я подписался»',
                               reply_markup=get_inline_buttons(channel1=channels[0], channel2=channels[1], channel3=channels[2], channel4=channels[3], channel5=channels[4]))
        