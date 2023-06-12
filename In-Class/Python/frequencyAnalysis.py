from collections import Counter



def fa(cipher_text):
    with open(cipher_text,"r") as txt:
        lines = txt.readlines()
        for line in lines:
            line = [letter.upper() for letter in line if letter.isalpha()]
            repeats = Counter(line)
            return repeats






if __name__ == "__main__":
    print(fa(r"In-Class\Python\ciphertxt.txt"))

