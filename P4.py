#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:26:27 2024

@author: jamesmiller
@packages: numpy, scipy, matplotlib
"""
import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt

# Define the matrix A
A = np.array([[-3, 2], [3, -2]])

# Initial conditions
x0 = np.array([100, 100])

# Time range for the solution
t_values = np.linspace(0, 10, 200)  # From 0 to 10 seconds, 200 points

# Initialize arrays to store solutions
x1_values = []
x2_values = []

# Compute the solution for each time value
for t in t_values:
    eAt = expm(A * t)
    x_t = np.dot(eAt, x0)
    x1_values.append(x_t[0])
    x2_values.append(x_t[1])

# Plotting the solutions
plt.figure(figsize=(10, 6))
plt.plot(t_values, x1_values, label='x1(t) - Processor A', color='blue')
plt.plot(t_values, x2_values, label='x2(t) - Processor B', color='red')
plt.title('Data in Processors A and B Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Amount of Data (Mbytes)')
plt.legend()
plt.grid(True)
plt.show()

