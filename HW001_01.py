number = int(input("Введите трёхзначное число: "))
num1 = number // 100
if (num1 >= 1 and num1 < 10):
    print ("Давайте считать")
    num3 = number % 10
    num2 = int(((number - num3) - num1 *100) / 10)
    print(f'В итоге получилось {num2}')
else:
    print("Попробуйте ввести трёхзначное число")