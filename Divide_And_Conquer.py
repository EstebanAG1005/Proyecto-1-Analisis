import sys

def MatrixChainOrder(p, i, j):
    if i == j:  # Caso base: no hay multiplicación necesaria
        return 0

    _min = sys.maxsize  # Inicializa el mínimo número de multiplicaciones

    # Itera sobre todas las posiciones posibles para colocar un paréntesis (Divide)
    for k in range(i, j):
        # Resuelve subproblemas de manera recursiva (Conquer)
        count = (
            MatrixChainOrder(p, i, k)
            + MatrixChainOrder(p, k + 1, j)
            + p[i - 1] * p[k] * p[j]  # Calcula el costo adicional de multiplicar las matrices
        )

        if count < _min:  # Actualiza el mínimo número de multiplicaciones si es necesario (Combine)
            _min = count

    return _min  # Retorna el mínimo número de multiplicaciones

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 3]  # Lista de dimensiones de matrices
    N = len(arr)

    # Llama a la función MatrixChainOrder y muestra el resultado
    print("Cantidad minima de multiplicaiones ", MatrixChainOrder(arr, 1, N - 1))
