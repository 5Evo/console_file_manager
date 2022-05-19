# Инициация баланса и истории

def separate(symb='*', num=20):
    return symb * num

def add_separators(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('-' * 20)
        result = f(*args, **kwargs)
        # поведение после вызова
        print('-' * 20)
        return result

    # возвращается функция inner с новым поведением
    return inner

def input_amount(question):
    result = None
    while result == None:
        try:
            result = int(input(question))
        except ValueError:
            print(' - Некорректная сумма')
    return result

@add_separators
def print_menu(menu):
    for menu_item in menu:
        print(menu_item)



