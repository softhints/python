import os

size = 80
file = 'budo'
folder = os.path.expanduser('~/Documents/Fortunes/')

# Read and store the entire file line by line
with open(f'{folder}{file}.txt') as reader:
    provers = reader.readlines()

# wrap/collate lines by separators [",", " ", "."]
def collate(text, size):
    new_text = []
    split_char = 1
    while split_char > 0:
        comma = str.find(text, ',', size)
        space = str.find(text, ' ', size)
        dot = str.find(text, '.', size)

        split_char = min(max(comma, dot), max(comma, space), max(dot, space))

        if text[:split_char]:
            new_text.append(text[:split_char])
        text = text[split_char+1:].replace('\n', "")

    return new_text

# write collated information to new(same) file
with open(f'{folder}{file}.txt', 'w') as writer:
    for wisdom in provers:
        if len(wisdom) > size:
            collated = collate(wisdom, size)
            for short in collated:
                writer.write(short)
                writer.write('\n')
        else:
            writer.write(wisdom)

# Executing Shell Commands with Python
import os
myCmd = f'strfile -c % {folder}{file}.txt {folder}{file}.txt.dat'
os.system(myCmd)