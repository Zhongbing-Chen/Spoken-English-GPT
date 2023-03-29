import asyncio
import io
import openai
import soundfile as sf  # module to handle wav files
import speech_recognition as sr
import whisper
from voice import play_without_saving


async def voice_to_text():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        print(audio)
        # Get the WAV data from the AudioData object
        wav_data = audio.get_wav_data(convert_rate=16000, convert_width=2)

        audio_buffer = io.BytesIO(wav_data)
        audio_data, rate = sf.read(audio_buffer, dtype='float32')  # Read the audio file data from the buffer

    model = whisper.load_model('base')
    transcript = model.transcribe(audio_data)
    return transcript['text']


def text_to_gpt(words):
    print(words)
    openai.api_key = 'Your Key'
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "user", "content": words}
        ]
    )
    answer = completion.choices[0].message["content"]
    return answer


async def main():
    while True:
        input_words = await voice_to_text()
        content_gpt = text_to_gpt(input_words)
        await play_without_saving(content_gpt)


if __name__ == '__main__':
    asyncio.run(main())
