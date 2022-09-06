import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()


apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    if englishText != "":
        french_text = language_translator.translate(text=englishText,model_id='en-fr').get_result()
        # print(json.dumps(frenchText, indent=2, ensure_ascii=False))
        translation_text = french_text["translations"][0]["translation"]
        return translation_text
    error_message = "Please enter english text"
    return error_message

def frenchToEnglish(frenchText):
    if frenchText != "":
        english_text = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
        # print(json.dumps(englishText, indent=2, ensure_ascii=False))
        translation_text = english_text["translations"][0]["translation"]
        return translation_text
    error_message = "Please enter french text"
    return error_message