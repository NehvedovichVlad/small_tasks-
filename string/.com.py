"""
.com or .ru
На вход программе подается строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести «YES» если введенная строка заканчивается подстрокой .com или .ru и «NO» в противном случае.

Sample Input 1:

www.stepik.org
Sample Output 1:

NO
Sample Input 2:

www.google.com
Sample Output 2:

YES
Sample Input 3:

www.yandex.ru
Sample Output 3:

YES
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
s = input()
flag = False
if s.endswith('.com') or s.endswith('.ru'):
    flag = True
if flag == True:
    print('YES')
else:
    print('NO')
# -------------------------------------------------------------------------------------------------

# 2)вариант
print('YES' if input().endswith(('.com', '.ru')) else 'NO')
