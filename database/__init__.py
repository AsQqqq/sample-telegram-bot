from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from setting.config import get_key
from setting import logger

# Строка подключения к PostgreSQL
username = get_key(key="USERNAME")
password = get_key(key="PASSWORD")
ip_address = get_key(key="IP_ADDRESS")
db_name = get_key(key="DATABASE_NAME")

# Получение типа базы данных
db_type = get_key(key="DATABASE_TYPE")

# Логика подключения
if db_type == "sqlite":
    DATABASE_URL = f"sqlite:///./{db_name}.db"
elif db_type == "mysql":
    DATABASE_URL = f"mysql+pymysql://{username}:{password}@{ip_address}/{db_name}"
elif db_type == "postgresql":
    DATABASE_URL = f"postgresql://{username}:{password}@{ip_address}/{db_name}"
else:
    raise ValueError("Unsupported database type")

logger.info(f"Подключение к базе данных {db_type}...")

# Создаем объект engine
try:
    engine = create_engine(DATABASE_URL)
    logger.info(f"Успешное подключение к {db_type}")
except Exception as e:
    logger.error(f"Ошибка подключения к {db_type}: {e}")
    raise

# Создаем базовый класс для декларативных моделей
Base = declarative_base()

# Создаем сессию для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logger.info("Сессия создана!")

# Функция для создания сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
# Тут нужно изменить под ваши задачи!
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True, nullable=False)

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)