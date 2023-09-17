from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_vostok_horo_buttons() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='🐭 Мышь', callback_data='Мышь')
    kb.button(text='🐮 Бык', callback_data='Бык')
    kb.button(text='🐯 Тигр', callback_data='Тигр')
    kb.button(text='🐰 Кролик', callback_data='Кролик')
    kb.button(text='🐲 Дракон', callback_data='Дракон')
    kb.button(text='🐍 Змея', callback_data='Змея')
    kb.button(text='🐴 Лошадь', callback_data='Лошадь')
    kb.button(text='🐐 Коза', callback_data='Коза')
    kb.button(text='🐵 Обезьяна', callback_data='Обезьяна')
    kb.button(text='🐔 Петух', callback_data='Петух')
    kb.button(text='🐶 Собака', callback_data='Собака')
    kb.button(text='🐷 Свинья', callback_data='Свинья')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard=True)