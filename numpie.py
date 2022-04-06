import numpy as np
CURVE_CENTER = 80

grades = np.array([63, 77, 63, 67, 87, 60, 70, 70, 57, 73, 80, 83,
                  27, 70, 43, 80, 47, 60, 53, 50, 63, 50, 63, 47, 50, 60, 37, 63, 57])


def curve(grades):
    average = grades.mean()
    change = CURVE_CENTER - average
    new_grades = grades + change
    return np.clip(new_grades, grades, 100)


print(curve(grades))
print("\n\n")

# Calculate powers of 2
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = 2

results = b ** a

print(results)
