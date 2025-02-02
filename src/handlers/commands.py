from aiogram import types


async def cmd_start(message: types.Message):
    welcome_message = """
🤖 *Привет! Я AI-бот с интеграцией Gemini*
Отправь мне любое сообщение, и я постараюсь помочь!
    """
    await message.answer(welcome_message)


async def cmd_help(message: types.Message):
    help_message = """
🤖 *Доступные команды:*
/start - Начать диалог
/help - Показать помощь

Просто отправьте мне любой текст, и я отвечу с помощью Gemini AI!
    """
    await message.answer(help_message)
