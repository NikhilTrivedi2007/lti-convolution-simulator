import numpy as np
import matplotlib.pyplot as plt

# 1. Define Input Signal x[n] (e.g., a rectangular pulse)
x = np.array([0, 0, 1, 1, 1, 1, 1, 0, 0])

# 2. Define Impulse Response h[n] (e.g., an exponential decay system)
h = np.array([0, 0, 1, 0.8, 0.6, 0.4, 0.2, 0, 0])

# 3. Compute Convolution y[n] = x[n] * h[n]
y = np.convolve(x, h)

# 4. Plot Signals
n_x = np.arange(len(x))
n_h = np.arange(len(h))
n_y = np.arange(len(y))

fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# Input x[n]
axs[0].stem(n_x, x, linefmt='b-', markerfmt='bo', basefmt='k-')
axs[0].set_title('Input Signal: $x[n]$')
axs[0].grid(True)

# Impulse Response h[n]
axs[1].stem(n_h, h, linefmt='g-', markerfmt='go', basefmt='k-')
axs[1].set_title('System Impulse Response: $h[n]$')
axs[1].grid(True)

# Output Response y[n]
axs[2].stem(n_y, y, linefmt='r-', markerfmt='ro', basefmt='k-')
axs[2].set_title('Output System Response: $y[n] = x[n] * h[n]$')
axs[2].set_xlabel('Discrete Time Sample ($n$)')
axs[2].grid(True)

plt.tight_layout()
plt.show()
