import numpy as np


def file_reader(path):
    """Reads content of a text file and returns precipitation data as a numpy array."""
    data = np.loadtxt(path, skiprows=1, usecols=2)
    return data


input_file = "data/precip_data.txt"
pd = file_reader(input_file)
statistics = {'Min': pd.min(), 'Max': pd.max(), 'Mean': pd.mean()}
print("Precipitation Data:\n")
for x, y in statistics.items():
    print('{0:4}:   {1:4.1f} mm'.format(x, y))
# • The script: it should call the function and display to the user:
# • The min precipitation
# • The max precipitation
# • The mean precipitation
