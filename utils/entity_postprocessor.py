def normalize_entity_text(text: str) -> str:

    text = text.strip()

    # remove HF subword markers
    text = text.replace("##", "")

    return text


def normalize_entity_label(label: str) -> str:

    mapping = {
        "PER": "PERSON",
        "LOC": "LOCATION",
        "ORG": "ORGANIZATION"
    }

    return mapping.get(label, label)