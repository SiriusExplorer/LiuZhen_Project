# The codes calculate the min, max and average length of the protein sequences from the input file
# Each sequence in the file should be kept in one line
# No blank line in the file
file = open('./sieved_dataset_acc_pssm/trainset/trainset_remove_CN', 'r')
file_lines = file.readlines()
seq_len = []
for i in [odds for odds in range(len(file_lines)) if odds%2 != 0]:
    seq_len.append(len(file_lines[i]) - 1)
print('The minimum of the protein sequences length is:', min(seq_len))
print('The maximum of the protein sequences length is:', max(seq_len))
print('The average of the protein sequences length is: %.2f' % (sum(seq_len)/len(seq_len)))
file.close()