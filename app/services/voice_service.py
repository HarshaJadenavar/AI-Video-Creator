import json
from pathlib import Path

from app.ai.voice_generator import VoiceGenerator


class VoiceService:

    def __init__(self):

        self.generator = VoiceGenerator()

    def generate(self, project_name):

        project_folder = Path("projects") / project_name

        scenes_file = project_folder / "scenes.json"

        audio_folder = project_folder / "audio"

        # Create audio folder if it doesn't exist
        audio_folder.mkdir(exist_ok=True)

        with open(scenes_file, "r", encoding="utf-8") as file:
            scenes = json.load(file)

        generated_audio = []

        for scene in scenes:

            scene_number = scene["scene"]

            # Use description as narration for now
            narration = scene["description"]

            output_file = audio_folder / f"scene_{scene_number}.mp3"

            print(f"Generating voice for Scene {scene_number}...")

            self.generator.generate_voice(
                narration,
                str(output_file)
            )

            generated_audio.append(output_file.name)

        print("Voice generation completed!")

        return generated_audio