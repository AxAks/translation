from constants import LANGUAGES, PROMPT_TEXTS

from libs import audio_renderer as ar
from libs import voice_analyzer as va

flag = 0


def main():
    voice_analyzer = va.VoiceAnalyzer()
    audio_renderer = ar.AudioRenderer()

    translation_request = voice_analyzer.take_command(prompt_text=PROMPT_TEXTS['listening'],
                                                      action='submit_phrase')
    while not translation_request:
        translation_request = voice_analyzer.take_command(prompt_text=PROMPT_TEXTS['repeat'],
                                                          action='submit_phrase')
    print(translation_request)
    translate_to = voice_analyzer.take_command(prompt_text=PROMPT_TEXTS['which_language'],
                                               action='set_language')
    print(translate_to)
    while translate_to not in LANGUAGES:
        audio_renderer.language_not_found()
        translate_to = voice_analyzer.take_command(prompt_text=PROMPT_TEXTS['repeat'],
                                                   action='set_language')
    audio_renderer.give_result(translation_request=translation_request,
                               translate_to=LANGUAGES[translate_to])


if __name__ == "__main__":
    main()
