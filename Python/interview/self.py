"""
 Для чего нужен “self” в функциях?
“Self” – это переменная, обозначающая принадлежность объекта самому себе.
В большинстве объектно-ориентированных языков, данная переменная передается
в качестве скрытого параметра методов, которые определяются объектами. Но в
Python это определение и передача осуществляется явно. В первом аргументе,
который создается в экземпляре класса A, происходит автоматическая передача
параметров метода. Происходит обращение к отдельным экземплярам переменной
для каждого отдельного объекта. Это первый аргумент, который используется в
экземпляре класса, а метод «self» определен явно для всех используемых и
существующих методов. Название переменных происходит вот по такому образцу: “self.xxx”.

Как в методе можно явно определить “self”?
“Self” – это ссылочная переменная и атрибут экземпляра, который используется
вместо локальной переменной внутри класса. Функция или переменная self, такая
как self.x или self.meth(), могут использоваться в том случае, если класс
неизвестен. У такого класса нет переменных, объявленных как локальные.
У него отсутствует какой-либо синтаксис, но в нем можно производить явную
передачу ссылки или вызвать метод, который используется этим классом.
Использование writebaseclass.methodname(self, <argument list>) показывает,
что метод _init_()  может быть расширен до базовых методов класса. Это также
решает синтаксическую проблему, которая возникала между оператором
присваивания и локальными переменными. Такой подход указывает интерпретатору,
когда будут использоваться переменные экземпляра класса, а когда локальные
переменные. Явное использование переменной self.var решает вышеупомянутую проблему.
"""