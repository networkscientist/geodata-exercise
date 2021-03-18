import numpy as np


def file_reader(path):
    """Reads content of a text file and returns precipitation data as a numpy array."""
    data = np.loadtxt(path, skiprows=1, usecols=2)
    return data


input_file = "data/precip_data.txt"
# call the file_reader function with the input_file path and store the returned data as pd
pd = file_reader(input_file)
# Calculate three statistical value and store the as a dictionary
statistics = {'Min': pd.min(), 'Max': pd.max(), 'Mean': pd.mean()}
print("Precipitation Data:\n")
# Go through the statistics dictionary and print the values in an ordered fashion
for x, y in statistics.items():
    print('{0:4}:   {1:4.1f} mm'.format(x, y))
