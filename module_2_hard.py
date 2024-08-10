def pw ():
    list_value = []
    list_password = []
    n = int(input('Введите число от 3 до 20: '))
    if n < 3 or n > 20:
        print('Число не подходит, повторите попытку')
        pw()
    else:
        for i in range (1, n):
            for j in range (1, n):
                if all ([n % (i + j) == 0 and i != j and [j, i] not in list_value]):
                    list_value.append([i, j])
    for i in list_value:
        list_password.extend(i)
    password = ''.join(str(x) for x in list_password)
    print (password)
pw()

