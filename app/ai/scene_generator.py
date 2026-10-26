import json
from app.ai.gemini import GeminiAI


class SceneGenerator:

    def __init__(self):
        self.gemini = GeminiAI()

    def generate_scenes(self, story):

        prompt = f"""
You are a professional storyboard creator.

Convert the following children's story into a storyboard.

IMPORTANT RULES:

- Return ONLY valid JSON.
- Do NOT use markdown.
- Do NOT use ```json.
- Do NOT explain anything.
- Return only a JSON array.

Each scene must contain:

- scene
- title
- description
- image_prompt
- duration

Story:

{story}
"""

        response = self.gemini.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
            )

        text = response.text.strip()

        print("\n========== GEMINI RESPONSE ==========\n")
        print(text)
        print("\n=====================================\n")

        # Remove markdown if Gemini accidentally adds it
        if text.startswith("```json"):
            text = text.replace("```json", "", 1).strip()

        if text.startswith("```"):
            text = text.replace("```", "", 1).strip()

        if text.endswith("```"):
            text = text[:-3].strip()

        try:
            scenes = json.loads(text)
            return scenes

        except json.JSONDecodeError as e:
            print("\nJSON PARSE ERROR\n")
            print(text)
            raise Exception(f"Failed to parse Gemini JSON: {e}")