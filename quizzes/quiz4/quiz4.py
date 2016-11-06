#!/usr/bin/env python3

import pickle
import matplotlib.pyplot as plt

with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

plt.subplot(221)
plt.plot(data['stim'], data['neuron1'].sum(0))
plt.subplot(222)
plt.plot(data['stim'], data['neuron2'].sum(0))
plt.subplot(223)
plt.plot(data['stim'], data['neuron3'].sum(0))
plt.subplot(224)
plt.plot(data['stim'], data['neuron4'].sum(0))

plt.show()
