import pickle
from sklearn.model_selection import train_test_split

with open('vm_cpuDataNormal.pkl', mode='rb') as f:
    all = pickle.load(f)

for k in all.keys():
    print(k)
    data = all[k]
    xs = []
    ys = []
    for (x, y) in data:
        xs.append(x)
        ys.append(y)

    print(k+'：', len(xs))
    train_x, test_x, train_y, test_y = train_test_split(xs, ys, test_size=0.2, random_state=42)
    with open('data/'+k[-2:], mode='wb') as f:
        pickle.dump((train_x, test_x, train_y, test_y), f)
