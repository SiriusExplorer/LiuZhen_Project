# The script classifies the label into two classes: 0 and 1

import numpy as np

label_array = np.load('./sieved_dataset_acc_pssm/testset/label_np_remove_CN.npy')
label_list = np.ndarray.tolist(label_array)
label_digit_01_list = []
# cat = sorted(list(set(label_array)))
for each in label_list:
    if 'Nucleus' in each:
        if 'Cytoplasm-Nucleus' in each:
            print('protein of Cytoplasm-Nucleus unclear')
        else:
            label_digit_01_list.append(1)
    else:
        label_digit_01_list.append(0)
    label_digit_01_array = np.array(label_digit_01_list)
print(label_digit_01_array)
print(np.shape(label_digit_01_array))
np.save('./sieved_dataset_acc_pssm/testset/label_digit_nucleus01_np.npy', label_digit_01_array)