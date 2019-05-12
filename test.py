# 1 QUESTION

class SumArgs:

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def result(self):
        return self.arg1 + self.arg2

    def __str__(self):
        return "{} + {}".format(self.arg1, self.arg2)


class SubtractArgs(SumArgs):

    def result(self):
        return self.arg1 - self.arg2

    def __str__(self):
        return "{} - {}".format(self.arg1, self.arg2)

# 2 QUESTION
# Кортеж в отличии от списка относится к неизменяемым типам данных,
# поэтому может использоваться в качестве ключа словаря,
# кортеж занимает меньше места в памяти, соответсвтенно время на обработку
# кортежа будет задействовано меньше чем на список.

# 3 QUESTION
# Генераторы - это итерируемые объекты которые генерируют данные на лету,
# а не хранят их все в памяти как итераторы. Ключевым словом для объявления
# функции-генератора является 'yield'. В отличии от обычных функций, генераторы
# выдают одно значение за раз.


def gen_func():
    arg = [1, 2, 3, 4, 5, 6]
    for i in arg:
        yield i

# a = gen_func()
# print(next(a)) Результат 1
# print(next(a)) Результат 2
# for i in a:
# 	print(i)
# Результат: 3 4 5 6

# 4 QUESTION
# List Comprehension - это своего рода синтаксический сахар для цикла 'for',
# альтернативный вариант сгенерировать список. Одно из преимуществ его
# использования это быстрота оработки, ну канечно же меньше кода.
# Пример:
# a = [x for x in range(10)]
# print(a) Результат: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [x for x in range(10) if x % 2 == 0]
# print(b) Результат: [0, 2, 4, 6, 8]
# c = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)]
# print(c) Результат: [0, 1, 4, 27, 16, 125, 36, 343, 64, 729]

# 5 QUESTION
# Лямбда-функция - это анониманая функция, используемая для выполнения,
# какой-то простой логики, одного выражения, при этом не требует чтоб её вызывали.
# Записывается в одну строку.
# a = lambda x: x ** 2
# print(a(2)) Рузультат 4
# print((lambda x: x ** 2)(2)) Рузультат 4

# 6 QUESTION
# for i in range(1, 10000):
# 	print(i)
# Результат выведит список чисел от 1 до 9999

# 7 QUESTION
# В этой функции 'x' объявлена как словарь. Так как словарь изменяемый тип данных,
# то при каждом вызове функции переменная 'x' будет ссылаться на один и тот же объект
# в памяти и будет накапливать изменения.

def f(t, x={}):
	x.update({t:0})
	return x

# print(f('arg1')) Результат: {'arg1': 0}
# print(f('arg2')) Результат: {'arg1': 0, 'arg2': 0}

# Один из вариантов решения проблемы

def ff(t):
	x = {}
	x.update({t:0})
	return x

# print(ff('arg1')) Результат: {'arg1': 0}
# print(ff('arg2')) Результат: {'arg2': 0}

# 8 QUESTION
# 'is' проверяет переменные, ссылаются ли они на один и тот же объект, а '==' проверяет
# имеют ли два объекта одинаковое значение, на которые ссылаются переменные.
