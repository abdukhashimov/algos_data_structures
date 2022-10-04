def reverse_items(array):
    length = len(array)
    n = length // 2

    for i in range(0, n):
        array[i], array[length-i-1] = array[length-i-1], array[i]

    return array
