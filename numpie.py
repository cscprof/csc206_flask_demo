from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import numpy as np
CURVE_CENTER = 80

# grades = np.array([63, 77, 63, 67, 87, 60, 70, 70, 57, 73, 80, 83,
#                   27, 70, 43, 80, 47, 60, 53, 50, 63, 50, 63, 47, 50, 60, 37, 63, 57])

# # Curve grades for a class
# def curve(grades):
#     average = grades.mean()
#     change = CURVE_CENTER - average
#     new_grades = grades + change
#     return np.clip(new_grades, grades, 100)

# print(curve(grades))
# print("\n\n")

# Standard Deviaiton of grades
# std_dev = np.std(grades)
# avg = np.average(grades)
# print("Standard deviation of the grades is {} and the average is {} \n".format(std_dev, avg))


# axes_2d = np.arange(0,6).reshape([2,3])

# # Print the array
# print(axes_2d)

# # Sum the full array
# sum_2d = np.sum(axes_2d)
# print("2D sum: {} \n".format(sum_2d))

# # Sum the 0 axis
# sum_2d_0 = np.sum(axes_2d, axis=0)
# print(" Axis 0 sum:\n")
# print(sum_2d_0)

# # Sum the 1 axis
# sum_2d_1 = np.sum(axes_2d, axis=1)
# print(" Axis 1 sum:\n")
# print(sum_2d_1)


# Concatenate arrays
# np_array_1s = np.array([[1,1,1],[1,1,1]])
# np_array_9s = np.array([[9,9,9],[9,9,9]])

# print("\nConcatenate on axis 0")
# concat_0 = np.concatenate([np_array_1s, np_array_9s], axis = 0)
# print(concat_0)

# print("\nConcatenate on axis 1")
# concat_1 = np.concatenate([np_array_1s, np_array_9s], axis = 1)
# print(concat_1)



# Calculate powers of 2
# a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# b = 2

# results = b ** a

# print(results)
