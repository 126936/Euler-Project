from three import gen_factors
import sys

def is_palindrome(input):
    ''' tests if int arg is a palindrome number
        returns bool '''
    number = str(input)
    length = len(number)
    mid_point = int(length / 2)

    #if number odd remove middle digit
    if length % 2 > 0:
        number = number[:mid_point] + number[mid_point+1:]

    #take a slice of the number from start to mid_point and 
    #check if == to a slice of the number starting at the end 
    #moving in steps of -1 to mid_point-1
    if number[:mid_point] == number[-1:mid_point-1:-1]:
        return True
    return False

def main():
    upper_limit = 999*999

    #loop through natural numbers 
    #starting at the upper_limit of the range and counting down
    for number in range(upper_limit,1,-1):
        if is_palindrome(number):
            for factor in gen_factors(number):
                #convert factors to str, and test if length of both factors is 3
                if len(str(factor[0])) == 3 and len(str(factor[1])) == 3:
                    sys.exit("largest palindrome made from the product of two 3-digit numbers: "
                        + str(factor[0] * factor[1]))

if __name__ == "__main__":
    main()