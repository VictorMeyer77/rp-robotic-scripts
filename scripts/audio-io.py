
"""

system library: sudo apt-get install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev ///gir1.2-gtk-4.0

"""

import speech_recognition as sr
from playsound import playsound
import gtts
import subprocess

PATH = "resources/output/audio/micro/audio_buffer.wav"
RECORD_COMMAND_PATTERN = "arecord --format=cd -d 3 {}"


def run_ear(output_path):
    process = subprocess.Popen(RECORD_COMMAND_PATTERN.format(output_path), shell=True)
    process.communicate()


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
