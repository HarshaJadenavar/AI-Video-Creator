from pathlib import Path
import json

def save_project(project_name, story, scenes):

    project = Path("projects") / project_name

    project.mkdir(parents=True, exist_ok=True)

    (project / "images").mkdir(exist_ok=True)
    (project / "audio").mkdir(exist_ok=True)
    (project / "video").mkdir(exist_ok=True)

    with open(project / "story.txt", "w", encoding="utf-8") as file:
        file.write(story)

    with open(project / "scenes.json", "w", encoding="utf-8") as file:
        json.dump(scenes, file, indent=4)