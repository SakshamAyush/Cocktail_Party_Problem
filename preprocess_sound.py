"""The script makes the sources to have same length,
as well as have the same sampling rate"""
from scipy.io import wavfile
import matplotlib.pyplot as plt
# Read the .wav files as numpy arrays
rate1, data1 = wavfile.read("./sources/sourceX.wav")
rate2, data2 = wavfile.read("./sources/sourceY.wav")
print(data1.shape)
print(data2.shape)


# Make both of the files to have same length as well as same sampling rate
minimum = min(data1.shape[0], data2.shape[0])
print(minimum
      )
# Slicing the array for both the sources
data1 = data1[0:minimum]
data2 = data2[0:minimum]

print(data1.shape)
print(data2.shape)

plt.plot(data1)
plt.title("data1")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()

plt.plot(data2)
plt.title("data2")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()
#writing the array into to the wav file with sampling rate which is average of the two
wavfile.write("./mixed/mixedX.wav", rate1, data1)
wavfile.write("./mixed/mixedY.wav", rate2, data2)