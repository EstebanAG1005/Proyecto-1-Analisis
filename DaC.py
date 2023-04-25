import sys
import time


def MatrixChainOrderDaC(p, i, j):
    if i == j:  # Caso base: no hay multiplicación necesaria
        return 0

    _min = sys.maxsize  # Inicializa el mínimo número de multiplicaciones

    # Itera sobre todas las posiciones posibles para colocar un paréntesis (Divide)
    for k in range(i, j):
        # Resuelve subproblemas de manera recursiva (Conquer)
        count = (
            MatrixChainOrderDaC(p, i, k)
            + MatrixChainOrderDaC(p, k + 1, j)
            # Calcula el costo adicional de multiplicar las matrices
            + p[i - 1] * p[k] * p[j]
        )

        # Actualiza el mínimo número de multiplicaciones si es necesario (Combine)
        if count < _min:
            _min = count

    return _min  # Retorna el mínimo número de multiplicaciones


# This code is contributed by Aryan Garg

# Modified by MarianoReyes & EstebanAG1005
