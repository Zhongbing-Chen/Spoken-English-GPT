import asyncio
import sys
import threading

import openai

from record_and_transcribe import transcribe_audio
from audio_player import play_without_saving


def text_to_gpt(words):
    print(words)
    openai.api_key = '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'
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "user", "content": words}
        ]
    )
    answer = completion.choices[0].message["content"]
    return answer


async def main():
    stop_event = threading.Event()
    try:
        print("Activating Wire, prepare to speak please. If you need to stop this program, type in 'stop'")
        while not stop_event.is_set():
            transcribed_text = transcribe_audio(stop_event)

            if transcribed_text is not None:
                gpt_content = text_to_gpt(transcribed_text)
                await play_without_saving(gpt_content)
                print('\033[91m' + 'Recording ' + '\033[0m')
    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')


if __name__ == "__main__":
    asyncio.run(main())
