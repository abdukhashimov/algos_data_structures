def is_even(number):
    isEven = True
    for i in range(1, number + 1):
        if isEven:
            isEven = False
        else:
            isEven = True
    return isEven
