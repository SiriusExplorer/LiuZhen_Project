# Calculate the amino acid composition of input FASTA format file
# Each sequence in the file should be kept in one line
# No blank line in the file

def aacfun(seq): # Calculate the frequency of 20 kinds of amino acids in the input sequence.
    aac_result = []
    for each in 'ACDEFGHIKLMNPQRSTVWY':
        aac_result.append('{0}:{1}'.format(each, seq.count(each)/len(seq)))
    #    aac_result.append(repr(seq.count(each)/len(seq))) #if you want to return a list rather a string, use this line instead the line above
        str = ' '
    return str.join(aac_result)+'\n'

file = open('sieved_dataset_acc_pssm/testset/testset_remove_CN', 'r')
file_AAC = open('sieved_dataset_acc_pssm/testset/testset_AAC', 'w+')
file_lines = file.readlines()
AAC_lines = []
for i in range(len(file_lines)):
    if i%2 == 0:
        AAC_lines.append(file_lines[i])
    else:
        AAC_lines.append(aacfun(file_lines[i]))
file_AAC.writelines(AAC_lines)
file.close()
file_AAC.close()
