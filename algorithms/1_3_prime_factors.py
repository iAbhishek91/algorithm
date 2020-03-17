number = 7


def prime_factors(num):
    divisor = 2  # we start with 2 as all numbers are divisible by 1
    result = []

    while num >= divisor:
        # the below loop help not to loop through composite numbers
        while num % divisor == 0:
            result.append(divisor)

            num /= divisor
            print(num)

        divisor += 1

    return result


def prime_factors_optimised(num):
    divisor = 2
    result = []

    while num >= divisor:
        if num % divisor == 0:
            result.append(divisor)
            num /= divisor
            print(num)
        else:
            divisor += 1

    return result


print(prime_factors(number))

print(prime_factors_optimised(number))
