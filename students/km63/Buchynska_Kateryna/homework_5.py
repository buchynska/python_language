#task1--------------------------
"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""
def enter():
    data = input().split()
    return data

def operation(element):
    list = []
    for i in range(0, len(element), 2):
      list.append(element[i])
    return list

def output(output_data):
    	for i in output_data:
        print (i, end = ' ')
        
 output(operation(enter()))       
#-----------------------------------------


#task2--------------------------
"""
Выведите все четные элементы списка.
"""
def enter():
    data = input().split()
    return data

def operation(element):
    list = []
    for i in element:
         if int(i) % 2 == 0:
            list.append(i)
    return list

def output(output_data):
    for i in output_data:
        print (i, end = ' ')

output(operation(enter()))
#-----------------------------------------


#task3--------------------------
"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""
def enter():
    data = input().split()
    return data
    
def operation(elements):
    data = []
    for i in range(0, len(elements)):
        if i < len(elements)-1:
            if int(elements[i]) < int(elements[i + 1]):
                data.append(elements[i +1])
    return data

def result(output_data):
    for i in output_data:
        print (i, end=' ')

result(operation(enter()))
#-----------------------------------------


#task4--------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, 
выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. 
Если таких пар соседей несколько — выведите первую пару.
"""
def enter():
    data = input().split()
    return data

def operation(elements):
    data = []
    for i in range(0, len(elements)):
        if len(data) == 0:
            if i < len(elements)-1:
                if int(elements[i]) * int(elements[i + 1]) > 0:
                    data = [elements[i]]
                    data.append(elements[i + 1])

    return data


def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation(enter()))

#-----------------------------------------


#task5--------------------------
"""
Дан список чисел. Определите, сколько в этом списке элементов, 
которые больше двух своих соседей, и выведите количество таких элементов. 
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
def input_data():
    data = input().split()
    return data

def operation(elements):
    count = 0
    for i in range(1, len(elements) - 1):
        if int(elements[i-1]) < int(elements[i]) > int(elements[i+1]):
            count +=1
    return count

def print_data(output_data):
    print (output_data)

print_data(operation(input_data()))
 
#-----------------------------------------


#task6--------------------------
"""
Дан список чисел. Выведите значение наибольшего элемента в списке, 
а затем индекс этого элемента в списке. Если наибольших элементов несколько, 
выведите индекс первого из них.
"""
def input_data():
    data = input().split()
    return data
    
def operation(elements):
    data = []
    max_elements = elements[0]
    data = [max_elements]
    data.append(0)
    for i in range(1, len(elements)):
        if int(max_elements) < int(elements[i]):
            max_elements = elements[i]
            data = [max_elements]
            data.append(i)
    return data
    
def print_data(output_data):
    for i in output_data:
        print (i, end=' ')

print_data(operation(input_data()))

#-----------------------------------------
#task7--------------------------
"""
Петя перешёл в другую школу. 
На уроке физкультуры ему понадобилось определить своё место в строю. 
Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, 
означающих рост каждого человека в строю. После этого вводится число X – рост Пети. 
Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. 
Если в строю есть люди с одинаковым ростом, таким же, как у Пети, 
то он должен встать после них.
"""
def input_data():
    heigh = input().split()
    return heigh

def operation(children):
    x = int(input())
    position = 0
    while position<len(children) and int(children[position])>= x:
        position += 1
    return position

def print_data(output_data):
    print (output_data + 1)
    
print_data(operation(input_data()))
#-----------------------------------------


#task10--------------------------
"""
В списке все элементы различны. 
Поменяйте местами минимальный и максимальный элемент этого списка.
"""
def input_data():
    data = input().split()
    return data

def operation_data(elements):
    max_element = elements[0]
    min_element = elements[0]
    index_min = 0
    index_max = 0
    for i in range(0, len(elements)):
        if  int(min_element) > int(elements[i]):
            min_element = elements[i]
            index_min = i
        if  int(max_element) < int(elements[i]):
            max_element = elements[i]
            index_max = i
    
    elements[index_min], elements[index_max] = elements[index_max], elements[index_min]    
    return elements

def print_data(output_data):
    for i in output_data:
        print (i, end=' ')

print_data(operation_data(input_data()))


#-----------------------------------------
#task11--------------------------
"""
Дан список из чисел и индекс элемента в списке k. 
Удалите из списка элемент с индексом k, 
сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k. 
Программа сдвигает все элементы, а после этого удаляет последний элемент 
списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, 
а не делать это при выводе элементов. Также нельзя использовать дополнительный список. 
Также не следует использовать метод pop(k) с параметром.
"""
def input_data():
    data = input().split()
    return data

def operation_data(elements):
    k = int(input())
    for i in range(k, len(elements) - 1):
        elements[i] = elements[i + 1]
    elements.pop()
    return elements

def print_data(output_data):
    for i in output_data:
        print (i, end=' ')
       
print_data(operation_data(input_data()))


#-----------------------------------------
#task12--------------------------
"""
Дан список целых чисел, число k и значение C. 
Необходимо вставить в список на позицию с индексом k элемент, 
равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается, 
после считывания списка в его конец нужно будет добавить новый элемент, 
используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого 
при выводе и не создавая дополнительного списка.
"""
def input_data():
    data = input().split()
    return data
    
def operation_data(elements):
    data = input().split()
    elements.append(data[1])
    for i in range(len(elements) - 1, int(data[0]), -1):
        elements[i] = elements[i - 1]
    elements[int(data[0])] = int(data[1])
    return elements
    
def print_data(output_data):
   for i in output_data:
        print (i, end=' ')

print_data(operation_data(input_data()))


#-----------------------------------------
