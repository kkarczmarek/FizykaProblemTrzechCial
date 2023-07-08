import scipy as sci
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Stała grawitacji

G = 6.67408e-11  # N-m2/kg2


m_nd = 1.989e+30  # kg
r_nd = 5.326e+12  # m
v_nd = 30000  # m/s
t_nd = 79.91 * 365.25 * 24 * 3600  # s

# Stałe
K1 = G * t_nd * m_nd / (r_nd ** 2 * v_nd)
K2 = v_nd * t_nd / r_nd

# Masy ciał
m1 = 1.1  # Star 1
m2 = 0.907  # Star 2
m3 = 1.425  # Star 3

# Początkowe wektry położeń
r1 = [-0.5, 1, 0]  # m
r2 = [0.5, 0, 0.5]  # m
r3 = [0.2, 1, 1.5]  # m

r1 = np.array(r1)
r2 = np.array(r2)
r3 = np.array(r3)

# Środek masy
r_com = (m1 * r1 + m2 * r2 + m3 * r3) / (m1 + m2 + m3)

# Początkowe wektory prędkości
v1 = [0.02, 0.02, 0.02]  # m/s
v2 = [-0.05, 0, -0.1]  # m/s
v3 = [0, -0.03, 0]

v1 = np.array(v1)
v2 = np.array(v2)
v3 = np.array(v3)

v_com = (m1 * v1 + m2 * v2 + m3 * v3) / (m1 + m2 + m3)


def ThreeBodyEquations(w, t, G, m1, m2):
    r1 = w[:3]
    r2 = w[3:6]
    r3 = w[6:9]
    v1 = w[9:12]
    v2 = w[12:15]
    v3 = w[15:18]

    # Znajdź odległości między trzema ciałami
    r12 = sci.linalg.norm(r2 - r1)
    r13 = sci.linalg.norm(r3 - r1)
    r23 = sci.linalg.norm(r3 - r2)

    # Zdefiniuj pochodne zgodnie z równaniami
    dv1bydt = K1 * m2 * (r2 - r1) / r12 ** 3 + K1 * m3 * (r3 - r1) / r13 ** 3
    dv2bydt = K1 * m1 * (r1 - r2) / r12 ** 3 + K1 * m3 * (r3 - r2) / r23 ** 3
    dv3bydt = K1 * m1 * (r1 - r3) / r13 ** 3 + K1 * m2 * (r2 - r3) / r23 ** 3
    dr1bydt = K2 * v1
    dr2bydt = K2 * v2
    dr3bydt = K2 * v3

    # Dodajemy pochodne do tablicy
    r12_derivs = np.concatenate((dr1bydt, dr2bydt))
    r_derivs = np.concatenate((r12_derivs, dr3bydt))
    v12_derivs = np.concatenate((dv1bydt, dv2bydt))
    v_derivs = np.concatenate((v12_derivs, dv3bydt))
    derivs = np.concatenate((r_derivs, v_derivs))
    return derivs

init_params = np.array([r1, r2, r3, v1, v2, v3])  # Tablica o rozmiarze 18
init_params = init_params.flatten()  # Tablica jednowymiarowa
time_span = np.linspace(0, 20, 1000)  # Przedział czasowy

import scipy.integrate

three_body_sol = sci.integrate.odeint(ThreeBodyEquations, init_params, time_span, args=(G, m1, m2))

# Zapis rozwiązania pozycji w trzech różnych tablicach
r1_sol = three_body_sol[:, :3]
r2_sol = three_body_sol[:, 3:6]
r3_sol = three_body_sol[:, 6:9]

# Narysuj orbity trzech ciał
fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection="3d")
ax.plot(r1_sol[:, 0], r1_sol[:, 1], r1_sol[:, 2], color="mediumblue")
ax.plot(r2_sol[:, 0], r2_sol[:, 1], r2_sol[:, 2], color="red")
ax.plot(r3_sol[:, 0], r3_sol[:, 1], r3_sol[:, 2], color="gold")
ax.scatter(r1_sol[-1, 0], r1_sol[-1, 1], r1_sol[-1, 2], color="darkblue", marker="o", s=80, label="Star 1")
ax.scatter(r2_sol[-1, 0], r2_sol[-1, 1], r2_sol[-1, 2], color="darkred", marker="o", s=80, label="Star 2")
ax.scatter(r3_sol[-1, 0], r3_sol[-1, 1], r3_sol[-1, 2], color="goldenrod", marker="o", s=80, label="Star 3")
ax.set_xlabel("x-coordinate", fontsize=14)
ax.set_ylabel("y-coordinate", fontsize=14)
ax.set_zlabel("z-coordinate", fontsize=14)
ax.set_title("Visualization of orbits of stars in a 3-body system\n", fontsize=14)
ax.legend(loc="upper left", fontsize=14)

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection="3d")

r1_sol_anim = r1_sol[::1, :].copy()
r2_sol_anim = r2_sol[::1, :].copy()
r3_sol_anim = r3_sol[::1, :].copy()

head1 = [ax.scatter(r1_sol_anim[0, 0], r1_sol_anim[0, 1], r1_sol_anim[0, 2], color="darkblue", marker="o", s=80,
                    label="Star 1")]
head2 = [ax.scatter(r2_sol_anim[0, 0], r2_sol_anim[0, 1], r2_sol_anim[0, 2], color="darkred", marker="o", s=80,
                    label="Star 2")]
head3 = [ax.scatter(r3_sol_anim[0, 0], r3_sol_anim[0, 1], r3_sol_anim[0, 2], color="goldenrod", marker="o", s=80,
                    label="Star 3")]


def Animate(i, head1, head2, head3):
    head1[0].remove()
    head2[0].remove()
    head3[0].remove()

    # Wykreśl orbity (każdą iterację wykreślamy od pozycji początkowej do bieżącej)
    trace1 = ax.plot(r1_sol_anim[:i, 0], r1_sol_anim[:i, 1], r1_sol_anim[:i, 2], color="mediumblue")
    trace2 = ax.plot(r2_sol_anim[:i, 0], r2_sol_anim[:i, 1], r2_sol_anim[:i, 2], color="red")
    trace3 = ax.plot(r3_sol_anim[:i, 0], r3_sol_anim[:i, 1], r3_sol_anim[:i, 2], color="gold")

    head1[0] = ax.scatter(r1_sol_anim[i - 1, 0], r1_sol_anim[i - 1, 1], r1_sol_anim[i - 1, 2], color="darkblue",
                          marker="o", s=100)
    head2[0] = ax.scatter(r2_sol_anim[i - 1, 0], r2_sol_anim[i - 1, 1], r2_sol_anim[i - 1, 2], color="darkred",
                          marker="o", s=100)
    head3[0] = ax.scatter(r3_sol_anim[i - 1, 0], r3_sol_anim[i - 1, 1], r3_sol_anim[i - 1, 2], color="goldenrod",
                          marker="o", s=100)
    return trace1, trace2, trace3, head1, head2, head3,

ax.set_xlabel("x-coordinate", fontsize=14)
ax.set_ylabel("y-coordinate", fontsize=14)
ax.set_zlabel("z-coordinate", fontsize=14)
ax.set_title("Visualization of orbits of stars in a 3-body system\n", fontsize=14)
ax.legend(loc="upper left", fontsize=14)

# Animacja
repeatanim = animation.FuncAnimation(fig, Animate, frames=3000, interval=1, repeat=False, blit=False,
                                     fargs=(head1, head2, head3))
plt.show()