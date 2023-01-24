from aiogram import types
from setting_bot_ import bot, dp

@dp.message_handler(commands="start")
async def start(message: types.Message):
    try:
        await message.delete()
    except Exception as es:
        return "ERROR: ", es
    user_id = message.from_user.id
    text = "Привет!"
    await bot.send_message(user_id, text)

def start_file_start():
    return "Файл запущен"