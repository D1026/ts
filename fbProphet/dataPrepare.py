import pickle
import pandas as pd

with open('vm_cpu.pkl', mode='rb') as f:
    dic = pickle.load(f)

data = {}
for k in dic.keys():
    data[k] = pd.DataFrame(dic[k]['COLL_TIME'], dic[k]['KPI_VALUE'])