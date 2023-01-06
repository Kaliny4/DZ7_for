"""
Ввести с клавиатуры целое число n.
Получить сумму кубов всех целых чисел от 1 до n(включая n).
Исключения составляют все числа кратные цифре 3.
Использовать цикл for

"""

n = input('Ввести с клавиатуры целое число n: ')
n1 = int(n) if n.isdigit() else 0

res = 0
for item in range(1, n1 + 1):
    if item % 3 != 0:
        res += item ** 3
        print('Res on each step: ', res, ', ', end='')
print()
print('Final sum: ', res)
