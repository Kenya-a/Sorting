# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements #created list with elements # of elements
    # TO-DO

    partA = 0
    partB = 0

    for i in range(0, elements):
        if partA >= len(arrA):
            merged_arr[i] = arrB[partB]
            partB += 1
        elif partB >= len(arrB):
            merged_arr[i] = arrA[partA]
            partA += 1 
        elif arrA[partA] < arrB[partB]:
            merged_arr[i] = arrA[partA]
            partA += 1
        else: 
            merged_arr[i] = arrB[partB]
            partB += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) <= 1:
        return arr
    else: 
        pivot =  len(arr) // 2
        left = arr[:pivot]
        right = arr[pivot:]

    arrayI = merge_sort(left)
    arrayII = merge_sort(right)

    return merge(arrayI, arrayII)

    #return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
