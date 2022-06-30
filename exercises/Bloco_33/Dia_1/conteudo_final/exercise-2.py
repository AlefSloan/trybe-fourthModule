def arithmetic_average(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum / len(arr)


print(arithmetic_average([10, 10, 10]))
