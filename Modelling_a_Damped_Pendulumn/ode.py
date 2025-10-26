import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt
import math

#funcyion that return d(theta)/dt:
def odefun(theta,t,b,g,l,m):
    theta1=theta[0]
    theta2=theta[1]
    dtheta1_dt=theta2
    dtheta2_dt=-(b/m)*theta2-(g/l)*math.sin(theta1)
    dtheta_dt=[dtheta1_dt,dtheta2_dt]
    return dtheta_dt

#Inputs:
b=0.05 #(damping constant)
g=9.81 #(acceleration due to gravity)
l=1 #length of pendulumn
m=0.1 #mass of pendulumn

#Initial Conditions:
theta_i=[0,3]

#time
t_ndarray=np.linspace(0,20,300) #To simulate till 30 seconds with 300 time-steps
t=t_ndarray.tolist() #Type setting to a list.


#Solving the ODE:
theta=odeint(odefun,theta_i,t,args=(b,g,l,m))

#Plotting;
plt.plot(t,theta[:,0],'b-',label=r'$\frac{d\theta_1}{dt}=\theta_2$')
plt.plot(t,theta[:,1],'r--',label=r'$\frac{d\theta_2}{dt}=-\frac{b}{m}\theta_2-\frac{g}{l}sin(\theta_1)$')
plt.legend(loc='lower right')
plt.title("Angular Position and Angular Velocity of a Damped Pendulumn as a Function of Time")
plt.xlabel("t (in sec)")
plt.show()



