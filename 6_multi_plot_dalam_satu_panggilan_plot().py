# multi plot dalam satu pemanggilan fungsi plot()

import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0., 5., 0.2) # ada 3 parameter, pertama dan keduan merepresentasi minumum maximum, yang ketiga
                           # merepresentasi sekumpulan nilai antara dengan interval yang konsisten 0.2
                           # beda linespace dan arange, parameter ketiga di linespace menunjukkan jumlah nilai antara
                           # sedangkan di arange menunjukkan interval nilai antara
print(t) 

# plt.plot(t, t, 'r--')
# plt.plot(t, t**2, 'bs')
# plt.plot(t, t**3, 'g^')
# plt.show()

# kita juga bisa melakukan multiplot dalam satu pemanggilan fungsi plot()
plt.plot(t, t, 'r--',
         t, t**2, 'bs',
         t, t**3, 'g^'
        )
plt.show()
