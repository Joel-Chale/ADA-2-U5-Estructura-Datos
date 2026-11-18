"""
Implementación de Métodos de Ordenamiento Avanzados en Python:
1. ShellSort
2. Quicksort
3. Heapsort
4. Radix Sort
"""


def shell_sort(arr):
    """Ordena una lista utilizando el algoritmo ShellSort por intervalos (gaps)."""
    datos = arr.copy()
    n = len(datos)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = datos[i]
            j = i
            while j >= gap and datos[j - gap] > temp:
                datos[j] = datos[j - gap]
                j -= gap
            datos[j] = temp
        gap //= 2

    return datos


def quick_sort(arr):
    """Ordena una lista utilizando el algoritmo Quicksort (Divide y Vencerás)."""
    if len(arr) <= 1:
        return arr.copy()

    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)


def _heapify(arr, n, i):
    """Mantiene la propiedad de Max-Heap en el subárbol con raíz en el índice i."""
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    if izquierda < n and arr[izquierda] > arr[mayor]:
        mayor = izquierda

    if derecha < n and arr[derecha] > arr[mayor]:
        mayor = derecha

    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        _heapify(arr, n, mayor)


def heap_sort(arr):
    """Ordena una lista utilizando un árbol binario Max-Heap (Heapsort)."""
    datos = arr.copy()
    n = len(datos)

    # Construcción del Max-Heap inicial
    for i in range(n // 2 - 1, -1, -1):
        _heapify(datos, n, i)

    # Extracción uno a uno de los elementos del montículo
    for i in range(n - 1, 0, -1):
        datos[0], datos[i] = datos[i], datos[0]
        _heapify(datos, i, 0)

    return datos


def _counting_sort_para_radix(arr, exp):
    """Counting Sort estable basado en el dígito representado por exp."""
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10

    for i in range(n):
        indice = (arr[i] // exp) % 10
        conteo[indice] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    for i in range(n - 1, -1, -1):
        indice = (arr[i] // exp) % 10
        salida[conteo[indice] - 1] = arr[i]
        conteo[indice] -= 1

    for i in range(n):
        arr[i] = salida[i]


def _radix_positivos(arr):
    """Aplica LSD Radix Sort a una lista de enteros no negativos."""
    if not arr:
        return []
    datos = arr.copy()
    maximo = max(datos)
    exp = 1
    while maximo // exp > 0:
        _counting_sort_para_radix(datos, exp)
        exp *= 10
    return datos


def radix_sort(arr):
    """Ordena números enteros (positivos y negativos) usando LSD Radix Sort."""
    if not arr:
        return []

    negativos = [-x for x in arr if x < 0]
    positivos = [x for x in arr if x >= 0]

    negativos_ordenados = [-x for x in reversed(_radix_positivos(negativos))]
    positivos_ordenados = _radix_positivos(positivos)

    return negativos_ordenados + positivos_ordenados


def solicitar_numeros():
    """Solicita al usuario la cantidad de números y captura cada elemento."""
    while True:
        try:
            cantidad = int(input("\nIngrese la cantidad de números a ordenar: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser un número entero mayor a 0.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    numeros = []
    print(f"Ingrese los {cantidad} números enteros:")
    for i in range(cantidad):
        while True:
            try:
                valor = int(input(f"  Elemento [{i + 1}/{cantidad}]: "))
                numeros.append(valor)
                break
            except ValueError:
                print("  Entrada inválida. Por favor, ingrese un número entero.")

    return numeros


def mostrar_menu():
    """Muestra las opciones del menú principal en consola."""
    print("\n" + "=" * 55)
    print("        MENÚ DE MÉTODOS DE ORDENAMIENTO EN PYTHON")
    print("=" * 55)
    print("1. Ordenar por ShellSort")
    print("2. Ordenar por Quicksort")
    print("3. Ordenar por Heapsort")
    print("4. Ordenar por Radix Sort")
    print("5. Ingresar una nueva lista de números")
    print("6. Salir")
    print("=" * 55)


def main():
    print("BIENVENIDO AL SISTEMA DE ORDENAMIENTO DE DATOS")
    numeros = solicitar_numeros()

    while True:
        mostrar_menu()
        print(f"Lista actual ({len(numeros)} elementos): {numeros}")
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            resultado = shell_sort(numeros)
            print("\n--- RESULTADO CON SHELLSORT ---")
            print(f"Lista original: {numeros}")
            print(f"Lista ordenada: {resultado}")

        elif opcion == "2":
            resultado = quick_sort(numeros)
            print("\n--- RESULTADO CON QUICKSORT ---")
            print(f"Lista original: {numeros}")
            print(f"Lista ordenada: {resultado}")

        elif opcion == "3":
            resultado = heap_sort(numeros)
            print("\n--- RESULTADO CON HEAPSORT ---")
            print(f"Lista original: {numeros}")
            print(f"Lista ordenada: {resultado}")

        elif opcion == "4":
            resultado = radix_sort(numeros)
            print("\n--- RESULTADO CON RADIX SORT ---")
            print(f"Lista original: {numeros}")
            print(f"Lista ordenada: {resultado}")

        elif opcion == "5":
            numeros = solicitar_numeros()

        elif opcion == "6":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Por favor, elija una opción entre 1 y 6.")


if __name__ == "__main__":
    main()