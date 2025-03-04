# 🚀 Шаблон бота на Aiogram 3

Добро пожаловать в репозиторий шаблона бота на **Aiogram 3**! 📌 Этот проект предназначен для быстрого старта при разработке Telegram-ботов с использованием **асинхронного фреймворка Aiogram**.

## Языки и инструменты
![Python](https://img.shields.io/badge/-Python-4B0082?style=for-the-badge&logo=python&logoColor=FFD700)
![Aiogram](https://img.shields.io/badge/-aiogram-4B0082?style=for-the-badge&logo=aiogram&logoColor=7CFC00)


## 🌳 Структура проекта

Проект разделен на несколько папок для удобства и лучшей организации кода.

### 📁 handler — обработчики команд

Здесь находятся основные обработчики команд, которые обрабатывают входящие сообщения от пользователей.

- `__init__.py` — файл для импорта и запуска обработчиков.
- `start.py` — содержит обработчик команды `/start`, который приветствует пользователей и инициализирует взаимодействие с ботом.

### 📁 logs — логирование событий

Логи бота автоматически записываются с помощью библиотеки **cololog**. Она позволяет удобно отслеживать ошибки и события.

Установка библиотеки:

```bash
pip install cololog
```

### 📁 setting — основные настройки бота

В этой папке хранятся конфигурационные файлы и важные параметры:

- `__init__.py` — импорт всех настроек бота, логирования и функций очистки консоли.
- `bot.py` — содержит основные настройки, а также создает экземпляры **bot** и **dp (dispatcher)** для обработки сообщений.
- `config.py` — отвечает за загрузку параметров из `.env` файла. [Подробнее об этом ниже](#🔧-настройки).
- `logger.py` — конфигурация логирования, включая указание пути сохранения логов и функцию очистки консоли на разных ОС.

### 📁 utils — вспомогательные утилиты

Папка содержит модули для обработки данных и оптимизации работы бота:

- `optimization_data.py` — отвечает за валидацию данных пользователя (ФИО) и генерацию JSON-профиля.

Пример выходных данных:

```json
{
    "user_id": 12345678,
    "first_name": "имя<",
    "last_name": "фамилия",
    "full_name": "Имя Фамилия",
    "is_admin": false
}
```

Входные данные это ``message`` из обработчика.

✅ Функция автоматически удаляет нежелательные символы (например, `<`), которые могут вызывать ошибки при форматировании сообщений в HTML.

### 📝 Файл `app.py` — главный запускной файл

Этот файл используется для запуска бота:

```bash
python app.py
```

При старте:

1. Загружаются все обработчики.
2. Бот подключается к API Telegram.
3. Администраторы, указанные в `.env`, получают уведомление о запуске бота. 📩

## 🔧 Настройки

Конфигурационные параметры бота хранятся в `.env` файле. В нем можно задать **токен API**, **администраторов** и другие параметры.

Пример `.env` файла:

```env
# Токен бота Telegram
TELEGRAM_KEY=ВАШ_ТОКЕН

# Список администраторов (разделенные запятой)
TELEGRAM_ADMIN=USER1,USER2,USER3
```

## ▶️ Запуск проекта

Для корректной работы бота выполните следующие шаги:

1️⃣ **Создайте виртуальное окружение** (рекомендуется для изоляции зависимостей):

```bash
python -m venv .venv
```

2️⃣ **Активируйте виртуальное окружение**:

- Для Linux/macOS:
  ```bash
  source .venv/bin/activate
  ```
- Для Windows:
  ```bash
  source .venv/Scripts/activate
  ```

3️⃣ **Установите зависимости**:

```bash
pip install -r requirements.txt
```

4️⃣ **Запустите бота**:

```bash
python app.py
```

## 🎯 Заключение

Этот проект является **простым и удобным шаблоном** для быстрого старта разработки ботов на **Aiogram 3**. Он поможет вам:

✅ Организовать код в удобной структуре;
✅ Работать с логами для отслеживания ошибок;
✅ Гибко настраивать бота через `.env` файл;
✅ Быстро развернуть и запустить своего Telegram-бота.

💡 Надеюсь, этот шаблон окажется **полезным** и сэкономит ваше время при создании нового бота! 🚀

### Связь со мной
[![Telegram](https://img.shields.io/badge/-Telegram-4B0082?style=for-the-badge&logo=telegram)](https://t.me/danilka_pikaso)
