# подключаем модуль random
import random

# генерируем случайное число
random_number = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

print('Ты готов?')
answer = input()
if answer == 'да':
    print('Угадай число')

while True:
    if answer == 'нет':
        break


    def is_valid(number):
        if number >= 1 and number <= 100:
            return True
        else:
            return False


    new_number = int(input())
    examination = is_valid(new_number)

    if examination == True:
        if new_number > random_number:
            print('Слишком много, попробуйте ещё раз')
            continue
        elif new_number < random_number:
            print('Слишком мало, попробуйте ещё раз')
            continue
        elif new_number == random_number:
            print('Вы угадали, поздравляю!')
            print('Хотите сыграть ещё раз?')
            q = input()
            if q == 'да':
                continue
            else:
                break
        else:
            print('А может быть введем число от 1 до 100?')
            continue
    elif examination == False:
        print('А может быть все-таки введем число от 1 до 100?')
        continue
