from flask import Blueprint
from flask import request
from flask import jsonify

from app.services.scene_service import SceneService

scene_bp = Blueprint(
    "scene",
    __name__
)

service = SceneService()


@scene_bp.route("/generate-scenes",methods=["POST"])
def generate_scenes():

    data = request.get_json()

    project = data["project_name"]

    scenes = service.generate(project)

    return jsonify(scenes)