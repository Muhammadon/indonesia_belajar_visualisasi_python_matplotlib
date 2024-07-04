# plotting dengan keyword

# matplotlib juga memunkinkan kita untuk melakukan plotting sekumpulan nilai yang tersimpan
# dalam struktur data yang disertai keywords argumen (kwargs) seperti pada dictionary dan 
# pandas data frame

import matplotlib.pyplot as plt
import numpy as np

data = {
    'a': np.arange(50),
    'c': np.random.randint(0, 50, 50),
    'd': np.random.randn(50)
}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

# print(data)

# plt.scatter('a', 'b', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()