#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_a = []
    for idx in range(list_length):
        try:
            result = my_list_1[idx]/my_list_2[idx]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            list_a.append(result)
    return list_a
