# # normalization/normalization_pipeline.py

# from normalization.entity_normalizer import (
#     EntityNormalizer
# )

# from normalization.entity_lemmatizer import (
#     EntityLemmatizer
# )


# class NormalizationPipeline:

#     def __init__(self):

#         self.normalizer = (
#             EntityNormalizer()
#         )

#         self.lemmatizer = (
#             EntityLemmatizer()
#         )

#     def process(
#         self,
#         entity
#     ):

#         normalized = (
#             self.normalizer.normalize(
#                 entity.text
#             )
#         )

#         lemma = (
#             self.lemmatizer.lemmatize(
#                 normalized
#             )
#         )

#         entity.original_text = entity.text

#         entity.text = lemma

#         entity.lemma = lemma

#         return entity


from normalization.entity_normalizer import (
    EntityNormalizer
)

from normalization.entity_lemmatizer import (
    EntityLemmatizer
)

from normalization.entity_lemmatizer import (
    get_lemmatizer
)

class NormalizationPipeline:

    def __init__(self):

        self.normalizer = EntityNormalizer()

        # self.lemmatizer = EntityLemmatizer()
        self.lemmatizer = get_lemmatizer()

    def process_text(
        self,
        text
    ):

        text = self.normalizer.normalize(
            text
        )

        text = self.lemmatizer.lemmatize(
            text
        )

        return text