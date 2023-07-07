from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    '''1'''
    translator = MyMemoryTranslator(source='en-GB', target='fr-CA')
    translation = translator.translate(english_text)
    french_text = translation
    
    return french_text

def french_to_english(french_text):
    '''2'''
    translator = MyMemoryTranslator(source='fr-CA', target='en-GB')
    translation = translator.translate(french_text)
    english_text = translation
    return english_text
