# utils/entity_merger.py

def merge_adjacent_entities(entities):

    if not entities:
        return entities

    merged = [entities[0]]

    for current in entities[1:]:

        previous = merged[-1]

        if (
            previous.label == current.label
            and previous.label == "ORGANIZATION"
            and current.start - previous.end <= 2
        ):

            previous.text += current.text
            previous.end = current.end

        else:
            merged.append(current)

    return merged