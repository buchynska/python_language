#task1------------------------------------------------------


"""
Задача «Количество различных чисел»
Условие
Дан список чисел. Определите, сколько в нем встречается различных чисел.
"""
#
a=set(input())
print(len(a)-1)
#-----------------------------------------------------------


#task2------------------------------------------------------

"""
Задача «Количество совпадающих чисел»
Условие
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

"""
#
a=set(input().split())
b=set(input().split())
count=0
for i in a:
    for j in b:
        if i==j:
            count+=1
print(count)
#-----------------------------------------------------------


#task3------------------------------------------------------


"""
Задача «Пересечение множеств»
Условие
Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.

Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
"""
#
a=set([int(i) for i in input().split()])
b=set([int(i) for i in input().split()])
c=list(a&b)
c.sort()
print(' '.join([str(i) for i in c]))
#-----------------------------------------------------------


#task4------------------------------------------------------


"""
Задача «Встречалось ли число раньше»
Условие
Во входной строке записана последовательность чисел через пробел. 
Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
"""
#
a=set()
for i in input().split():
    n=int(i)
    if n in a:
        print('YES')
    else:
        print('NO')
    a.add(n)
#-----------------------------------------------------------


#task5------------------------------------------------------


"""
Задача «Кубики»
Условие
Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны по цвету. 
Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах. 
Для этого они занумеровали все цвета случайными числами от 0 до 108. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.

В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори. 
В следующих N строках заданы номера цветов кубиков Ани. В последних M строках номера цветов Бори.

Найдите три множества: номера цветов кубиков, которые есть в обоих наборах; 
номера цветов кубиков, которые есть только у Ани и номера цветов кубиков, которые есть только у Бори. 
Для каждого из множеств выведите сначала количество элементов в нем, а затем сами элементы, отсортированные по возрастанию.
"""
#
n,m=[int(i) for i in input().split()]
a=set()
b=set()
for i in range(n):
    a.add(int(input()))
for i in range(m):
    b.add(int(input()))
a_b=list(a&b)
a_b.sort()
only_a=list(a-b)
only_a.sort()
only_b=list(b-a)
only_b.sort()
print(len(a&b))
print(' '.join([str(i) for i in (a_b)]))
print(len(a-b))
print(' '.join([str(i) for i in (only_a)]))
print(len(b-a))
print(' '.join([str(i) for i in (only_b)]))
#-----------------------------------------------------------

#task6------------------------------------------------------


"""
Задача «Количество слов в тексте»
Условие
Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.

Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
"""
#
a=int(input())
count=set()
for i in range(a):
    for j in input().split():
        count.add(j)
print(len(count))
#-----------------------------------------------------------
