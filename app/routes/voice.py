from flask import Blueprint, request, jsonify, send_from_directory
from pathlib import Path

from app.services.voice_service import VoiceService

voice_bp = Blueprint("voice", __name__)

service = VoiceService()

# Absolute path to project root
BASE_DIR = Path(__file__).resolve().parents[2]


@voice_bp.route("/generate-voice", methods=["POST"])
def generate_voice():

    data = request.get_json()

    project_name = data["project_name"]

    audio_files = service.generate(project_name)

    return jsonify(audio_files)


@voice_bp.route("/projects/<path:project_name>/audio/<path:filename>")
def get_audio(project_name, filename):

    folder = BASE_DIR / "projects" / project_name / "audio"

    return send_from_directory(folder, filename)