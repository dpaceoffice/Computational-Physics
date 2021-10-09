import matplotlib.pyplot as plt

W = 0
THETA = 1
TIME = 2
N = 10000

def main():
    for i in range(0, 2000):
        w_i = data[i][W] - (g/l)*data[i][THETA]*dt
        θ_i = data[i][THETA] + w_i * dt
        t_i = data[i][TIME] + dt
        data[i + 1] = [w_i, θ_i, t_i]

def plot(x, y, title, labelx, labely, style='-', legendLabel=None):
    if(labelx is not None):
        plt.xlabel(labelx)
    if(labely is not None):
        plt.ylabel(labely)
    if(title is not None):
        plt.title(title)
    line = plt.plot(x,y,style,label=legendLabel, color='k')
    if(legendLabel is not None):
        plt.legend()
    return line

if __name__ == '__main__':
    ω = 0
    θ = 0.2
    t = 0
    g = 9.81
    l = 1
    dt = 0.04
    data = dict()
    data[0] = [ω, θ, t]
    radians = []
    time = []
    main()
    for key in data.keys():
        radians.append(data[key][THETA])
        time.append(data[key][TIME])
    plot(time, radians, "Simple Pendulum - Euler-Cromer method", "times (s)", "θ (Radians)", legendLabel="Length = "+str(l)+" m  time step = "+str(dt)+"s")
    plt.xlim([0, 10])
    plt.ylim([-0.3, 0.3])
    plt.show()
    