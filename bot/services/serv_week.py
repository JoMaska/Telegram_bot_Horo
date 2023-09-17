import openai
import logging
from config.config import Config, load_config

Config = load_config()

openai.api_key = Config.serv.openai_api_key

async def openai_cmd_week_1(bot):
    await bot.send_message(text=f"Сейчас начнется рассылка для гороскопа на неделю", chat_id=Config.tg_bot.admin_id)
    responce_1 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для овнов на неделю',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Овен неделя{responce_1['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)

    responce_2 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для тельцов на неделю',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Телец неделя{responce_2['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_3 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для близнецов на неделю',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Близнецы неделя{responce_3['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
async def openai_cmd_week_2(bot):
    responce_4 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для раков на неделю',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Рак неделя{responce_4['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_5 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для львов на неделю',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Лев неделя{responce_5['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_6 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для зодиака "дева" на неделю',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Дева неделя{responce_6['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
async def openai_cmd_week_3(bot):
    responce_7 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для весов на неделю',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Весы неделя{responce_7['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_8 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для скорпионов на неделю',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Скорпион неделя{responce_8['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_9 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для стрельцов на неделю',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Стрелец неделя{responce_9['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
async def openai_cmd_week_4(bot):
    responce_10 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для козерогов на неделю',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Козерог неделя{responce_10['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_11 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для водолеев на неделю',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Водолей неделя{responce_11['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_12 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для рыб на неделю',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Рыбы неделя{responce_12['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    await bot.send_message(text=f"Конец рассылки гороскопа на неделю", chat_id=Config.tg_bot.admin_id)
    