from transformers import pipeline


class RelationModel:

    def __init__(self):

        self.classifier = pipeline(
            task="zero-shot-classification",
            model="MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7"
        )

    def predict(
        self,
        text,
        candidate_labels
    ):
        return self.classifier(
            text,
            candidate_labels
        )


_MODEL = None


def get_relation_model():

    global _MODEL

    if _MODEL is None:
        _MODEL = RelationModel()

    return _MODEL