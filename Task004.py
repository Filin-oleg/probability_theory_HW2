# Задание 4. В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# а) Какова вероятность того, что все мячи белые?
# б) Какова вероятность того, что ровно два мяча белые?
# в) Какова вероятность того, что хотя бы один мяч белый?

from math import factorial


def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


n1 = combinations(10, 2)
n2 = combinations(11, 2)

m1 = combinations(7, 2)
m2 = combinations(9, 2)


print(f'а) Вероятность того, что все извлечённые мячи белые = {(m1/n1)*(m2/n2):.4f}%')


a1 = combinations(7, 2)
a2 = combinations(2, 2)
p1 = a1/n1
p2 = a2/n2
pa = p1*p2

a1 = combinations(2, 2)
a2 = combinations(9, 2)
p1 = a1/n1
p2 = a2/n2
pb = p1*p2

a1 = combinations(7, 1)
a2 = combinations(9, 1)
b1 = combinations(3, 1)
b2 = combinations(2, 1)
p1 = (a1*b1)/n1
p2 = (a2*b2)/n2
pc = p1*p2
p = pa+pb+pc


print(f'б) Вероятность того, что ровно два мяча белые = {p:.4f}%')


m1 = combinations(3, 2)
m2 = combinations(2, 2)


print(f'в) Вероятность того, что будет извлечен хотя бы один белый мяч = {1-(m1/n1)*(m2/n2):.4f}%')