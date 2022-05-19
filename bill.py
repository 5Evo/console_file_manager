import os.path

import use_functions
import json


balance = 0
history = []
FILE_NAME = 'bill.json'

def pay_history():
    print(use_functions.separate())
    print('Ваша история покупок: ')
    for k, v in history:
        print(k, v)
    print(use_functions.separate())

def load_account():
    if os.path.isfile(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            load_data = json.load(f)
            load_balance = load_data[0]
            load_history = load_data[1]
    else:
        print('Файла с данными не существует, начнем все с самого начала.')
        load_balance = 0
        load_history = []

    return load_balance, load_history

def save_account():
    # подготовим данные для записи в файл:
    save_data = []
    save_data.append(balance)
    save_data.append(history)
    # запишем все в файл:
    with open(FILE_NAME, 'w') as f:
        f = json.dump(save_data, f)

balance, history = load_account()

menu_bill = ('0. Узнать баланс',
             '1. пополнение счета',
             '2. покупка',
             '3. история покупок',
             '4. выход'
             )
stay_in = True
while stay_in:
    use_functions.print_menu(menu_bill)

    choice = input('Выберите пункт меню: ')
    if choice == '0':
        print(use_functions.separate())
        print(f'Ваш баланс: {balance}')
        print(use_functions.separate())

    elif choice == '1':
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
        print(history)
        pay_history()

    elif choice == '4':
        print("Досвидания, до новыйх встреч!")
        save_account()
        stay_in = False
        # sys.exit(0)

    else:
        print('Неверный пункт меню')