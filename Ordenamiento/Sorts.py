class Sorts:
    def __init__(self):
        self.lista = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]

        def reset_lista():
            global lista
            lista = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]

        def bubble_sort(lista):
            n = len(lista)
            for i in range(n):
                for j in range(0, n-i-1):
                    if lista[j] > lista[j+1]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]
            return lista
        print(bubble_sort(lista))
        reset_lista()


        def selection_sort(lista):
            n = len(lista)
            for i in range(n):
                min_idx = i
                for j in range(i+1, n):
                    if lista[j] < lista[min_idx]:
                        min_idx = j
                lista[i], lista[min_idx] = lista[min_idx], lista[i]
            return lista
        print(selection_sort(lista))
        reset_lista()


        def insertion_sort(lista):
            n = len(lista)
            for i in range(1, n):
                key = lista[i]
                j = i - 1
                while j >= 0 and key < lista[j]:
                    lista[j + 1] = lista[j]
                    j -= 1
                lista[j + 1] = key
            return lista
        print(insertion_sort(lista))
        reset_lista()


        def merge_sort(lista):
            if len(lista) > 1:
                mid = len(lista) // 2
                L = lista[:mid]
                R = lista[mid:]

                merge_sort(L)
                merge_sort(R)

                i = j = k = 0

                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        lista[k] = L[i]
                        i += 1
                    else:
                        lista[k] = R[j]
                        j += 1
                    k += 1

                while i < len(L):
                    lista[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    lista[k] = R[j]
                    j += 1
                    k += 1
            return lista
        print(merge_sort(lista))
        reset_lista()


        def quick_sort(lista):
            if len(lista) <= 1:
                return lista
            else:
                pivot = lista[len(lista) // 2]
                left = [x for x in lista if x < pivot]
                middle = [x for x in lista if x == pivot]
                right = [x for x in lista if x > pivot]
                return quick_sort(left) + middle + quick_sort(right)
        print(quick_sort(lista))
        reset_lista()


        def random_quick_sort(lista):
            if len(lista) <= 1:
                return lista
            else:
                import random
                pivot_index = random.randint(0, len(lista) - 1)
                pivot = lista[pivot_index]
                left = [x for x in lista if x < pivot]
                middle = [x for x in lista if x == pivot]
                right = [x for x in lista if x > pivot]
                return randomized_quick_sort(left) + middle + randomized_quick_sort(right)
        print(random_quick_sort(lista))
        reset_lista()


        def counting_sort(lista):

            max_val = max(lista)
            count = [0] * (max_val + 1)
            for num in lista:
                count[num] += 1
            sorted_lista = []
            for i in range(len(count)):
                sorted_lista.extend([i] * count[i])
            return sorted_lista
        print(counting_sort(lista))
        reset_lista()