from constants import PROMPT_TEXTS, ORDER_ACTION_DICT, SET_SOURCE_LANGUAGE, SET_TRANSLATION_REQUEST, SET_TRANSLATE_TO, \
    LANGUAGES

from libs import audio_renderer as ar
from libs import voice_analyzer as va

flag = 0


def main():
    voice_analyzer = va.VoiceAnalyzer()
    audio_renderer = ar.AudioRenderer()
    source_language, translate_to, translation_request = "", "", ""

    for order, action in ORDER_ACTION_DICT.items():
        _input = voice_analyzer.take_command(prompt_text=PROMPT_TEXTS[order], action=action)
        if action == SET_SOURCE_LANGUAGE:
            source_language = LANGUAGES.GET(_input.lower())
        elif action == SET_TRANSLATION_REQUEST:
            translation_request = _input
        elif action == SET_TRANSLATE_TO:
            translate_to = LANGUAGES.GET(_input.lower())
        else:
            raise Exception

        while not _input:
            _input = voice_analyzer.take_command(prompt_text=PROMPT_TEXTS['repeat'], action=action)
            if action == SET_SOURCE_LANGUAGE:
                source_language = LANGUAGES.GET(_input.lower())
            elif action == SET_TRANSLATION_REQUEST:
                translation_request = _input
            elif action == SET_TRANSLATE_TO:
                translate_to = LANGUAGES.GET(_input.lower())
            else:
                raise Exception
    audio_renderer.give_result(source_language=source_language,
                               translation_request=translation_request,
                               translate_to=translate_to)


if __name__ == "__main__":
    main()
