print('Задание 9.')

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.

d = list(map(int, input('Введите числа через пробел: ').split()))

sum = 0
num = max(d)
print(f'Самое большое число ряда: {num}')
for i in d:
    while num != 0:
        sum += num % 10
        num //= 10
print(f'Сумма его цифр{sum}')

