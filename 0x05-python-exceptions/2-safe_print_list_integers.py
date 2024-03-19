#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
        return count
    except IndexError:
        print()
        raise


if __name__ == "__main__":
    my_list = [1, 2, 3, 4]
    nb_print = safe_print_list_integers(my_list, len(my_list) + 4)
    print("nb_print: {:d}".format(nb_print))
