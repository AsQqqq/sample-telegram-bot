from aiogram import Bot, Dispatcher
from setting.config import get_key
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


print("Запуск настроек приложения")
bot = Bot(token=get_key(key="TELEGRAM_KEY"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
print("bot создан")
dp = Dispatcher(storage=MemoryStorage())
print("dp создан")