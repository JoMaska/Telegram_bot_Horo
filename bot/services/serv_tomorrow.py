import openai
import logging
from config.config import Config, load_config


Config = load_config()




openai.api_key = Config.serv.openai_api_key

async def openai_cmd_tomorrow_1(bot):
    await bot.send_message(text=f"Сейчас начнется рассылка для гороскопа на завтра", chat_id=Config.tg_bot.admin_id)
    responce_1 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для овнов на завтра',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Овен завтра{responce_1['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)

    responce_2 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для тельцов на завтра',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Телец завтра{responce_2['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_3 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для близнецов на завтра',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Близнецы завтра{responce_3['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
async def openai_cmd_tomorrow_2(bot):
    responce_4 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для раков на завтра',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Рак завтра{responce_4['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_5 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для львов на завтра',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Лев завтра{responce_5['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_6 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для дев на завтра',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Дева завтра{responce_6['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
async def openai_cmd_tomorrow_3(bot):
    responce_7 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для весов на завтра',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Весы завтра{responce_7['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_8 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для скорпионов на завтра',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Скорпион завтра{responce_8['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_9 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для стрельцов на завтра',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Стрелец завтра{responce_9['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
async def openai_cmd_tomorrow_4(bot):
    responce_10 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для козерогов на завтра',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Козерог завтра{responce_10['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_11 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для водолеев на завтра',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Водолей завтра{responce_11['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_12 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для рыб на завтра',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Рыбы завтра{responce_12['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    await bot.send_message(text=f"Конец рассылки гороскопа на завтра", chat_id=Config.tg_bot.admin_id)
    
    