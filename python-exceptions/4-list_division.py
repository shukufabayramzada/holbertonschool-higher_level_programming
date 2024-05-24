#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            if (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
                new_list.append(num1 / num2)
            else:
                print("wrong type")
                new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            print("Processed element {:d}".format(i))

    return new_list
