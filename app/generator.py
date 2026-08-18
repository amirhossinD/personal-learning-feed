import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_lesson():
    prompt = """
You are my personal learning feed.

Create ONE short micro-learning lesson for me.

Topic:
Business and entrepreneurship

Requirements:
- 3 to 5 minutes of reading
- Assume the reader is an intelligent software engineer and aspiring founder
- Do not explain basic concepts like to a beginner
- Focus on one specific concept
- Explain the concept clearly
- Include one practical insight
- End with one question that makes me think
- No unnecessary introduction
- No motivational fluff

Format:

🧠 TITLE

Explanation

💡 Key Insight:
...

🧩 Think:
...

⏱ 3-5 min
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )

    return response.text