import numpy as np


def DBE(text):
    remove_char = ".,?/;:!&()"
    for char in remove_char: text.replace(char,"")
    text = text.split()
    unique_words = []
    for i in text: 
        if i not in unique_words: unique_words.append(i)
    num_unique = len(unique_words)
    print(num_unique)
    print(unique_words)
    x = np.log2(np.ceil(np.log2(num_unique)))

    return f"Uncompressed size = {len([j for i in text for j in i])}\nCompressed size = {x*num_unique}"



if __name__ == "__main__":
    print(DBE(
        "What a start to this game. Belief from Morocco that they can take the game to Crotia. This is constant pressure from Morocco"
    ))