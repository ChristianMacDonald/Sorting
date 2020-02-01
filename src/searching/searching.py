# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  if len(arr) > 0:
    low = 0
    high = len(arr) - 1
    while True:
      if low != high:
        mid = (low + high) // 2
        if target < arr[mid]:
          high = mid
        elif target > arr[mid]:
          low = mid
        else:
          return mid
      elif arr[low] == target:
        return low
      else:
        break
  return -1


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  if len(arr) > 0:
    if low != high:
      mid = (low + high) // 2
      if target < arr[mid]:
        return binary_search_recursive(arr, target, low, mid)
      elif target > arr[mid]:
        return binary_search_recursive(arr, target, mid, high)
      else:
        return mid
    else:
      if arr[low] == target:
        return low
      else:
        return -1
  else:
    return -1
