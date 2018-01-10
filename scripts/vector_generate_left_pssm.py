# This file creates the input vectors from DeepLoc dataset (Include AAcomposition, pseudoAAcomposition, PSSM profile)
# Using the left matrix of pssm file

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from time import clock as now
import re
import os
import numpy as np


def normal(array): # return a list
    if np.sum(array == [0]*20) != 20:
        return np.ndarray.tolist((array - np.average(array))/np.std(array))
    if np.sum(array == [0]*20) == 20:
        return [0.0]*20

def parse_pssm_to_normal_vector(pssm_filename):
    vector = []
    flag = re.compile(' +\d+ [A-Z]')
    with open(pssm_filename, 'r') as file:
        for line in file:
            if flag.match(line):
                vector.append(normal(np.array([float(x)/100 for x in line.split()[2:22]])))
                if len(line.split()[2:22]) != 20:
                    error_pssm.append(protein_ID)
                    print(protein_ID, line.split()[0])
        file.close()
    return np.array(vector)

def psepssm(PSSM_file, n = 3, lam = 1): # The function return a list; The factor n is means the protein will be divided into n parts; factor lam is the maximum of lambda factor in psePSSM, similar with pseAAC
    pssm_normal_matrix = parse_pssm_to_normal_vector(PSSM_file)
    whole_len = np.shape(pssm_normal_matrix)[0] # whole_len denotes the length of the whole protein sequence
    first_sub_len = int(whole_len/n) # The rows of the first n-1 sub fragment
    last_sub_len = (whole_len % n) + first_sub_len
    psepssm_list = []
    for i in range(n - 1):
        sub_pssm_matrix = pssm_normal_matrix[i * first_sub_len:(i + 1) * first_sub_len]
        part1 = np.ndarray.tolist(sub_pssm_matrix.sum(axis=0) / first_sub_len)
        part2 = []
        for e in [ x + 1 for x in range(lam)]:
            part2_e = np.ndarray.tolist(((sub_pssm_matrix[0:-e] - sub_pssm_matrix[e:]) ** 2) .sum(axis=0) / (first_sub_len - e))
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
    return psepssm_list

def read_aacline(aacline):
    aacline_list = re.split(' |:', aacline)
    vector = []
    for i in [x for x in range(len(aacline_list)) if x % 2 != 0]:
        vector.append(float(aacline_list[i]))
    return vector

def read_pseaacline(pseaacline):
    pseaacline_list = re.split(' |:', pseaacline)
    vector = []
    for i in [x for x in range(len(pseaacline_list)) if x % 2 != 0]:
        vector.append(float(pseaacline_list[i]))
    return vector

def parse_aac_to_vector(aac_filename, protein_id = None, protein_order_num = None, protein_line_index = None):
    with open(aac_filename, 'r') as file:
        lines = file.readlines()
        if protein_id is not None:
            for i in [x for x in range(len(lines)) if x % 2 == 0]:
                if protein_id in lines[i]:
                    return read_aacline(lines[i+1])
        if protein_order_num is not None:
            return read_aacline(lines[protein_order_num*2+1]) # protein_order_num should begin with 0
        if protein_line_index is not None:
            return read_aacline(lines[protein_line_index+1])
        file.close()

def parse_pseaac_to_vector(pseaac_filename, protein_id = None, protein_order_num = None, protein_line_index = None):
    with open(pseaac_filename, 'r') as file:
        lines = file.readlines()
        if protein_id is not None:
            for i in [x for x in range(len(lines)) if x % 2 == 0]:
                if protein_id in lines[i]:
                    return read_pseaacline(lines[i+1])
        if protein_order_num is not None:
            return read_pseaacline(lines[protein_order_num*2+1]) # protein_order_num should begin with 0
        if protein_line_index is not None:
            return read_pseaacline(lines[protein_line_index+1])
        file.close()

def label_digitalize(label_list):  # Return a digitalized list of label
    cat = sorted(list(set(label_list)))
    label_digit_list = []
    for each in label_list:
        label_digit_list.append(cat.index(each))
    return label_digit_list

time1 = now()
error_pssm = []
N_list = [x + 1 for x in range(10)]
LAM_list = [int(40/x)-1 for x in N_list]
with open('./sieved_dataset_acc_pssm/trainset/trainset_remove_CN', 'r') as file:
    lines = file.readlines()
    for N, LAM in zip(N_list, LAM_list):
        # label_list = []
        vector_list = []
        for i in [x for x in range(len(lines)) if x % 2 == 0]:
            protein_ID = re.split('>| ', lines[i])[1]
            # label_list.append(lines[i].split()[1])
            vector = psepssm('./pssm_deeploc/{0}.pssm'.format(protein_ID), n = N, lam = LAM) + parse_aac_to_vector('./sieved_dataset_acc_pssm/trainset/trainset_AAC', protein_line_index = i) + parse_pseaac_to_vector('./sieved_dataset_acc_pssm/trainset/trainset_pseAAC_lam40_w0.5', protein_line_index = i)
            # np.save('./sieved_dataset_acc_pssm/testset/left_pssm/vectors_lam12/{0}_lam12.npy'.format(protein_ID), np.array(vector))
            vector_list.append(vector)
        vector_np = np.array(vector_list)
        # label_np = np.array(label_list)
        # label_digit_np = np.array(label_digitalize(label_list))
        np.save('./sieved_dataset_acc_pssm/trainset/left_pssm/n{0}/vector_np_lam{1}.npy'.format(N, LAM), vector_np)
        # np.save('./sieved_dataset_acc_pssm/testset/label_np.npy', label_np)
        # np.save('./sieved_dataset_acc_pssm/testset/label_digit_np.npy', label_digit_np)
time2 = now()
print('time cost:', time2 - time1)
print(error_pssm)

