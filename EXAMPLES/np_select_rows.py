import numpy as np

sample_data = np.loadtxt(   # Read some data into 2d array
    "../DATA/columns_of_numbers.txt",
    skiprows=1,
    dtype=np.int16,
)

print("first 5 rows of sample_data:")
print(sample_data[:5, :], '\n')
print(sample_data.shape)

selected = sample_data[  # Index into the existing data
    (sample_data[:, 0] < 10) &  # Combine two Boolean expressions with &
    (sample_data[:, -1] > 35)
]

print("selected")
print(selected)
