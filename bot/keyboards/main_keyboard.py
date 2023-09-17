from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_start_buttons() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='💟 Совместимость')
    kb.button(text='🔮 Гороскоп')
    kb.button(text='🟣 Магия чисел')
    kb.button(text='🀄️ Карты таро')
    kb.button(text='🏵 Восточный гороскоп')
    kb.button(text='🕯 ОСОБЫЕ ВОЗМОЖНОСТИ')
    kb.adjust(2, 2, 2)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)

def get_exit_menu_buttons() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='🏠 Выйти в меню')
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)