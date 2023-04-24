import sys
import time


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
            # Calcula el costo adicional de multiplicar las matrices
            + p[i - 1] * p[k] * p[j]
        )

        # Actualiza el mínimo número de multiplicaciones si es necesario (Combine)
        if count < _min:
            _min = count

    return _min  # Retorna el mínimo número de multiplicaciones


if __name__ == "__main__":
    # Lista de dimensiones de matrices
    arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
           55, 60, 65, 70, 75, 80, 85]
    n = len(arr)

    start_time = time.time()
    # Llama a la función MatrixChainOrder y muestra el resultado
    cantidad = MatrixChainOrder(arr, 1, n - 1)
    end_time = time.time()

    time_elapsed = end_time - start_time
    print("\nTiempo de ejecución para el algoritmo DaC: ", time_elapsed)
    print("\nCantidad minima de multiplicaiones ", cantidad)

# This code is contributed by Aryan Garg

# Modified by MarianoReyes & EstebanAG1005
