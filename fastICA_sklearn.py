import numpy as np
from sklearn.decomposition import FastICA
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Read the wave file
rate1, data1 = wavfile.read('./mixed/mixedX.wav')
rate2, data2 = wavfile.read('./mixed/mixedY.wav')

X = list(zip(data1, data2))

#Displaying raw data
plt.plot(data1)
plt.title("data1")
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(data2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("data2")
plt.show()

# Initialize FastICA with n_components=3
ica = FastICA(n_components=2, max_iter = 10000, whiten = True , tol = 0.00001)

# Run the FastICA algorithm using fit_transform on dataset X
ica_result = ica.fit_transform(X)

result_signal_1 = ica_result[:,0]
result_signal_2 = ica_result[:,1]

#Displaying output signals
plt.plot(result_signal_1)
plt.plot(result_signal_2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("source1 and source2 overlap")
plt.show()

plt.plot(result_signal_1)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("Source 1")
plt.show()

plt.plot(result_signal_2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("Source 2")
plt.show()


# Convert to int, map the appropriate range, and increase the volume a little bit
result_signal_1_int = np.int16(result_signal_1*32767*100)
result_signal_2_int = np.int16(result_signal_2*32767*100)


# Write wave files
wavfile.write("result_signal_1.wav", rate1, result_signal_1_int)
wavfile.write("result_signal_2.wav", rate1, result_signal_2_int)
