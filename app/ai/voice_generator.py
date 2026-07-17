import asyncio
import edge_tts


class VoiceGenerator:

    def __init__(self):

        # You can change this voice later
        self.voice = "en-US-AriaNeural"

    async def _generate(self, text, output_file):

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice
        )

        await communicate.save(output_file)

    def generate_voice(self, text, output_file):

        asyncio.run(
            self._generate(
                text,
                output_file
            )
        )

        return output_file