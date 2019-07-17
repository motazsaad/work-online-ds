from random import randint


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def is_even2(x):
    return x % 2 == 0


def gen_list(list_size, max_num):
    return [randint(0, max_num) for _ in range(list_size)]


def read_even_num():
    while True:
        num = int(input('plz enter even num: '))
        if is_even(num):
            break
    return num


def search(a_list, num):
    found = False
    for n in a_list:
        if not is_even(n):
            continue
        if n == num:
            found = True
            break
    return found


def search2(a_list, num):
    found = False
    indx = -1
    for i in range(len(a_list)):
        if not is_even(a_list[i]):
            continue
        if a_list[i] == num:
            found = True
            indx = i
    return found, indx


def increment(number=1, by=1):  # function with default parameters
    return (number, number + by)


def increment2(number:int, by:int) -> int:
    return number + by

def f1():
    f2()


def f2():
    print('hello')


if __name__ == '__main__':
    print('welcome to my functions')
    f1()


