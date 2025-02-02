#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists
    Returns a new list with all divisions
    """
    result = []
    for i in range(list_length):
        try:
            div = 0
            if i < len(my_list_1) and i < len(my_list_2):
                if not (isinstance(my_list_1[i], (int, float)) and 
                       isinstance(my_list_2[i], (int, float))):
                    print("wrong type")
                elif my_list_2[i] == 0:
                    print("division by 0")
                else:
                    div = my_list_1[i] / my_list_2[i]
            else:
                print("out of range")
        except Exception:
            div = 0
        finally:
            result.append(div)
    return result
