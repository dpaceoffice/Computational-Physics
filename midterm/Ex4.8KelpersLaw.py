import math
import matplotlib.pyplot as plt
"""
Planetary Orbit
Figure 4.6
"""
X = 0
Y = 1
VX = 2
VY = 3
R = 4


def main(N=2000, β=2.0, dt=0.001):
    for i in range(0, N):
        x = data[X][i]
        y = data[Y][i]
        vx = data[VX][i]
        vy = data[VY][i]

        r_i = (x**2 + y**2)**0.5
        vx_i = vx - (4*math.pi**2*x)/r_i**(β + 1) * dt
        vy_i = vy - (4*math.pi**2*y)/r_i**(β + 1) * dt
        x_i = x + vx_i * dt
        y_i = y + vy_i * dt
        data[X].append(x_i)
        data[Y].append(y_i)
        data[VX].append(vx_i)
        data[VY].append(vy_i)


"""
Figure 4.6
"""


def fig4_6():
    N = 650
    dt = 0.002
    B_list = [2.10, 2.01]
    fig = plt.figure('Figure 4.6 Page 106')
    axs = fig.subplots(1, 2)
    fig.tight_layout(pad=5.0)
    i = 0

    for β in B_list:
        data.clear()
        data[X] = [1]
        data[Y] = [0]
        data[VX] = [0]
        #data[VY] = [2*math.pi]
        data[VY] = [4]
        main(N, β, dt)
        axs[i].axhline(y=0, color='k', linestyle=':')
        axs[i].axvline(x=0, color='k', linestyle=':')
        #axs[i].axhline(x=0, color='k', linestyle=':')

        axs[i].plot(data[X], data[Y], color='k',
                    linestyle=':', label='β = '+str(β), )

        axs[i].set_xlabel('x (AU)')
        axs[i].set_ylabel('y (AU)')
        axs[i].set_title('Simulation of elliptical orbit')
        axs[i].legend(loc='upper left')
        axs[i].set_xlim([-1, 1])
        axs[i].set_ylim([-1, 1])
        i += 1
    plt.show()


def ex4_8():
    N = 2000
    β = 2.0

    #name, AU, T, dt
    initilizers = [('Venus', 0.72, 0.610, 0.001), ('Earth', 1, 0.9989, 0.001), ('Mars', 1.52, 1.878, 0.001), ('Jupiter', 5.20, 11.916, 0.01), ('Saturn', 9.54, 29.289, 0.1)]
    elliptical = [('Elliptical Orbit 1', 4, 1, 0.002, 2),('Elliptical Orbit 2', 8, 1, 0.002,2),('Elliptical Orbit 3', 4, 1, 0.002, 1.15), ('Elliptical Orbit 4', 8, 1, 0.05,2.15), ('Elliptical Orbit 5', 5, 2, 0.002,2)]
    fig = plt.figure('Exercise 4.8', figsize=(23,8), dpi=80)
    fig.subplots_adjust(wspace=0.6,hspace=0.3)
    axs = fig.subplots(2, 5)
    i = 0
    for planet in initilizers:
        data.clear()
        data[X] = [planet[1]]
        data[Y] = [0]
        data[VX] = [0]
        data[VY] = [2* math.pi * (planet[1]/planet[2])]
        dt = planet[3]
        main(N, β, dt)
        axs[0][i].set_title(planet[0])
        axs[0][i].plot(data[X], data[Y], 'k', linestyle='-', label='T²/a³ = '+str(round(planet[2]**2/planet[1]**3,3)))
        axs[0][i].legend(bbox_to_anchor=(0,1.02,1,0.2), loc="upper left")
        axs[0][i].axhline(y=0, color='k', linestyle=':')
        axs[0][i].axvline(x=0, color='k', linestyle=':')
        i += 1
    N = 2500
    i = 0
    for planet in elliptical:
        data.clear()
        data[X] = [1]
        data[Y] = [0]
        data[VX] = [0]
        data[VY] = [(planet[1]/planet[2])]
        dt = planet[3]
        main(N, planet[4], dt)
        axs[1][i].set_title(planet[0])
        axs[1][i].plot(data[X], data[Y], 'k', linestyle='-', label='T²/a³ = '+str(round(planet[2]**2/planet[1]**3,3)))
        axs[1][i].legend(bbox_to_anchor=(0,1.02,1,0.2), loc="upper left")
        axs[1][i].axhline(y=0, color='k', linestyle=':')
        axs[1][i].axvline(x=0, color='k', linestyle=':')
        i += 1

    plt.show()


if __name__ == '__main__':
    data = dict()
    #fig4_6()
    ex4_8()
