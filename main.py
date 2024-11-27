from src.models import AHP_SORT

if __name__ == '__main__':
    path_data = './data/crimenes_andalucia_norm.xlsx'
    path_criterios = './data/Comp_criterios.xlsx'
    path_classes = './data/Clases.xlsx'
    # C --> R --> V --> O --> D
    path_prioridades = ['./data/Prioridades/PC_Crimenes_Norm.xlsx',
                        './data/Prioridades/PC_Robos_Norm.xlsx',
                        './data/Prioridades/PC_VEHICULOS_Norm.xlsx',
                        './data/Prioridades/PC_ORDEN_Norm.xlsx',
                        './data/Prioridades/PC_DROGAS_Norm.xlsx',
                        ]

    path_result = './results/ejercicio2.xlsx'
    ahp_sort = AHP_SORT(path_data, path_criterios, path_classes, path_prioridades)
    result = ahp_sort.apply(path_result)

    print(result.to_string(index=False))
