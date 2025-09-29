def sumpol(numbers):
    total = 0
    for num in numbers:
        if num < 0:
            break
        total += num
    return total
print("Сумма:", sumpol((1, 2, 3, -1)))