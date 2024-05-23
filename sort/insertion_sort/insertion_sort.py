def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

        print(f'STEP{i}: ', arr)
    return arr


arr = [40, 60, 70, 50, 10, 30, 20]
print('SOURCE ARRAY: ', arr)
sorted = insertion_sort(arr)
print('SORTED ARRAY: ', sorted)
