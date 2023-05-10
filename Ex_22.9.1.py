numbers = list(input('введите целые числа через пробел:\n').split())
num = [int(s) for s in numbers]
your_num = int(input('введите целое положительное число:\n'))


def sort_num():
    for i in range(len(num)):
        for j in range(len(num) - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num

def compare():
    center = len(num) // 2
    left = 0
    right = len(num) - 1

    while num[center] != your_num and left <= right:
        if your_num > num[center]:
            left = center + 1
        else:
            right = center - 1
        center = (left + right) // 2
        if left >= right:
            break

    if your_num == num[center]:
        print("ID вашего числа равно", center)
    elif your_num > num[-1]:
        print(f'Ваше число {your_num} больше крайнего числа диапазона {num[-1]}')
        num.append(your_num)
    elif your_num < num[0]:
        print(f'Ваше число {your_num} меньше начального числа диапазона {num[0]}')
        num.append(your_num)
    elif num[0] < your_num < num[-1] and your_num < num[center]:
        print(f'ваше число {your_num} находится между {num[center-1]} и {num[center]}')
        num.append(your_num)
    else:
        print(f'ваше число {your_num} находится между {num[center]} и {num[center+1]}')
        num.append(your_num)
    return num

sort_num()
compare()
print(sort_num())