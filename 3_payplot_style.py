# pada dasarnya terdapat dua cara dalam menggunakan matplotlib dan melakukan plotting :
# 1. OO Style
# 2. Pyplot Style, kita akan bahas di sini

# mengandalkan pyplot untuk membuat dan mengelola 'figures' dan 'axes', serta menggunkan
# fungsi pada pyplot untuk melakukan plotting, dalam arti lain kita tidak secara explisit
# mendefinisikan 'figure' dan 'axes' seperti pada OO Style

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2, 100)
print(x)

# plotting tiga varian pada axes
plt.plot(x, x, label = 'linear')
plt.plot(x, x**2, label = 'quadratic')
plt.plot(x, x**3, label = 'cibic')

plt.xlabel('x label') # menyertakana x label pada axes
plt.ylabel('y label') # menyertakan y label pada axes
plt.title("simple plot") # menyertakan title pada axes
plt.legend() # menyertakan legend

plt.show()

