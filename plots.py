from montecarlo import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N = np.zeros(shape=(10, 22, 2), dtype=int)  # dealersum-1, playersum, action (0=hit, 1=stick)
Q = np.random.rand(10, 22, 2) - 0.5
for i in range(5000000):
    if i % 10000 == 0: print(i)
    N, Q = montecarlo(N, Q)

np.ndarray(shape=(10, 22))

Q = np.transpose(Q, axes=(1, 0, 2))
X = np.arange(1, 11, 1)
Y = np.arange(0, 22, 1)
X, Y = np.meshgrid(X, Y)

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111, projection='3d')
ax1.set_zlim(-1.01, 1.01)
ax1.plot_wireframe(X, Y, Q[:, :, 1])
fig1.show()
plt.savefig('stick.png')

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111, projection='3d')
ax2.set_zlim(-1.01, 1.01)
ax2.plot_wireframe(X, Y, Q[:, :, 0])
fig2.show()
plt.savefig('hit.png')

fig3 = plt.figure(3)
ax3 = fig3.add_subplot(111, projection='3d')
ax3.set_zlim(-2.01, 2.01)
ax3.plot_wireframe(X, Y, Q[:, :, 0] - Q[:, :, 1])
fig3.show()
plt.savefig('dif.png')

fig4 = plt.figure(4)
ax4 = fig4.add_subplot(111)
ax4.pcolormesh(X, Y, np.argmax(Q, axis=2))
plt.savefig('choice.png')
