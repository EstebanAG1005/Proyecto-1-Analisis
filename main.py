import matplotlib.pyplot as plt
import time
from DaC import MatrixChainOrderDaC
from PrograDinamica import MatrixChainOrderPD

# Valores de entrada
pruebas = [
    [10, 20, 50, 60, 70, 80, 90, 100, 110, 120,
        130, 140, 150, 160],
    [12, 23, 23, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
        12, 23, 23, 5, 10, 15, 20],
    [12, 23, 12, 3, 7, 9, 13, 19, 21, 27, 31, 37, 39, 43, 47,
        12, 23, 12, 3, 7, 9, 13, 19],
    [1, 4, 2, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 1,
        4, 2, 2, 3, 5, 7, 11, 13, 17],
    [56, 45, 56, 34, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56,
        56, 45, 56, 34, 8, 12, 16, 20],
    [12, 23, 23, 23, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43,
        12, 23, 23, 23, 4, 7, 10, 13, 16],
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 200, 23, 23, 1,
        4, 9, 16, 25, 36, 49, 64, 81, 100],
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120,
        1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
]

dac_times = []

for prueba in pruebas:
    n = len(prueba)
    start_time = time.time()
    # Llama a la función MatrixChainOrder y muestra el resultado
    cantidad = MatrixChainOrderDaC(prueba, 1, n - 1)
    end_time = time.time()
    time_elapsed = end_time - start_time

    dac_times.append(time_elapsed)


pd_times = []

for prueba in pruebas:
    n = len(prueba)
    start_time = time.time()
    # Llama a la función MatrixChainOrder y muestra el resultado
    cantidad = MatrixChainOrderPD(prueba, n)
    end_time = time.time()
    time_elapsed = end_time - start_time
    pd_times.append(time_elapsed)

# Código para calcular las listas dac_times y pd_times
dac_times = [round(time, 4) for time in dac_times]
dac_times.sort()
print("Tiempos DaC: ", dac_times)

pd_times = [round(time, 4) for time in pd_times]
pd_times.sort()
print("Tiempos PD: ", pd_times)

plt.plot(dac_times, label='DaC')
plt.plot(pd_times, label='PD')
plt.xlabel('Número de prueba')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.show()
