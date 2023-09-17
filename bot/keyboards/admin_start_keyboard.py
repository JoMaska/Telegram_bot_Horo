from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def get_admin_start_buttons() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='💟 Совместимость')
    kb.button(text='🔮 Гороскоп')
    kb.button(text='🟣 Магия чисел')
    kb.button(text='🀄️ Карты таро')
    kb.button(text='🏵 Восточный гороскоп')
    kb.button(text='🕯 ОСОБЫЕ ВОЗМОЖНОСТИ')
    kb.button(text='✍🏻 Изменить каналы')
    kb.button(text='✍🏻 Добавить рассылку')
    kb.adjust(2, 2, 2, 2)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)

def get_admin_buttons() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='🗑 Удалить канал')
    kb.button(text='➕ Мои каналы')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)

def get_inline_channel_admin_buttons_delete() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='Удалить 1 канал', callback_data='delete_silk_and_id_1')
    kb.button(text='Удалить 2 канал', callback_data='delete_silk_and_id_2')
    kb.button(text='Удалить 3 канал', callback_data='delete_silk_and_id_3')
    kb.button(text='Удалить 4 канал', callback_data='delete_silk_and_id_4')
    kb.button(text='Удалить 5 канал', callback_data='delete_silk_and_id_5')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)

def get_choise_media() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='📷 Фото', callback_data='photo_media')
    kb.button(text='🎞 Видео', callback_data='video_media')
    kb.button(text='❌ Ничего', callback_data='none_media')
    kb.adjust(2, 1)
    return kb.as_markup(resize_keyboard=True)

def get_end_send_ras():
    kb = InlineKeyboardBuilder()
    kb.button(text='Да', callback_data='end_ras_yes')
    kb.button(text='Нет', callback_data='end_ras_no')
    kb.adjust(1, 1)
    return kb.as_markup(resize_keyboard=True)

def get_nemeling_silk():
    kb = InlineKeyboardBuilder()
    kb.button(text='🔮 Подробнее', callback_data='nemeling_silk', url='https://t.me/Osobie_v_bot')
    kb.adjust(1, 1)
    return kb.as_markup(resize_keyboard=True)