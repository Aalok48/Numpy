import numpy as np

arr1 = np.array(['a','s','d','f'])      # Creating a new array
check = [False, True, True, False]      # a new array is created which has true in the index of element that has to be chosen otherwise false
filtered_array = arr1[check]            # the array if filtered by passing the check array to the first array
print(filtered_array)