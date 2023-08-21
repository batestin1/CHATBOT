import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import random

class YodaTranslator:
    def __init__(self, nlu_api_key, nlu_url):
        authenticator = IAMAuthenticator(nlu_api_key)
        self.nlu = NaturalLanguageUnderstandingV1(version='2021-09-01', authenticator=authenticator)
        self.nlu.set_service_url(nlu_url)

    def __call__(self, text: str) -> str:
        response = self.nlu.analyze(
            text=text,
            features={"syntax": {"tokens": {"text": True, "part_of_speech": True}}}
        ).get_result()

        objects = []
        subjects = []
        verbs = []
        others = []

        for token in response['syntax']['tokens']:
            text = token['text']
            pos = token['part_of_speech']

            if pos == 'NOUN' or pos == 'PROPN':
                objects.append(text)
            elif pos == 'PRON' or pos == 'NOUN' or pos == 'PROPN':
                subjects.append(text)
            elif pos == 'VERB':
                verbs.append(text)
            else:
                others.append(text)

        reordered_text = ' '.join(objects + subjects + verbs + others)

        return reordered_text

class YodaNLU(YodaTranslator):
    def __init__(self):
        nlu_api_key = 'YourKey'
        nlu_url = 'Your url'
        super().__init__(nlu_api_key, nlu_url)

def main(dict):
    print(dict)
    text = dict['message']
    translate = YodaNLU()
    listend = ["hmmm...", "Yes, hmmm...", "yeap!"]
    text = translate(text)
    text = text.capitalize()
    text = f"{text}, {random.choice(listend)}"
    text = text.replace('"','')

    response_dict = {
        'message': text
    }

    return response_dict
