import numpy as np
# 1. #Make a 1D array of 5, 10, 15 … up to 50. Do not type the numbers.
array_1d = np.arange(5,51,5)
2. #Reshape it into 2 rows.

arr_res = array_1d.reshape((2,-1))
print(arr_res)
# 3. #Print its shape , ndim and dtype .

print(f"Shape of an array:{arr_res.shape}")
print(f"Dimension:{arr_res.ndim}")
print(arr_res.dtype)

marks = np.array([45, 82, 67, 91, 38, 74, 59, 88])
# 1. How many students scored 60 or above?

mask = marks >= 60
print(f"Expression only give list of true or flase:{mask}")
print(f"Students scored 60 or above: {marks[mask].size}")

# 2. What is the average of only those scores?

print(f"Average of socre 60 or above: {marks[mask].mean()}")
# 3. Print the scores that are 60 or above but below 85.

mask = (60 <= marks) & (marks < 85)

print(f"Scores above 60 but below 85: {marks[mask]}")
#Print each student passed or fail marks greater than = 40

print(np.where((marks >= 40),'passed','fail'))

#Last basic concept linspace(start,end,count)
print(f"Five elements array:{np.linspace(5,50,5)}")

'''VECTORISATION means One operation applied to every
element at once, instead of looping.'''#No loop anywhere
array = np.array([230,450,300,400])
add = array + 25
sub = array - 10
multi = array * 2
div = array / 100
print(add,sub,multi,div)

print(array.max(),array.min(),array.std().round(2))

