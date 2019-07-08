from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = [ -0.39,-0.35,-0.81,-0.58,0.819,0.395,0.107,0.331,0.302,0.215,0.818,-0.11,0.105,-0.49,0.330,0.171,-0.97,0.367,0.316,-0.04,-0.35,0.282,0.070,0.476,-0.27,-0.87,-0.85,0.081,0.706,0.008,-0.81,0.849,-0.36,-0.27,-0.46,0.895,-0.81,-0.47,-0.75,-0.36,-0.08,-0.08,0.514,0.818,-0.66,-0.61,0.146,-0.36,-0.76,0.239,-0.38,0.020,0.725,0.805,-0.26,0.249,0.472,0.552,-0.43,-0.76,0.545,-0.29,0.548,-0.27,-0.05,-0.24,-0.95,0.017,-0.81,0.800,-0.51,0.169,-0.24,-0.22,0.032,0.865,0.656,0.552,-0.80,0.809,0.642,-0.69,-0.16,-0.06,-0.56,-0.94,0.046,-0.11,0.131,-0.65,-0.24,0.915,-0.47,-0.87,0.447,0.426,-0.18,0.657,-0.02,-0.04 ]
Y = [ -0.06,0.156,-0.38,-0.15,-0.85,-0.38,-0.07,0.688,-0.32,0.878,-0.52,0.122,0.309,0.721,0.541,-0.06,-0.95,0.376,-0.32,0.893,0.711,-0.39,0.706,-0.79,0.538,-0.28,-0.26,-0.90,0.415,-0.62,0.021,-0.69,0.374,-0.14,0.580,0.710,0.856,-0.06,-0.35,0.652,0.841,0.691,-0.67,0.049,0.589,0.485,0.674,-0.79,-0.55,0.074,0.993,-0.09,-0.57,-0.75,-0.42,-0.04,-0.89,-0.25,-0.02,-0.78,-0.16,0.855,0.581,0.387,-0.87,0.375,-0.15,-0.59,-0.03,0.200,-0.25,0.447,-0.00,0.716,-0.34,0.409,0.456,-0.52,-0.33,-0.53,-0.04,-0.88,-0.12,0.654,-0.31,-0.44,-0.79,0.760,0.953,0.763,0.405,0.715,-0.45,0.488,0.921,0.973,0.019,0.908,0.039,0.382 ]
Z = [ 0.070,-0.78,0.396,-0.17,0.841,-0.15,0.347,0.948,0.640,0.693,-0.36,0.788,-0.59,0.252,0.400,-0.98,-0.06,-0.37,0.301,0.180,0.660,-0.21,-0.90,0.814,0.355,-0.70,-0.66,0.713,-0.60,-0.71,0.997,-0.40,-0.69,-0.48,-0.94,-0.23,0.493,0.592,0.007,0.379,-0.59,-0.29,-0.91,-0.06,-0.48,-0.77,-0.92,0.017,0.661,0.314,0.156,-0.15,0.171,-0.77,0.810,0.295,-0.02,0.171,0.612,-0.31,-0.31,0.590,-0.98,-0.74,-0.16,0.791,0.896,-0.35,0.616,0.832,-0.33,-0.47,-0.89,0.493,0.619,-0.00,0.842,-0.75,0.212,-0.58,0.159,-0.39,0.604,0.320,0.978,0.387,-0.15,0.316,0.977,-0.55,0.390,0.510,-0.60,-0.95,-0.26,0.282,0.490,0.251,0.204,-0.03 ]

ax.scatter(X, Y, Z, marker='o')

# STEP 0
i, j, k = 91, 16, 0
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='orange')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='orange')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='orange')

i, j, k, l = 91, 16, 0, 42
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='orange')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='orange')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='orange')

