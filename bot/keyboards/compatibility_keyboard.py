from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_compatibility_buttons() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='♈️ Овен', callback_data='Овен')
    kb.button(text='♉️ Телец', callback_data='Телец')
    kb.button(text='♊️ Близнецы', callback_data='Близнецы')
    kb.button(text='♋️ Рак', callback_data='Рак')
    kb.button(text='♌️ Лев', callback_data='Лев')
    kb.button(text='♍️ Дева', callback_data='Дева')
    kb.button(text='♎️ Весы', callback_data='Весы')
    kb.button(text='♏️ Скорпион', callback_data='Скорпион')
    kb.button(text='♐️ Стрелец', callback_data='Стрелец')
    kb.button(text='♑️ Козерог', callback_data='Козерог')
    kb.button(text='♒️ Водолей', callback_data='Водолей')
    kb.button(text='♓️ Рыбы', callback_data='Рыбы')
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)
