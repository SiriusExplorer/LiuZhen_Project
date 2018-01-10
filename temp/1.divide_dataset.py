# The codes only divide the 'deeploc_dataset' file without blank lines. The file will be divided into training set and testing set
# Each sequence in the file should be kept in one line
import os
file = open('./sieved_dataset/sieved_deeploc_pseaac', 'r')
file_lines = file.readlines()
list_train = []
list_test = []
for i in [evens for evens in range(len(file_lines)) if evens%2 == 0]:
    if i + 1 >= len(file_lines):
        break
    if file_lines[i].find('test') >= 0:
        list_test = list_test + [file_lines[i], file_lines[i+1]]
    else:
        list_train = list_train + [file_lines[i], file_lines[i+1]]
file_train = open('./sieved_dataset/trainset/sieved_deeploc_trainset_pseaac', 'w+')
file_test = open('./sieved_dataset/testset/sieved_deeploc_testset_pseaac', 'w+')
file_train.writelines(list_train)
file_test.writelines(list_test)
file.close()
file_train.close()
file_test.close()