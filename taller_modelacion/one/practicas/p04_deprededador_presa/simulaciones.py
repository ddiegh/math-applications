#en este archivo se hace las resoluciones de los ejercicios, donde se grafican los datos 
#importamos el solucionador y algunas cosas que ocupamos 

from math_core.ode.euler_method import euler_solve
from models import conejos, zorros
import matplotlib.pyplot as plt


def graficas(t, valores: list, a, b):
    Cn = valores[0]
    Zn = valores[1]

    fig, axs = plt.subplots(3, 1, figsize=(8, 8))

    axs[0].plot(t, Cn, c='green')
    axs[0].set_title('Conejos a través del tiempo')
    axs[0].set_xlabel('Tiempo (t)')
    axs[0].set_ylabel('Conejos ($C_n$)')

    axs[1].plot(t, Zn, c='orange')
    axs[1].set_title('Zorros a través del tiempo')
    axs[1].set_xlabel('Tiempo (t)')
    axs[1].set_ylabel('Zorros ($Z_n$)')

    axs[2].plot(Cn, Zn, c='blue')
    axs[2].set_title('Retrato de fase')
    axs[2].set_xlabel('Conejos ($C_n$)')
    axs[2].set_ylabel('Zorros ($Z_n$)')
    axs[2].scatter(a, b, c='red', label='punto de equilibrio')
    axs[2].legend()

    plt.tight_layout()
    plt.show()


v1 = dict(r=0.08, c=0.1, b=0.01, d=0.15, n=100, co=0.2, zo=0.9)
v2 = dict(r=0.25, c=1.8, b=0.91, d=0.6, n=1000, co=0.2, zo=0.5)
v3 = dict(r=0.25, c=1.1, b=0.95, d=0.55, n=300, co=0.2, zo=0.5)

for v in [v1, v2, v3]:
    cn = conejos(v['r'], v['b'])
    zn = zorros(v['d'], v['c'])

    a = v['d'] / v['c']
    b = (v['r'] * (v['c'] - v['d'])) / (v['b'] * v['c'])

    t, valores = euler_solve([cn, zn], [v['co'], v['zo']], 0, v['n'], 1)
    graficas(t, valores, a, b)