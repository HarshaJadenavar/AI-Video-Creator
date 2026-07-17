import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


class GeminiAI:

    def __init__(self):
        self.model = model

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
            response = self.model.generate_content(full_prompt)

            if response.text:
                return response.text.strip()

            return "Story generation failed."

        except Exception as e:
            return f"Error: {str(e)}"