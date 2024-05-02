# Learning NumPy from scratch
import numpy as np

def create_array(lst):
    # 1D array of integers
    my_array = np.array(lst)

    # 1D array of floating-point numbers
    my_array = np.array(lst, dtype=float)

    # 1D array with predefined values
    my_array = np.array([3, 4, 15, 2.4])

    # 2D array
    my_array = np.array([[1, 2, 4], [3, 6, 26]])

    # 2D array using list comprehension
    my_array = np.array([range(i, i + 3) for i in range(4)])

    # Zero-dimensional array with a single value 5
    my_array = np.array(5)

    # 3D array with ndmin parameter
    my_array = np.array([1, 4], ndmin=3)

    # Another example of a 3D array with ndmin
    my_array = np.array([[[1, 4]]], ndmin=1)

    # Checking the type of the array
    a = type(my_array)  # <class 'numpy.ndarray'>

def built_in_array():
    zero_array = np.zeros(10, dtype=float)  # 1D array of 10 zeros
    
    zero_array_2d = np.zeros((3, 4))  # 2D array of zeros with shape (3, 4)
    
    ones_array = np.ones((3, 4), dtype=float)  # 3x4 array of ones
    
    same_num_array = np.full((3, 4), 15)  # 3x4 array with all elements set to 15
    
    sequence_array = np.arange(0, 20, 2)  # 1D array with values [0, 2, 4, 6, ...., 18]
    
    array = np.linspace(0, 1, 5)  # 1D array with 5 values evenly spaced between 0 and 1
    
    random_array = np.random.random((3, 4))  # 3x4 array with random values between 0 and 1
    
    ran_array = np.random.normal(0, 1, (3, 4))  # 3x4 array with random values from a normal distribution
    
    eye_matrix = np.eye(3)  # 3x3 identity matrix
    
    empty_array = np.empty(3)  # 1D array with uninitialized values (not recommended for use)
 
import numpy as np

def numpy_attributes(my_array):
    my_array = np.random.random(size=(3, 4, 5))  # Create a random 3D array
    
    number_of_dimensions = my_array.ndim  # Number of dimensions: 3
    
    type_of_elements = my_array.dtype  # Data type of elements: float64
    
    number_of_elements = my_array.size  # Number of elements: 60
    
    shape = my_array.shape  # Shape of the array: (3, 4, 5)

def array_indexing():
    # First indexing of 1D array
    my_array = np.array([1, 3, 35, 6, 2, 6, 783, 67, 7])
    
    print(my_array[0])  # 1
    print(my_array[1])  # 3
    print(my_array[-1])  # 7
    print(my_array[-2])  # 67
    print(my_array[:2])  # [1, 3]
    print(my_array[2:])  # [35, 6, 2, 6, ....]
    print(my_array[::-1])  # Reverse array

    # Second indexing of 2D array
    my_array = np.array([[3, 1, 3, 7], [4, 0, 2, 3], [0, 0, 6, 9]], dtype=int)
    
    print(my_array[0, 0])  # 3
    print(my_array[1, 2])  # 2
    print(my_array[2, -1])  # 9
    my_array[0, 0] = 2.4  # Modify an element
    print(my_array[0, 0])  # 2
    print(my_array[:2, :3])  # First 2 rows and first 3 columns
    print(my_array[::-1, ::-1])  # Reverse all rows and columns
    print(my_array[0, :])  # Get row zero

def modification_making_copy():
    # Example of modifying the original array and using copy
    my_array = np.array([1, 2, 3, 4, 5])
    
    # Sub-array referencing (not a copy)
    sub_array = my_array[2:]
    sub_array[0] = -33
    print(my_array)  # [1 2 -33 4 5]
    
    # Creating a copy to avoid modifying the original array
    my_array[2] = 3
    sub_array = my_array[2:].copy()
    sub_array[0] = -33
    print(my_array)  # [1 2 3 4 5]

def reshaping_array():
    # Example of reshaping arrays
    my_array = np.array([1, 2, 3, 4, 5, 6])
    
    # Reshape to a 3x2 array
    reshaped_array = my_array.reshape(3, 2)
    print(reshaped_array)
    
    # Reshape to a 3x2 array with automatic determination of the number of columns
    reshaped_array = my_array.reshape(3, -1)
    print(reshaped_array)
    
    # Flatten the array to a 1D array
    my_array = my_array.reshape(-1)
    print(my_array)
    
    # Reshape using np.reshape with explicit shape
    y = np.reshape(my_array, (3, -1))
    print(y)
    
    # Add a new axis (row-wise) using np.newaxis
    my_array = my_array[np.newaxis, :]
    print(my_array[np.newaxis, :])
    
    # Add a new axis (column-wise) using np.newaxis
    my_array = my_array[:, np.newaxis]
    print(my_array)

