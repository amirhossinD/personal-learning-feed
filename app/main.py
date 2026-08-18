from dotenv import load_dotenv

from generator import generate_lesson
from telegram import send_message


load_dotenv()


if __name__ == "__main__":
    lesson = generate_lesson()

    send_message(lesson)

    print("Learning lesson sent successfully.")