import os
import aiohttp
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in environment variables.")

GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"


async def generate_gemini_response(prompt: str) -> str:
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                GEMINI_API_URL, json=payload, headers=headers
            ) as response:
                if response.status != 200:
                    error_text = await response.text()
                    logger.error(
                        f"API Error: Status {response.status}, Response: {error_text}"
                    )
                    return f"⚠️ Ошибка при обращении к API Gemini (Статус: {response.status})"

                json_response = await response.json()
                logger.debug(f"API response json: {json_response}")
                try:
                    return json_response["candidates"][0]["content"]["parts"][0]["text"]
                except (KeyError, IndexError) as e:
                    logger.error(f"Parse Error: {str(e)}, Response: {json_response}")
                    return "❌ Не удалось обработать ответ от Gemini"
    except aiohttp.ClientError as e:
        logger.error(f"Connection Error: {str(e)}")
        return "🔌 Ошибка подключения к API Gemini"
    except Exception as e:
        logger.error(f"Unexpected Error: {str(e)}")
        return "⚠️ Произошла непредвиденная ошибка"
