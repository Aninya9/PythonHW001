ticket = int(input('Введите шестизначный номер билета: '))
num1 = ticket // 100000
if (num1 >= 1 and num1 < 10):
    print ("Давайте считать")

    num6 = ticket % 10
    num5 = int((ticket % 100 - num6) / 10)
    num4 = int((ticket % 1000 - num6 - num5) / 100)
    num3 = int((ticket % 10000 - num6 - num5 - num4) / 1000)
    num2 = int((ticket % 100000 - num6 - num5 - num4 - num3) / 10000)
    
    print(f'В итоге получилось {num1, num2, num3, num4, num5, num6}')

    sum1 = num1+num2+num3
    sum2 = num4+num5+num6
    if (sum1 == sum2): print('Счастливый!')
    else: (print('Не счастливый'))
else:
    print("Попробуйте ввести шестизначное число")