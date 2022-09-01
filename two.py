def get_even_fibonacci(number1,number2,limit):
    ''' returns list of even fibonacci numbers
        starting with "number1", "number2"
        less than "limit" '''
    numbers = []
    next_number = number1 + number2

    #check if starting numbers can be added to list of even-valued terms
    if number1 % 2 == 0:
        numbers.append(number1)
    if number2 % 2 == 0:
        numbers.append(number2)

    while next_number <= limit:
        #if even add to list of even terms
        if next_number % 2 == 0:
            numbers.append(next_number)

        #incriment values here so they are checked by while loop condition before next loop
        next_number = number1 + number2
        number1 = number2
        number2 = next_number
    return numbers

def main():
    print("Starting with 1 and 2.",
        "Sum of all even-valued terms of the fibonacci sequence,",
        "whose values do not exceed four million:",
        sum(get_even_fibonacci(1,2,4000000)))


if __name__ == "__main__":
    main()