from aiogram.utils import executor
from setting_bot_.settingBot import dp
from handler_.main.start.start import start_file_start
from handler_.main.other_.unknown_word import start_file_unknows_word

start_file_start()

"""---OTHER---"""
start_file_unknows_word()

async def on_startup(_):
    print("Код запущен!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)