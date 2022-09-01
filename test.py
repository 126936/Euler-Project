import sys

def is_prime(number):
    factors = []
    #1 cannot be a prime number
    if number == 1:
        return False
    for factor in gen_factors(number):
        print("factor:",factor)
        factors = factors + factor
        if len(factors) > 2:
            return False
    return True

def gen_factors(number):
    count = 1
    factor = 2

    #count up from 1, checking if count is factor of number
    #if so yield pair of factors in a list
    while count < factor:
        factor = number / count
        if number % count == 0:
                yield [count,int(factor)]
        count += 1
    return

def main():
    input = 600851475143
    small_factors = []

    for factor in gen_factors(input):
        small_factors.append(factor[0])

        if is_prime(factor[1]):
            sys.exit(f"Largest Prime factor: {factor[1]}")

    for factor in reversed(small_factors):
        if is_prime(factor):
            sys.exit(f"Largest Prime factor: {factor}")


if __name__ == "__main__":
    main()