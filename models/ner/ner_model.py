# # models/ner/ner_model.py

# from transformers import pipeline


# class TamilNERModel:

#     def __init__(self):

#         self.model = pipeline(
#             task="token-classification",
#             model="exentai/SriLankan_Tamil_NER",
#             aggregation_strategy="simple"
#         )

#     def predict(self, text: str):

#         return self.model(text)

from transformers import (
    AutoTokenizer,
    AutoModelForTokenClassification,
    pipeline
)


class TamilNERModel:

    def __init__(self):

        model_name = "exentai/SriLankan_Tamil_NER"

        tokenizer = AutoTokenizer.from_pretrained(
            model_name
        )

        model = AutoModelForTokenClassification.from_pretrained(
            model_name
        )

        self.model = pipeline(
            "token-classification",
            model=model,
            tokenizer=tokenizer,
            aggregation_strategy="simple"
        )

    def predict(self, text):

        return self.model(text)