# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    for i in range(elements):
        if arrA and arrB:
            if arrA[0] <= arrB[0]:
                merged_arr[i] = arrA.pop(0)
            else:
                merged_arr[i] = arrB.pop(0)
        elif arrA:
            merged_arr[i] = arrA.pop(0)
        elif arrB:
            merged_arr[i] = arrB.pop(0)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        half = len(arr) // 2
        arrA = merge_sort(arr[:half])
        arrB = merge_sort(arr[half:])
        arr = merge(arrA, arrB)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    if arr[mid] > arr[mid + 1]:
        while start <= mid and mid + 1 <= end:
            if arr[start] > arr[mid + 1]:
                arr.insert(start, arr.pop(mid + 1))
                start += 1
                mid += 1
            else:
                start += 1
    


def merge_sort_in_place(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
