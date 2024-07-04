# pada dasarnya terdapat dua cara dalam menggunakan matplotlib dan melakukan plotting :
# 1. OO Style
# 2. Pyplot Style

# OO Style (Object Oriented Style ) : Secara eksplisit membuat 'figures' beserta 'axes', dan
# memanggil method dari ke duanya.
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)
print(x)

# membuat sebuah 'figure' dan sebuah 'axes'
fig, ax = plt.subplots()

# plotting tiga varian data pada axes
ax.plot(x, x, label = 'linear')
ax.plot(x, x**2, label = 'quadratic')
ax.plot(x, x**3, label = 'cibic')

ax.set_xlabel('x label') # menyertakana x label pada axes
ax.set_ylabel('y label') # menyertakan y label pada axes
ax.set_title("simple plot") # menyertakan title pada axes
ax.legend() # menyertakan legend

plt.show()