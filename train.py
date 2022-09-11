import numpy as np
import re

def fit():
    name_file = str(input('enter a name of training file: '))

    text = ''
    with open(name_file, encoding='UTF-8') as file:
        text = str(file.read())
    text = text.lower()
    text = text.strip()
    text = re.split("[^a-zа-яё]+", text)

    dictionary = {}
    for i in range(len(text) - 1):
        if dictionary.get(text[i], 0):
            values = dictionary.get(text[i])
            values.append(text[i + 1])
            dictionary[text[i]] = values
        else:
            dictionary[text[i]] = [text[i + 1]]

    name_model = str(input('enter a name to save the model: '))
    np.save('{}.npy'.format(name_model), dictionary)
