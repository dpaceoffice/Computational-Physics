import matplotlib.pyplot as plt
import math

W = 0
THETA = 1
TIME = 2
N = 250000


def main():
    for i in range(0, N):
        w_i = data[i][W] + (-(g/l) * math.sin(data[i][THETA]) -
                            q*data[i][W] +
                            F * math.sin(Ω * data[i][TIME])) * dt
        θ_i = data[i][THETA] + w_i * dt
        if(θ_i < -math.pi):
            θ_i = θ_i + 2*math.pi
        elif(θ_i > math.pi):
            θ_i = θ_i - 2*math.pi

        t_i = data[i][TIME] + dt
        data[i + 1] = [w_i, θ_i, t_i]


def plot(x, y, title, labelx, labely, style='-', legendLabel=FileNotFoundError):
    if(labelx is not None):
        plt.xlabel(labelx)
    if(labely is not None):
        plt.ylabel(labely)
    if(title is not None):
        plt.title(title)
    line = plt.plot(x, y, style, label=legendLabel, color='k')
    if(legendLabel is not None):
        plt.legend()
    return line


if __name__ == '__main__':
    ω_i = 0
    θ = [0.05, 0.2, 0.4, 0.6]
    t = 0
    g = 9.8
    l = 9.8
    dt = 0.04

    # Amplitude
    F = 1.2
    # Angular Frequency
    Ω = (2/3)
    # strength of damping
    q = 0.5

    data = dict()
    fig, ax = plt.subplots(2, 2)
    j = 0
    for each in θ:
        data.clear()
        data[0] = [ω_i, each, t]
        main()

        ω = []
        theta = []
        i = 0
        for key in data.keys():
            rem = data[key][TIME] - (2*i*math.pi/Ω)
            if(abs(rem) <= dt):
                ω.append(data[key][W])
                theta.append(data[key][THETA])
                i += 1
        label = 'Intial θ = '+str(each)+''
        if(j == 0):
            entry = (0, 0)
        elif(j == 1):
            entry = (0, 1)
        elif(j == 2):
            entry = (1, 0)
        elif(j == 3):
            entry = (1, 1)
        ax[entry].set_ylim(-2, 1)
        ax[entry].set_xlim(-4, 4)
        ax[entry].set_ylabel('ω (radians/s)')
        ax[entry].set_xlabel('θ (radians)')
        ax[entry].scatter(theta, ω, 2, 'k', marker=".")
        ax[entry].set_title(label)
        j += 1
    for a in ax.flat:
        a.label_outer()
    plt.show()
