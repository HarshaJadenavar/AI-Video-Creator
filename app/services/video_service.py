from app.ai.video_generator import VideoGenerator


class VideoService:

    def __init__(self):

        self.generator = VideoGenerator()

    def generate(self, project_name):

        print("Generating Final Video...")

        video = self.generator.generate(project_name)

        print("Video Created Successfully!")

        return video