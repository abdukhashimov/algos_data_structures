def minmax(numbers):
    min_number = float('inf')
    max_number = float('-inf')

    for number in numbers:
        if number < min_number:
            min_number = number

        if number > max_number:
            max_number = number

    return (min_number, max_number)
