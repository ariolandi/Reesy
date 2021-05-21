def detect_languages(text):
    from langdetect import detect_langs
    return [language.lang for language in detect_langs(text)
            if language.prob > 0.9]


def is_english_text(text):
    return 'en' in detect_languages(text)
