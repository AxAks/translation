from gtts import gTTS
from playsound import playsound

from constants import PROMPT_TEXTS, VOCALS_PATH
from libs import voice_analyzer as va


class TranslationProcessor:
    def __init__(self):
        self.voice_analyzer = va.VoiceAnalyzer()

    def analyze(self, audio, recognizer):
        vocal_prompt_listening = gTTS(text=PROMPT_TEXTS['recognizing'], slow=False)
        vocal_prompt_listening.save(f"{VOCALS_PATH}/vocal_prompt_recognizing.mp3")
        playsound(f"{VOCALS_PATH}/vocal_prompt_recognizing.mp3")
        query = recognizer.recognize_google(audio)
        return query

