"""
Файл старта бота, основная команда /start
"""

from aiogram import Router, F, types
from setting.bot import bot
from setting import logger
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from utils import getUserData


logger.info("Файл start запущен!")
start_router = Router()


@start_router.message(F.text.startswith("/start"))
async def start_func(message: Message, state: FSMContext) -> None:
    """
    Первая функция для команды /start
    """

    data = await getUserData(message=message)

    text = f"Привет, {data['full_name']}, статус админа: {data['is_admin']}"
    await message.answer(text)