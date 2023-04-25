import matplotlib.pyplot as plt
import time
from DaC import MatrixChainOrderDaC
from PrograDinamica import MatrixChainOrderPD

# Valores de entrada
pruebas = [
    [10, 20, 50, 60, 70],
    [12, 23, 23, 5, 10, 15],
    [12, 23, 12, 3, 7, 9, 13],
    [1, 4, 2, 2, 3, 5, 7, 11],
    [56, 45, 56, 34, 8, 12, 16, 20, 24],
    [12, 23, 23, 23, 4, 7, 10, 13, 16, 19],
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121],
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91],
    [32, 23, 23, 123, 23, 23, 32, 12, 34, 34, 100, 12, 32],
    [12, 25, 25, 125, 23, 23, 32, 12, 34, 34, 100, 15, 34, 56],
    [12, 25, 25, 125, 23, 23, 32, 12, 34, 34, 100, 15, 34, 56, 34],
    [12, 25, 25, 125, 23, 23, 32, 12, 34, 34, 100, 15, 34, 56, 35, 100],
    [12, 25, 25, 125, 23, 23, 32, 12, 34, 34, 100, 15, 34, 56, 54, 102, 123],
    [12, 25, 25, 125, 23, 23, 32, 12, 34, 34, 100, 15, 34, 56, 54, 102, 123, 122],
    [12, 25, 25, 125, 23, 23, 32, 12, 34, 34,
        100, 15, 34, 56, 54, 102, 123, 102, 140],

]

dac_times = []

for prueba in pruebas:
    n = len(prueba)
    start_time = time.time()
    # Llama a la función MatrixChainOrder y muestra el resultado
    cantidad = MatrixChainOrderDaC(prueba, 1, n - 1)
    end_time = time.time()
    time_elapsed = end_time - start_time
    print(cantidad, time_elapsed)
    dac_times.append(time_elapsed)


pd_times = []

for prueba in pruebas:
    n = len(prueba)
    start_time = time.time()
    # Llama a la función MatrixChainOrder y muestra el resultado
    cantidad = MatrixChainOrderPD(prueba, n)
    end_time = time.time()
    time_elapsed = end_time - start_time
    print(cantidad, time_elapsed)
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
