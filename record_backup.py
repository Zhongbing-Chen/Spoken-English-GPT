import sounddevice as sd
import numpy as np
import whisper
import sys
import webrtcvad
import threading

# SETTINGS
MODEL_TYPE = "small"
LANGUAGE = "English"
BLOCKSIZE = 480
SAMPLERATE = 16000
SILENCE_LIMIT = 100

vad = webrtcvad.Vad(3)
silent_frames = 0
silence_detected = False

global_ndarray = None
model = whisper.load_model(MODEL_TYPE)

def callback(indata, frames, time, status):
    global global_ndarray, silent_frames

    if global_ndarray is not None:
        global_ndarray = np.concatenate((global_ndarray, indata), dtype='int16')
    else:
        global_ndarray = indata

    is_silence = not vad.is_speech(indata.tobytes(), sample_rate=SAMPLERATE)

    if is_silence:
        silent_frames += 1
    else:
        silent_frames = 0

    if silent_frames >= SILENCE_LIMIT:
        global silence_detected
        silence_detected = True


def check_user_input(stop_event):
    while not stop_event.is_set():
        user_input = input("Type 'stop' to exit: ").strip()
        if user_input.lower() == 'stop':
            stop_event.set()

def main(stop_event):
    global global_ndarray, silent_frames, silence_detected
    print('\nActivating wire ...\n')

    with sd.InputStream(samplerate=SAMPLERATE, channels=1, dtype='int16', blocksize=BLOCKSIZE, callback=callback):

        user_input_thread = threading.Thread(target=check_user_input, args=(stop_event,), daemon=True)
        user_input_thread.start()

        while not stop_event.is_set():

            if silence_detected:
                print('\n \033[91m' + 'Recording Done ' + '\033[0m\n')
                local_ndarray = global_ndarray.copy()
                global_ndarray = None
                indata_transformed = local_ndarray.flatten().astype(np.float32) / 32768.0
                result = model.transcribe(indata_transformed, language=LANGUAGE)
                print(result["text"])
                silent_frames = 0
                silence_detected = False
                print('\033[91m' + 'Recording ' + '\033[0m')


if __name__ == "__main__":
    stop_event = threading.Event()
    try:
        main(stop_event)
    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')



