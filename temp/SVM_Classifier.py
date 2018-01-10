import numpy as np
from sklearn.svm import SVC

vector = np.load('./sieved_dataset_acc_pssm/trainset/right_pssm/n1/vector_np_lam39.npy')
label = np.load('./sieved_dataset_acc_pssm/trainset/label_digit_nucleus01_np.npy')
clf = SVC()
clf.fit(vector, label)
test_vector = np.load('./sieved_dataset_acc_pssm/testset/right_pssm/n1/vector_np_lam39.npy')
predict_label = clf.predict(test_vector)
test_label = np.load('./sieved_dataset_acc_pssm/testset/label_digit_nucleus01_np.npy')
accuracy = np.sum(predict_label == test_label) / len(test_label)

print(predict_label)
print(accuracy)