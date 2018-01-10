import numpy as np
from sklearn.neural_network import MLPClassifier

vector = np.load('./sieved_dataset_acc_pssm/trainset/vector_np_lam12.npy')
label = np.load('./sieved_dataset_acc_pssm/trainset/label_digit_012_np.npy')
clf = MLPClassifier()
clf.fit(vector, label)
test_vector = np.load('./sieved_dataset_acc_pssm/testset/vector_np_lam12.npy')
predict_label = clf.predict(test_vector)
test_label = np.load('./sieved_dataset_acc_pssm/testset/label_digit_012_np.npy')
accuracy = np.sum(predict_label == test_label) / len(test_label)

print(predict_label)
print(accuracy)