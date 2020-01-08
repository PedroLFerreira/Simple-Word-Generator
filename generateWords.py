import sys
import numpy as np

# print("This is the name of the script: ", sys.argv[0])
# print("Number of arguments: ", len(sys.argv))
# print("The arguments are: " , str(sys.argv))

filename = str(sys.argv[1])
min_word_size = int(sys.argv[2])
max_word_size = int(sys.argv[3])
word_count = int(sys.argv[4])


def extract_ngrams(filename):
    file = open(filename,"r")

    words = [line.lower().strip() for line in file]
    chars = ["<START>","<STOP>"]

    for word in words:
        for char in word:
            if char not in chars:
                chars.append(char)

    unigrams = np.zeros(len(chars))
    bigrams = np.zeros((len(chars),len(chars)))

    for word in words:
        unigrams[chars.index("<START>")] += 1
        unigrams[chars.index("<STOP>")] += 1
        for char in word:
            unigrams[chars.index(char)] += 1

    unigrams /= np.sum(unigrams)




    for word in words:
        current_char = "<START>"

        for next_char in word:
            bigrams[chars.index(current_char),chars.index(next_char)] += 1
            current_char = next_char

        bigrams[chars.index(current_char),chars.index("<STOP>")] += 1

    for i in range(len(chars)):
        if i == 1:
            continue
        bigrams[i] /= np.sum(bigrams[i])
    
    return chars,bigrams


def generate_word(chars, bigrams, min_length = 2, max_length=10):

    generated_chars = [np.random.choice(chars,p=bigrams[chars.index("<START>")])]

    for i in range(max_length):
        probs = bigrams[chars.index(generated_chars[-1])]
        new_char = np.random.choice(chars,p=probs)

        if new_char == "<STOP>":
            if len(generated_chars) >= min_length:
                generated_chars.append(new_char)
                break
            else:
                tries = 0
                while new_char == "<STOP>":
                    new_char = np.random.choice(chars,p=probs)
                    tries += 1
                    if tries > 100:
                        print("TOO MANY TRIES")
                        return ""

        generated_chars.append(new_char)

        
        if i == max_length - 1:
            generated_chars.append("<STOP>")

    return "".join(generated_chars[:-1]).capitalize()


chars, bigrams = extract_ngrams(filename)

for _ in range(word_count):
    print(generate_word(chars, bigrams, min_word_size, max_word_size))
