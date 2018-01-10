import numpy as np

N_list = [x + 1 for x in range(10)]
LAM_list = [int(40/x)-1 for x in N_list]
for N, LAM in zip(N_list, LAM_list):
    train_np = np.load('./sieved_dataset_acc_pssm/trainset/left_pssm/n{0}/vector_np_lam{1}.npy'.format(N, LAM))
    test_np = np.load('./sieved_dataset_acc_pssm/testset/left_pssm/n{0}/vector_np_lam{1}.npy'.format(N, LAM))
    newset = np.concatenate((train_np, test_np))
    np.save('./sieved_dataset_acc_pssm/10folds_cross_val/left_pssm/vector_np_n{0}_lam{1}.npy'.format(N, LAM), newset)
    print(np.shape(newset))
# trainlabel_np = np.load('./sieved_dataset_acc_pssm/trainset/label_digit_nucleus01_np.npy')
# testlabel_np = np.load('./sieved_dataset_acc_pssm/testset/label_digit_nucleus01_np.npy')
# newlabel = np.concatenate((trainlabel_np, testlabel_np))
# np.save('./sieved_dataset_acc_pssm/10folds_cross_val/label_digit_nucleus01_np.npy', newlabel)
# print(np.shape(newlabel))