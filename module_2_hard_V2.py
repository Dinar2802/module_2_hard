def pw():
    password = []
    n = int(input('Введите число от 3 до 20: '))
    if n < 3 or n > 20:
        print('Число не подходит, повторите попытку')
        pw()
    else:
        for i in range(1, n):
            for j in range(i + 1, n):
                if n % (i + j) == 0 and i != j:
                    password.append(str(i) + '+' + str(j))

    print(*password)
    pw()


pw()
