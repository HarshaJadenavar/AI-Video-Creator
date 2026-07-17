import json
from pathlib import Path

from app.ai.image_generator import ImageGenerator


class ImageService:

    def __init__(self):

        self.generator = ImageGenerator()

    def generate(self, project_name):

        project = Path("projects") / project_name

        with open(project / "scenes.json", encoding="utf-8") as file:

            scenes = json.load(file)

        images_folder = project / "images"

        generated = []

        for scene in scenes:

            filename = f"scene_{scene['scene']}.png"

            output = images_folder / filename

            self.generator.generate_image(

                scene["image_prompt"],

                output

            )

            generated.append(filename)

        return generated