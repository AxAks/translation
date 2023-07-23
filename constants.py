LANGUAGES = {'afrikaans': 'af',
             'albanian': 'sq',
             'amharic': 'am',
             'arabic': 'ar',
             'armenian': 'hy',
             'azerbaijani': 'az',
             'basque': 'eu',
             'belarusian': 'be',
             'bengali': 'bn',
             'bosnian': 'bs',
             'bulgarian': 'bg',
             'catalan': 'ca',
             'cebuano': 'ceb',
             'chichewa': 'ny',
             'chinese': 'zh-cn',
             'corsican': 'co',
             'croatian': 'hr',
             'czech': 'cs',
             'danish': 'da',
             'dutch': 'nl',
             'english': 'en',
             'esperanto': 'eo',
             'estonian': 'et',
             'filipino': 'tl',
             'finnish': 'fi',
             'french': 'fr',
             'frisian': 'fy',
             'galician': 'gl',
             'georgian': 'ka',
             'german': 'de',
             'greek': 'el',
             'gujarati': 'gu',
             'haitian creole': 'ht',
             'hausa': 'ha',
             'hawaiian': 'haw',
             'hebrew': 'he',
             'hindi': 'hi',
             'hmong': 'hmn',
             'hungarian': 'hu',
             'icelandic': 'is',
             'igbo': 'ig',
             'indonesian': 'id',
             'irish': 'ga',
             'italian': 'it',
             'japanese': 'ja',
             'javanese': 'jw',
             'kannada': 'kn',
             'kazakh': 'kk',
             'khmer': 'km',
             'korean': 'ko',
             'kurdish (kurmanji)': 'ku',
             'kyrgyz': 'ky',
             'lao': 'lo',
             'latin': 'la',
             'latvian': 'lv',
             'lithuanian': 'lt',
             'luxembourgish': 'lb',
             'macedonian': 'mk',
             'malagasy': 'mg',
             'malay': 'ms',
             'malayalam': 'ml',
             'maltese': 'mt',
             'maori': 'mi',
             'marathi': 'mr',
             'mongolian': 'mn',
             'myanmar (burmese)': 'my',
             'nepali': 'ne',
             'norwegian': 'no',
             'odia': 'or',
             'pashto': 'ps',
             'persian': 'fa',
             'polish': 'pl',
             'portuguese': 'pt',
             'punjabi': 'pa',
             'romanian': 'ro',
             'russian': 'ru',
             'samoan': 'sm',
             'scots gaelic': 'gd',
             'serbian': 'sr',
             'sesotho': 'st',
             'shona': 'sn',
             'sindhi': 'sd',
             'sinhala': 'si',
             'slovak': 'sk',
             'slovenian': 'sl',
             'somali': 'so',
             'spanish': 'es',
             'sundanese': 'su',
             'swahili': 'sw',
             'swedish': 'sv',
             'tajik': 'tg',
             'tamil': 'ta',
             'telugu': 'te',
             'thai': 'th',
             'turkish': 'tr',
             'ukrainian': 'uk',
             'urdu': 'ur',
             'uyghur': 'ug',
             'uzbek': 'uz',
             'vietnamese': 'vi',
             'welsh': 'cy',
             'xhosa': 'xh',
             'yiddish': 'yi',
             'yoruba': 'yo',
             'zulu': 'zu'
             }

INPUT_TIME_LIMIT = 20

#  orders
ASK_SOURCE_LANGUAGE = 'ask_source_language'
SET_SOURCE_LANGUAGE = 'set_source_language'
ASK_TRANSLATION_REQUEST = 'ask_submit_phrase'
SET_TRANSLATION_REQUEST = 'set_submit_phrase'
ASK_TRANSLATE_TO = 'ask_target_language'
SET_TRANSLATE_TO = 'set_target_language'

#  text prompts
ASK_TRANSLATION_REQUEST_TXT = "Please give me something to translate:"
READY_TXT = "Speak Now, i am listening !"
RECOGNIZING_TXT = "please wait ....."
REPEAT_TXT = "please, say again:"
GIVEN_INPUT_TXT = 'You said: '
ASK_SOURCE_LANGUAGE_TXT = 'Give me the language from which you want to convert:'
ASK_TRANSLATE_TO_TXT = 'Give me the language in which you want to convert:'
LANGUAGE_NOT_FOUND_TXT = "I cannot find the language in which you are trying to convert, " \
                         "please say again or give another language:"

# orders/actions mapping
ORDER_ACTION_DICT = {
    ASK_SOURCE_LANGUAGE: SET_SOURCE_LANGUAGE,
    ASK_TRANSLATION_REQUEST: SET_TRANSLATION_REQUEST,
    ASK_TRANSLATE_TO: SET_TRANSLATE_TO,
}


PROMPT_TEXTS = {
    'ready': READY_TXT,
    ASK_TRANSLATION_REQUEST: ASK_TRANSLATION_REQUEST_TXT,
    'recognizing': RECOGNIZING_TXT,
    'repeat': REPEAT_TXT,
    'given_input': GIVEN_INPUT_TXT,
    ASK_SOURCE_LANGUAGE: ASK_SOURCE_LANGUAGE_TXT,
    ASK_TRANSLATE_TO: ASK_TRANSLATE_TO_TXT,
    'language_not_found': LANGUAGE_NOT_FOUND_TXT
}

VOCALS_PATH = 'vocals'

