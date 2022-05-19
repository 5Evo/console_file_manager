import os
import use_functions

menu_manager = ('1. создать папку',
                '2. удалить (файл/папку)',
                '3. копировать (файл/папку)',
                '4. просмотр содержимого рабочей директории',
                '5. посмотреть только папки',
                '6. посмотреть только файлы',
                '7. просмотр информации об операционной системе',
                '8. создатель программы',
                '9. играть в викторину',
                '10. мой банковский счет',
                '11. смена рабочей директории',
                '12. сохранить содержимое рабочей директории в файл',
                '13. выход')

while True:
    #print(use_functions.separate('-', 20))
    use_functions.print_menu(menu_manager)
    #print(use_functions.separate('-', 20))

    choice = input('Выберите пункт меню: ')
    if choice == '1':               # ________________создаем новую папку____________
        new_dir = input('Введите название папки: ')
        if not os.path.isdir(new_dir):
            os.mkdir(new_dir)
            print(f'Новая папка: {os.path.abspath(new_dir)}')
        else:
            print(f"Такая папка уже существует: {os.path.abspath(new_dir)}")

    elif choice == '2':             # ________________удаление файла/папки____________
        del_dir = input('Введите название папки/файла: ')
        if os.path.isdir(del_dir):
            os.rmdir(del_dir)
            print(f'удалили папку: {os.path.abspath(del_dir)}')
        elif os.path.isfile(del_dir):
            os.remove(del_dir)
            print(f'удалили файл: {os.path.abspath(del_dir)}')
        else:
            print(f"Такая папка/файл не существует: {os.path.abspath(del_dir)}")

    elif choice == '3':             # ________________копирование файла/папки____________
        import shutil
        src_file = input('Откуда копируем: ')
        if os.path.exists(src_file): # файл существует:
            dest_file = input('Куда копируем: ')
            if src_file != dest_file:
                # Скопиоруем файл:
                if os.path.isfile(src_file):
                    shutil.copyfile(src_file, dest_file)
                    # Проверим как скопировали:
                    print('Скопировали удачно!') if os.path.exists(dest_file) else print('Что-то пошло не так...')
                else:
                    shutil.copytree(src_file, dest_file) if not os.path.exists(dest_file) else print('Такая папка уже существует, не могу скопировать')
            else:
                print('попытка копирования в самого себя')
        else:                        # файла не существует:
            print(f'Файла {src_file} не существует')

    elif choice == '4':                 # _______________просмотр содержимого рабочей директории___________
        print(os.listdir(os.getcwd()))

    elif choice == '5':                 # _______________просмотр только папок___________
        with os.scandir(os.getcwd()) as listOfEntries:
            for entry in listOfEntries:
            # печать всех записей, являющихся файлами
                if entry.is_dir():
                    print(entry.name)

    elif choice == '6':                 # _______________просмотр только файлов___________
        with os.scandir(os.getcwd()) as listOfEntries:
            for entry in listOfEntries:
            # печать всех записей, являющихся файлами
                if entry.is_file():
                    print(entry.name)

    elif choice == '7':                 # _____________________просмотр информации об операционной системе_______
        import sys
        print('My OS is', sys.platform, '(', os.name, ')')

    elif choice == '8':         # создатель программы
        import getpass
        name = getpass.getuser()
        print(f'Разраотчик программы: {name}')


    elif choice == '9':                 # Программа Викторина
        import victory
        victory

    elif choice == '10':                # программа Счет
        import bill
        bill

    elif choice == '11':                # смена рабочей директории
        print('текущая директория: ', os.path.abspath(os.getcwd()))
        new_path = input('Введите путь для создания новой папки: ')
        if os.path.isdir(new_path):
            os.chdir(new_path)
            print('перешли в существующую директорию: ', os.getcwd())
        else:
            os.mkdir(new_path)
            os.chdir(new_path)
            print('создали и перешли в новую директорию: ', os.getcwd())

    elif choice == '12':                # сохранение модержимого директории в файл
        import json
        FILE_NAME ='listdir.txt'
        # подготовим список для сохраниения:
        list_file = 'files: '
        list_dir = ' dirs: '
        with os.scandir(os.getcwd()) as listOfEntries:
            for entry in listOfEntries:
                if entry.is_file():
                    list_file += entry.name + ' '
                else:
                    list_dir += entry.name + ' '
        listdir_data = list_file + list_dir

        with open(FILE_NAME, 'w') as f:
            json.dump(listdir_data, f)


    elif choice == '13':
        print("Досвидания, до новыйх встреч!")
        exit(0)

    else:
        print('Неверный пункт меню')
