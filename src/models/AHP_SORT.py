import math

import numpy as np
import pandas
import pandas as pd

from ..utils import Reader, Eigenvalue


class AHP_SORT():
    def __init__(self, path_data, path_criterios, path_clases, paths_prioridades):
        """

        :param path_data:
        :param path_criterios:
        :param path_clases:
        :param paths_prioridades:

        :note El orden de los criterios es importante y debe ser el mismo en todos los datos
        """
        reader = Reader()
        print("Leyendo datos...")
        self.alternativas, self.criterios, self.data = reader.read_all(path_data)
        self.data_df = pd.DataFrame(self.data,index=self.alternativas,columns=self.criterios)
        self.priorities_criterios,self.priorities_criterios_df = reader.read(path_criterios)
        self.classes, self.classes_df = reader.read(path_clases)

        self.priorities_rp_cp = []
        self.priorities_rp_cp_df = []

        for path in paths_prioridades:

            val1 , val2 = reader.read(path)

            self.priorities_rp_cp.append(val1)
            self.priorities_rp_cp_df.append(val2)

        self.global_criterios = None
        self.global_classes = None
        self.global_alternatives = None

    def apply(self,name_result="./results/result.xlsx"):

        self.obtain_criterios_weights()
        self.obtain_classes_weights()
        self.obtain_priorities_alternatives()

        # Por cada alternativa, determinar su clase
        ranking = []

        for value_alt in self.global_alternatives:
            # Clasificación para extremos
            if value_alt >= self.global_classes[0]:
                ranking.append(1)
            elif value_alt <= self.global_classes[-1]:
                ranking.append(len(self.global_classes))
            else:
                # Clasificación para valores intermedios
                min_distance = float('inf')
                best_class = None
                for i in range(len(self.global_classes) - 1):
                    # Calcula la distancia a los dos valores consecutivos
                    dist_current = abs(value_alt - self.global_classes[i])
                    dist_next = abs(value_alt - self.global_classes[i + 1])

                    # Clasificación optimista
                    if dist_current <= dist_next and dist_current < min_distance:
                        best_class = i + 1
                        min_distance = dist_current
                    elif dist_next < dist_current and dist_next < min_distance:
                        best_class = i + 2
                        min_distance = dist_next

                # Asigna la clase encontrada
                ranking.append(best_class)

        result = {}
        result['Alternatives'] = self.alternativas
        global_alternatives = [value.real for value in self.global_alternatives]
        result['GlobalPriority'] = global_alternatives
        result['NivelSeguridad'] = ranking

        df = pandas.DataFrame(result)
        df.to_excel(name_result,index=False)
        return df

    def obtain_criterios_weights(self):
        print("Obteniendo pesos criterios...")
        e = Eigenvalue()
        eigenvalue, eigenvector_norm = e.obtain_eigenvector_normalized(self.priorities_criterios)
        self.priorities_criterios_df['Global'] = eigenvector_norm
        self.global_criterios = eigenvector_norm

    def obtain_classes_weights(self):
        print("Obteniendo pesos clases...")
        wclasses = []
        for row in self.classes:
            sum = 0.0
            for i, value in enumerate(row):
                sum += value * self.global_criterios[i]
            wclasses.append(sum.real)
        self.classes_df['Global'] = wclasses
        print(self.classes_df)
        self.global_classes = np.array(wclasses)

    def obtain_priorities_alternatives(self):
        print("Obteniendo prioridades globales de las alternativas...")
        alternatives_priorities = []

        for alternative in self.data:
            weight = 0
            for i, value in enumerate(alternative):
                p_j, p_j1, s_j, s_j1 = self.priority_alternative(i, value)
                if s_j != s_j1:
                    priority = p_j + ((p_j1 - p_j) / (s_j1 - s_j)) * (value - s_j)
                else:
                    priority = p_j

                weight += priority * self.global_criterios[i]

            alternatives_priorities.append(weight)
        self.data_df['Global'] = alternatives_priorities
        self.global_alternatives = np.array(alternatives_priorities)

    def priority_alternative(self, id_criterio, value_alternative):
        rp_cp_priorities = self.priorities_rp_cp[id_criterio]
        # Valores extremos para asegurar límites
        min_value = rp_cp_priorities[0][0]  # Mínimo valor en rp/cp
        max_value = rp_cp_priorities[-1][0]  # Máximo valor en rp/cp

        # Si value_alternative es menor que el mínimo, usamos los valores mínimos
        if value_alternative <= min_value:
            p_j = rp_cp_priorities[0][1]
            p_j1 = p_j  # Ambos son el mismo ya que no hay un rango menor
            s_j = min_value
            s_j1 = min_value  # Ambos son el mismo ya que no hay un rango menor
            return p_j, p_j1, s_j, s_j1

        # Si value_alternative es mayor que el máximo, usamos los valores máximos
        if value_alternative >= max_value:
            p_j = rp_cp_priorities[-1][1]
            p_j1 = p_j  # Ambos son el mismo ya que no hay un rango mayor
            s_j = max_value
            s_j1 = max_value  # Ambos son el mismo ya que no hay un rango mayor
            return p_j, p_j1, s_j, s_j1

        # Encontrar el valor rp/cp mayor que value_alternative
        indice = 0
        value = rp_cp_priorities[indice][0]

        while value_alternative >= value:
            indice += 1
            value = rp_cp_priorities[indice][0]

        # El valor cuyo índice es "indice" es el inmediatamente superior al valor_alternative
        anterior = indice - 1
        siguiente = indice

        # Obtenemos valores necesarios
        p_j = rp_cp_priorities[anterior][1]
        p_j1 = rp_cp_priorities[siguiente][1]

        s_j = rp_cp_priorities[anterior][0]
        s_j1 = rp_cp_priorities[siguiente][0]

        return p_j, p_j1, s_j, s_j1

