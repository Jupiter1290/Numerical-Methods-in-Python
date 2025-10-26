#Code to calculate the Drag Force experienced by a bicyclist:
import math
import numpy as np
import matplotlib.pyplot as plt
#Inputs:
cd=0.8 #Coefficient of drag
A=0.1 #Frontal Area
rho=1.2 #Density
v_ndarray=np.linspace(1,20,20)
v=v_ndarray.tolist()
print(type(v),v)
#Initialising an empty list for 'dragForce':
dragForce=[]

for el in v:
    temp=0.5*rho*el*el*A*cd
    dragForce.append(temp)

plt.plot(v,dragForce)
plt.title("Drag Forces vs Velocities")
plt.xlabel("Velocity (in m/s)")
plt.ylabel("Drag Force (in N)")
plt.savefig("DFvsV") #To save the plot
plt.show() #The plot is expected to be parabolic

#Code to study the variation of drag force with the coefficient of drag:(linear realtionship expected)
velocity=15
cd_2_ndarray=np.linspace(0.1,0.99,25)
cd_2=cd_2_ndarray.tolist()
#initialising an empty array for drag_forces:
drag_forces=[]
for k in cd_2:
    tem=0.5*rho*k*velocity*velocity*A
    drag_forces.append(tem)

plt.plot(cd_2,drag_forces)
plt.title("Drag Force vs Coefficient of Drag (at constant velocity=15m/s)")
plt.xlabel("Cd (dimensionless)")
plt.ylabel("Drag Forces (in N)")
plt.savefig("DFvsCd") #To save the plot
plt.show()



