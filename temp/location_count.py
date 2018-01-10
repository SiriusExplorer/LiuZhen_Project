# The codes count the number of proteins at each location in the input file.
# Each sequence in the file should be kept in one line
# No blank line in the file
file = open('./sieved_dataset_acc_pssm/testset/testset_remove_CN', 'r')
file_lines = file.readlines()
locations_list = []
for i in [evens for evens in range(len(file_lines)) if evens%2 == 0]:
    for eachword in file_lines[i].split():
        if eachword[0] != '>' and eachword.find('test') < 0:
            locations_list = locations_list + [eachword]
locations_kinds = sorted(list(set(locations_list))) # Count the kinds of different locations
print('The number of different kinds of locations is:', len(locations_kinds))
for eachlocation in locations_kinds:
    print('The number of proteins located at %s is %d' % (eachlocation, locations_list.count(eachlocation)))