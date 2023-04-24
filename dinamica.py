import sys

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

def MatrixChainOrder(p, n):
    i = 1
    j = n - 1
    return matrixChainMemoised(p, i, j)  # Llama a la función con memoización

# Código del controlador
arr = [1, 2, 3, 4, 3]  # Lista de dimensiones de matrices
n = len(arr)
print("Cantidad minima de multiplicaiones ", MatrixChainOrder(arr, n))
