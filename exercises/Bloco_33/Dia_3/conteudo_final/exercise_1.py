def fizz_buzz(num):
    num_list = []
    for n in range(1, num + 1):
        if n % 5 == 0 and n % 3 == 0:
            num_list.append("FizzBuzz")
        elif n % 5 == 0:
            num_list.append("Buzz")
        elif n % 3 == 0:
            num_list.append("Fizz")
        else:
            num_list.append(n)

    return num_list


print(fizz_buzz(20))