# STEP 1
i, j, k, l = 91, 16, 0, 30
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 2
i, j, k, l = 91, 16, 42, 4
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 91, 16, 30, 4
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 3
i, j, k, l = 91, 0, 42, 93
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 16, 0, 42, 93
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 91, 0, 30, 93
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 16, 0, 30, 93
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 4
i, j, k, l = 91, 42, 4, 53
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 16, 42, 4, 53
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 91, 42, 93, 53
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 5
i, j, k, l = 91, 30, 4, 88
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 91, 30, 93, 88
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 6
i, j, k, l = 16, 30, 4, 27
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 7
i, j, k, l = 16, 42, 93, 25
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 8
i, j, k, l = 16, 30, 93, 66
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 16, 30, 27, 66
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 9
i, j, k, l = 91, 4, 53, 31
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 10
i, j, k, l = 16, 42, 53, 81
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 16, 42, 25, 81
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 11
i, j, k, l = 16, 4, 53, 56
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 16, 4, 27, 56
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 12
i, j, k, l = 91, 93, 53, 62
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 42, 93, 53, 62
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 91, 93, 88, 62
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 13
i, j, k, l = 91, 4, 88, 69
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 14
i, j, k, l = 30, 4, 88, 84
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 30, 4, 27, 84
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 16, 27, 66, 84
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 30, 27, 66, 84
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 15
i, j, k, l = 30, 93, 88, 36
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 30, 93, 66, 36
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 93, 88, 62, 36
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k = 16, 93, 25
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 42, 93, 25
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 16, 93, 66
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 91, 4, 31
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

# STEP 16
i, j, k, l = 91, 53, 31, 35
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 91, 53, 62, 35
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 91, 88, 62, 35
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k = 4, 53, 31
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 16, 53, 81
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 42, 53, 81
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 16, 25, 81
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 42, 25, 81
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 16, 53, 56
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 4, 53, 56
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 16, 27, 56
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 4, 27, 56
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

# STEP 17
i, j, k, l = 42, 93, 62, 15
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k = 42, 53, 62
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 91, 4, 69
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

# STEP 18
i, j, k, l = 91, 88, 69, 76
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 19
i, j, k, l = 4, 88, 69, 7
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 88, 69, 76, 7
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k = 30, 88, 84
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 4, 88, 84
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 4, 27, 84
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

# STEP 20
i, j, k, l = 16, 27, 84, 48
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 16, 66, 84, 48
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k = 30, 66, 84
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 30, 88, 36
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 30, 66, 36
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 93, 66, 36
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

# STEP 21
i, j, k, l = 93, 62, 36, 40
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 88, 62, 36, 40
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 88, 62, 35, 40
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k = 91, 31, 35
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 53, 31, 35
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 53, 62, 35
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

# STEP 22
i, j, k, l = 91, 88, 35, 97
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 88, 35, 40, 97
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 62, 35, 40, 97
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k = 42, 93, 15
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 42, 62, 15
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 93, 62, 15
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 91, 88, 76
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 91, 69, 76
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 4, 88, 7
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 4, 69, 7
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 88, 76, 7
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 69, 76, 7
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 16, 27, 48
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 27, 84, 48
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 16, 66, 48
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 66, 84, 48
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

# STEP 23
i, j, k, l = 93, 62, 40, 22
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 24
i, j, k, l = 93, 36, 40, 89
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 93, 40, 22, 89
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 25
i, j, k, l = 88, 36, 40, 50
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 88, 40, 97, 50
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 36, 40, 89, 50
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k = 91, 88, 97
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 91, 35, 97
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

# STEP 26
i, j, k, l = 62, 35, 97, 94
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 62, 40, 97, 94
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 62, 40, 22, 94
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 40, 97, 50, 94
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

# STEP 27
i, j, k, l = 93, 62, 22, 34
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 93, 22, 89, 34
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k = 93, 36, 89
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 40, 22, 89
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 88, 36, 50
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

# STEP 28
i, j, k, l = 88, 97, 50, 95
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k, l = 97, 50, 94, 95
ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')
ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')
ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')

i, j, k = 36, 89, 50
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 40, 89, 50
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 62, 35, 94
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 35, 97, 94
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 62, 22, 94
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 40, 22, 94
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 40, 50, 94
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 93, 62, 34
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 62, 22, 34
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 93, 89, 34
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 22, 89, 34
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 88, 97, 95
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 88, 50, 95
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 97, 94, 95
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

i, j, k = 50, 94, 95
ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')
ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')
ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
