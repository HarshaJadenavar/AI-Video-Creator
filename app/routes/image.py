from flask import Blueprint, request, jsonify, send_from_directory
from app.services.image_service import ImageService
from pathlib import Path

image_bp = Blueprint("image", __name__)

service = ImageService()

# Absolute path to the project root
BASE_DIR = Path(__file__).resolve().parents[2]


@image_bp.route("/generate-images", methods=["POST"])
def generate_images():

    data = request.get_json()

    project = data["project_name"]

    images = service.generate(project)

    return jsonify(images)


@image_bp.route("/projects/<path:project_name>/images/<path:filename>")
def get_image(project_name, filename):

    folder = BASE_DIR / "projects" / project_name / "images"

    print("Serving image from:", folder)
    print("Filename:", filename)

    return send_from_directory(folder, filename)