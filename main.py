import train
import generate

train.fit()
with open('generation_text', 'w') as file:
    file.write(generate.gen())


