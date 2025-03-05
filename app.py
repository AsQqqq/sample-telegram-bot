from setting.bot import bot, dp
from setting import logger, clear
from setting.config import get_key
from datetime import datetime
from handler import sr_start
import asyncio
import database


async def main():
    clear()

    # Регистрируем оброботчики
    dp.include_router(sr_start)

    await bot.delete_webhook(drop_pending_updates=True)
    logger.warning("Бот запущен!")

    all_admins = get_key("TELEGRAM_ADMIN").split(',')
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for admin in all_admins:
        try:
            admin = int(admin)
            await bot.send_message(chat_id=admin, text=f"Bot started at {start_time}")
        except Exception as e:
            logger.warning(f"Failed to send message to {admin}: {e}")

    await dp.start_polling(bot)


if __name__ == '__main__':
    logger.info("Запуск бота...")
    asyncio.run(main())