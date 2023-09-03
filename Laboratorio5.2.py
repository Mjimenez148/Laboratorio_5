# Paso 1: Pedir al usuario que ingrese una serie de números separados por espacios.
numeros_str = input("Ingresa una serie de números separados por espacios: ")

# Paso 2: Divide la cadena ingresada en una lista de cadenas de números utilizando el método split().
numeros_str_lista = numeros_str.split()

# Paso 3: Convierte cada cadena en un número entero y almacénalos en una lista.
numeros_enteros = [int(num) for num in numeros_str_lista]

# Paso 4: Implementa el algoritmo de ordenamiento de selección para ordenar la lista de números.
def seleccion_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]

seleccion_sort(numeros_enteros)

# Paso 5: Imprime la lista ordenada.
print("Lista ordenada:", numeros_enteros)
