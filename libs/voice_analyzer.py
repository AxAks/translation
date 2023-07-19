from time import sleep

from pyaudio import PyAudio
import speech_recognition as sr

from constants import PROMPT_TEXTS, VOCALS_PATH

from libs import translation_processor as tp
from libs import audio_renderer as ar


class VoiceAnalyzer:
    """

    """
    def __init__(self):
        self.py_audio = PyAudio()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def take_command(self, prompt_text):
        translation_processor = tp.TranslationProcessor()
        audio_renderer = ar.AudioRenderer()

        print(prompt_text)
        save_path = f"{VOCALS_PATH}/vocal_prompt_listening.mp3"
        audio_renderer.text_to_audio_converter(text_to_render=prompt_text, save_path=save_path)

        with self.microphone as source:
            self.recognizer.pause_threshold = 1
            audio = self.recognizer.listen(source)

        try:
            requested_phrase = translation_processor.analyze(audio, self.recognizer)
            spoken_phrase = f"{PROMPT_TEXTS['requested_translation']}{requested_phrase}"
            audio_renderer.render_translation_request(spoken_phrase)
            print(spoken_phrase)

        except Exception:
            print(PROMPT_TEXTS['repeat'])
            return None

        return requested_phrase

    def set_destination_language(self):
        audio_renderer = ar.AudioRenderer()

        print(PROMPT_TEXTS['which_language'])

        save_path = f"{VOCALS_PATH}/vocal_prompt_which_language.mp3"
        vocal_prompt_which_language = audio_renderer.text_to_audio_converter(
            text_to_render=PROMPT_TEXTS['which_language'],
            save_path=save_path)
        vocal_prompt_which_language.save(save_path)

        to_lang = self.take_command(prompt_text=PROMPT_TEXTS['which_language'])
        while not to_lang:
            to_lang = self.take_command(prompt_text=PROMPT_TEXTS['repeat'])
        to_lang = to_lang.lower()
        return to_lang

