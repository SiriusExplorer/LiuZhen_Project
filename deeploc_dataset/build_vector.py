# This file creates the input vectors from DeepLoc dataset (Include AAcomposition, pseudoAAcomposition, PSSM profile)

import re
import numpy as np


def parse_pssm_to_vector(pssm_filename):
    vector = np.array([])
    flag = re.compile(' +\d+ [A-Z]')
    with open(pssm_filename, 'r') as file:
        for line in file:
            if flag.match(line):
                vector = np.append(vector, [float(x)/100 for x in line.split()[22:42]])
    return vector

def read_aacline(aacline):
    aacline_list = re.split(' |:', aacline)
    vector = []
    for i in [x for x in range(len(aacline_list)) if x % 2 != 0]:
        vector.append(float(aacline_list[i]))
    return np.array(vector)

def read_pseaacline(pseaacline):
    pseaacline_list = re.split(' |:', pseaacline)
    vector = []
    for i in [x for x in range(len(pseaacline_list)) if x % 2 != 0]:
        vector.append(float(pseaacline_list[i]))
    return np.array(vector)

def parse_aac_to_vector(aac_filename, protein_number = None, protein_order_num = None, protein_line_index = None):
    with open(aac_filename, 'r') as file:
        lines = file.readlines()
        if protein_number is not None:
            for i in [x for x in range(len(lines)) if x % 2 == 0]:
                if protein_number in lines[i]:
                    return read_aacline(lines[i+1])
        if protein_order_num is not None:
            return read_aacline(lines[protein_order_num*2+1]) # protein_order_num should begin with 0
        if protein_line_index is not None:
            return read_aacline(lines[protein_line_index+1])

def parse_pseaac_to_vector(pseaac_filename, protein_number = None, protein_order_num = None, protein_line_index = None):
    with open(pseaac_filename, 'r') as file:
        lines = file.readlines()
        if protein_number is not None:
            for i in [x for x in range(len(lines)) if x % 2 == 0]:
                if protein_number in lines[i]:
                    return read_pseaacline(lines[i+1])
        if protein_order_num is not None:
            return read_pseaacline(lines[protein_order_num*2+1]) # protein_order_num should begin with 0
        if protein_line_index is not None:
            return read_pseaacline(lines[protein_line_index+1])

with open('./sieved_dataset_acc_pssm/trainset/trainset', 'r') as file:
    lines = file.readlines()
    protein_number_np = np.array([])
    label_np = np.array([])
    # vector_np = np.array([[]]) # I want to create a 2D matrix contains all the vector. Each vector for one protein is one line in the vector_np
    for i in [x for x in range(len(lines)) if x % 2 == 0]:
        if i > 1:
            break # Just use the first protein as a try
        protein_number = re.split('>| ', lines[i])[1]
        protein_number_np = np.append(protein_number_np, protein_number)
        label_np = np.append(label_np, lines[i].split()[1])
        vector = np.concatenate((parse_pssm_to_vector('./pssm_deeploc/{0}.pssm'.format(protein_number)), parse_aac_to_vector('./sieved_dataset_acc_pssm/trainset/trainset_AAC', protein_line_index = i), parse_pseaac_to_vector('./sieved_dataset_acc_pssm/trainset/trainset_pseAAC', protein_line_index = i)))
    #    vector_np = np.concatenate((vector_np, vector)) If I run this command, there be an error: ValueError: all the input arrays must have same number of dimensions

print(protein_number_np)
print(label_np)
print(vector, np.shape(vector))