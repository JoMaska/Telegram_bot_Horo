from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_taro_buttons() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='✨ 1 ✨', callback_data='taro_random')
    kb.button(text='✨ 2 ✨', callback_data='taro_random')
    kb.button(text='✨ 3 ✨', callback_data='taro_random')
    kb.button(text='✨ 4 ✨', callback_data='taro_random')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard=True)