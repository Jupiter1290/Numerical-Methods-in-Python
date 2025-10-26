import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Defining the linear model:
def linear_model(t,a,b):  
    return (a*t+b)
#Defining the cubic model:
def cubic_model(t,l,m,n,o):
    return(l*pow(t,3)+m*pow(t,2)+n*t+o)
def biquadratic_model(t,d,e,f,g,h):
    return(d*pow(t,4)+e*pow(t,3)+f*pow(t,2)+g*t+h)
#Dedfining a functiion to calculate the residual:
def residual(cp_dat,modelledVal):
    return abs(cp_dat-modelledVal)


#Function to read the data from the file:
def read_file():
    #Initialising empty arrays for temperatures/Cp
    temp=[]
    cp=[]
    for el in open("data","r"):
        values=el.split(",")
        temp.append(float(values[0]))
        cp.append(float(values[1]))
    return [temp,cp]
#Reading the data from the supplied file:
temp,cp=read_file()  
params_linear,covar_linear=curve_fit(linear_model,temp,cp)
#'params_linear' are the optimised parameters obtained from the curve fitting using the linear function
#'covar_linear' is the resulting covariance matrix
fit_linear=linear_model(np.array(temp),*params_linear)  #fit_linear will be an 'ndarray'
params_cubic,covar_cubic=curve_fit(cubic_model,temp,cp)
#'params_cubic' are the optimised parameters obtained from the curve fitting using the cubic function
#'covar_cubic' is the resulting covariance matrix
fit_cubic=cubic_model(np.array(temp),*params_cubic)  #fit_cubic will be an 'ndarray'
params_biquadratic,covar_biquadratic=curve_fit(biquadratic_model,temp,cp)
#'params_cubic' are the optimised parameters obtained from the curve fitting using the cubic function
#'covar_cubic' is the resulting covariance matrix
fit_biquadratic=biquadratic_model(np.array(temp),*params_biquadratic)  #fit_quadratic will be an 'ndarray'

#calculating residuals:(an empirical way to measure how good the fitting is)
residual_linear=residual(np.array(cp),np.array(fit_linear))
residual_cubic=residual(np.array(cp),np.array(fit_cubic))
residual_biquadratic=residual(np.array(cp),np.array(fit_biquadratic))

#Plotting the actual data with the fitted curves;
plt.figure()
plt.plot(temp,cp,color='blue')
plt.plot(temp,fit_linear,color='red')
plt.title("Fitted Curves (using Linear Model) vs Actual Data")
plt.xlabel("Temperatures")
plt.ylabel("C_p")
plt.legend(['Actual Data','Linear Model'])
plt.show()

plt.figure()
plt.plot(temp,cp,color='blue')
plt.plot(temp,fit_cubic,color='green')
plt.title("Fitted Curves (using Cubic Model) vs Actual Data")
plt.xlabel("Temperatures")
plt.ylabel("C_p")
plt.legend(['Actual Data','Cubic Model'])
plt.show()

plt.figure()
plt.plot(temp,cp,color='blue')
plt.plot(temp,fit_biquadratic,color='yellow')
plt.title("Fitted Curves (using Biquadratic Model) vs Actual Data")
plt.xlabel("Temperatures")
plt.ylabel("C_p")
plt.legend(['Actual Data','Biquadratic Model'])
plt.show()

plt.figure()
plt.plot(temp,residual_linear,color='red')
plt.plot(temp,residual_cubic,color='green')
plt.plot(temp,residual_biquadratic,color='yellow')
plt.title("Residuals")
plt.xlabel("Temperatures")
plt.ylabel("Residuals")
plt.legend(['Linear Model','Cubic Model','Biquadratic Model'])
plt.show()

