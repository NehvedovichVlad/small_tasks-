"""
На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая создает из указанных строк список и выводит его.

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести список состоящий из указанных строк.

Sample Input:

5
C#
C++
C
Python
F#
Sample Output:

['C#', 'C++', 'C', 'Python', 'F#']
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
num = int(input())
numbers = []  # создаем пустой список
a = ""
for i in range(num):
    a = input()
    numbers.append(a)
print(numbers)
