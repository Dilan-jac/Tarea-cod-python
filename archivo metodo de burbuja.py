def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numeros = [45, 21, 89, 45, 78, 23, 90, 12, 4, 3, 7]
burbuja(numeros)
print("lista ordenada:", numeros)
