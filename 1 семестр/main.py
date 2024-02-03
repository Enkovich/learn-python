setting = {
    'numAttempt': 8,
    'maxNum': 15,
    'numInts': 4
}
numbers = set()

# functions
def helpCommand():
    print('''help - справка по командам
currSetting - текущие настройки для игры
exit - выход из игры
changeMaxNum - сменить максимальное генерируемое число
changeNumAttempts - сменить кол-во попыток
''')
def currComSetting():
    print(f'''Кол-во попыток: {setting['numAttempt']}
Диапазон генерируемых чисел: 0 - {setting['maxNum']}
Кол-во генерируемых чисел: {setting['numInts']}''')
def changeMaxNum():
    try:
        print('Введите число для изменения максимального числа (от 9)')
        tmp = int(input())
        
        if tmp > 9:
            global setting
            setting['maxNum'] = tmp
        else: raise ValueError
    except ValueError:
        print('Ошибка ввода')
        changeMaxNum()
def changeNumAttempts():
    try:
        print('Введите желаемое число попыток (от 3)')
        tmp = int(input())
        
        if tmp >= 2:
            global setting
            setting['numAttempt'] = tmp
        else:
            raise ValueError
    except ValueError:
        print('Ошибка ввода')
        changeNumAttempts()

def main():
    while True:
        command = input('->')
        if command=='exit':
            break
        elif command=='help':
            helpCommand()
        elif command=='currSetting':
            currComSetting()
        elif command=='changeMaxNum':
            changeMaxNum()
        elif command=='changeNumAttempts':
            changeNumAttempts()

# code

main()