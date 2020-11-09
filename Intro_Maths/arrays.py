#arrays have attributes ndim (the number of dimensions), shape (the size of each dimension), size (the total size of the array), dtype (data type of array), itemsize (size of each element in the array in terms of bytes), and nbytes (total size of array in bytes)
np.random.seed(0)  # seed for reproducibility
x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

print("x3 ndim: ", x3.ndim) #would print x3 ndim:  3
print("x3 shape:", x3.shape) #would print x3 shape: (3, 4, 5)
print("x3 size: ", x3.size)
