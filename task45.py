# Два различных натуральных числа n и m называются дружественными, если сумма делителей
# числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 –
# дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое 
# из которых не превосходит k. Программа получает на вход одно натуральное число k, не 
# превосходящее 10^5. Программа должна вывести  все пары дружественных чисел, каждое из 
# которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# a =[]
# b = []

for i in range(int(input("Введите число K: "))):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
#     a.append(sum)
# print(len(a))
    if sum > i:
        sum1 = 0
        for k in range(1,sum):
            if sum % k == 0:
                sum1 += k
#         b.append(sum1)
# print(b)
        if sum1 == i:
            print(sum1, sum)

