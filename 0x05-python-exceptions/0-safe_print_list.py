#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print()
    return ret

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, 5)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, 7)
    print("nb_print: {:d}".format(nb_print))
