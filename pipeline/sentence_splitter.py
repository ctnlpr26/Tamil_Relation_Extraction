# pipeline/sentence_splitter.py

import re
from typing import List


class SentenceSplitter:
    """
    Splits a Tamil document into sentences.
    """

    SENTENCE_PATTERN = r'(?<=[.!?।])\s+'

    def split(self, document: str) -> List[str]:
        if not document:
            return []

        sentences = re.split(
            self.SENTENCE_PATTERN,
            document.strip()
        )

        return [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]