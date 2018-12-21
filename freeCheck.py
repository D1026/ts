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
# se = pd.Series(np.arange(10), index=[1, 2, 3, 4, 4, 5, 6, 7, 8, 9])
# print(len(se))
# print(se[4])    # index值重复， series[index] 返回类型为 Series, 否则返回单元素，类型同dtype
# print(len(se[4]))
# print(pd.Series)
# print(type(se[1:3]))
# print(se[1:3])

# -----------------------------------------------------
# se = pd.Series(np.arange(10), index=[1, 2, 3, 4, 4, 5, 6, 7, 8, 9])
# print(se.max())
# print(type(se[0:3].values))
# 使用切片 series [ x: y]时，x,y 为默认0-(len-1) 的下标，不管指定的index 是自然数还是什么

# --------------------------------------------------------

a = pd.Series(np.arange(10))
b = []
for i in range(len(a)-1):
    x = a[i:i+1].values
    y = a[i+1]
    b.append((x, y))
print(b)

# b = a[0:3].values
# print(b)
# c.append(b)
# print(c)
# a[1] = 888
# print(c)
# b[1] = 666
# print(a)
# print(c)