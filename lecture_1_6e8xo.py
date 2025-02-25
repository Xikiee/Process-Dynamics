# import numpy as np
# import sympy as sp
# s, t = sp.symbols('s t')
# trans_func = 1/((s+0.2+0.5j)*(s+0.2-0.5j))
# result = sp.inverse_laplace_transform(trans_func, s, t)

# print(result)


import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the ODE system
def ode_system(t, y):
    dydt = y[1]
    d2ydt2 = -2 * y[1] - 2 * y[0] + 1  # g(t) = 1
    return [dydt, d2ydt2]

# Initial conditions
y0 = [2, -3/2]  # y(0) = 2, dy/dt(0) = -3/2

# Time span for the solution
t_span = (0, 10)  # from t=0 to t=10

# Solve the ODE
sol = solve_ivp(ode_system, t_span, y0, t_eval=np.linspace(0, 10, 1000))

# Plot the solution
plt.plot(sol.t, sol.y[0], label='y(t)')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solution of the ODE with g(t) = 1')
plt.legend()
plt.grid()
plt.show()