my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print('Ряд чисел: ',my_list)
print('Положительные числа до первого отрицательного:')
index = 0
while index >= 0 or index <= len(my_list):
    number = my_list[index]
    if number == 0:
        index += 1
        continue
    elif number > 0:
        print(number)
        index += 1
    else:
        break










