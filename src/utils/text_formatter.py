import re

MARKDOWN_SPECIAL_CHARS = r"[_*\[\]()~`>#+\-=|{}.!]"


def contains_markdown_chars(text: str) -> bool:
    """Проверяет, содержит ли текст специальные символы Markdown."""
    return bool(re.search(MARKDOWN_SPECIAL_CHARS, text))


def escape_markdown(text: str) -> str:
    """Экранирует специальные символы Markdown в тексте."""
    if not text:
        return text

    def escape_char(match):
        return f"\\{match.group(0)}"

    return re.sub(MARKDOWN_SPECIAL_CHARS, escape_char, text)


def escape_html(text: str) -> str:
    """Экранирует HTML-символы в тексте."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def format_code_blocks(text: str) -> str:
    """Форматирует блоки кода с экранированием HTML."""

    # Паттерн для поиска блоков кода
    code_pattern = r"```([\s\S]*?)```|`([^`]+)`"

    def process_code_block(match):
        # Получаем содержимое блока кода
        multi_line = match.group(1)
        single_line = match.group(2)

        if multi_line is not None:
            # Многострочный блок кода
            escaped_code = escape_html(multi_line.strip())
            return f"\n<pre><code>{escaped_code}</code></pre>\n"
        else:
            # Однострочный блок кода
            escaped_code = escape_html(single_line)
            return f"<code>{escaped_code}</code>"

    # Заменяем все блоки кода с экранированием
    return re.sub(code_pattern, process_code_block, text)


def prepare_message_for_telegram(text: str) -> str:
    """Подготавливает сообщение для отправки в Telegram."""
    # Форматируем блоки кода
    formatted_text = format_code_blocks(text)
    return formatted_text


def prepare_text_for_telegram(text: str) -> str:
    """Подготавливает текст для отправки в Telegram."""
    if contains_markdown_chars(text):
        return escape_markdown(text)
    return text
