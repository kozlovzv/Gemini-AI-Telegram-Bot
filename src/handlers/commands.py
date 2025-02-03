from aiogram import types


async def cmd_start(message: types.Message):
    welcome_message = """
🤖 <b>Привет! Я AI-бот с интеграцией Gemini</b>

Отправь мне любое сообщение, и я постараюсь помочь! 
Я помню контекст нашего общения, так что можно вести полноценный диалог.
    """
    await message.answer(welcome_message)


async def cmd_help(message: types.Message):
    help_message = """
🤖 <b>Доступные команды:</b>

📝 <code>/start</code> - Начать диалог
❓ <code>/help</code> - Показать помощь
🔄 <code>/clear</code> - Очистить историю диалога

💡 Просто отправьте мне любой текст, и я отвечу с помощью <b>Gemini AI</b>!
    """
    await message.answer(help_message)
