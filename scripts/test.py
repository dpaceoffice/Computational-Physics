import math

m=0.145
v_i = 50.512
#inital angle
angle_i = 0.6109
#Drag Velocity
v_drag = 35
#Delta
delta = 5
#inital velocity x component
v_x = v_i * math.cos(angle_i)
#inital velocity y component
v_y = v_i * math.sin(angle_i)
v = math.sqrt(v_x**2 + v_y**2)
B = (0.0039 + 0.0058/(1+math.exp((v - v_drag)/delta))) * m
print(str(B))