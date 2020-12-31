import numpy as np

def calc_stats(fname):
    data = np.loadtxt(fname,delimiter = ',')
    return (np.round(np.mean(data),1), np.round(np.median(data),1))

print(calc_stats("data.csv"))
