import openai
import logging
from config.config import Config, load_config


Config = load_config()




openai.api_key = Config.serv.openai_api_key

async def openai_cmd_month_1(bot):
    await bot.send_message(text=f"Сейчас начнется рассылка для гороскопа на месяц", chat_id=Config.tg_bot.admin_id)
    responce_1 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для овнов на этот месяц',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Овен месяц{responce_1['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)

    responce_2 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для тельцов на этот месяц',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Телец месяц{responce_2['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_3 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для близнецов на этот месяц',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Близнецы месяц{responce_3['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
async def openai_cmd_month_2(bot):
    responce_4 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для раков на этот месяц',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Рак месяц{responce_4['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_5 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для львов на этот месяц',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Лев месяц{responce_5['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_6 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для дев на этот месяц',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Дева месяц{responce_6['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
async def openai_cmd_month_3(bot):
    responce_7 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для весов на этот месяц',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Весы месяц{responce_7['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_8 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для скорпионов на этот месяц',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Скорпион месяц{responce_8['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_9 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для стрельцов на этот месяц',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Стрелец месяц{responce_9['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
async def openai_cmd_month_4(bot):
    responce_10 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для козерогов на этот месяц',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Козерог месяц{responce_10['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_11 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для водолеев на этот месяц',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Водолей месяц{responce_11['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_12 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для рыб на этот месяц',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Рыбы месяц{responce_12['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    await bot.send_message(text=f"Конец рассылки гороскопа на месяц", chat_id=Config.tg_bot.admin_id)
    
    