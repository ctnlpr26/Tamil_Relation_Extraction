# pipeline/extraction_pipeline.py

from pipeline.sentence_splitter import SentenceSplitter
from pipeline.ner_stage import NERStage
from pipeline.pair_generator import PairGenerator
from pipeline.entity_marker import EntityMarker
from pipeline.relation_stage import RelationStage
from pipeline.triple_builder import TripleBuilder


class ExtractionPipeline:

    def __init__(self):

        self.splitter = SentenceSplitter()
        self.ner = NERStage()
        self.pair_generator = PairGenerator()
        self.marker = EntityMarker()
        self.relation_stage = RelationStage()
        self.triple_builder = TripleBuilder()

    def run(self, document):

        triples = []

        sentences = self.splitter.split(document)

        print("Sentences:", sentences)

        for sentence in sentences:

            entities = self.ner.extract(sentence)
            entities = [
                e for e in entities
                if len(e.text.strip()) > 2
            ]   

            print("\nSentence:", sentence)
            print("Entities:", entities)

            pairs = self.pair_generator.generate(
                entities
            )

            print("Pairs:", pairs)

            for pair in pairs:

                marked_sentence = self.marker.mark(
                    sentence,
                    pair.entity1,
                    pair.entity2
                )

                print("Marked:", marked_sentence)

                # relation = self.relation_stage.predict(
                #     marked_sentence
                # )
                # relation = self.relation_stage.predict(
                #     sentence=marked_sentence,
                #     entity1=pair.entity1,
                #     entity2=pair.entity2
                # )   

                relation = self.relation_stage.predict(

                    sentence=marked_sentence,

                    entity1=pair.entity1,

                    entity2=pair.entity2

                )

                print("Relation:", relation)

                triple = self.triple_builder.build(
                    pair,
                    relation
                )

                print("Triple:", triple)

                triples.append(triple)

        return triples