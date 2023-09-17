import openai
import logging
from config.config import Config, load_config


Config = load_config()




openai.api_key = Config.serv.openai_api_key

async def openai_cmd_year_1(bot):
    await bot.send_message(text=f"Сейчас начнется рассылка для гороскопа на год", chat_id=Config.tg_bot.admin_id)
    responce_1 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для овнов на этот год',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Овен год{responce_1['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)

    responce_2 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для тельцов на этот год',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Телец год{responce_2['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_3 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для близнецов на этот год',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Близнецы год{responce_3['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
async def openai_cmd_year_2(bot):
    responce_4 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для раков на этот год',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Рак год{responce_4['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_5 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для львов на этот год',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Лев год{responce_5['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_6 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для дев на этот год',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Дева год{responce_6['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
async def openai_cmd_year_3(bot):
    responce_7 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для весов на этот год',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Весы год{responce_7['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_8 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для скорпионов на этот год',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Скорпион год{responce_8['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_9 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для стрельцов на этот год',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Стрелец год{responce_9['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
async def openai_cmd_year_4(bot):
    responce_10 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для козерогов на этот год',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Козерог год{responce_10['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_11 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для водолеев на этот год',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Водолей год{responce_11['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    
    responce_12 = openai.Completion.create(
        model='text-davinci-003',
        prompt='Придумай гороскоп для рыб на этот год',
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        )
    await bot.send_message(text=f"🔮 Рыбы год{responce_12['choices'][0]['text']}", chat_id=Config.tg_bot.admin_id)
    await bot.send_message(text=f"Конец рассылки гороскопа на год", chat_id=Config.tg_bot.admin_id)
    
    