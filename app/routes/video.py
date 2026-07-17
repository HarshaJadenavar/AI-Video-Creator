from flask import Blueprint, request, jsonify, send_from_directory
from pathlib import Path

from app.services.video_service import VideoService

video_bp = Blueprint("video", __name__)

service = VideoService()

BASE_DIR = Path(__file__).resolve().parents[2]


@video_bp.route("/generate-video", methods=["POST"])
def generate_video():

    data = request.get_json()

    project_name = data["project_name"]

    video = service.generate(project_name)

    return jsonify({"video": video})


@video_bp.route("/projects/<path:project_name>/video/<path:filename>")
def get_video(project_name, filename):

    folder = BASE_DIR / "projects" / project_name / "video"

    return send_from_directory(folder, filename)