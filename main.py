setting = {
    'numAttempt': 8,
    'maxNum': 9,
    'numInts': 4
}

# functions
def helpCommand():
    print('''help - справка по командам
currSetting - текущие настройки для игры
exit - выход из игры''')
def currComSetting():
    print(f'''Кол-во попыток: {setting['numAttempt']}
Диапазон генерируемых чисел: 0 - {setting['maxNum']}
Кол-во генерируемых чисел: {setting['numInts']}''')
def editSettings():
    try:
        tmp = input()
    except Exception as e:
        print(e)

def main():
    while True:
        command = input()
        if command=='exit':
            break
        elif command=='help':
            helpCommand()
        elif command=='currSetting':
            currComSetting()
        elif command=='editSetting':
            editSettings()

# code

main()