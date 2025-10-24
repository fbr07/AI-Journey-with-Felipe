def evenNumbers(numbers):
    evenPointer = 0
    for i in range(0, len(numbers)):
        if numbers[i] % 2 == 0:
            numbers[evenPointer], numbers[i] = numbers[i], numbers[evenPointer]
            evenPointer += 1
    return numbers


print(evenNumbers([1, 2, 3, 4]))
