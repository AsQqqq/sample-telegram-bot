"""
Файл старта бота, основная команда /start
"""

from aiogram import Router, F
from setting import logger
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils import getUserData
from database.request import new_user, user_exists


logger.info("Файл start запущен!")
start_router = Router()


@start_router.message(F.text.startswith("/start"))
async def start_func(message: Message, state: FSMContext) -> None:
    """
    Первая функция для команды /start
    """

    data = await getUserData(message=message)
    logger.info(f"Запущена команда /start от пользователя - {data['user_id']}")

    # Запись пользователя в базу данных!
    if user_exists(data['user_id']) == True:
        logger.info(f"Пользователь с ID {data['user_id']} уже зарегистрирован")
    else:
        logger.info(f"Новый пользователь с ID {data['user_id']} зарегистрирован")
        new_user(data['user_id'])

        logger.info(f"Данные пользователя {data['user_id']} успешно сохранены в БД")

    text = f"Привет, {data['full_name']}, статус админа: {data['is_admin']}"
    await message.answer(text)