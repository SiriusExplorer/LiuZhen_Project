# The codes calculate the Pseudo Amino Acid Composition of input file.
# Each sequence in the file should be kept in one line
# No blank line in the file
# If you want to change the input file and the value of weight and lambda, pls change the open file name and the value of wei and lam

import math
import numpy as np

def normal(list):
    return (list - np.average(list))/np.std(list)

def pse_aac(seq):
    theta = []
    for t in range(lam):
        sumcorf = 0
        for i in range(len(seq)):
            if i + t + 1 >= len(seq) or seq[i + t + 1] == '\n':
                break
            ind1 = 'ACDEFGHIKLMNPQRSTVWY'.index(seq[i])
            ind2 = 'ACDEFGHIKLMNPQRSTVWY'.index(seq[i + t + 1])
            corf = (math.pow((H1[ind1] - H1[ind2]), 2) + math.pow((H2[ind1] - H2[ind2]), 2) + math.pow((M[ind1] - M[ind2]), 2))/3
            sumcorf += corf
        theta.append(sumcorf/(len(seq) - (t + 1)))
    return theta

def aac(seq):
    aac_result = []
    for each in 'ACDEFGHIKLMNPQRSTVWY':
        aac_result.append(seq.count(each)/len(seq))
    return aac_result

def nor_pse_aac(seq):
    part_aac = np.ndarray.tolist(np.array(aac(seq)) / (sum(aac(seq)) + wei * sum(pse_aac(seq))))
    part_pse = np.ndarray.tolist(np.array(pse_aac(seq)) * wei / (sum(aac(seq)) + wei * sum(pse_aac(seq))))
    strlist_part_aac = []
    strlist_part_pse = []
    lambd = []
    for (i, j) in zip('ACDEFGHIKLMNPQRSTVWY', part_aac):
        strlist_part_aac.append('{0}:{1}'.format(i, j))
    for i in range(lam):
        lambd.append('lambd{0}'.format(i + 1))
    for (i, j) in zip(lambd, part_pse):
        strlist_part_pse.append('{0}:{1}'.format(i, j))
    str = ' '
    return str.join(strlist_part_aac + strlist_part_pse) + '\n'

H10 = [0.62, 0.29, -0.9, -0.74, 1.19, 0.48, -0.4, 1.38, -1.5, 1.06, 0.64, -0.78, 0.12, -0.85, -2.53, -0.18, -0.05, 1.08, 0.81, 0.26]
H20 = [-0.5, -1, 3, 3, -2.5, 0, -0.5, -1.8, 3, -1.8, -1.3, 0.2, 0, 0.2, 3, 0.3, -0.4, -1.5, -3.4, -2.3]
M0 = [15, 47, 59, 73, 91, 1, 82, 57, 73, 57, 75, 58, 42, 72, 101, 31, 45, 43, 130, 107]
H1 = normal(H10)
H2 = normal(H20)
M = normal(M0)
lam = 40
wei = 0.5
file = open('sieved_dataset_acc_pssm/testset/testset_remove_CN', 'r')
file_pseaac = open('sieved_dataset_acc_pssm/testset/testset_pseAAC_lam40_w0.5', 'w+')
file_lines = file.readlines()
pseaac_lines = []
for i in range(len(file_lines)):
    if i%2 == 0:
        pseaac_lines.append(file_lines[i])
    else:
        pseaac_lines.append(nor_pse_aac(file_lines[i]))
file_pseaac.writelines(pseaac_lines)
file.close()
file_pseaac.close()
