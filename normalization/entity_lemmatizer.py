# # normalization/entity_lemmatizer.py

# import stanza


# class EntityLemmatizer:

#     def __init__(self):

#         self.nlp = stanza.Pipeline(

#             lang="ta",

#             processors="tokenize,pos,lemma",

#             use_gpu=False,

#             download_method=None
#         )

#     def lemmatize(
#         self,
#         text: str
#     ):

#         doc = self.nlp(text)

#         lemmas = []

#         for sentence in doc.sentences:

#             for word in sentence.words:

#                 lemmas.append(
#                     word.lemma
#                 )

#         return " ".join(lemmas)

import stanza

_LEMMATIZER = None


class EntityLemmatizer:

    def __init__(self):

        self.nlp = stanza.Pipeline(

            lang="ta",

            processors="tokenize,pos,lemma",

            use_gpu=False,

            download_method=None
        )

    def lemmatize(
        self,
        text
    ):

        doc = self.nlp(text)

        lemmas = []

        for sentence in doc.sentences:

            for word in sentence.words:

                lemmas.append(
                    word.lemma
                )

        return " ".join(lemmas)


def get_lemmatizer():

    global _LEMMATIZER

    if _LEMMATIZER is None:

        _LEMMATIZER = EntityLemmatizer()

    return _LEMMATIZER