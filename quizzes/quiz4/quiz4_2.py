#!/usr/bin/env python3

import pickle
import matplotlib.pyplot as plt
import numpy as np

with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

with open('pop_coding_3.4.pickle', 'rb') as f:
    data2 = pickle.load(f)

v_pop = np.array([0., 0.])
for i in range(1,5):
    r_max = data['neuron' + str(i)].sum(0).max()
    r = data2['r' + str(i)].mean()
    v = r / r_max * data2['c' + str(i)]
    v_pop += v

print(v_pop)
