import numpy as np

def build_matrixes():
    data = np.arange(12)
    data = data.reshape(3,4)
    return data

def build_stack():
    data = []
    data.append(build_matrixes())
    data.append(build_matrixes())
    data.append(build_matrixes())
    return data

def compute_stack(data):
    nb_stack = len(data)  # 3
    nb_col = len(data[0][0])  # 4
    nb_row = len(data[0])  # 3
    result = []
    for r in range(0,nb_row):
        for c in range(0,nb_col):
            cell = []
            for s in range(0,nb_stack):
                cell.append(data[s][r][c])
            result.append(np.mean(cell))
    return result

stack= build_stack()
print(stack)
print(compute_stack(stack))