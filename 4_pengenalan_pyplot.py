# Pyplot adalah modul dalam Matplotlib yang menyediakan antarmuka 
# tingkat tinggi untuk membuat dan memanipulasi grafik dengan cara
# yang lebih sederhana. Modul ini sering digunakan karena kemudahannya 
# dalam membuat grafik dengan cepat, mirip dengan cara kerja plotting di MATLAB.

# dengan kata lain : koleksi atau kumpulan fungsi yang menjadikan 
# matplotlib dapat bekerja menyerupai matlab


# pyplot api : memungkinkan Anda untuk membuat grafik secara cepat dengan 
# fungsi-fungsi sederhana. Anda tidak perlu membuat objek Figure atau Axes 
# secara eksplisit; Pyplot akan membuatnya

# secara umum tidak se fleksibel object oriented api

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

# pemanggilan fungsi plot() dapat dilakukan dengan menyertakan hanya sebuah deret
# bilangan (list/array) atau dua deret bilangan (list/array)

# bila pemanggilan hanya menyertakan sebuah deret bilangan, maka nilai pada deret
# bilanagan tersebut akan di jadikan data poin untuk nilai pada sumbu y; sedangkan 
# nilai pada sumbu x akan secara otomatis dibuatkan sebuah deret bilangan terurut
# dengan nilai di mulai dari nol

plt.plot([2, 5, 7, 11])
plt.ylabel('sumbu y')
plt.show()

plt.plot([2, 3, 4, 7], [5, 4, 2, 16])
plt.show()