from scipy.io import wavfile
from FastICA import FastICA
import matplotlib.pyplot as plt
import utilities as utl
import numpy as np

# Read the mixed signals
rate1, data1 = wavfile.read('./mixed/mixedX.wav')
rate2, data2 = wavfile.read('./mixed/mixedY.wav')

# Centering the mixed signals and scaling the values as well
data1 = data1 - np.mean(data1)
data1 = data1/32768
data2 = data2 - np.mean(data2)
data2 = data2/32768

#Display raw data from First wave file
plt.plot(data1)
plt.title("data1")
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

#Display raw data from Second wave file
plt.plot(data2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("data2")
plt.show()

# Creating a matrix out of the signals
signals = [data1, data2]

plt.figure()
plt.plot(signals[0], signals[1], '*b')
plt.ylabel('Signal 2')
plt.xlabel('Signal 1')
plt.title("Original data")

matrix = np.vstack(signals)

# Whitening the matrix as a pre-processing step
whiteMatrix = utl.whitenMatrix(matrix)

X = whiteMatrix

#Display the whitened matrix
plt.figure()
plt.plot(X[0], X[1], '*b')
plt.ylabel('Signal 2')
plt.xlabel('Signal 1')
plt.title("Whitened data")
plt.show()


# Find the individual components one by one
vectors = []
for i in range(0, X.shape[0]):
	# The FastICA function is used
	vector = FastICA(X, vectors, eps=0.00000000001)
	vectors.append(vector)

# Stack the vectors to form the unmixing matrix
W = np.vstack(vectors)

# Get the original matrix
S = np.dot(W, whiteMatrix)

# Plot the separated sound signals
plt.plot(S[0])
plt.plot(S[1])
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("source1 and source2 overlap")
plt.show()

plt.plot(S[0])
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("Source 1")
plt.show()

plt.plot(S[1])
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("Source 2")
plt.show()

# Write the separated sound signals, 5000 is multiplied so that signal is audible
wavfile.write("separate1.wav", rate1, 5000*S[0].astype(np.int16))
wavfile.write("separate2.wav", rate1, 5000*S[1].astype(np.int16))
