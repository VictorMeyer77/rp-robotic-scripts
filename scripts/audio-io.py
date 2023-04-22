
"""

system library: sudo apt-get install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-4.0

"""


from pvrecorder import PvRecorder
import speech_recognition as sr
from playsound import playsound
import struct
import wave
import gtts

PATH = "resources/output/audio/micro/audio_buffer.wav"


def save_audio(output_path, audio):
    with wave.open(output_path, "w") as f:
        f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        f.writeframes(struct.pack("h" * len(audio), *audio))


def run_ear(output_path):
    recorder = PvRecorder(device_index=-1, frame_length=512)
    audio = []
    try:
        recorder.start()
        while True:
            frame = recorder.read()
            audio.extend(frame)
    except KeyboardInterrupt:
        recorder.stop()
        save_audio(output_path, audio)
    recorder.delete()


def recognize_input(path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="fr")
        return text


def say_answer_audio(answer, path, language="fr"):
    tts = gtts.gTTS(answer, lang=language)
    tts.save(path)
    playsound(path)


if __name__ == "__main__":
    run_ear(PATH)
    words = recognize_input(PATH)
    say_answer_audio(f"Votre réponse est: {words}", PATH)
