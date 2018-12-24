import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from pandas.core.series import

with open('vm_cpu.pkl', mode='rb') as f:
    data = pickle.load(f)

cputs_Dic = {}
print(data.keys())

# print(type(data['FusionCompute.m3_urn:sites:43F10830:vms:i-0000002B']['COLL_TIME']))
# print(data['FusionCompute.m3_urn:sites:43F10830:vms:i-0000002B']['COLL_TIME'])
# print(data['FusionCompute.m3_urn:sites:43F10830:vms:i-0000002B']['COLL_TIME'][7064])
for k in data.keys():
    print(k)
    # print(data[k]['COLL_TIME'][0], type(data[k]['COLL_TIME'][0])) # 指定的index为整数，则自然数索引失效
    # print(data[k]['COLL_TIME'][data[k]['COLL_TIME'].index[0]], type(data[k]['COLL_TIME'][data[k]['COLL_TIME'].index[0]]))
    # print(data[k]['KPI_VALUE'][data[k]['KPI_VALUE'].index[0]], type(data[k]['KPI_VALUE'][data[k]['KPI_VALUE'].index[0]]))
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


# for k in data.keys():
#     vm_ts = data[k]
#     print(vm_ts.index)
#     vm_ts = vm_ts.resample('6min')
#     if 'NaN' in vm_ts:
#         print('存在插值')
#     vm_ts = vm_ts.ffill()
#     exit(666)

for k in cputs_Dic.keys():
    vm_ts = cputs_Dic[k]
    print(len(vm_ts))
    print(len(vm_ts.index.unique()))    # <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
    # for i in vm_ts.index:
    #     if isinstance(vm_ts[i], pd.Series):
    #         print(vm_ts[i])
    vm_ts = vm_ts.drop_duplicates()
    converted = vm_ts.asfreq('6Min', method='pad')
    print(converted)
    # print(vm_ts.isnull())
    cputs_Dic[k] = converted

# ----------- 时间序列清洗完毕，生成训练数据 ------------------
samplesDic = {}
for k in cputs_Dic.keys():
    smps = []
    ts = cputs_Dic[k]
    for i in range(len(ts)-(48*6+6)+1):
        x = ts[i:i+480].values
        x = x/100
        y = ts[i+480:i+490].max()
        y = y/100
        smps.append((x, y))
    samplesDic[k] = smps



with open('vm_cpuDataNormal.pkl', mode='wb') as f:
    pickle.dump(samplesDic, f)
