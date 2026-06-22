# models/ner/ner_model.py

from transformers import pipeline


class TamilNERModel:

    def __init__(self):

        self.model = pipeline(
            task="token-classification",
            model="exentai/SriLankan_Tamil_NER",
            aggregation_strategy="simple"
        )

    def predict(self, text: str):

        return self.model(text)