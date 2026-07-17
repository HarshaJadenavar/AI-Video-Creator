"""
Automates creation of the AI-Video-Creator project folder structure.
Run with: python create_structure.py
"""

import os

ROOT = "AI-Video-Creator"

# Folders to create (relative to ROOT)
FOLDERS = [
    "app/routes",
    "app/ai",
    "app/services",
    "app/utils",
    "app/templates",
    "app/static/css",
    "app/static/js",
    "app/static/images",
    "generated/scripts",
    "generated/scenes",
    "generated/images",
    "generated/audio",
    "generated/subtitles",
    "generated/videos",
    "uploads/images",
    "uploads/audio",
    "uploads/scripts",
    "assets/music",
    "assets/fonts",
    "tests",
    "logs",
]

# Files to create (relative to ROOT), empty unless content specified below
FILES = [
    "app/__init__.py",
    "app/config.py",
    "app/routes/__init__.py",
    "app/routes/home.py",
    "app/routes/project.py",
    "app/routes/api.py",
    "app/ai/__init__.py",
    "app/ai/gemini.py",
    "app/ai/story_generator.py",
    "app/ai/scene_splitter.py",
    "app/ai/image_generator.py",
    "app/ai/voice_generator.py",
    "app/ai/video_creator.py",
    "app/services/story_service.py",
    "app/services/image_service.py",
    "app/services/voice_service.py",
    "app/services/video_service.py",
    "app/utils/helpers.py",
    "app/utils/logger.py",
    "app/utils/ffmpeg_utils.py",
    "app/templates/base.html",
    "app/templates/index.html",
    "app/templates/dashboard.html",
    "app/templates/project.html",
    "app/static/css/style.css",
    "app/static/js/main.js",
    ".env",
    ".gitignore",
    "requirements.txt",
    "README.md",
    "run.py",
]


def create_structure():
    # Create root
    os.makedirs(ROOT, exist_ok=True)
    print(f"Created root folder: {ROOT}/")

    # Create all folders
    for folder in FOLDERS:
        path = os.path.join(ROOT, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")

    # Create all files
    for file in FILES:
        path = os.path.join(ROOT, file)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                pass  # create empty file
            print(f"Created file: {path}")
        else:
            print(f"Already exists, skipped: {path}")

    print("\n✅ Project structure created successfully!")


if __name__ == "__main__":
    create_structure()