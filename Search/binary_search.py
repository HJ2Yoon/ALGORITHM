# 재귀함수 구현

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        binary_search(arr, target, start, mid-1)
    else:
        binary_search(arr, target, mid+1, start)

# 반복문 구현

def binary_search(arr, target, start, end):
    while start > end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            end = mid - 1
        else:
            start = mid + 1
    return None