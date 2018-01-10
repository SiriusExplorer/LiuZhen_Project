file = open('deeploc_dataset', 'r')
file_lines = file.readlines()
all_letter = []
for i in [odds for odds in range(len(file_lines)) if odds%2 != 0]:
    all_letter.extend(list(file_lines[i]))
letter_kinds = sorted(list(set(all_letter)))
print(letter_kinds)
file.close()