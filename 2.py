# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input('Enter x>> '))
y = bool(input('Enter y>> '))
z = bool(input('Enter z>> '))
res = False

if not(x or y or z) == (not x and not y and not z):
    res = True
else: res = False

print(f'Result>> {res}')
