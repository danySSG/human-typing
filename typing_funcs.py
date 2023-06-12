from keyboard import write, press_and_release
from time import sleep
from random import random, uniform, choice
from map import get_neighbors, ALPHABETS

EAL = ALPHABETS["en"]
RAL = ALPHABETS["ru"]
special_symbols = (
    " ",
    ",",
    ".",
    "!",
    "?",
    ":",
    ";",
    "\n",
    "\t",
    "[",
    "]",
    "{",
    "}",
    "(",
    ")",
    "'",
    '"',
    "_",
)


def type_correct_char(current_position, text):
    write(text[current_position])
    current_position += 1
    if current_position < len(text):
        if text[current_position] in special_symbols:
            sleep(uniform(0.7, 1.2))  # большая задержка перед новым словом
        else:
            sleep(uniform(0.1, 0.2))  # обычная задержка для букв внутри слова
    return current_position


def err_typo_1(current_position, text):
    # мимо клавиши
    error_chance = random()
    if error_chance < 0.05:
        if current_position > 0:
            neighbors = get_neighbors(
                text[current_position - 1], text[current_position]
            )
            if neighbors:
                # добавляем случайный соседний символ
                write(choice(neighbors))
                sleep(uniform(0.3, 0.5))  # задержка перед исправлением
                press_and_release("backspace")  # исправляем ошибку
                sleep(uniform(0.1, 0.2))
                return type_correct_char(current_position, text)
    return None


def err_typo_2(current_position, text):
    # соседние буквы (случайный пробел вписывается в эту концепцию)
    error_chance = random()
    if error_chance < 0.05:
        if current_position + 1 < len(text):
            a, b = text[current_position], text[current_position + 1]
            if (
                (b in EAL + " " and a in EAL + " ")
                or (b in RAL + " " and a in RAL + " ")
            ) and a != b:
                write(b)
                write(a)
                sleep(uniform(1, 2))
                press_and_release("backspace")
                sleep(uniform(0.1, 0.2))
                press_and_release("backspace")
                sleep(uniform(0.1, 0.2))
                return type_correct_char(current_position, text)
    return None


def err_typo_3(current_position, text):
    # удвоенная буква
    error_chance = random()
    if error_chance < 0.05:
        a = text[current_position]
        if a in EAL or a in RAL:
            residual_length = 0
            space_position = text.find(" ", current_position)
            if space_position == -1:
                residual_length = len(text) - current_position - 1
            else:
                residual_length = space_position - current_position - 1
            # если до конца слова слишком далеко, не будем этого делать
            if residual_length < 6:
                write(text[current_position])
                sleep(uniform(0.1, 0.3))
                # не замечаем её до конца слова
                for i in range(residual_length + 1):
                    write(text[current_position + i])
                    sleep(uniform(0.1, 0.3))
                sleep(uniform(0.7, 1.25))
                for _ in range(residual_length):
                    press_and_release("left")
                    sleep(uniform(0.1, 0.2))
                press_and_release("backspace")
                for _ in range(residual_length):
                    press_and_release("right")
                    sleep(uniform(0.1, 0.2))
                current_position += residual_length + 1
                sleep(uniform(0.1, 0.2))
                if current_position < len(text):
                    return type_correct_char(current_position, text)
                return current_position
    return None


def err_typo_4(current_position, text):
    # пропуск буквы
    error_chance = random()
    if error_chance < 0.05:
        a = text[current_position]
        if a in EAL or a in RAL:
            residual_length = 0
            space_position = text.find(" ", current_position)
            if space_position == -1:
                residual_length = len(text) - current_position - 1
            else:
                residual_length = space_position - current_position - 1
            # если до конца слова слишком далеко, не будем этого делать
            if residual_length < 6:
                # write(text[current_position])
                # sleep(uniform(0.1, 0.3))
                # не замечаем пропуска до конца слова
                for i in range(residual_length):
                    write(text[current_position + i + 1])
                    sleep(uniform(0.1, 0.3))
                sleep(uniform(0.7, 1.25))
                for _ in range(residual_length):
                    press_and_release("left")
                    sleep(uniform(0.1, 0.2))
                # keyboard.press_and_release("backspace")
                write(text[current_position])
                for _ in range(residual_length):
                    press_and_release("right")
                    sleep(uniform(0.1, 0.2))
                current_position += residual_length + 1
                sleep(uniform(0.1, 0.2))
                if current_position < len(text):
                    return type_correct_char(current_position, text)
                return current_position
    return None
