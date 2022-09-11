import numpy as np

def gen():
    name_model = str(input('enter a name of model: '))
    dictionary = np.load('{}.npy'.format(name_model), allow_pickle=True).item()

    len_text = int(input('enter a length of text: '))
    last_word = np.random.choice(list(dictionary.keys()))
    text = last_word + ' '
    for i in range(1, len_text):
        current_word = np.random.choice(dictionary.setdefault(last_word, list(dictionary.keys())))
        text += current_word + ' '
        last_word = current_word

    return text


