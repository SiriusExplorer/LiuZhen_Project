import numpy as np

label_array = np.load('./sieved_dataset_acc_pssm/testset/label_np.npy')
label_list = np.ndarray.tolist(label_array)
label_digit_list = []
cat = sorted(list(set(label_array)))
for each in label_list:
    label_digit_list.append(cat.index(each))
    label_digit_array = np.array(label_digit_list)
print(label_digit_array)
print(np.shape(label_digit_array))
np.save('./sieved_dataset_acc_pssm/testset/label_digit_np.npy', label_digit_array)