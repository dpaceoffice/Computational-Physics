import math
import matplotlib.pyplot as plt

"""
Keeps track of the variable's index stored in dictionary
"""
X = 0
Y = 1
VX = 2
VY = 3
N = 2000

"""
Calculates the magnitude of two vector componenets
"""
def magnitude(var1, var2):
    return math.sqrt(var1**2 + var2**2)

"""
Main function, iterates till y <= 0 or the instances calculated reaches N

The variable i usually means index in computer science, but it can be better understood physically as 'instance,' as in, an instance of dt
"""
def main():
    for i in range(0, N):
        #Get our variables value of i, starting at index 0
        x = data[i][X]
        y = data[i][Y]
        vx = data[i][VX]
        vy = data[i][VY]

        #calculate i + 1
        x_i = x + vx * dt
        y_i = y + vy * dt
        vx_i = vx 
        vy_i = vy - g * dt
        
        if(y_i <= 0):
            break
        data[i + 1] = [x_i,y_i,vx_i,vy_i]
"""
Generic plot function
"""
def plot(x, y, title, labelx, labely, style='-', legendLabel=None):
    if(labelx is not None):
        plt.xlabel(labelx)
    if(labely is not None):
        plt.ylabel(labely)
    if(title is not None):
        plt.title(title)
    if(legendLabel is None):
        legendLabel = title
    line = plt.plot(x,y,style,label=legendLabel)
    plt.legend()
    return line

"""
Initial declarations
"""
if __name__ == '__main__':
    x = 0 
    y = 0 
    v = 700.0 #m/s
    dt = 0.1 #s
    g = 9.81
    angles = [(55, '-'), (50, '--'), (45, '--'), (40,'-.'), (35,':'), (30,'-')]

    
    #Inital velocity components change depending on angle
    data = dict()
    for theta in angles:
        vx = (v * math.cos(theta[0] * (math.pi/180)))
        vy = (v * math.sin(theta[0] * (math.pi/180)))
        
        data.clear()    
        data[0] = [x,y,vx,vy]
        main()

        x_list = []
        y_list = []
        for key in data.keys():
            x_list.append(data[key][X] / 10 ** 3)
            y_list.append(data[key][Y] / 10 ** 3)
        plot(x_list,y_list, "Trajectory of a cannon shell", "x (km)", "y (km)",style=theta[1], legendLabel=''+str(theta[0])+'°')

    plt.ylim([0, 20])
    plt.xlim([0, 60])
    plt.show()

