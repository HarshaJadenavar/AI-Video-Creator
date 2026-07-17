from pathlib import Path

from moviepy import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips
)


class VideoGenerator:

    def generate(self, project_name):

        project_folder = Path("projects") / project_name

        image_folder = project_folder / "images"
        audio_folder = project_folder / "audio"
        video_folder = project_folder / "video"

        video_folder.mkdir(exist_ok=True)

        clips = []

        image_files = sorted(image_folder.glob("*.png"))

        for image_file in image_files:

            scene_name = image_file.stem

            audio_file = audio_folder / f"{scene_name}.mp3"

            if not audio_file.exists():
                continue

            audio = AudioFileClip(str(audio_file))

            clip = (
                ImageClip(str(image_file))
                .with_duration(audio.duration)
                .with_audio(audio)
            )

            clips.append(clip)

        if not clips:
            raise Exception("No clips were created.")

        final_video = concatenate_videoclips(
            clips,
            method="compose"
        )

        output = video_folder / "final_video.mp4"

        final_video.write_videofile(
            str(output),
            fps=24
        )

        return output.name