"""        > Program: Welcome to the Lottery numbers generator.
> Program: Please enter how many random numbers would you like to have:
User: 7
> Program: [4, 19, 21, 31, 42, 5, 10]
> Program: END               """


import random


def loto_length(length):            # makes random int numbers and put them to the table. When the lenght of table is the same as raw_input number, breaks
    loto_list = []

    while True:
        if len(loto_list) == length:
          break

        random_num = random.randint( 0, 50 )
        if random_num not in loto_list:
            loto_list.append(random_num)

    return loto_list

def main():                      #main function: prints, run a loop for number and then prints loto_lenght of ask_for_number
    print "Welcome to the Lottery numbers generator."

    while True:
        ask_for_number = int(raw_input("Please enter how many random numbers would you like to have: "))
        if ask_for_number == 7:
            break

        else:
            print "Loto cannot have %s numbers. Please choose another number. " % (ask_for_number)


    print loto_length(ask_for_number)
    print "END"

if __name__ == "__main__":
    main()