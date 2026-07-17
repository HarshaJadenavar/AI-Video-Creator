import json
from pathlib import Path

from app.ai.scene_generator import SceneGenerator


class SceneService:

    def __init__(self):
        self.generator = SceneGenerator()

    def generate(self, project_name):

        project = Path("projects") / project_name

        story = (project / "story.txt").read_text(
            encoding="utf-8"
        )

        scenes = self.generator.generate_scenes(story)

        with open(
            project / "scenes.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                scenes,
                file,
                indent=4,
                ensure_ascii=False
            )

        return scenes