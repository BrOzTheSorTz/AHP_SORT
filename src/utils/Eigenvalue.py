import numpy as np


class Eigenvalue:
    def __init__(self):

        self.columns = None
        self.rows = None
        self.matrix = None
        self.eigenvalue = None
        self.eigenvector = None
        self.priority_vector = None

    def max_nonnegative_eigenvalue(self, matrix):
        """
        Finds the largest non-negative, real eigenvalue and corresponding eigenvector.
        """
        self.matrix = matrix
        self.rows = np.shape(matrix)[0]
        self.columns = np.shape(matrix)[1]

        eigenvalues, eigenvectors = np.linalg.eig(self.matrix)

        # Filtrar autovalores no negativos y reales junto con sus eigenvectores correspondientes
        real_non_negative_eigenvalues = [(value.real, eigenvectors[:, i])
                                         for i, value in enumerate(eigenvalues)
                                         if value.imag == 0 and value.real >= 0]

        # Encontrar el mayor autovalor no negativo real
        if real_non_negative_eigenvalues:
            self.eigenvalue, self.eigenvector = max(real_non_negative_eigenvalues, key=lambda x: x[0])
        else:
            self.eigenvalue = None
            self.eigenvector = None

    def obtain_eigenvector_normalized(self, matrix):
        """
        Normalizes the principal eigenvector to obtain the priority vector (sums to 1).
        :return eigenvalue, eigenvector_norm
        """
        # Primero, calcular el mayor eigenvalor no negativo y su vector correspondiente
        self.max_nonnegative_eigenvalue(matrix)
        if self.eigenvector is not None:
            # Normalizar el eigenvector principal para obtener el vector de prioridades
            self.priority_vector = self.eigenvector / self.eigenvector.sum()
            print("Priority vector (normalized):", self.priority_vector)
            return self.eigenvalue,self.priority_vector
        else:
            print("No suitable eigenvalue found for priority calculation.")
            return None
