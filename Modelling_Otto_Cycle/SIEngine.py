import math
import numpy as np
import matplotlib.pyplot as plt

def volEng(bore,stroke,conRod,cr,start_crank,end_crank,div):
    a=stroke*0.5
    R=conRod/a
    v_s=math.pi/4*bore*bore*stroke #Swept volume of piston
    v_c=v_s/(cr-1) #Clearance volume

    # theta=math.radians(0)
    sc=math.radians(start_crank)
    ec=math.radians(end_crank)
    theta_ndarray=np.linspace(sc,ec,div)
    theta=theta_ndarray.tolist()
    v=[]
    for t in theta:
        term1=0.5*(cr-1)
        term2=R+1-math.cos(t)
        term3_temp=pow(R,2)-pow(math.sin(t),2)
        term3=pow(term3_temp,0.5)
        vol=(1+term1*(term2-term3))*v_c
        v.append(vol)
    return v        





#Engine parameters:
bore=0.1
stroke=0.1
conRod=0.15
gamma=1.4 #For air
v_s=math.pi/4*bore*bore*stroke #Swept volume of piston
cr=8
v_c=v_s/(cr-1) #Clearance volume

#inputs:
p1=101325
t1=500
v1=v_c+v_s
rhs=p1*v1/t1  #as it is a closed system, 'pv/t' will be constant throughout...
t3=2300  #Combution temperatures
div=50 #For resolution

#Point 2; (1->2 is an isentropic process)
v2=v_c
p2=p1*pow(v1,gamma)/pow(v2,gamma) #isentropic relationship
t2=(p2*v2)/rhs

#Point 3; (2->3 is an isochoric process of heat addition)
v3=v2
#t3 is already defined as the combution temp...
p3=rhs*t3/v3

#Point 4; (3->4 is an isentropic process of heat rejection)
v4=v1
p4=p3*pow(v3,gamma)/pow(v4,gamma)
t4=(p4*v4)/rhs


v_12=volEng(bore,stroke,conRod,cr,0,180,div)
v_34=volEng(bore,stroke,conRod,cr,180,0,div)
const_12=p1*pow(v1,gamma)
const_34=p3*pow(v3,gamma)
p_12=[]
p_34=[]

for el in v_12:
    p_12a=const_12/(pow(el,gamma))
    p_12.append(p_12a)
for elm in v_34:
    p_34a=const_34/(pow(elm,gamma))
    p_34.append(p_34a)
#Calculation of thermal efficiency:
neta_otto=1-1/(pow(cr,gamma-1))    
print("The thermal efficiency is ",neta_otto*100,"%.")

   
plt.plot([v2,v3],[p2,p3])
plt.plot([v4,v1],[p4,p1])
plt.plot(v_12,p_12)
plt.plot(v_34,p_34)
plt.xlabel("V")
plt.ylabel("P")
plt.title("PV Diagram for Otto cycle (Comp. Ratio=8)")
plt.show()
plt.savefig("OttoCycleCr8.png")
# plt.close()











