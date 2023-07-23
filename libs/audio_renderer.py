import os

from googletrans import Translator
from gtts import gTTS
from playsound import playsound
from constants import VOCALS_PATH, PROMPT_TEXTS
from libs import voice_analyzer as va


class AudioRenderer:
    """

    """

    def __init__(self):
        self.voice_analyzer = va.VoiceAnalyzer()

    def text_to_audio_converter(self, text_to_render: str, save_path: str, lang: str = 'en-US', slow=False):
        rendered_audio = gTTS(text=text_to_render, lang=lang, slow=slow)
        rendered_audio.save(save_path)
        playsound(save_path)
        return rendered_audio

    def render_translation_request(self, requested_phrase, source_language=None):
        save_path = f"{VOCALS_PATH}/vocal_prompt_requested_translation.mp3"
        self.text_to_audio_converter(text_to_render=requested_phrase, save_path=save_path, lang=source_language)
        os.remove(save_path)
        return requested_phrase

    def language_not_found(self):
        self.text_to_audio_converter(text_to_render=PROMPT_TEXTS['language_not_found'],
                                     save_path=f"{VOCALS_PATH}/vocal_prompt_language_not_found.mp3")
        print(PROMPT_TEXTS['language_not_found'])
        _input = self.voice_analyzer.take_command(prompt_text=PROMPT_TEXTS['repeat'],
                                                  action='set_language')
        return _input

    def give_result(self, translation_request, source_language, translate_to):
        translator = Translator()
        spoken_text_to_translate = self.render_translation_request(translation_request,
                                                                   source_language=source_language)
        text_to_translate = translator.translate(spoken_text_to_translate, dest=translate_to)
        translation = text_to_translate.text
        save_path = f"{VOCALS_PATH}/captured_voice.mp3"
        self.text_to_audio_converter(text_to_render=f"{translation}", lang=translate_to, save_path=save_path)
        os.remove(save_path)
        print(f"{translation_request} = {translation}")
