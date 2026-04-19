#En este archivo se encuentran las implementaciones de los modelos que ya construimos y el metodo de resolucion creando el cual importaremos 
from math_core.ode.euler_method import euler_solve 
from modelos import S, I, R, R_o
import matplotlib.pyplot as plt

if __name__ == "__main__":
    caso1 = [1000000, 127, 0, 1, 0.6, 150]
    caso2 = [100000, 200000, 0, 0.7, 0.5, 150]
    caso3 = [200000, 1000000, 0, 0.75, 0.5, 150]
    caso4 = [1000000, 10, 0, 0.75, 0.5, 100]
    # [So, Io, Ro, alfa, beta, iteraciones]
    casos = [caso1, caso2, caso3, caso4]

    for caso in casos:
        So, Io, Ro, alfa, beta, iteraciones = caso
        N = So + Io + Ro

        sistema = [S(alfa, N), I(alfa, N, beta), R(beta)]
        r0_valor = R_o(alfa, So, N, beta)

        tiempos, valores = euler_solve(sistema, [So, Io, Ro], 0, iteraciones, 1)
        # valores[0] = Susceptibles, valores[1] = Infectados, valores[2] = Recuperados

        plt.style.use('seaborn-v0_8-whitegrid')
        plt.figure(figsize=(12, 7))
        plt.plot(tiempos, valores[0], c='blue', label='Susceptibles', linewidth=2.5)
        plt.plot(tiempos, valores[1], c='red', label='Infectados', linewidth=2.5)
        plt.plot(tiempos, valores[2], c='green', label='Recuperados', linewidth=2.5)
        plt.legend(loc='upper right', fontsize=12, frameon=True, shadow=True)
        plt.text(
            0.05, 0.95, f'$R_0 = {r0_valor:.2f}$',
            transform=plt.gca().transAxes,
            fontsize=14, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5')
        )
        plt.title('Dinámica del Modelo Epidemiológico SIR', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Tiempo (días)', fontsize=13)
        plt.ylabel('Número de Individuos', fontsize=13)
        plt.margins(x=0.02)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

