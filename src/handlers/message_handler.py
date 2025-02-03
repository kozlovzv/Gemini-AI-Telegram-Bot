from aiogram import types
from aiogram.fsm.context import FSMContext
from src.services.gemini import generate_gemini_response
import logging

logger = logging.getLogger(__name__)


async def handle_message(message: types.Message, state: FSMContext):
    # Проверяем команду очистки истории
    if message.text.startswith("/clear"):
        await state.set_data({"history": []})
        await message.answer("История очищена.")
        return

    # Логирование входящих сообщений и состояния
    current_state = await state.get_data()
    logger.debug(f"Новое сообщение: {message.text}")
    logger.debug(f"Текущее состояние: {current_state}")

    # Получаем существующую историю или инициализируем
    history = current_state.get("history", [])
    history.append(message.text)

    # Объединяем историю в один контекст
    context_text = "\n".join(history)
    logger.debug(f"Формируемый контекст для API: {context_text}")

    try:
        response = await generate_gemini_response(context_text)
        await message.answer(response)
        # Добавляем ответ в историю (опционально)
        history.append(response)
        await state.update_data(history=history)
    except Exception as e:
        logger.error(f"Ошибка в handle_message: {e}")
        await message.answer(
            "Произошла ошибка при обработке сообщения. Попробуйте позже."
        )
