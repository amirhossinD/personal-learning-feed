from dotenv import load_dotenv

from feed_engine import (
    create_lesson_spec,
    save_lesson_to_history,
)
from generator import generate_lesson
from telegram import send_message


load_dotenv()


if __name__ == "__main__":
    lesson_spec = create_lesson_spec()

    print("Selected lesson:")
    print(lesson_spec)

    lesson = generate_lesson(lesson_spec)

    send_message(lesson)

    save_lesson_to_history(lesson_spec)

    print("Learning lesson sent successfully.")