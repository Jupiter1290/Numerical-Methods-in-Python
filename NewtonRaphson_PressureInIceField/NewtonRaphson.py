import math
import numpy as np
import matplotlib.pyplot as plt
#Supplied function:
def funct(p,h,beta,sigma,r):
    term1=pow(p,3)*(1-pow(beta,2))
    term2=((0.4*h*pow(beta,2))-((sigma*pow(h,2))/pow(r,2)))*(pow(p,2))
    term3=((pow(sigma,2)*pow(h,4))/(3*pow(r,4)))*p
    term4=pow(((sigma*pow(h,2))/(3*pow(r,2))),3)
    return (term1+term2+term3-term4)
#Derivative of the supplied function:
def functPrime(p,h,beta,sigma,r):
    term1=3*pow(p,2)*(1-pow(beta,2))
    term2=(0.4*h*(pow(beta,2))-(sigma*pow(h,2))/pow(r,2))*(2*p)
    term3=((pow(sigma,2)*pow(h,4))/(3*pow(r,4)))
    return (term1+term2+term3)


#Function that utilises the Newton-Raphson method to find the roots:
#[As we must solve for funct(p)=0:
#Newtons-Raphson's method can be employed to find the roots of functPrime()=0]
def findRoots(alpha,tol,p,h,beta,sigma,r):
    iter=1
    while (abs(funct(p,h,beta,sigma,r))>tol):
        p=p-alpha*((funct(p,h,beta,sigma,r))/(functPrime(p,h,beta,sigma,r)))
        print("Iteration: ",iter,"; pressure: ",p)
        iter+=1
    return p,iter-1

#Given Inputs:
beta=0.5
sigma=(150*144) #to convert to pounds per sq. foot
r=40
h=0.6
# alpha=1.3
p_guess=90
tol=1e-5
params=(p_guess,h,beta,sigma,r)

alpha=np.linspace(0.1,1.8,20)
iterations=[]
pr=[]
for el in alpha:
    p,iter=findRoots(el,tol,*(params))
    iterations.append(int(iter))
    pr.append(float(p))
print(iterations)
print(pr)
plt.figure()
plt.plot(alpha,iterations)
plt.title("Iterations vs Alpha")
plt.xlabel("Alpha (Relaxation factor)")
plt.ylabel("Iterations") 
plt.show()   

iter,p=findRoots(1,tol,*(params))
print(iter,p)

#To plot the "Minimum Pressures vs Height" graph
#(The chosen value of the relaxation factor is '1' as the above plot tells us that it requires the least iterations.)
heights = [0.6,1.2,1.8,2.4,3,3.6,4.2] 
p_min=[] #initializing an empty array fro  minimum pressures:
it_required=[]
for ht in heights:
    p_temp,it=findRoots(1,tol,p_guess,ht,beta,sigma,r)
    p_min.append(float(p_temp))
    it_required.append(it)
#To print the number of iterations needed for each value of height 'h':
for i in range(0,len(heights)-1):
    print("Iterations needed for height '",heights[i],"ft.' -> ",it_required[i])
    

plt.figure()
plt.plot(heights,p_min)
plt.xlabel("Height (in ft.)")
plt.ylabel("Minimum Pressure (in pounds/sq.ft.)")
plt.title("Minimum Pressures vs Height")
plt.show()
    



