# The script is used to generate a machine learning model based on random forest classifier.

from sklearn.ensemble import RandomForestClassifier
import numpy as np

vector = np.load('./sieved_dataset_acc_pssm/trainset/left_pssm/n5/vector_np_lam7.npy')
label = np.load('./sieved_dataset_acc_pssm/trainset/label_digit_nucleus01_np.npy')
clf = RandomForestClassifier(n_estimators = 100)
clf.fit(vector, label)
test_vector = np.load('./sieved_dataset_acc_pssm/testset/left_pssm/n5/vector_np_lam7.npy')
predict_label = clf.predict(test_vector)
test_label = np.load('./sieved_dataset_acc_pssm/testset/label_digit_nucleus01_np.npy')
accuracy = np.sum(predict_label == test_label) / len(test_label)

print(clf.feature_importances_)
print(accuracy)
