from scipy.integrate import trapezoid
import matplotlib.pyplot as plt
import sys
lct=1
rpm=1500 #given data
fuel_cons=20*pow(10,-9)
stroke_cycle=(rpm/60)*0.5
for line in open("engine_data.out","r"):
    if(lct>5 and lct<8671):
        if (len(line.split())!=17):
            print("File is not compatible...")
            sys.exit()
    lct+=1 
print("File is compatible")   

#Function to visualise data:
def plotData(c1,c2):
    lc=1 #Initialising line counter
    #Initialising empty arrays 
    c1_arr=[] 
    c2_arr=[] 
    for line in open("engine_data.out","r"):
        data_set=line.split()
        if (lc==3):
            ylab=str(data_set[c2])
            xlab=str(data_set[c1])
        if (lc>5):
            c1_arr.append(float(data_set[c1-1]))    #Must subtract '1'' from column numbers
            c2_arr.append(float(data_set[c2-1]))    #to get the indexing right
        lc+=1 
    #Plotting:        
    plt.plot(c1_arr,c2_arr)
    plt.xlabel(xlab) 
    plt.ylabel(ylab)
    plt.title(ylab+" vs "+xlab) 
    plt.show()

    

#Function to fetch data from the file:   
def fetchData(c1,c2):
    lc=1
    c1_arr=[]
    c2_arr=[]
    for line in open("engine_data.out","r"):
        data_set=line.split()
        if (lc==3):
            xlab=data_set[c1]
            ylab=data_set[c2]
        if (lc>5):
            c1_arr.append(float(data_set[c1-1]))    #Must subtract '1'' from column numbers
            c2_arr.append(float(data_set[c2-1]))    #to get the indexing right
        lc+=1    
    return [c1_arr,c2_arr,xlab,ylab]

plotData(8,2)   #calling the "plotData" function... 
plotData(1,8)
volume,pressure,x,y=fetchData(8,2)
area_pv=(trapezoid(pressure,volume))*pow(10,6)
print("Approximate area under the PV graph (using the trapezoid rule) ",area_pv,"Joule/Cycle")
power_output=area_pv*rpm/(2*60) #in watts
print("Power output is: ",power_output,"Watts")
sfc=((fuel_cons/power_output)*stroke_cycle)*3600*1000
print("Specific fuel consumption is ",sfc,"Kg/(kw*hr)")
    
         



