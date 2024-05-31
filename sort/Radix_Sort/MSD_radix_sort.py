from collections import deque

def msd_sort(nums):
    max_val = max(nums)
    digit = len(str(max_val))

    buckets = [deque() for _ in range(10)]
    for num in nums:
        buckets[(num // (10 ** (digit - 1))) % 10].append(num)

    result = []
    for bucket in buckets:
        if len(bucket) > 1 and digit > 1:
            result.extend(msd_sort(list(bucket)))
        else:
            result.extend(bucket)

    return result


# 테스트
nums = [170, 45, 75, 90, 802, 24, 2, 66]
print(msd_sort(nums))
