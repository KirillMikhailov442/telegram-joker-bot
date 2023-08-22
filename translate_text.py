from translate import Translator


def translate_text(text, language):

    translator = Translator(to_lang=language)
    translater_text = translator.translate(text)

    return translater_text