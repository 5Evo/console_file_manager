'''
Задание
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]
# 2 - количество случайных элементов
result = random.sample(numbers, 2)
print(result) # [5, 1]
После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'
Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде: третье января 2009 года, склонением можно пренебречь
В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
'''

dob_tuple = (
    ('Пушкин Александр Сергеевич', '06.06.1799', 'шестого июня 1799'),
    ('Ломоносов Михаил Васильевич', '19.11.1711', 'девятнадцатого ноября 1711'),
    ('Гагарин Юрий Алексеевич', '09.03.1934', 'девятого марта 1934'),
    ('Владимир Семенович Высоцкий', '25.01.1938', 'двадцать пятого января 1938'),
    ('Георгий Константинович Жуков','01.12.1896', 'первого декабря 1896'),
    ('Владимир Ильич Ленин', '22.04.1870', 'двадцать второго апреля 1870'),
    ('Илья Ефимович Репин', '05.08.1844', 'пятого августа 1844'),
    ('Павел Петрович Бажов', '27.01.1879', 'двадцать седьмого января 1879'),
    ('Иван Васильевич Грозный', '25.08.1530', 'двадцать пятого августа 1530'),
    ('Екатерина II Великая', '02.05.1729', 'второго мая 1729')
)

import random

num_quest = 5   # количество вопросов в викторине

again = '1'
while again == '1':
    question_vic = random.sample(dob_tuple, num_quest)      # выберем случайных персон для викторины
    #print(question_vic)
    goods = 0
    for person in question_vic:
        answer = input(f'Введите дату рождения "{person[0]}" в формате 01.01.1999: ')
        if answer == person[1]:
            goods += 1
            print(f'Правильно, вам засчитан 1 бал. Всего у вас {goods}')
        else:
            print(f'Неправльно, правильный ответ: {person[2]}') # тут можно конвертировать дату в текстовую,
                                                                # но это потребует модуль datetime, что противоречит условию
    print(f'Вы закончили викторину и набрали баллов: {goods}')
    again = input('Хотите начать снова? /(1-Да, Любой другой символ - нет/): ')

print('Вы закончили Викторину, спасибо')