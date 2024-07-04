# pengaturan format pada plot

# selain menyertakan dua deret bilangan sebagai parameter untuk sumbu x dan y,
# terdapat parameter ketiga yang bisa kita sertakan untuk mengatur warna dan jenis plotting

# pengaturan parameter ketiga ini sepenuhnya mengadopsi gaya formatting pada MATLAB

# nilai default untuk parameter ketiga ini adalah 'b-' (warna biru dan markernya ----)

# pemanggilan fungsi axis() menyertakan list[xmin, xmax, ymin, ymax]

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo') # contoh parameter ketiga lainnya ('g-', 'b*')
plt.axis([0, 6, 0, 20])
plt.show()
