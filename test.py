import pickle
with open('vm_cputs_cleaned.pkl', mode='rb') as f:
    all = pickle.load(f)
for k in all.keys():
    ts = all[k].values
    for i in range(len(ts)-1):
        if (ts[i+1]-ts[i])/ts[i] > 3.0:
            print(ts[i-2:i+2])
    exit(666)
