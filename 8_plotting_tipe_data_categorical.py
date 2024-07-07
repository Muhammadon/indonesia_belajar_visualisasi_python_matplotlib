import matplotlib.pyplot as plt

# matplotlib juga mendukung plotting untuk data dengan tipe kategori atau biasa
# dikenal dengan istilah categorical data atau categorical variables

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

# plt.plot(names, values)
# plt.show()

# plt.scatter(names, values)
# plt.show()

plt.bar(names, values)
plt.show()