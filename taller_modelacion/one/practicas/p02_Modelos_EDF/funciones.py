import matplotlib.pyplot as plt

from math_core.base.operaciones import arange, linspace
from math_core.ode.euler_method import euler_solve
from recurrencias import crec_exp, logistica, lineal, simp, solucion


# Las funciones en recurrencias.py probablemente reciben y como escalar,
# pero euler_sistemas siempre pasa y como lista.
# Este wrapper convierte y[0] -> escalar para compatibilidad.
def wrap(f):
    return lambda t, y: f(t, y[0])


# Ejercicio 1
def grafica1():
    x = list(range(50))
    k_valores = [2, 1, 0.5, -0.5, -1, -2]

    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    ejes = axs.flatten()

    for i, k in enumerate(k_valores):
        datos_y = crec_exp(k)
        ejes[i].scatter(x, datos_y, s=10, color='red')
        ejes[i].plot(x, datos_y, color='blue', linewidth=1)
        ejes[i].set_title(f'comportamiento con k={k}')
        ejes[i].grid(True)

        if k == 2 or k == 0.5:
            ejes[i].set_yscale('log')
        elif k < 0:
            ejes[i].set_yscale('symlog', linthresh=0.1)

        if k == -2:
            ejes[i].set_ylim(-2e30, 2e30)

    plt.tight_layout()
    plt.show()


# Ejercicio 2
def grafica2():
    x = list(range(41))
    valores_iniciales = [5, 1000, 1500]

    fig, axs = plt.subplots(3, figsize=(10, 12), sharex=True, sharey=True)
    ejes = axs.flatten()

    for i, po in enumerate(valores_iniciales):
        _, resultado = euler_solve([wrap(logistica)], [float(po)], 0, 39, 1)
        valores = resultado[0]  # resultado[0] es la primera (y única) ecuacion

        ejes[i].plot(x, valores, color='black', linewidth=1)
        ejes[i].scatter(x, valores, color='red', s=12)
        ejes[i].set_title(f'comportamiento con Po={po}')
        ejes[i].grid()

    plt.tight_layout()
    plt.show()


# Ejercicio 3
def grafica3():
    x = list(range(21))
    r = [0.5, 1, 1, 2]
    b = [2, 1, 0, 2]

    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    ejes = axs.flatten()

    for i in range(len(r)):
        valores = lineal(r[i], b[i])
        ejes[i].scatter(x, valores, c='red')
        ejes[i].plot(x, valores, c='black')
        ejes[i].set_title(f'comportamiento con r={r[i]} y b={b[i]}')
        ejes[i].grid()

    plt.tight_layout()
    plt.show()


# Ejercicio 4
def grafica4():
    deltas = [0.5, 1, 5, 20]

    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    ejes = axs.flatten()

    for i, delta in enumerate(deltas):
        tiempo = delta * 20
        tiempos, resultado = euler_solve([wrap(simp)], [2.0], 0, tiempo, delta)
        valores = resultado[0]  # primera (y única) ecuacion

        # Solucion continua real
        t_cont = linspace(0, tiempo, 200)
        v_real = [solucion(t) for t in t_cont]

        ejes[i].plot(t_cont, v_real, color='blue', label='Solución Real',
                     alpha=0.6, linewidth=2)
        ejes[i].plot(tiempos, valores, color='black', label='Euler', linewidth=1)
        ejes[i].scatter(tiempos, valores, c='red', s=12)
        ejes[i].set_title(f'Delta = {delta} | Rango [0, {tiempo}]')
        ejes[i].grid(True, linestyle='--', alpha=0.7)
        ejes[i].legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    grafica1()
    grafica2()
    grafica3()
    grafica4()