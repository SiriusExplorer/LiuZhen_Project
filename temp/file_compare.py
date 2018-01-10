import os
import re

file_list = os.listdir('./sieved_dataset_acc_pssm/trainset/vectors2')
with open('./sieved_dataset_acc_pssm/trainset/trainset', 'r') as file:
    lines = file.readlines()
    for i in [x for x in range(len(lines)) if x % 2 == 0]:
        protein = re.split('>| ', lines[i])[1]
        if '{0}.npy'.format(protein) not in file_list:
            print(protein)
            break
file.close()