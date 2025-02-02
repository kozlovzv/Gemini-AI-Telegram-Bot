from aiogram import types
from src.services.gemini import generate_gemini_response


async def handle_message(message: types.Message):
    if message.text and not message.text.startswith("/"):
        try:
            response = await generate_gemini_response(message.text)
            await message.answer(response)
        except Exception as e:
            await message.answer(
                "Произошла ошибка при обработке сообщения. Попробуйте позже."
            )
