# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

while True:
    today = int(input('Enter number day today or enter 0 for break>> '))
    if today == 0:
        break
    if today > 7 or today < 1:
        print('Your number is out of range')
        print('Pls, enter new nuber or enter 0 (zero) for close')
    if today in range(1,6):
        print('No')
    else: print('Yes')
     
    



