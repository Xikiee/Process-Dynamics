import numpy as np
import scipy as sp
import cmath
import math

#problem 1 complex numbers 
#question 1:
# (2+3i)(3+2i)
# (6+4i+9i-6)
#(13i)

z_1= (0+13j)
# print(z_1.real, z_1.imag)

#question 2:
#(2+4i)/(1+i)

z_2 = (2+4j)/(1+1j)

# print(z_2.real,z_2.imag)
# print(z_2)


#question 3:
# exp((-2pi/3) - i)
# cos(-2pi/3) + isin(-pi/3)
z_3 = math.cos((-2*math.pi)/3) + 1j*math.cos((-2*math.pi)/3)
# print(z_3)


#question 4:
#find the argument and the modulus

#q4 part a
#z = 4-2i

#finding mod
x_4a = 4 - 2j
x_4a_comp = 4 + 2j
z_4a = np.sqrt(x_4a*x_4a_comp)

#finding argument
z_4a_arg = np.arctan(-2/4)
# print(f"4a modulus is{z_4a}, and the argument is {z_4a_arg}")


#q4 part b

x_4b = (2+3j)/(4+5j)

z_4b_mod = np.sqrt(x_4b*np.conjugate(x_4b))
z_4b_arg = np.angle(x_4b)
# print(f"4b modulus is {z_4b_mod}, and the argument is {z_4b_arg}")


#question 5
# (1+i)^2011

x_5 = (1+1j)
x_5_mod = np.sqrt(x_5 * np.conjugate(x_5))
x_5_arg = np.angle(x_5)

z_5 = (x_5_mod**2011 * np.exp(1j*2011 * x_5_arg))
# print(f"ans to 5 is {z_5}")


#problem 2: Orginary Differential Equations

#part a
k = [1,5,4]
root = np.roots(k)
# print(f"The following are the roots {root}")

#part b 
kb = [1,1,-3,-5,-2]
root_b = np.roots(kb)
# print(f"the following are roots for b {root_b}")

#Problem 3 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt 

#part a

#solving the ode: 

def ode_solver(t, y):
    dy_dt = y[1]
    d2y_dt = 1 - 2*y[0] - 2*y[1]
    return dy_dt, d2y_dt

y0a = [2,-3/2]
t_span = (0,10)
t_eval = np.linspace(0,10,1000)
sola = solve_ivp(ode_solver, t_span, y0a, t_eval= t_eval)

# plt.plot(sola.t, sola.y[0])
# plt.show()


#part b 

def ode_solverb(t,y):
    dy_dt = y[1]
    d2y_dt = -2*y[0] - 2*y[1] + 1 + np.sin(t)
    return dy_dt, d2y_dt 


t_span = (0,20)
t_eval = np.linspace(0,20,2000)
sola = solve_ivp(ode_solverb, t_span, y0a, t_eval = t_eval)

plt.plot(sola.t, sola.y[0])
plt.show()



