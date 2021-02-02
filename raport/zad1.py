from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from scipy.optimize import fminbound
def function(t, x):
    return [ x[1], 10*x[0] -3*x[1] ]

y_a = 4 # Miejsce zerowe w punkcie y(0) = 4
dy = -2 # Miejssce zerowe w punkcie y'(0) = -2
t_p = 0 # Początek przedziału
t_k = 1 # Koniec przedziału

y0 = [y_a, dy]
t = np.arange(0, t_k, 0.001)

result = solve_ivp(function, [t_p, t_k], y0, t_eval=t ,atol=1e-10, rtol=13-8,method="LSODA")

plt.plot(result.t, result.y[0])
plt.plot(result.t, result.y[1])

plt.grid(color='darkgrey', linestyle='-', linewidth=0.5)
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(["LSODA","dy/dt(LSODA)" ])
plt.show()

extremum = argrelextrema(result.y[0], np.less)[0]
print("Ekstremum" ,result.t[extremum]) #extremum funkcji











from scipy.integrate import odeint







# def model(x,t):
#     y = x[0]
#     dy = x[1]
#
#     xdot = [[], []]
#     xdot[0] = dy
#     xdot[1] = -3*dy + 10*y
#     return xdot
#
# zakres = np.linspace(0, 1, 1000)
# z2 = odeint(model, [4, -2], zakres)
#
# plt.plot(zakres, z2[:, 0], 'g:')
# plt.plot(zakres, z2[:, 1], 'k-.')
#






# def fur1(t,y):
#     return [y[1], -3*y[1] + 10*y[0]]
# utest = [-25, -6, 0.5]
# y_a = 4
# t_k = 1
# y_b = -2
# for u in utest:
#     y0 =[y_a, u]
#     wu=solve_ivp(fur1, [0, t_k],y0, atol=1e-10, rtol=13-8)
#     napis = 'u=' + str(u)
#     plt.plot(wu.t, wu.y[0], label=napis)

# plt.plot([0, t_k], [y_a, y_b], 'o')
# plt.legend()



# def function(t, y):
#     return [ y[1], -3*y[1] + 10*y[0]]
#
# u = -2
# y_a = 4
# t_k = 1
#
# y0 = [y_a, u]
#
# wu = solve_ivp(function, [0, t_k], y0, atol=1e-10, rtol=13-8,method="LSODA")
#
# plt.plot(wu.t, wu.y[0])


# czyli dobrze
# def matiego(u,x):
#     return [u[1], -3 * u[1] + 10 * u[0]]
#
# y0 = [4, -2]
# xs = np.linspace(0,1,1000)
# us = odeint(matiego, y0,xs)
# ys = us[:, 0]
# plt.plot(xs, ys, '-')

#


