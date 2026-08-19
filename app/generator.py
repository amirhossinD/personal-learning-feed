import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_lesson(lesson_spec):
    prompt = f"""
You are my personal learning tutor.

Generate one learning unit based on this specification:

Domain:
{lesson_spec["domain"]}

Learning type:
{lesson_spec["learning_type"]}

Topic:
{lesson_spec["topic"]}

Difficulty:
{lesson_spec["difficulty"]}

Target duration:
{lesson_spec["duration_minutes"]} minutes

My overall goal:
Build broad and progressively deep knowledge required to become a capable founder who can build teams, build products, run a company, and make better decisions.

Important requirements:

- Teach one specific concept deeply enough to be useful.
- Assume the learner is an intelligent software engineer and aspiring founder.
- Do not explain things in a childish or overly simplified way.
- Connect the concept to real-world decision making when appropriate.
- Do not add motivational fluff.
- Prefer reasoning, trade-offs, mechanisms, and practical implications.
- If the topic is part of a progression, build naturally on the topic rather than restarting from basics.
- Keep the unit under 10 minutes.

Structure:

🧠 Title

Explanation

💡 Key insight

🔗 Practical application


⏱ Estimated reading time
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )

    lesson = response.text

    if not lesson or not lesson.strip():
        raise ValueError("Gemini returned an empty response.")

    return lesson