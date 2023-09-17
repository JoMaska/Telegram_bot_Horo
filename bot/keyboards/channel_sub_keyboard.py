import logging
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_buttons(channel1, channel2, channel3, channel4, channel5) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    
    logging.info(f'\n\nВ начале проверки ошибки\n\n')
    
    if channel1 != 'Подписан':
        kb.button(text='🥺 Подпишись', url=str(channel1))
    if channel2 != 'Подписан':
        kb.button(text='🥺 Подпишись', url=str(channel2))
    if channel3 != 'Подписан':
        kb.button(text='🥺 Подпишись', url=str(channel3))
    if channel4 != 'Подписан':
        kb.button(text='🥺 Подпишись', url=str(channel4))
    if channel5 != 'Подписан':
        kb.button(text='🥺 Подпишись', url=str(channel5))
    
    logging.info(f'\n\nПосле проверки ошибки\n\n')
    
    kb.button(text='✅ Я подписался!', callback_data='delete')
    
    kb.adjust(1, 1, 1, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)