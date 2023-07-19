from constants import LANGUAGES, PROMPT_TEXTS

from libs import audio_renderer as ar
from libs import voice_analyzer as va

flag = 0


def main():
    voice_analyzer = va.VoiceAnalyzer()
    audio_renderer = ar.AudioRenderer()

    translation_request = voice_analyzer.take_command(prompt_text=PROMPT_TEXTS['listening'])
    while not translation_request:
        translation_request = voice_analyzer.take_command(prompt_text=PROMPT_TEXTS['repeat'])

    translate_to = voice_analyzer.set_destination_language()
    while translate_to not in LANGUAGES:
        translate_to = audio_renderer.language_not_found()

    audio_renderer.give_result(translation_request, translate_to=LANGUAGES[translate_to])


if __name__ == "__main__":
    main()
