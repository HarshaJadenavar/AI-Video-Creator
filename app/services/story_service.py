from pathlib import Path
from app.ai.gemini import GeminiAI


class StoryService:

    def __init__(self):
        self.gemini = GeminiAI()

    def generate_story(self, prompt, project_name):

        # Generate story using Gemini
        story = self.gemini.generate_story(prompt)

        # Create project folder
        project_folder = Path("projects") / project_name
        project_folder.mkdir(parents=True, exist_ok=True)

        # Create subfolders
        (project_folder / "images").mkdir(exist_ok=True)
        (project_folder / "audio").mkdir(exist_ok=True)
        (project_folder / "video").mkdir(exist_ok=True)

        # Save story
        with open(project_folder / "story.txt", "w", encoding="utf-8") as file:
            file.write(story)

        # Return JSON
        return {
            "success": True,
            "story": story
        }