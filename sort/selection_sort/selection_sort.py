def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        #temp = arr[i]
        #arr[i] = arr[min_idx]
        #arr[min_idx] = temp

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f'STEP{i}: ', arr)
    return arr


arr = [9, 6, 7, 3, 5]
print('SOURCE ARRAY: ', arr)
sorted = selection_sort(arr)
print('SORTED ARRAY: ', sorted)
