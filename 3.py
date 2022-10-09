# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# 2 -+ | 1 ++
# 3 -- | 4 +-

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

while True: 
    print('if you want to leave enter empty string')
    x = int(input('Enter x>>' ))
    y = int(input('Enter y>>' ))
    if x == "" or y == "": break

    if x == 0 or y == 0:
        print('x or y !=0')
                
    if x > 0 and y > 0: print('1')
    elif x < 0 and y > 0: print('2')
    elif x < 0 and y < 0: print('3')
    elif x > 0 and y < 0: print('4')
    



