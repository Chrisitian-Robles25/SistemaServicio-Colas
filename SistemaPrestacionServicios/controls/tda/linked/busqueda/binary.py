from controls.tda.linked.ordenacion.quickSort import QuickSort

class Binary:
    def search_binary(self, array, element):
        quickSort = QuickSort()
        array = quickSort.sort_primitive_ascendent(array)  # Ordenar el array
        
        left = 0
        right = len(array) - 1

        while left <= right:
            middle = (left + right) // 2  # Encontrar el índice medio
            if array[middle] == element:
                return middle  # Elemento encontrado
            elif array[middle] < element:
                left = middle + 1  # Buscar en la mitad derecha
            else:
                right = middle - 1  # Buscar en la mitad izquierda
                
        return -1
    """ def search_binary(self, array, element):
        quickSort = QuickSort()
        array = quickSort.sort_primitive_ascendent(array)
        left = 0
        right = len(array) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if array[middle] == element:
                return middle
            elif array[middle] < element:
                left = middle + 1
            else:
                right = middle - 1
        return -1 """
    
    
    def search_binary_models(self, array, element, attribute):
        quickSort = QuickSort()
        array = quickSort.sort_models_ascendent(array, attribute)
        left = 0
        right = len(array) - 1
        while left <= right:
            middle = (left + right) // 2
            if getattr(array[middle], attribute) == element:
                return middle
            elif getattr(array[middle], attribute) < element:
                left = middle + 1
            else:
                right = middle - 1
        return -1
    