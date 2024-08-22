import numpy as np
import matplotlib.pyplot as plt

def find_peaks(data):
    maxima = []
    minima = []
   
    # Loop through data points
    for i in range(1, len(data) - 1):
        if data[i - 1] < data[i] > data[i + 1]:
            maxima.append(i)
        elif data[i - 1] > data[i] < data[i + 1]:
            minima.append(i)
   
    return maxima, minima

# Load data from file
data_1 = np.loadtxt('/content/Data_1.txt')
data_2 = np.loadtxt('/content/Data_2.txt')

# Find peaks
maxima_1, minima_1 = find_peaks(data_1)
maxima_2, minima_2 = find_peaks(data_2)

print("Data 1 Maxima indices:", maxima_1)
print("Data 1 Minima indices:", minima_1)

print("Data 2 Maxima indices:", maxima_2)
print("Data 2 Minima indices:", minima_2)

# Plot Data 1
plt.figure(figsize=(10, 5))
plt.plot(data_1, label='Data 1')
plt.scatter(maxima_1, data_1[maxima_1], color='red', label='Maxima', marker='o')
plt.scatter(minima_1, data_1[minima_1], color='blue', label='Minima', marker='o')
plt.title('Data 1 - Sinusoidal Wave with Peaks')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Plot Data 2
plt.figure(figsize=(10, 5))
plt.plot(data_2, label='Data 2')
plt.scatter(maxima_2, data_2[maxima_2], color='red', label='Maxima', marker='o')
plt.scatter(minima_2, data_2[minima_2], color='blue', label='Minima', marker='o')
plt.title('Data 2 - Sinusoidal Wave with Peaks')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.legend()
plt.show()