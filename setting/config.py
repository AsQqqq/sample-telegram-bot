import os
from dotenv import load_dotenv



def get_key(key: str) -> str:
    """
    Передача данных из конфига
    """

    dotenv_path = os.path.join('.', '.env')

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    return os.getenv(key)
