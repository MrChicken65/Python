def toPirate(text):
    pirate_words = {
        # Greetings
        "hello": "avast",
        "excuse": "arr",

        # Nouns
        "sir": "matey",
        "boy": "matey",
        "man": "matey",
        "madam": "proud beauty",
        "officer": "foul blaggart",

        # Articles
        "the": "th'",
        "my": "me",
        "your": "yer",
        "is": "be",
        "are": "be",
        "am": "be",
        "and": "an'",

        # Places
        "kitchen": "galley",
        "hotel": "fleabag inn"
    }

    words = text.split()
    translation = []

    for word in words:
        if word in pirate_words:
            translated = pirate_words[word]
        else:
            translated = word

        translation.append(translated)

    return " ".join(translation)

normal_text = input("Enter normal text here: ")
print(toPirate(normal_text))