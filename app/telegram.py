import os
import requests


MAX_MESSAGE_LENGTH = 4096


def send_message(text: str):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not text or not text.strip():
        raise ValueError("Telegram message is empty.")

    print(f"Message length: {len(text)} characters")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # Telegram allows max 4096 characters per text message.
    chunks = [
        text[i:i + MAX_MESSAGE_LENGTH]
        for i in range(0, len(text), MAX_MESSAGE_LENGTH)
    ]

    for index, chunk in enumerate(chunks, start=1):
        response = requests.post(
            url,
            json={
                "chat_id": chat_id,
                "text": chunk,
            },
            timeout=10,
        )

        print(f"Telegram response for chunk {index}: {response.text}")

        response.raise_for_status()

    return True