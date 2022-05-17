# Инициация баланса и истории

def separate(symb='*', num=20):
    return symb * num

def input_amount(question):
    result = ''
    while not result.isdigit():
        result = input(question)
        if not result.isdigit():
            print(' - Некорректная сумма')
    return int(result)





