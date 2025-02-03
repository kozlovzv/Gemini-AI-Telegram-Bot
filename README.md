# 🤖 Gemini AI Telegram Bot

Telegram бот с интеграцией Google Gemini AI, поддерживающий контекстные диалоги и форматирование кода.

## 🛠 Установка

### Через Docker (рекомендуется)
```bash
# 1. Клонируйте репозиторий
git clone git@github.com:kozlovzv/GeminiChat.git
cd GeminiChat

# 2. Создайте файл .env
BOT_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key

# 3. Запустите бота
docker compose up -d --build
```

### Локальная установка
```bash
# 1. Клонируйте репозиторий, если еще не сделали
git clone git@github.com:kozlovzv/GeminiChat.git
cd GeminiChat

# 2. Создайте виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# или
.venv\Scripts\activate     # Windows

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Запустите бота
python -m src.bot
```

## 🚀 Возможности

- Контекстные диалоги (бот помнит историю общения)
- Форматирование кода с подсветкой синтаксиса
- HTML-разметка сообщений
- Автоматический перезапуск при сбоях (в Docker)
- Подробное логирование

## 🎯 Команды бота

- `/start` - Начать диалог
- `/help` - Список команд
- `/clear` - Очистить историю

## 🐳 Docker команды

```bash
# Просмотр логов
docker compose logs -f

# Остановка бота
docker compose down

# Перезапуск
docker compose restart
```

## 📁 Структура проекта
```
GeminiChat/
├── src/
│   ├── bot.py           # Инициализация бота
│   ├── handlers/        # Обработчики команд
│   ├── services/        # API сервисы
│   └── utils/          # Форматирование, логи
├── Dockerfile          # Сборка Docker образа
├── docker-compose.yml  # Конфигурация Docker
├── requirements.txt    # Зависимости
└── .env               # Переменные окружения
```

## ⚙️ Переменные окружения

- `BOT_TOKEN`: Получить у @BotFather
- `GEMINI_API_KEY`: Получить в Google AI Studio

## 📋 Требования

- Python 3.9+
- Docker и Docker Compose (для контейнеризации)
- Токены для Telegram и Gemini API

## 🤝 Разработка

1. Форкните репозиторий на [GitHub](https://github.com/kozlovzv/GeminiChat)
2. Создайте ветку для новой функции
3. Отправьте пулл-реквест в основной репозиторий

## 📝 Логирование

Бот использует стандартный модуль logging Python:
- DEBUG: Детальная отладка
- INFO: Основные события
- ERROR: Ошибки и исключения

## 📄 Лицензия

MIT License
