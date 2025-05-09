def quicksort(arr):
    if len(arr) <=1:
      return arr
    pivot = arr[len(arr) // 2]
    left  = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

arr = [90, 76, 6, 45, 92, 1, 76, 56, 34, 98097, 5, 8, 6]
sorted_arr = quicksort(arr)
print("lista ordenada:", sorted_arr)