def heapify(arr, n, i):
    largest = i  # 루트
    left = 2 * i + 1  # 왼쪽 자식
    right = 2 * i + 2  # 오른쪽 자식

    # 왼쪽 자식이 루트보다 큰 경우
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 현재 가장 큰 요소보다 큰 경우
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 가장 큰 요소가 루트가 아닌 경우
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 교체
        heapify(arr, n, largest)  # 재귀적으로 힙을 정리


def heap_sort(arr):
    n = len(arr)

    # 최대 힙을 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 하나씩 요소를 힙에서 추출하여 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 현재 루트와 교체
        heapify(arr, i, 0)  # 루트를 제외하고 다시 힙을 구성


# 사용 예시
arr = [7, 6, 5, 8, 3, 5, 9, 1, 6]
heap_sort(arr)
print("정렬된 배열:", arr)
