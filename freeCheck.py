import pandas as pd
import numpy as np

# df = pd.DataFrame(np.arange(14).reshape([7, 2]), index=[11, 12, 13, 14, 15, 16, 17], columns=['A', 'B'])
# df1 = pd.DataFrame(df[df['B']<0])
# print(df)
#
# # print(df1['B'].index[1])
# print(('A' in df))
# print((17 in df['A']))  # X in DataFrame: return x in dataframe.column,    X in Series: return x in series.index

# -----------------------------------------------
# rng = pd.date_range('1/1/2011', periods=72, freq='H')
# ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print(type(ts.index))
# converted = ts.asfreq('45Min', method='pad')
# print(converted.head())

# ------------------------------------------------
se = pd.Series(np.arange(10), index=[1, 2, 3, 4, 4, 5, 6, 7, 8, 9])
print(len(se))
print(se[4])    # index值重复， series[index] 返回类型为 Series, 否则返回单元素，类型同dtype
print(len(se[4]))
print(pd.Series)