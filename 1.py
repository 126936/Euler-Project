def get_multiples(number,limit):
    #returns a list with all multiples of number < limit
    multiples = []
    multiple = number

    while multiple < limit:
        multiples.append(multiple)
        multiple += number

    return multiples

def main():
    #get lists of all multiples of 3 and 5 < 1000
    #add these lists together and convert to a set to remove duplicates
    #sum this set to get the answer
    print("Sum of all the multiples of 3 or 5 below 1000:", 
    sum(set(get_multiples(3,1000) + get_multiples(5,1000))))

if __name__ == "__main__":
    main()
