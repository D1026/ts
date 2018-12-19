import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from pandas.core.series import

with open('vm_cpu.pkl', mode='rb') as f:
    data = pickle.load(f)
for k in data.keys():
    print(data[k]['COLL_TIME'][0], type(data[k]['COLL_TIME'][0]))
    print(data[k]['KPI_VALUE'][0], type(data[k]['KPI_VALUE'][0]))
    idx = pd.DatetimeIndex(data[k]['COLL_TIME'])
    print(idx)
    ts = pd.Series(np.array(data[k]['KPI_VALUE']), index=idx)
    ts.plot(kind='line', figsize=(32, 10))
    plt.show()
    plt.savefig('123.png')
    print(type(ts))

    exit(888)