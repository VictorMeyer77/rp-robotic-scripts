
"""

system library: sudo apt-get install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev flac vlc

"""

import speech_recognition as sr
import gtts
import subprocess

PATH = "resources/output/audio/micro/audio_buffer.wav"
RECORD_COMMAND = "arecord -f cd -d 3 {}"
PLAY_SOUND_COMMAND = "cvlc --play-and-exit {}"


def run_ear(output_path):
    process = subprocess.Popen(RECORD_COMMAND.format(output_path), shell=True)
    process.communicate()


def recognize_input(path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="fr")
        return text


def say_answer(answer, path, language="fr"):
    tts = gtts.gTTS(answer, lang=language)
    tts.save(path)
    process = subprocess.Popen(PLAY_SOUND_COMMAND.format(path), shell=True)
    process.communicate()


if __name__ == "__main__":
    run_ear(PATH)
    words = recognize_input(PATH)
    say_answer(f"Votre réponse est: {words}", PATH)
