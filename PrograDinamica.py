import sys
import time

# Tabla para almacenar resultados previamente calculados (memoización)
dp = [[-1 for i in range(100)] for j in range(100)]


def matrixChainMemoised(p, i, j):
    if i == j:  # Caso base: no hay multiplicación necesaria
        return 0

    if dp[i][j] != -1:  # Si el resultado ya ha sido calculado, retornarlo
        return dp[i][j]

    dp[i][j] = sys.maxsize  # Inicializa el mínimo número de multiplicaciones

    # Itera sobre todas las posiciones posibles para colocar un paréntesis
    for k in range(i, j):
        dp[i][j] = min(
            dp[i][j],
            matrixChainMemoised(p, i, k)
            + matrixChainMemoised(p, k + 1, j)
            + p[i - 1] * p[k] * p[j],
        )

    return dp[i][j]  # Retorna el mínimo número de multiplicaciones


def MatrixChainOrderPD(p, n):
    i = 1
    j = n - 1
    return matrixChainMemoised(p, i, j)  # Llama a la función con memoización


# Código del controlador
# Lista de dimensiones de matrices
arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
       55, 60, 65, 70, 75, 80, 85]
n = len(arr)

start_time = time.time()
cantidad = MatrixChainOrderPD(arr, n)
end_time = time.time()

time_elapsed = end_time - start_time
print("\nTiempo de ejecución para el algoritmo DaC: ", time_elapsed)
print("\nCantidad minima de multiplicaiones ", cantidad)

# This code is contributed by rag2127

# Modified by MarianoReyes & EstebanAG1005
