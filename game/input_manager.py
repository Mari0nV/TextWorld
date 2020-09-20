from autocorrect import Speller
import nltk
import json

from game.internal_mapping import internal_mapping

class InputManager:
    def __init__(self):
        with open("../data/replacements.json") as json_file:
            self.replacements = json.load(json_file)
        
        self.speller = Speller()
        self.internal_mapping = internal_mapping
    
    def _variant_responses(self, response):
        # TODO handle different verbs conjugaisons
        pass

    def _preprocess_response(self, response):
        # check spelling
        response = self.speller(response)

        text = nltk.word_tokenize(response.lower())
        tags = nltk.pos_tag(text)

        return text, tags