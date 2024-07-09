# multiple subplot

# dalalm sesi ini kita akan pelajari

# simple line plot
# multiple subplot dengan OO Style
# Multiple subplot dengan pyplot Style

# 1. Simple Line Plot
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

# siapka sample dataset
x = np.arange(0.0, 2.0, 0.01)
# print(x)

s = np.sin(2 * np.pi * x)
# print(s)

# melakukan plotting dengan gaya OO Style
fig, ax = plt.subplots()

ax.plot(x, s)

ax.set(xlabel='nilai x',
        ylabel='nilai sin(x)',
        title='vusialisasi nilai sin')
ax.grid()
plt.show()