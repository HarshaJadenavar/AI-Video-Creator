from flask import Blueprint, request, jsonify
from app.services.story_service import StoryService

api_bp = Blueprint("api", __name__)

story_service = StoryService()


@api_bp.route("/generate-story", methods=["POST"])
def generate_story():
    data = request.get_json()

    prompt = data.get("prompt", "")
    project_name = data.get("project_name", "my_project")

    result = story_service.generate_story(
        prompt,
        project_name
    )

    return jsonify(result)