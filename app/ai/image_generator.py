import requests
from pathlib import Path
from urllib.parse import quote


class ImageGenerator:

    def generate_image(self, prompt, output_path):

        encoded_prompt = quote(prompt)

        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

        response = requests.get(url, timeout=120)

        if response.status_code == 200:

            with open(output_path, "wb") as file:

                file.write(response.content)

            return True

        return False