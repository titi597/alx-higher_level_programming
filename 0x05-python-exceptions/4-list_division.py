#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    result_list = []

    for i in range(list_length):
        try:
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 0

            if not isinstance(elem_1, (int, float)) or not isinstance(elem_2, (int, float)):
                raise TypeError("wrong type")

            if elem_2 == 0:
                raise ZeroDivisionError("division by 0")

            result = elem_1 / elem_2
        except TypeError as e:
            result = 0
            print(e)
        except ZeroDivisionError as e:
            result = 0
            print(e)
        except IndexError:
            result = 0
            print("out of range")
        finally:
            result_list.append(result)

    return result_list
