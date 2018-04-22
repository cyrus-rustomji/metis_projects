# x * w = y
# find w
# problem A: w = [4]
# B: no solution
# C: w = [4,0],[0,2]
# D: w = [-2,3]
# E: no solution
# F: w = [1,1]
# G: no solution
# H: w = [8,6]
# I: w = [4,4,2]
# J: no solution
# Yes, we can use numpy to check solutions.

import numpy as np

# A
x = np.array([[2]])
w = np.array([4])
print(x.dot(w))

# B
# no solution

# C has 3 solutions
x = np.array([[2,4]]) # sol 1
# w = np.array([4,0]) # sol 2
w = np.array([0,2]) # sol 3
# w = np.array([2,1]) # sol 4
print(x.dot(w))

# D
x = np.array([[2,4],[0,1]])
w = np.array([-2,3])
print(x.dot(w))

# E
# no solution

# F
x = np.array([[2,2],[3,3]])
w = np.array([1,1])
print(x.dot(w))

# G
# no solution
# x = [['dog'],['cat']]
# w = [4,3]
# depends what dog and cat are
# print(x.dot(w))


# H
x = np.array([[1,0],[0,1]])
w = np.array([8,6])
print(x.dot(w))

# I
x = np.array([[1,1,0],[1,0,1]])
w = np.array([4,4,2])
print(x.dot(w))

# J
x = np.array([[1,0],[1,1]])
w = np.array([8,-2])
print(x.dot(w))