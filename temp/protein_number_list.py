# This code generate the list of protein number from the import file

with open('./sieved_dataset/trainset/sieved_deeploc_trainset', 'r') as file:
    lines = file.readlines()
    protein_number = []
    for i in [x for x in range(len(lines)) if x%2 == 0]:
        protein_number.append(lines())