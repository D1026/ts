import pandas as pd
import numpy as np
import tensorflow as tf
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
# print(se.values)
# print(se[0:3].values)
# print(type(se[0:3].values))
# 使用切片 series [ x: y]时，x,y 为默认0-(len-1) 的下标，不管指定的index 是自然数还是什么

# --------------------------------------------------------

# a = pd.Series(np.arange(10))
# b = []
# for i in range(len(a)-1):
#     x = a[i:i+1].values
#     y = a[i+1]
#     b.append((x, y))
# print(b)

# b = a[0:3].values
# print(b)
# c.append(b)
# print(c)
# a[1] = 888
# print(c)
# b[1] = 666
# print(a)
# print(c)

# -------------------------
# a = np.array(range(10))
# print(a)
# print(a/10)

# -------------------------
# import tensorflow as tf
# a = tf.constant([1.0, 2.0, 3.0])
# b = tf.constant([0.1, 0.2, 0.3])
# with tf.Session() as sess:
#     print(sess.run(a))
#     print(sess.run((a-b)))

# --------------------
# a = [(1, 2), (3, 4)]
# for (x, y) in a:    # for x, y in a:
#     print(x, y)

# -----------------
# a = [[1, 2, 3],
#      [4, 5, 6]]
# c = [np.array([1, 2, 3]),
#      np.array([4, 5, 6])]
# b = np.array(a)
# d = np.array(c)
# print(b.shape)
# print(d.shape)

# ------------------
a = tf.constant([[1, 2, 3],
                 [4, 5, 6]])
b = tf.constant([[0, 1, 2],
                 [2, 2, 2]])
c = a*b
with tf.Session() as sess:
    print(sess.run(c))
