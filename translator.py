from deep_translator import GoogleTranslator

def get_languages():
    return GoogleTranslator().get_supported_languages(as_dict=True)

def translate_text(text, source, target):
    return GoogleTranslator(
        source=source,
        target=target
    ).translate(text)