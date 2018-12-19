import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root_8086',
                       db='sit01',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

kpi_id = " 'PM-V-01-010-11' "
tables = " hy_coll_201809, hy_coll_201810, hy_coll_201811 "
try:
    with conn.cursor() as cursor:
        # 查询虚拟机个数
        sql_0 = "SELECT distinct HY_ID FROM hy_coll_201811;"
        cursor.execute(sql_0)
        VM_id = cursor.fetchall()
        print(len(VM_id))  # 29 台
        print(VM_id)

        # sql = "SELECT* FROM hy_coll_201811 WHERE KPI_ID='PM-V-01-010-11' and HY_ID='" + VM_id[0]['HY_ID'] + "'"
        sql = "SELECT* FROM hy_coll_201809 WHERE KPI_ID='PM-V-01-010-11'"
        df_09 = pd.read_sql(sql, conn)
        print(df_09.shape)

        sql = "SELECT* FROM hy_coll_201810 WHERE KPI_ID='PM-V-01-010-11'"
        df_10 = pd.read_sql(sql, conn)
        print(df_10.shape)

        sql = "SELECT* FROM hy_coll_201811 WHERE KPI_ID='PM-V-01-010-11'"
        df_11 = pd.read_sql(sql, conn)
        print(df_11.shape)

        all = df_09.append(df_10.append(df_11))
        #
        # sql = "SELECT* FROM hy_coll_201810 WHERE KPI_ID='PM-V-01-010-11'"
        # df_10 = pd.read_sql(sql, conn)
        # print(df_10.shape)
        #
        # sql = "SELECT* FROM hy_coll_201811 WHERE KPI_ID='PM-V-01-010-11'"
        # df_11 = pd.read_sql(sql, conn)
        # print(df_11.shape)
        #
        # all = df_09.append(df_10.append(df_11))
        # print(all.shape)
        all.to_csv('cpu_091011.csv')

finally:
    conn.close()


# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ts = pd.Series(df_09['KPI_VALUE'].astype(float), index=df_09['COLL_TIME'])
# print(type(ts))
# print(ts.index)
#
#
# ts.plot(x=ts.index, y=ts)
#
# plt.show()




# plt.plot(x, y)
# foo_fig = plt.gcf()    # 'get current figure'
# foo_fig.savefig('foo.eps', format='eps')
# plt.show()
