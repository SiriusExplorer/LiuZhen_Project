# This script is used to get the pseAAC vector of input PSSM file

import numpy as np
import re

def normal(list):
    return (list - np.average(list))/np.std(list)

def parse_pssm_to_normal_vector(pssm_filename):
    vector = []
    flag = re.compile(' +\d+ [A-Z]')
    with open(pssm_filename, 'r') as file:
        for line in file:
            if flag.match(line):
                vector.append(normal([float(x)/100 for x in line.split()[2:22]]))
    return np.array(vector)

def psepssm(PSSM_file, n = 3, lam = 8): # The function return a list; The factor n is means the protein will be divided into n parts; factor lam is the maximum of lambda factor in psePSSM, similar with pseAAC
    pssm_normal_matrix = parse_pssm_to_normal_vector(PSSM_file)
    whole_len = np.shape(pssm_normal_matrix)[0] # whole_len denotes the length of the whole protein sequence
    first_sub_len = int(whole_len/n) # The rows of the first n-1 sub fragment
    last_sub_len = (whole_len % n) + first_sub_len
    psepssm_list = []
    for i in range(n - 1):
        sub_pssm_matrix = pssm_normal_matrix[i * first_sub_len:(i + 1) * first_sub_len]
        part1 = np.ndarray.tolist(sub_pssm_matrix.sum(axis = 0) / first_sub_len)
        part2 = []
        for e in [ x + 1 for x in range(lam)]:
            part2_e = np.ndarray.tolist(((sub_pssm_matrix[0:-e] - sub_pssm_matrix[e:]) ** 2).sum(axis = 0) / (first_sub_len - e))
            part2.extend(part2_e)
        sub_psepssm_list = part1 + part2
        psepssm_list.extend(sub_psepssm_list)
    last_sub_pssm_matrix = pssm_normal_matrix[(n-1) * first_sub_len:]
    part1 = np.ndarray.tolist(last_sub_pssm_matrix.sum(axis=0) / last_sub_len)
    part2 = []
    for e in [x + 1 for x in range(lam)]:
        part2_e = np.ndarray.tolist(((last_sub_pssm_matrix[0:-e] - last_sub_pssm_matrix[e:]) ** 2).sum(axis=0) / (last_sub_len - e))
        part2.extend(part2_e)
    sub_psepssm_list = part1 + part2
    psepssm_list.extend(sub_psepssm_list)
    print(last_sub_len)
    return psepssm_list

vector_list = []
protein_ID = 'Q5I0E9'
vector = psepssm('./pssm_deeploc/{0}.pssm'.format(protein_ID), n=3, lam=8)
vector_list.append(vector)
vector_np = np.array(vector_list)

print(vector_np[0, 0:220])