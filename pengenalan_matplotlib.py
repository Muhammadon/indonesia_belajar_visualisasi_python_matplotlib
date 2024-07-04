import matplotlib.pyplot as plt
import numpy as np

# membuat plotting sederhana
# membuat sebuah 'figure' yang memiliki sebuah 'axes'; melakukan plotting
# data pada axes

# Figure = Kanvas atau kertas tempat menggambar. (kontainer dasa, dalam boleh lebih 1 axes)
# Axes = Area di dalam kanvas tempat grafik digambar.
# Axis = Garis skala pada grafik (sumbu x dan y).

# persiapan sample data
# x = [1, 2, 3, 4]
# y = [1, 4, 2, 3]

# membuat sebuah figure dan sebuah axes
# fig, ax = plt.subplots()

# melakukan plotting data pada axes
# ax.plot(x, y)

# menampilkan plotting
# plt.show()


# alternatif lain, kita bisa langsung memanfaatkan method plot() pada
# pyplot untuk melakukan plotting sederhana
# x = [1, 2, 3, 4]
# y = [1, 4, 2, 3]

# plt.plot(x, y)
# plt.show()


# berikut beberapa cara untuk membuat 'figure' dan 'axes'
# { membuat objek 'figure' tanpa axes : fig = plt.figure() }
# { membuat objek 'figure' dengan sebuah axes : fig, ax = plt.subplots() }
# { sebuah objek 'figure' dengan 2 x 3 grif 'axes' : fig, axs = plt.subplots(2, 3) }

fig, axs = plt.subplots(2, 3)
ig, axs = plt.subplots(3, 2)
plt.show()