import numpy as np
import re

with open('./sieved_dataset_acc_pssm/trainset/trainset', 'r') as file:
    lines = file.readlines()
    matrix = np.load('./sieved_dataset_acc_pssm/trainset/vector_np2.npy')
    n_bool = np.isnan(matrix)
    nan_indexs_matrix = np.where(n_bool == True)[0]
    nan_indexs_list = list(set(nan_indexs_matrix))
    protein_list = []
    for i in nan_indexs_list:
        protein_ID = re.split('>| ', lines[i*2])[1]
        print(protein_ID)
        protein_list.append(protein_ID)
print(len(protein_list))