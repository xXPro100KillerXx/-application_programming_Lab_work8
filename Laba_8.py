import random
from loguru import logger

logger.remove(handler_id=None)
logger.add('laba_8.log', format='{time} {level} {message}', level='INFO', rotation='10 KB', compression='zip')

prosloe = set()
while True:
    logger.info("Включение программы")
    print('Введите номер бочонка')
    try:
        bochonok = int(input())
        logger.info(f"Пользователь ввел {bochonok}")
        if bochonok<=0:
            print('Нужно ввести целое положительное число')
            logger.error("Неправильное число")
            continue
        generated_range = [*range(1, bochonok+1)] #цифры от 1 до введенного номера
        loto = list(set(generated_range) - prosloe)
        loto.sort(key=lambda _: random.random()) #рандомный порядок
        prosloe.add(bochonok)
        for c in loto:
            print(c)
            logger.info(f"Программа вывела {c}")
            input("Нажмите enter")
        logger.info("Конец программы")
    except ValueError:
        print("Нужно ввести целое положительное число")
        logger.error("Неправильное число")
        continue