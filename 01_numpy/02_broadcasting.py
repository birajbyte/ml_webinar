# Broadcasting
import numpy as np
"""Broadcasting: Line up .
shape tuples from right to left (padding missing left slots with 1s) — 
every pair must either match or have a 1 that stretches to fit the other.
------------------------------------------------------------------------"""
g = np.arange(1, 17).reshape(4, 4)#Qn 1
print(g)
# 1. Print the third row.
print(f"Third row:{g[2,:]}")
# 2. Print the last column.
print(f"Last column:{g[:,-1]}")
# 3. Print the bottom-right 2 x 2 corner.
print(f"Bottom right 2*2 :\n {g[-2:,-2:]}")#negative indexing better when last elements
# Qn 2------------------------------------------------------------------
rng = np.random.default_rng(7)
m = rng.integers(10, 100, (5, 3)).astype(float)
# 1. Subtract each column's mean and divide by its standard deviation — in one line.
print(m)
result = (m - m.mean(axis = 0))/m.std(axis = 0)
print(result)
# 2. Print the column means and column standard deviations of the result.
print(f"Result col_means: {result.mean(axis=0)}\nResult col_std: {result.std(axis=0)}")
print(f"col_mean in clean way: {np.round(result.mean(axis = 0),6)}")
#np.round round up the 1e-16 scientific notation and give upto 6 decimal numbers

#Qn 3-------------------------------------------------------------------------
marks = np.array([38, 72, 45, 19, 88, 40, 61, 29, 95, 55])
# 1. Turn it into 1 for pass and 0 for fail, with 40 as the cut-off.
result = np.where(marks >= 40,1,0)
print(f"Result 1 for pass and 0 for fail: {result}")
# 2. How many passed?
st_pass = marks[marks >= 40].size
print(f"Passed:{st_pass}")
# 3. What percentage passed?
percen_pass = (st_pass/marks.size) * 100
print(f"Total percentage of student passed: {percen_pass}")

scores = np.array([[78, 85, 62],
[90, 71, 88],
[55, 64, 70],
[82, 93, 79]])
# rows = students, columns = subjects
# 1. Each student's total.
print(f"Student's total: {scores.sum(axis = 1)}")
# 2. Each subject's mean.
print(f"Subject Mean: {scores.mean(axis = 0)}")
# 3. The index of the student with the highest total.
total = scores.sum(axis = 1)
print(f'Index of students with highest total: {total.argmax()}')
# 4. The index of the subject with the lowest mean
sub_mean = scores.mean(axis = 1)
print(f'Index of the subject with lowest mean:{sub_mean.argmin()}')









