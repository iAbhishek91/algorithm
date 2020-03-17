# find all prime numbers less than or equal to number

number = 458

# solution 1


def is_prime(num):
    divisor = 2

    while num > divisor:
        print(num)
        if num % divisor == 0:
            return False
        else:
            divisor += 1

    return True


def find_prime(num):
    prime_numbers = []
    while num > 1:
        if is_prime(num):
            prime_numbers.append(num)

        num -= 1

    return prime_numbers


print(find_prime(number))


# solution 2 optimised
prime_numbers_arr = []


def is_prime_from_arr(num):
    for prime in prime_numbers_arr:
        if num % prime == 0:
            return False

    return True


def find_prime_optimised(num):
    curr = 2
    while num > curr:
        if is_prime_from_arr(curr):
            prime_numbers_arr.append(curr)

        curr += 1


find_prime_optimised(number)

print(prime_numbers_arr)
