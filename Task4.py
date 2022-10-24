# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def polinom_index(k):
    pind = [randint(0, 100) for i in range(k+1)]
    if pind[0] == 0:
        pind[0] = randint(1, 100)
    pind = list(map(str, pind))
    return pind

def create_file(text):
    name = input('Задайте путь к файлу: ')
    with open(name, 'w') as f:
        f.write(text)


k = int(input('Задайте натуральную степень полинома: '))
ind = polinom_index(k)
print('Список коэффициентов: ', polinom_index(k))
terms = polinom_index(k)
equation = ' + '.join(terms) + ' = 0'
print('Полином: ', equation)
create_file(equation)