resu = []  #Сумма для накопления ответа
print('Для начала работы или обновления суммы нажмите "у"')
print('Каждое вычесление начинается с новой строки')
print('Для окончания вычесления введние буквенное значение из 2х символов ')

def start():
    print("Выберите действие")
    y = str(input())
    if 'y' in y:   #сокрощение от Yes
        for i in y:
            if i == y:
                while i == y:
                    print("Введите переменные")
                    a = float(input())  #переменная 1
                    zn = str(input())   #Действие
                    b = float(input())  #Переменная 2
                    if zn == '+':
                        result = a + b
                        resu.append(result)
                        print(result)
                    elif zn == '-':
                        result = a - b
                        resu.append(result)
                        print(result)
                    elif zn == '*':
                        result = a * b
                        resu.append(result)
                        print(result)
                    elif zn == '/' or ':':
                        result = a / b
                        resu.append(result)
                        print(result)
                    else:
                        print("Unknow result")

                    return start()
            else:
                break
    elif '+' in y:
        for i in resu:
            x = float(input())
            result = i + x
            resu.append(result)
            print(result)
            return start()
    elif '-' in y:
        for i in resu:
            x = float(input())
            result = i - x
            resu.append(result)
            print(result)
            return start()
    elif '*' in y:
        for i in resu:
            x = float(input())
            result = i * x
            resu.append(result)
            print(result)
            return start()
    elif '/' or ':' in y:
        for i in resu:
            x = float(input())
            result = i / x
            resu.append(result)
            print(result)
            return start()
    elif '0' or '=' in y:
        x = int(input())
        if x == 0:
            print('Thx 4 use')
    else:
        print('Not ccount message')
        return start()

start()


