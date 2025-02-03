from aiogram import types
from aiogram.fsm.context import FSMContext
from src.services.gemini import generate_gemini_response
from src.utils.text_formatter import prepare_message_for_telegram
import logging
import re

logger = logging.getLogger(__name__)


def format_response(text: str) -> str:
    """Форматирует ответ, оборачивая блоки кода в HTML-теги code."""
    # Ищем блоки кода, обрамленные ``` или `
    code_blocks_pattern = r"```[\s\S]*?```|`[\s\S]*?`"

    def replace_code_block(match):
        code = match.group(0)
        # Убираем обрамляющие ``` или `
        code = code.strip("`")
        # Оборачиваем в HTML-тег code
        return f"\n<code>{code}</code>\n"

    # Заменяем все блоки кода
    formatted_text = re.sub(code_blocks_pattern, replace_code_block, text)
    return formatted_text


async def handle_message(message: types.Message, state: FSMContext):
    if message.text.startswith("/clear"):
        await state.set_data({"history": []})
        await message.answer("✨ <b>История диалога очищена!</b>")
        return

    # Логирование входящих сообщений и состояния
    current_state = await state.get_data()
    logger.debug(f"Новое сообщение: {message.text}")
    logger.debug(f"Текущее состояние: {current_state}")

    # Получаем историю, инициализируем для маркировки: добавляем префикс "Пользователь:"
    history = current_state.get("history", [])
    user_message = f"👤 Пользователь: {message.text}"
    history.append(user_message)

    # Объединяем историю в один контекст
    context_text = "\n".join(history)
    logger.debug(f"Формируемый контекст для API: {context_text}")

    try:
        response = await generate_gemini_response(context_text)
        bot_message = f"🤖 Бот: {response}"

        # Форматируем ответ с безопасной обработкой кода
        formatted_response = prepare_message_for_telegram(response)
        formatted_message = f"<b>🤖 Ответ:</b>\n\n{formatted_response}"
        await message.answer(formatted_message, parse_mode="HTML")

        # В историю сохраняем оригинальный текст
        history.append(bot_message)
        await state.update_data(history=history)

        logger.debug(f"Сохранено в историю: {bot_message}")
    except Exception as e:
        logger.error(f"Ошибка в handle_message: {e}")
        await message.answer(
            "⚠️ <b>Произошла ошибка при обработке сообщения.</b>\nПопробуйте позже."
        )
