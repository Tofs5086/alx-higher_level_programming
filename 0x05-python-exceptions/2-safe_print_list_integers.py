#!/usr/bin/python3
def safe_print_list_integers(my_list=None, x=0):
    try:
        count_integers = 0
        index = 0

        while count_integers < x:
            value = my_list[index]

            if type(value) is int:
                print("{:d}".format(value), end="")
                count_integers += 1

                if count_integers < x:
                    print(" ", end="")

            index += 1

    except (IndexError, TypeError):
        pass

    print()
    return count_integers

