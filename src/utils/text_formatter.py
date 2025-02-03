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


def prepare_text_for_telegram(text: str) -> str:
    """Подготавливает текст для отправки в Telegram."""
    if contains_markdown_chars(text):
        return escape_markdown(text)
    return text
