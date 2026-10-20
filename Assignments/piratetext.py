
import csv


def toPirate(text, pirate_words):
    words = text.split()
    translation = []

    for word in words:
        if word in pirate_words:
            translated = pirate_words[word]
        else:
            translated = word

        translation.append(translated)

    return " ".join(translation)


# Read dictionary from csv
with open("dict.csv", "r", newline="") as file:
    reader = csv.reader(file)
    keys = next(reader)
    replacements = next(reader)

    pirate_words = dict(zip(keys, replacements))

# Read the input from the txt file
with open("in.txt", "r") as file:
    normal_text = file.read()

# translate it
pirate_text = toPirate(normal_text, pirate_words)

# save it in another txt file, use w to overwrite
with open("out.txt", "w") as file:
    file.write(pirate_text)
