#Question
#One mole of an ideal gas with Cp = (7/2)R and Cv = (512) R expands from PI = 8 bar and Tl = 600 K to P2 = 1 bar by each of the following paths:
# (a) Constant volume; (b) Constant temperature; (c) Adiabatically.
# Assuming mechanical reversibility, calculate W, Q, ΔU, and ΔH for each process.
# Sketch each path on a single P V diagram.
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
import math
print("Enter the values of Cp and Cv as a multiple of R")
Cp= float(input())
Cv= float(input())
T1= int(input("Enter the initial value of temperature in Kelvin  "))
P1= int(input("Enter the initial value of pressure in Bar  "))
P2= int(input("Enter the final value of pressure in Bar  "))
print("1) Expansion by keeping volume constant:-\n")
print("As V is constant therefore, PdV is 0. Work Done= 0\n")
print("Calculating Final temperature by using P1/T1 = P2/T2")
T2=P2*T1/P1
print("Final temperature is", T2, "K \n")
print("The volume is R.T1/P1")
V1=8.314*T1/P1
print("V =", V1, "\n")
print("Heat is, \nQ = Cv(T2-T1)")
Q=Cv*8.314*(T2-T1)
print("Q =", Q, "J \n")
print("Change in Internal Energy U is,\nΔU = Q+W")
U=Q+0
print("ΔU =", U, "J \n")
print("Change in Enthalpy H is,\nΔH = Q+ VΔP")
H=Q+(V1*(P2-P1))
print("ΔH =", H, "J\n")
print("2) Expansion by keeping temperature constant:-\n")
print("The work done W = nRTln(P2/P1)")
W= 8.314*T1*math.log(P2/P1)
print("W =", W, "J\n")
print("As the temperature is constant, dT=0\nTherefore, ∆U = ∆H = 0 J\n")
U=0
print("The heat change is given by,\nQ = ∆U-W")
Q=U-W
print("Q =", Q, "J\n")
print("3) Expansion Adiabatically:-\n")
print("Finding the final temperature,\nT2=T1(P2/P1)^γ-1/γ")
gamma=Cp/Cv
T2=T1*(P2/P1)**((gamma-1)/gamma)
print("T2 =", T2, "K\n")
print("In adiabatic process the change in heat is 0,\nTherefore, Q = 0")
print("Q = ∆U-W\n∆U = W")
print("Internal energy is equal to work done which is given by,")
print("∆U = W = PdV = nR(T2 - T1)/γ-1")
W=8.314*(T2-T1)/(gamma-1)
U=W
print("∆U = W =", W, "J\n")
print("The Enthalpy of the process H is,\n∆H = nCp∆T")
H=Cp*8.314*(T2-T1)
print("ΔH =", H, "J\n")
x11=[V1,V1]
y11=[P1,P2]
plt.plot(x11,y11, label="Constant Volume")
y = np.linspace(P1, P2) 
x = 8.314*T1/y
plt.plot(x, y, label="Constant Temperature") 
y1 = np.linspace(P1, P2) 
x1 = (P1*(V1**gamma)/y1)**(1/gamma)
plt.plot(x1, y1, label="Adiabatic") 
plt.xlabel('Volume')
plt.ylabel('Pressue')
plt.title("Graph")
plt.legend()
