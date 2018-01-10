# The codes are used to sieve dataset again because some proteins are not included in the pssm_deeploc directory.

import os
import re

def sieve_acc_pssm(filename, savedname):
    protein_list = os.listdir('./pssm_deeploc')
    new_file = open(savedname, 'w+')
    new_file_lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in [x for x in range(len(lines)) if x % 2 == 0]:
            protein_number = re.split('>| ', lines[i])[1]
            if '{0}.pssm'.format(protein_number) in protein_list:
                new_file_lines.append(lines[i])
                new_file_lines.append(lines[i + 1])
    new_file.writelines(new_file_lines)
    new_file.close()

sieve_acc_pssm('./sieved_dataset/sieved_deeploc_pseaac', './sieved_dataset_acc_pssm/pseAAC')