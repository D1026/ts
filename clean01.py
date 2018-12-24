import pymysql
import pickle
import numpy as np
import pandas as pd

cpu = pd.read_csv('cpu_091011.csv')
cpu['COLL_TIME'] = pd.to_datetime(cpu['COLL_TIME'])
VM_id = cpu['HY_ID'].unique()
print(type(VM_id[0]), len(VM_id), VM_id[0])
print(type(cpu['COLL_TIME'][1]))

data_byVM = {}
for vm in VM_id:
    data_byVM[vm] = pd.DataFrame(cpu[cpu['HY_ID'] == vm])

for vm in VM_id:
    print('VMid:    ')
    print(data_byVM[vm].shape)



with open('vm_cpu.pkl', mode='wb') as f:
    pickle.dump(data_byVM, f)
