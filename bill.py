import use_functions

balance = 0
history = []

def pay_history():
    print(use_functions.separate())
    print('Ваша история покупок: ')
    for k, v in history:
        print(k, v)
    print(use_functions.separate())


stay_in = True
while stay_in:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        print(use_functions.separate())
        balance += int(use_functions.input_amount('на сколько хотите пополнить баланс? '))
        print(f'Ваш новый баланс: {balance} руб.')
        print(use_functions.separate())

    elif choice == '2':
        print(use_functions.separate())
        purchase = int(use_functions.input_amount('Сколько Вы хотите потратить? '))
        if purchase > balance:
            print(f'Ваша покупка на {purchase} превысит ваш баланс {balance}. Вы не можете столько потратить')
            print(use_functions.separate())
        else:
            balance -= purchase
            purchase_item = input('Введите название покупки: ')
            history.append([purchase, purchase_item])
            print(f'На вашем счету осталось {balance} руб.')
            print(use_functions.separate())

    elif choice == '3':
        pay_history()

    elif choice == '4':
        print("Досвидания, до новыйх встреч!")
        stay_in = False
        # sys.exit(0)

    else:
        print('Неверный пункт меню')