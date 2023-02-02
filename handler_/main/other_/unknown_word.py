from aiogram import types
from setting_bot_ import bot, dp

async def other(message: types.Message):
    try:
        await message.delete()
    except Exception as es:
        return "ERROR: ", es
    user_id = message.from_user.id
    text = "Данная команда не известна, напиши /help"
    await bot.send_message(user_id, text)

def start_file_unknows_word(dp):
    dp.register_message_handler(other)