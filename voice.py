import asyncio
import io
import logging
import sounddevice as sd
import edge_tts
import soundfile as sf

voice = "en-GB-SoniaNeural"
Logger = logging.getLogger(__name__)

async def say(message, **opt):
    mp3 = b''
    tts = edge_tts.Communicate(
        message,
        voice=voice,
        rate=opt.get('rate', '+0%'),
        volume=opt.get('volume', '+0%'),
    )
    try:
        async for chunk in tts.stream():
            if chunk["type"] == "audio":
                mp3 += chunk["data"]
            else:
                Logger.debug('%s: audio.metadata: %s', chunk)
    except edge_tts.exceptions.NoAudioReceived:
        Logger.warning('%s: failed: %s'[message, opt])
        return None
    return mp3



async def play_without_saving(message):
    bytes = await say(message)
    if bytes:
        with io.BytesIO(bytes) as audio_file:
            audio_data, samplerate = sf.read(audio_file, dtype='int16')
            print(message)
            sd.play(audio_data, samplerate, blocking=True)


# Test the function
async def main():
    await play_without_saving("Hello, how are you today?")

if __name__ == "__main__":
    asyncio.run(main())
