import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import f1_score

N_list = [x + 1 for x in range(10)]
LAM_list = [int(40/x)-1 for x in N_list]

N = 1
LAM = 39
vector_np = np.load('./sieved_dataset_acc_pssm/10folds_cross_val/right_pssm/vector_np_n{0}_lam{1}.npy'.format(N, LAM))
label_np = np.load('./sieved_dataset_acc_pssm/10folds_cross_val/label_digit_nucleus01_np.npy')
skf = StratifiedKFold(n_splits = 10)
accuracy_list = []
mcc_list = []
f1_score_list = []
for train, test in skf.split(vector_np, label_np):
    clf = RandomForestClassifier(n_estimators=50)
    clf.fit(vector_np[train], label_np[train])
    predict_label_np = clf.predict(vector_np[test])
    accuracy_list.append(accuracy_score(label_np[test], predict_label_np))
    mcc_list.append(matthews_corrcoef(label_np[test], predict_label_np))
    f1_score_list.append(f1_score(label_np[test], predict_label_np))
accuracy_average = sum(accuracy_list) / len(accuracy_list)
mcc_average = sum(mcc_list) / len(mcc_list)
f1_score_average = sum(f1_score_list) / len(f1_score_list)
print('The average accuracy of n = {0}, lam = {1}:'.format(N, LAM), accuracy_average)
print('The average mcc of n = {0}, lam = {1}:'.format(N, LAM), mcc_average)
print('The average f1 score of n = {0}, lam = {1}:'.format(N, LAM), f1_score_average)
print(len(f1_score_list))