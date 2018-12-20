import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from pandas.core.series import

with open('vm_cpu.pkl', mode='rb') as f:
    data = pickle.load(f)

cputs_Dic = {}
print(data.keys())
print(type(data['FusionCompute.m3_urn:sites:43F10830:vms:i-0000002B']['COLL_TIME']))
for k in data.keys():
    print(data[k]['COLL_TIME'][0], type(data[k]['COLL_TIME'][0]))
    print(data[k]['KPI_VALUE'][0], type(data[k]['KPI_VALUE'][0]))
    idx = pd.DatetimeIndex(data[k]['COLL_TIME'])
    # print(idx)
    ts = pd.Series(np.array(data[k]['KPI_VALUE']), index=idx)

    cputs_Dic[k] = ts
    # ---------- plot ----------
    # ts.plot(kind='line', figsize=(32, 10))
    # plt.show()
    # plt.savefig('123.png')
    # print(type(ts))
with open('vm_cputs.pkl', mode='wb') as f:
    pickle.dump(cputs_Dic, f)
exit(888)

for k in data.keys():
    vm_ts = data[k]
    print(vm_ts.index)
    vm_ts = vm_ts.resample('6min')
    if 'NaN' in vm_ts:
        print('存在插值')
    vm_ts = vm_ts.ffill()
    exit(666)