# Create Array Using NumPy:

start with command:

```python
import numpy as np
```

simple array:

```python
arr = np.array([1, 2, 3, 4, 5])
```

Two Dimensional array with bit initialization:

```python
myArray=np.array([[2,3,4,5]],np.int32) #showing bits, how much number can take bits
```

**Initializing arrays:**

```python
# 3x3 array of zeros
zeros_array = np.zeros((3, 3))

# 2x4 array of ones
ones_array = np.ones((2, 4))

# 2x2 array filled with 7
full_array = np.full((2, 2), 7)

print("Zeros Array:\n", zeros_array)
print("\nOnes Array:\n", ones_array)
print("\nFull Array:\n", full_array)
```

Output:

```python
Zeros Array:
 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]

Ones Array:
 [[1. 1. 1. 1.]
 [1. 1. 1. 1.]]

Full Array:
 [[7 7]
 [7 7]]
```

**Explanation:**

Using `np.zeros()`, `np.ones()`, and `np.full()` is helpful in many situations when working with NumPy arrays. 

- Before running algorithms (like machine learning, image processing, or simulations), you might need a placeholder array.
- When working with numerical computations, you often need to initialize an array before filling it with values.
- These functions provide a quick and efficient way to create arrays of a specific shape.
- When creating arrays with `np.empty()`, the values inside are random (whatever was in memory).
- Using `zeros()` or `ones()` ensures a clean starting point.

**Example Use Cases:**

1. Image Processing:

```python
import numpy as np

# Create a blank black image (all zeros)
image = np.zeros((512, 512, 3), dtype=np.uint8)

```

(Used for initializing images before drawing shapes)

**2. Machine Learning Weights Initialization**

```python

weights = np.ones((10, 5))  # Initializing weights with ones

```

**3. Creating a Board Game Grid**

```python

game_board = np.full((3, 3), "-")  # Tic-Tac-Toe board

```

### 3. Create an Array with `arange()` and `linspace()`

```python
np.arange(1, 10, 2)   # [1 3 5 7 9]
np.linspace(0, 5, 10) # 10 equally spaced numbers from 0 to 5

```

### Accessing & Modifying Arrays

### 1. Indexing (Same as Python Lists)

```python

arr = np.array([10, 20, 30, 40])
print(arr[1])   # 20

```

### 2. Slicing

```python

arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])  # [20 30 40]

```

### 3. Reshaping Arrays

```python
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = arr.reshape(2,3)  # Converts 1D to 2D array
print(new_arr)

```

*Output:*

```

[[1 2 3]
 [4 5 6]]

```

---

### Mathematical Operations

NumPy supports element-wise operations:

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2) # [5 7 9]
print(arr1 * 2)    # [2 4 6]
print(arr1 * arr2) # [4 10 18]
print(np.sqrt(arr1)) # [1. 1.414 1.732]

```

---

### Useful NumPy Functions

### 1. Statistical Operations

```python
arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))   # 3.0
print(np.median(arr)) # 3.0
print(np.std(arr))    # Standard deviation

```

### 2. Random Numbers

```python
np.random.rand(3,3)  # 3x3 matrix of random numbers (0 to 1)
np.random.randint(1, 100, (2,2)) # Random integers from 1 to 100

```

---

### Working with 2D Arrays (Matrices)

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)  # (2,3)
print(matrix[0, 1])  # Element at row 0, column 1 (2)

```

### Matrix Multiplication

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.dot(A, B)  # Matrix multiplication
print(C)
```