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

    def take_command(self, prompt_text, action):
        translation_processor = tp.TranslationProcessor()
        audio_renderer = ar.AudioRenderer()
        save_path = ''
        print(prompt_text)
        if action == 'submit_phrase':
            save_path = f"{VOCALS_PATH}/vocal_prompt_listening.mp3"
        elif action == 'set_language':
            save_path = f"{VOCALS_PATH}/vocal_prompt_which_language.mp3"
        audio_renderer.text_to_audio_converter(text_to_render=prompt_text, save_path=save_path)

        print(PROMPT_TEXTS['ready'])
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, 1)
            self.recognizer.pause_threshold = 1
            self.recognizer.non_speaking_duration = 0.5
            audio = self.recognizer.listen(source)
        try:
            _input = translation_processor.analyze(audio, self.recognizer)
            spoken_input = f"{PROMPT_TEXTS['given_input']}{_input}"
            audio_renderer.render_translation_request(spoken_input)
            print(spoken_input)

        except Exception:
            print(PROMPT_TEXTS['repeat'])
            return None
        return _input