def canocation_of_array():
    x = np.array([1, 2, 3])
    y = np.array([3, 2, 1])
    z=np.concatenate([x, y]) #array([1, 2, 3, 3, 2, 1])
    #You can also concatenate more than two arrays at once:
    z = np.array([99, 99, 99])
    print(np.concatenate([x, y, z])) #[ 1 2 3 3 2 1 99 99 99]
    #And it can be used for two-dimensional arrays:
    grid = np.array([[1, 2, 3],[4, 5, 6]])
    # concatenate along the first axis
    l=np.concatenate([grid, grid]) #same as vertical stack
    # array([[1, 2,3]
    #       [4, 5, 6],
    #       [1, 2, 3],
    #       [4, 5, 6]])
    # concatenate along the second axis (zero-indexed)
    f=np.concatenate([grid, grid], axis=1) #same as horizontal stack
    #array([[1, 2, 3, 1, 2, 3],
    #       [4, 5, 6, 4, 5, 6]])

def splitting_array():
    # Example of splitting 2D array vertically and horizontally
    my_array = np.array([[1, 3, 5, 5], [4, 7, 87, 2]])
    
    # Vertical split at index 1
    upper, lower = np.vsplit(my_array, [1])
    print("Vertical Split:")
    print(upper)
    print(lower)
    
    # Horizontal split at column index 2
    right_part, left_part = np.hsplit(my_array, [2])
    print("\nHorizontal Split:")
    print(right_part)
    print(left_part)
    
    # Example of splitting a 1D array at indices 1 and 3
    my_array = np.array([1, 4, 77, 3, 5, 86, 2])
    a, b, c = np.split(my_array, [1, 3])
    print("\n1D Array Split:")
    print(a, b, c)

def arithmitic_operation():
    my_array = np.arange(0, 10)
    
    # Arithmetic operations:
    add_result = my_array + 10
    mul_result = my_array * 10
    sub_result = my_array - 10
    div_result = my_array / 10
    int_div_result = my_array // 10
    unary_minus_result = -my_array
    reminder_result = my_array % 2
    power_result = my_array**2
    equation_result = my_array * 5 + 16
    
    # Print the results for illustration
    print("Addition:", add_result)
    print("Multiplication:", mul_result)
    print("Subtraction:", sub_result)
    print("Division:", div_result)
    print("Integer Division:", int_div_result)
    print("Unary Minus:", unary_minus_result)
    print("Reminder:", reminder_result)
    print("Power:", power_result)
    print("Equation:", equation_result)

def trig_func():
    # Trigonometric functions example
    my_array = np.linspace(0, 2*np.pi, 3)
    
    print(f'The sin of the data is {np.sin(my_array)}')
    print(f'The cos of the data is {np.cos(my_array)}')
    print(f'The tan of the data is {np.tan(my_array)}')
    
    my_array = np.array([-1, 0, 1])
    print(f'The sin inverse of the data is {np.arcsin(my_array)}')
    print(f'The cos inverse of the data is {np.arccos(my_array)}')
    print(f'The tan inverse of the data is {np.arctan(my_array)}')

def exp_log_operations():
    my_array = np.arange(1, 6)
    
    # Exponential and logarithmic operations:
    exp_result = np.exp(my_array)
    log_result = np.log(my_array)
    log10_result = np.log10(my_array)
    log2_result = np.log2(my_array)
    
    # Print the results for illustration
    print("Exponential:", exp_result)
    print("Natural Logarithm:", log_result)
    print("Base-10 Logarithm:", log10_result)
    print("Base-2 Logarithm:", log2_result)

def aggregation_operations():
    my_array = np.array([1, 5, 7, 2, 8, 3, 6, 4])
    
    # Aggregation operations:
    min_value = np.min(my_array)
    max_value = np.max(my_array)
    sum_value = np.sum(my_array)
    mean_value = np.mean(my_array)
    std_value = np.std(my_array)
    var_value = np.var(my_array)
    median_value = np.median(my_array)
    any_value = np.any(my_array)
    all_value = np.all(my_array)
    arg_min = np.argmin(my_array)
    arg_max = np.argmax(my_array)
    
    # Print the results for illustration
    print("Array:", my_array)
    print("Minimum Value:", min_value)
    print("Maximum Value:", max_value)
    print("Sum:", sum_value)
    print("Mean:", mean_value)
    print("Standard Deviation:", std_value)
    print("Variance:", var_value)
    print("Median:", median_value)
    print("Any True:", any_value)
    print("All True:", all_value)
    print("Index of Minimum Value:", arg_min)
    print("Index of Maximum Value:", arg_max)

