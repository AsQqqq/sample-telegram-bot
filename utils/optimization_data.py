from setting import logger
from setting.config import get_key


def validateName(first_name: str, last_name: str):
    """
    Проверяет ФИО на правильность написания и возвращает ФИО в нижнем регистре без символов < и >.
    """
    
    # Инициализация списка для ФИО
    fio = []
    
    # Проверка на присутствие имени и фамилии
    if first_name and last_name:
        fio = [first_name, last_name]
        logger.info(f"Проверка полного ФИО: {fio}")
    elif first_name:
        logger.info(f"Проверка имени: {first_name}")
        fio = [first_name]
    elif last_name:
        fio = [last_name]
        logger.info(f"Проверка фамилии: {last_name}")
    
    # Обработка каждого элемента в ФИО
    FIO = []
    for i in fio:
        # Удаление символов < и >
        i = i.replace("<", "").replace(">", "").lower()
        
        # Делаем первую букву заглавной, если это буква
        if i and i[0].isalpha():
            i = i.capitalize()
        
        FIO.append(i)
    
    # Логирование успешной проверки
    logger.info(f"ФИО '{FIO}' успешно прошло проверку")
    
    # Возвращаем ФИО в виде строки с пробелом между именем и фамилией
    return " ".join(FIO)


async def getUserData(message: dict) -> dict:
    """
    Получение данных пользователя
    """

    user_id = message.from_user.id
    first_name=message.from_user.first_name
    last_name=message.from_user.last_name
    all_admins = get_key("TELEGRAM_ADMIN").split(',')
    is_admin = True if str(user_id) in all_admins else False
    full_name = validateName(
        first_name=first_name,
        last_name=last_name
    )

    return {
        "user_id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        "is_admin": is_admin
    }