import random
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_numbers_buttons() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    number3 = random.randint(1, 100)
    number4 = random.randint(1, 100)
    number5 = random.randint(1, 100)
    number6 = random.randint(1, 100)
    set_number = {number1, number2, number3, number4, number5, number6}
    if len(set_number) != 6:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        number3 = random.randint(1, 100)
        number4 = random.randint(1, 100)
        number5 = random.randint(1, 100)
        number6 = random.randint(1, 100)
        set_number = {number1, number2, number3, number4, number5, number6}
        return set_number
    else:
        kb.button(text=str(number1)+' 🔮', callback_data='numb_random')
        kb.button(text=str(number2)+' 🔮', callback_data='numb_random')
        kb.button(text=str(number3)+' 🔮', callback_data='numb_random')
        kb.button(text=str(number4)+' 🔮', callback_data='numb_random')
        kb.button(text=str(number5)+' 🔮', callback_data='numb_random')
        kb.button(text=str(number6)+' 🔮', callback_data='numb_random')
        kb.adjust(6)
    return kb.as_markup(resize_keyboard=True)