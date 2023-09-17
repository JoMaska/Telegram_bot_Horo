from environs import Env
from dataclasses import dataclass

@dataclass
class Serv:
    openai_api_key: str

@dataclass
class Channel:
    channel_1: str
    channel_2: str

@dataclass
class TgBot:
    token: str
    url: str
    admin_id: str
@dataclass
class Config:
    tg_bot: str
    serv: str
    
def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            url=env('DB_URL'),
            admin_id=env('ADMIN_ID')
            ),
        serv=Serv(
            openai_api_key=env('OPENAI_API_KEY')
        )
        )