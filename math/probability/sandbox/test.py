import numpy as np

nilai = [
    65, 70, 75, 80, 85, 90, 95, 100, 60, 78,
    88, 72, 68, 94, 82, 77, 89, 85, 91, 79,
    64, 74, 81, 87, 93, 62, 76, 84, 69, 71
]
nilai2 = [
    100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    100, 100, 100, 100, 100, 100, 100, 100, 100, 100
]
nilai3 = [
    60, 60, 60, 60, 60, 60, 60, 60, 60, 60,
    60, 60, 60, 60, 60, 60, 60, 60, 60, 60,
    60, 60, 60, 60, 60, 60, 60, 60, 60, 60
]


nilai_array = np.array(nilai3)
print(nilai_array)

std_dev = np.std(nilai_array)
mean = np.mean(nilai_array)

print(f'Standard Deviation: {std_dev}')
print(f'Mean: {mean}')
