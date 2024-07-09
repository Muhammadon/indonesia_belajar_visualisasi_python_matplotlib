# multiple subplots

import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.0, 5.0, 100)
x2 = np.linspace(0.0, 2.0, 100)

y1 = np.cos(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)

# print(x1)

# multiple subplot dengan OO Style
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('multiple subplots')

ax1.plot(x1, y1, 'ro-')
ax1.set_ylabel('nilai $cos(x_1)$')

ax2.plot(x2, y2, 'g.-')
ax2.set_ylabel('milai cos(x2)')

ax2.set_xlabel('nilai x')

plt.show()

# multiple subplots dengan Pyplot Style
plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'ro-')
plt.title('multiple subplots')
plt.ylabel('nilai $cos(x_1)$')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'g.-')
plt.ylabel('nilai $cos(x_2)$')
plt.xlabel('nilai $x$')
plt.show()