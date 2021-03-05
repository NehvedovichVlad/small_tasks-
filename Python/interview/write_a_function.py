"""
1) Какие есть способы написания функции,
 которая  использует передачу параметров по ссылке?
"""
"""
Аргументы в Python передаются по значению.
Значение создается путем присваивания, результатом
которого является объект, который не имеет никаких 
связей между именем аргумента на входе и выходе.
Процедура написания функции, которая использует
передачу параметров по ссылке, включает в себя:

Результатом является кортеж, который может быть 
возвращен объекту, который вызвал его. Ниже 
представлен пример, наглядно демонстрирующий это:
"""
def function(a, b):
    a = 'value'
    b = b + 1
    # a и b это локальные переменные, которые используются для
    # определения новых объектов
    return a, b
# Это функция, которая используется для возвращения значения хранимого # в a и b

"""
Использование глобальных переменных позволяет обратится 
к функции по ссылке, однако такой метод не является 
безопасным по отношению к любой функции;
Применение изменяемых объектов (обычно, это классы,
 состоящие их изменяемых объектов), необходимо для 
 передачи параметров по ссылке.function"""

def function(a):
    a[0] = 'string'
    a[1] = a[1] + 1
    # Массив ‘a’ предоставляет ссылку на изменяемый список и он уже
    # изменяет общие изменяемые объекты
args = ['string', 10]
function(args)
print(args[0], args[1])
#Вывод значений, хранящихся в массиве ‘a’