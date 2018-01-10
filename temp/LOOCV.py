from time import clock as now
import numpy as np
from sklearn.model_selection import LeaveOneOut

dataset_np = np.load('./sieved_dataset_acc_pssm/10folds_cross_val/right_pssm/vector_np_n1_lam39.npy')
label_np = np.load('./sieved_dataset_acc_pssm/10folds_cross_val/label_digit_nucleus01_np.npy')
loo = LeaveOneOut()
