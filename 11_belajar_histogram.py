import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# print(matplotlib.__version__)
# print(np.__version__)

# Sample Data
mu, sigma  = 100, 15 # nilai mean dan nilai standard deviation

x = mu + sigma * np.random.randn(10000) # normal distribution
# print(x)
# print(x.shape)

# Histogram dengan Pyplot Style
plt.hist(x,
         bins=50, # jumlah kelumpok data dari 10000
         facecolor='g',
         alpha=0.75) # tingkat transparansi

plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Constoh Histogram')

plt.text(45, 500, r'$\mu=100,\ \sigma=15$')
plt.grid()

# plt.show()

# Histogram dengan OO Style
fig, ax = plt.subplots()

ax.hist(x,
        bins=50,
        facecolor='r',
        alpha=0.75)
ax.set_xlabel('Sumbu X')
ax.set_ylabel('Sumbu Y')
ax.set_title('Contoh Histogram')

ax.text(45, 500, r'$\mu=100,\ \sigma=15$')
ax.grid()

plt.show()