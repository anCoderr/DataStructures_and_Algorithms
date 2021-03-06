from typing import List


def binary_search(arr: List[int], target: int) -> int:
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            r = mid-1
        else:
            l = mid+1
    return -1
