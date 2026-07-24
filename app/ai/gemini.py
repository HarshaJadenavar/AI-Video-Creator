import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class GeminiAI:

    def __init__(self):
        self.client = client

    def generate_story(self, prompt):

        full_prompt = f"""
You are a professional YouTube Kids story writer.

Your task is to create an ORIGINAL children's story.

Rules:
- Write ONLY the story.
- Do NOT explain anything.
- Do NOT give tips.
- Do NOT ask questions.
- Do NOT use markdown.
- Do NOT use headings.
- Do NOT write "Here is your story".
- Do NOT include introductions or conclusions outside the story.

Story Requirements:
- Age group: 4-10 years
- Language: Simple English
- Tone: Fun, emotional and engaging
- Happy ending
- Include a moral lesson
- Around 180-250 words
- Natural narration suitable for AI voice generation
- Keep the story visually descriptive so images can be generated later.

Story Idea:
{prompt}
"""

        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=full_prompt
            )

            return response.text.strip()

        except Exception as e:
            return f"Error: {e}"