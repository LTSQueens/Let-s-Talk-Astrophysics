import numpy as np
def GetRotCurve():

    with open('COdata.txt','r') as f:
        raw_data = f.readlines()

    R = []
    deltaR = []
    V = []
    deltaV = []

    header = raw_data[0].split(',')

    for line in raw_data[1:]:
        vals = list(float(x) for x in line.split(' '))
        R.append(vals[0])
        deltaR.append(vals[1])
        V.append(vals[2])
        deltaV.append(vals[3])

    return np.array(R, dtype=float), np.array(deltaR, dtype=float), np.array(V, dtype=float), np.array(deltaV, dtype=float)

