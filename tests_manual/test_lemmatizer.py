from normalization.entity_lemmatizer import (
    EntityLemmatizer
)

lemmatizer = EntityLemmatizer()

words = [

    "யாழ்ப்பாணத்தில்",

    "யாழ்ப்பாணத்திற்கு",

    "யாழ்ப்பாணத்தின்",

    "தமிழர்களின்",

    "மாணவர்களுக்கு"

]

for word in words:

    lemma = (
        lemmatizer.lemmatize(word)
    )

    print()

    print("Input :", word)

    print("Lemma :", lemma)