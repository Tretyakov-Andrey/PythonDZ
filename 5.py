# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt


xa = int(input('Enter x A>> '))
ya = int(input('Enter y A>> '))
xb = int(input('Enter x B>> '))
yb = int(input('Enter y B>> '))

res = round(sqrt(((xb - xa) ** 2)+((yb - ya) ** 2)),3)
print(f'Result: {res}')

