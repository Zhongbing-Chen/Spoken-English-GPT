# README Real-time Voice Assistant with Recording and Text-to-Speech
This is a Python-based real-time voice assistant application that listens to your voice, transcribes the speech using the Whisper ASR model, generates a response using GPT-3.5 Turbo, and plays the response using Microsoft Edge TTS.
### Requirements
- Python 3.7 or later
- Whisper ASR model
- GPT-3.5 Turbo API key
- Microsoft Edge TTS


### Usage
1. Ensure that you have the Whisper ASR model and GPT-3.5 Turbo API key.
2. Set the `MODEL_TYPE` and `LANGUAGE` variables in `record_and_transcribe.py` according to your preferences.
3. Set the `voice` variable in the TTS script to the desired Microsoft Edge TTS voice.
4. Set the GPT-3.5 Turbo API key in the `text_to_gpt` function.


Run the `main()` function in the script to start the application. The program will start listening for your voice input, and when it detects speech, it will transcribe the speech and generate a response using GPT-3.5 Turbo. The response will then be played back using Microsoft Edge TTS.

To stop the application, type `stop` in the terminal and press Enter.
### Example
```
Activating Wire, prepare to speak please. If you need to stop this program, type in 'stop'
Recording
Hello, how are you today?
Recording Done
[Transcription]: Hello, how are you today?
[GPT-3.5 Turbo]: I'm doing well, thank you! How can I help you today?
[Playing Response]
Recording

```
### Files
- `record_and_transcribe.py`: Records and transcribes the user's speech using the Whisper ASR model.
- `audio_player.py`: Plays the generated response using Microsoft Edge TTS.
- `main.py`: Combines the recording, transcription, GPT-3.5 Turbo response, and TTS functions to create a real-time voice assistant.

### Installation
The `requirements.txt` file lists all the necessary Python libraries required for this real-time voice assistant application. Installing these dependencies is crucial for the proper functioning of the application.

To install the dependencies, run the following command in your terminal:

```
pip install -r requirements.txt

```

Below is a brief explanation of each dependency:

1. `sounddevice`: A library that provides audio recording and playback capabilities.
2. `numpy`: A library for numerical operations on arrays and matrices.
3. `webrtcvad`: A library for Voice Activity Detection (VAD) based on the WebRTC project.
4. `soundfile`: A library for reading and writing audio files.
5. `edge_tts`: A library for text-to-speech synthesis using Microsoft Edge TTS.
6. `openai`: A library to interact with the OpenAI API, which includes GPT-3.5 Turbo.
7. `whisper`: A library for using the Whisper ASR model.


Ensure that all these dependencies are installed before running the application to avoid any issues.