from keyboard import wait, add_hotkey
from random import choice, shuffle
from pyperclip import paste
from threading import Thread
from pynput.mouse import Listener as mListener
from typing_funcs import (
    type_correct_char,
    err_typo_1,
    err_typo_2,
    err_typo_3,
    err_typo_4,
)

# Глобальные переменные для отслеживания текущего состояния и позиции в тексте
is_paused = True
text = ""
current_position = 0
typing_thread = None
typos = [err_typo_1, err_typo_2, err_typo_3, err_typo_4]


def shuffled(lst):
    new_lst = lst[:]
    shuffle(new_lst)
    return new_lst


def change_current_position(position):
    global current_position
    current_position = position


# Функция для набора текста
def type_text():
    while current_position < len(text):
        if not is_paused:
            for err_func in shuffled(typos):
                if (position := err_func(current_position, text)) is not None:
                    change_current_position(position)
                    break
            else:
                change_current_position(type_correct_char(current_position, text))

            # я понял, что в контексте простого написания кода эти функции бессмысленны, потому что по сути даже раскладку менять не придётся
            # зажатый капс
            # забыл сменить раскладку


# Функции для управления паузой
def pause_typing():
    global is_paused
    if is_paused:
        resume_typing()
    else:
        is_paused = True


# Функция для продолжения\начала печати
def resume_typing():
    global is_paused
    global typing_thread
    if typing_thread is None or not typing_thread.is_alive():
        typing_thread = Thread(target=type_text)
        typing_thread.start()
    is_paused = False


# Функция для сброса и начала новой сесси печати
def reset():
    global is_paused
    global text
    global current_position
    is_paused = True
    text = paste().replace("\r\n", "\n").replace("    ", "\t")
    current_position = 0


# Установка горячих клавиш
add_hotkey("pause", pause_typing)
add_hotkey("ctrl + enter", reset)


# Слушатель активности мыши
def on_activity(x, y, button=None, pressed=None, dx=None, dy=None):
    global is_paused
    is_paused = True


mouse_listener = mListener(
    on_move=on_activity, on_click=on_activity, on_scroll=on_activity
)
mouse_listener.start()

wait()
