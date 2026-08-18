import os

from dotenv import load_dotenv

from telegram import send_message


load_dotenv()


if __name__ == "__main__":
    send_message(
        "🧠 Personal Learning Feed\n\n"
        "Your feed is alive."
    )

    print("Message sent successfully.")