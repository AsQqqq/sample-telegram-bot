from database import SessionLocal
from database import User


def user_exists(user_id: int) -> bool:
    """
    Проверяет, существует ли пользователь в базе данных.
    """

    with SessionLocal() as session:
        return session.query(User).filter(User.user_id == str(user_id)).first() is not None


def new_user(user_id: int) -> bool:
    """
    Записывает пользователя в таблицу, если его там нет.
    """

    if user_exists(user_id):
        return False  # Пользователь уже существует

    with SessionLocal() as session:
        user = User(user_id=str(user_id))
        session.add(user)
        session.commit()
        return True
