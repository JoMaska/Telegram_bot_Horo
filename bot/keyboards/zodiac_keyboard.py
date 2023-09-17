from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_zodiac_buttons() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='♈️ Овен')
    kb.button(text='♉️ Телец')
    kb.button(text='♊️ Близнецы')
    kb.button(text='♋️ Рак')
    kb.button(text='♌️ Лев')
    kb.button(text='♍️ Дева')
    kb.button(text='♎️ Весы')
    kb.button(text='♏️ Скорпион')
    kb.button(text='♐️ Стрелец')
    kb.button(text='♑️ Козерог')
    kb.button(text='♒️ Водолей')
    kb.button(text='♓️ Рыбы')
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)

def get_timeday_1o_buttons():
    kb = ReplyKeyboardBuilder()
    kb.button(text='♈️ Завтра')
    kb.button(text='♈️ Неделя')
    kb.button(text='♈️ Месяц')
    kb.button(text='♈️ Год')
    kb.button(text='🏠 Выйти в меню')
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)

def get_timeday_2t_buttons():
    kb = ReplyKeyboardBuilder()
    kb.button(text='♉️ Завтра')
    kb.button(text='♉️ Неделя')
    kb.button(text='♉️ Месяц')
    kb.button(text='♉️ Год')
    kb.button(text='🏠 Выйти в меню')
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)

def get_timeday_3b_buttons():
    kb = ReplyKeyboardBuilder()
    kb.button(text='♊️ Завтра')
    kb.button(text='♊️ Неделя')
    kb.button(text='♊️ Месяц')
    kb.button(text='♊️ Год')
    kb.button(text='🏠 Выйти в меню')
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)

def get_timeday_4r_buttons():
    kb = ReplyKeyboardBuilder()
    kb.button(text='♋️ Завтра')
    kb.button(text='♋️ Неделя')
    kb.button(text='♋️ Месяц')
    kb.button(text='♋️ Год')
    kb.button(text='🏠 Выйти в меню')
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)

def get_timeday_5l_buttons():
    kb = ReplyKeyboardBuilder()
    kb.button(text='♌️ Завтра')
    kb.button(text='♌️ Неделя')
    kb.button(text='♌️ Месяц')
    kb.button(text='♌️ Год')
    kb.button(text='🏠 Выйти в меню')
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)

def get_timeday_6d_buttons():
    kb = ReplyKeyboardBuilder()
    kb.button(text='♍️ Завтра')
    kb.button(text='♍️ Неделя')
    kb.button(text='♍️ Месяц')
    kb.button(text='♍️ Год')
    kb.button(text='🏠 Выйти в меню')
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)

def get_timeday_7v_buttons():
    kb = ReplyKeyboardBuilder()
    kb.button(text='♎️ Завтра')
    kb.button(text='♎️ Неделя')
    kb.button(text='♎️ Месяц')
    kb.button(text='♎️ Год')
    kb.button(text='🏠 Выйти в меню')
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)

def get_timeday_8s_buttons():
    kb = ReplyKeyboardBuilder()
    kb.button(text='♏️ Завтра')
    kb.button(text='♏️ Неделя')
    kb.button(text='♏️ Месяц')
    kb.button(text='♏️ Год')
    kb.button(text='🏠 Выйти в меню')
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)

def get_timeday_9s_buttons():
    kb = ReplyKeyboardBuilder()
    kb.button(text='♐️ Завтра')
    kb.button(text='♐️ Неделя')
    kb.button(text='♐️ Месяц')
    kb.button(text='♐️ Год')
    kb.button(text='🏠 Выйти в меню')
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)

def get_timeday_10k_buttons():
    kb = ReplyKeyboardBuilder()
    kb.button(text='♑️ Завтра')
    kb.button(text='♑️ Неделя')
    kb.button(text='♑️ Месяц')
    kb.button(text='♑️ Год')
    kb.button(text='🏠 Выйти в меню')
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)

def get_timeday_11v_buttons():
    kb = ReplyKeyboardBuilder()
    kb.button(text='♒️ Завтра')
    kb.button(text='♒️ Неделя')
    kb.button(text='♒️ Месяц')
    kb.button(text='♒️ Год')
    kb.button(text='🏠 Выйти в меню')
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)

def get_timeday_12r_buttons():
    kb = ReplyKeyboardBuilder()
    kb.button(text='♓️ Завтра')
    kb.button(text='♓️ Неделя')
    kb.button(text='♓️ Месяц')
    kb.button(text='♓️ Год')
    kb.button(text='🏠 Выйти в меню')
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=False)