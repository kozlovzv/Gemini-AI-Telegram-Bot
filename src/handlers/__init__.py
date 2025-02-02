# Этот файл может быть пустым, так как мы перенесли логику регистрации хендлеров в bot.py

from aiogram import Dispatcher, F
from aiogram.filters import Command
from src.handlers.commands import cmd_start, cmd_help

# Импортируем обработчик сообщений из message_handler.py
from src.handlers.message_handler import handle_message


def register_handlers(dp: Dispatcher):
    # Регистрируем обработчики команд
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_help, Command("help"))

    # Регистрируем обработчик для обычных сообщений
    dp.message.register(handle_message, F.text)


# Этот файл помечает директорию как пакет Python
