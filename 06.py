from itertools import count

for el in count(int(input('Введите стартовое число '))):

    print(el)
    if el in (10000,10001):
        break

from itertools import cycle

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el)
    if el in (10001):
        break
