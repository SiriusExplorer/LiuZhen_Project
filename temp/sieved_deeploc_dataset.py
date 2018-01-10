# These codes check the amino acids kinds in each entry of deeploc_dataset. It keep out of the entries which have amino acids out of 'ACDEFGHIKLMNPQRSTVWY', the conventional amino acids.

file = open('deeploc_dataset', 'r')
file_sieved = open('sieved_deeploc_dataset', 'w+')
file_out = open('out_deeploc_dataset', 'w+')
file_lines = file.readlines()
sieved_lines = []
out_lines = []
for i in [odds for odds in range(len(file_lines)) if odds%2 != 0]:
    if set(list(file_lines[i])).issubset(set('ACDEFGHIKLMNPQRSTVWY\n')):
        sieved_lines.extend(file_lines[i - 1] + file_lines[i])
    if not set(list(file_lines[i])).issubset(set('ACDEFGHIKLMNPQRSTVWY\n')):
        out_lines.extend(file_lines[i - 1] + file_lines[i])
file_sieved.writelines(sieved_lines)
file_out.writelines(out_lines)
file.close()
file_sieved.close()
file_out.close()