# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# 2 -+ | 1 ++
# 3 -- | 4 +-

while True:
    print('Enter 0 for exit')
    quarter = int(input('Enter quarter 1-4>> '))
    if quarter == 0: break
    if quarter < 1 or quarter > 4: print('Pls, enter quarter 1-4')

    if quarter == 1: print('x > 0 & y > 0')
    elif quarter == 2: print('x < 0 & y > 0')
    elif quarter == 3: print('x < 0 & y < 0')
    elif quarter == 4: print('x > 0 & y < 0')

