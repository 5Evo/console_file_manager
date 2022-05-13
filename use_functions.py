# Инициация баланса и истории
balance = 0
history = []

def input_amount(question):
    result = ''
    while not result.isdigit():
        result = input(question)
        if not result.isdigit():
            print(' - Некорректная сумма')
    return int(result)

stay_in = True
while stay_in:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        balance += int(input_amount('на сколько хотите пополнить баланс? '))
        print(f'Ваш новый баланс: {balance} руб.')

    elif choice == '2':
        purchase = int(input_amount('Сколько Вы хотите потратить? '))
        if purchase > balance:
            print(f'Ваша покупка на {purchase} превысит ваш баланс {balance}. Вы не можете столько потратить')
        else:
            balance -= purchase
            purchase_item = input('Введите название покупки: ')
            history.append([purchase, purchase_item])
            print(f'На вашем счету осталось {balance} руб.')

    elif choice == '3':
        print('********************* ')
        print('Ваша история покупок: ')
        for k, v in history:
            print(k,v)
        print('********************* ')

    elif choice == '4':
        print("Досвидания, до новыйх встреч!")
        stay_in = False
        # exit(0)

    else:
        print('Неверный пункт меню')