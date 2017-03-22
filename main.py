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
        if random_num not in loto_list:               #if not yet it loto_list, append it now.
            loto_list.append(random_num)

    return loto_list

def main():                      #main function: prints, run a loop for number and then prints loto_lenght of ask_int. Try and except.
    print "Welcome to the Lottery numbers generator."

    while True:
        ask_for_number = raw_input("Please enter how many random numbers would you like to have: ")
        try:                                                        #try if you can transform string to a int number. That means that user entered a number and functions will work.
            ask_int = int(ask_for_number)
            if ask_int == 7:                                        #if user entered a number and this number is 7, continue with function logo_lenght + that number
                print loto_length(ask_int)
                print "END"
                break
            else:                                                   #if user did entered a number but this number is not 7, tell him that.
                print "Loto cannot have %s numbers. Please choose another number. " % (ask_int)

        except:                                                     #if user did NOT entered a number, you warn it.
            print "You didnt entered a number."


if __name__ == "__main__":
    main()