import logging
import random
import os

'''
Ввод целого числа с проверкой на ошибки.

Параметры:
msg - Информационное сообщение пользователю (type str). (Обязательный)
min - Минимальное доступное значение (type int). (Обязательный)

Ошибки:
Invalid input - Неверный ввод.
Number must be greater than 1 - Число не входит в заданный диапазон.

Возврат:
Целое число введенное пользователем.
'''
def input_int(msg: str, min: int = None, max: int = None) -> int:
    invalid_input_err = 'Invalid input'
    char_min = '-∞' if min == None else min
    char_max = '+∞' if max == None else max
    out_range_err = f'The number must be in the range [{char_min}, {char_max}]'

    # Возвращает форматированную строку ошибки.
    def get_error(text : str):
        return '\033[31m{}\033[0m'.format('ERROR: ' + text + '! Try again...')

    while True:
        try:
            logging.info(msg)
            num = int(input(msg + ': '))
            logging.info(f'Пользователь ввел: {num}')
        except:
            print(get_error(invalid_input_err))
            logging.error(invalid_input_err, exc_info=True)
            continue
        
        if min != None and num < min or max != None and num > max:
            print(get_error(out_range_err))
            logging.error(out_range_err)
            continue

        logging.info(f'Корректно введенное значение: {num}')
        return num

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="log_file.log", filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s")
    os.system('cls')

    # Ввод данных.
    max_value = input_int('Введите максимальное значение для генерации числа', 2)
    amount_attempts = input_int('Введите количество попыток', 1, max_value) 

    # Генерация случайного числа.
    num = random.randint(1, max_value)
    logging.info(f'Сгенерированное число: {num}')

    # Попытки пользователя угадать число.
    while True:
        current_value = input_int('Введите число для угадывания', 1, max_value)

        if current_value == num:
            print('\nЧисло угадано!')
            logging.info('Пользователь угадал число.')
            break

        amount_attempts -= 1
        if amount_attempts == 0:
            print(f'\nПопытки закончились! Загаданное число: {num}.')
            logging.info('У пользователя закончились попытки.')
            break

        if current_value < num:
            print('Введенное число меньше загаданного.')
            logging.info('Введенное пользователем число было меньше загаданного.')
        
        if current_value > num:
            print('Введенное число больше загаданного.')
            logging.info('Введенное пользователем число было больше загаданного.')