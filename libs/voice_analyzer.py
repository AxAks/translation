from pyaudio import PyAudio

import speech_recognition as sr

from constants import PROMPT_TEXTS, VOCALS_PATH, SET_TRANSLATE_TO, SET_TRANSLATION_REQUEST, SET_SOURCE_LANGUAGE

from libs import translation_processor as tp
from libs import audio_renderer as ar


class VoiceAnalyzer:
    """
    ENTRY POINT FOR VOCAL COMMANDS
    """

    def __init__(self):
        self.py_audio = PyAudio()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def take_command(self, prompt_text, action, source_language='en-US'):
        translation_processor = tp.TranslationProcessor()
        audio_renderer = ar.AudioRenderer()
        save_path = ''
        save_path = self.check_matching_vocal(action, save_path)

        audio_renderer.text_to_audio_converter(text_to_render=prompt_text, save_path=save_path)
        print(PROMPT_TEXTS['ready'])
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, 1)
            self.recognizer.pause_threshold = 1
            audio = self.recognizer.listen(source)

        try:
            _input = translation_processor.analyze(audio, self.recognizer)
            spoken_input = f"{PROMPT_TEXTS['given_input']}{_input}"
            audio_renderer.render_translation_request(spoken_input, source_language=source_language)
            return _input

        except Exception:
            return None

    @staticmethod
    def check_matching_vocal(action, save_path):
        if action == SET_SOURCE_LANGUAGE:
            save_path = f"{VOCALS_PATH}/vocal_prompt_which_source_language.mp3"
        elif action == SET_TRANSLATION_REQUEST:
            save_path = f"{VOCALS_PATH}/vocal_prompt_listening.mp3"
        elif action == SET_TRANSLATE_TO:
            save_path = f"{VOCALS_PATH}/vocal_prompt_which_target_language.mp3"
        return save_path

