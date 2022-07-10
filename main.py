import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import logic_gates as lg
from datetime import datetime

# Инициализация наборов, используемых в функции рандома
gates_for_1 = ['not', 'buf']
gates_for_2 = ['and', 'or', 'xor', 'nand', 'nor', 'xnor']
gates_for_3 = ['nor3']
true_false = [True, False]


def on_closing():
    """ Закрытие приложения """
    if messagebox.askokcancel('Выход из приложения', 'Хотите выйти из приложения?'):
        root.destroy()


root = Tk()  # Создание окна
root.protocol('WM_DELETE_WINDOW', on_closing)
root.title('Тренажер по цифровой логике')  # Заголовок окна
root.geometry('1600x800')
root.iconphoto(True, PhotoImage(file='icon.png'))

customizing_window = None
help_window = None

main_menu = Menu(root)
root.config(menu=main_menu)
notation_menu = Menu(main_menu, tearoff=0)

# Создание фреймов
frame_button = Frame(root)  # Фрейм с кнопками
frame_button.grid(column=0, row=0, sticky="nw", columnspan=2)

frame_gates = Frame(root)  # Фрейм с схемой
frame_gates.grid(column=1, row=1, sticky="w", padx=20, pady=20)

frame_task = Frame(root)  # Фрейм с заданием
frame_task.grid(column=1, row=2, sticky="sw")

frame_empty = Frame(root, width=50, height=740)  # Пустой фрейм, чтобы фрейм с заданием не скакал по экрану
frame_empty.grid(column=0, row=1, rowspan=2, sticky="w")

frame_counter = Frame(frame_button)  # Фрейм для счетчика
frame_counter.grid(row=0, column=6)

frame_reference = Frame(root, width=500, height=700)  # Фрейм с справка
frame_reference.grid(column=2, row=1, rowspan=2, sticky="ne", padx=20, pady=20)

# Подгрузка и преобразование изображений в словари
image_of_gates = {
    "true": ImageTk.PhotoImage(Image.open('image/input/true.png')),
    "false": ImageTk.PhotoImage(Image.open('image/input/false.png')),
    "question": ImageTk.PhotoImage(Image.open('image/input/qest.png')),
    "a": ImageTk.PhotoImage(Image.open('image/input/a.png')),
    "b": ImageTk.PhotoImage(Image.open('image/input/b.png')),
    "c": ImageTk.PhotoImage(Image.open('image/input/c.png')),
    "y": ImageTk.PhotoImage(Image.open('image/input/y.png')),
}

image_of_lines = {
    "basic": {  # Стандартные линии
        "1": ImageTk.PhotoImage(Image.open('image/line/basic/1.png')),
        "2": ImageTk.PhotoImage(Image.open('image/line/basic/2.png')),
        "3": ImageTk.PhotoImage(Image.open('image/line/basic/3.png')),
        "4": ImageTk.PhotoImage(Image.open('image/line/basic/4.png')),
        "5": ImageTk.PhotoImage(Image.open('image/line/basic/5.png')),
        "6": ImageTk.PhotoImage(Image.open('image/line/basic/6.png')),
        "7": ImageTk.PhotoImage(Image.open('image/line/basic/7.png')),
        "8": ImageTk.PhotoImage(Image.open('image/line/basic/8.png')),
        "9": ImageTk.PhotoImage(Image.open('image/line/basic/9.png')),
        "10": ImageTk.PhotoImage(Image.open('image/line/basic/10.png')),
        "11": ImageTk.PhotoImage(Image.open('image/line/basic/11.png')),
        "12": ImageTk.PhotoImage(Image.open('image/line/basic/12.png')),
        "13": ImageTk.PhotoImage(Image.open('image/line/basic/13.png')),
        "14": ImageTk.PhotoImage(Image.open('image/line/basic/14.png'))
    },
    "color": {  # Линии связи после взаимодействия с пользователем
        "green": {
            "1_green": ImageTk.PhotoImage(Image.open('image/line/color/green/1_green.png')),
            "2_green": ImageTk.PhotoImage(Image.open('image/line/color/green/2_green.png')),
            "4_green": ImageTk.PhotoImage(Image.open('image/line/color/green/4_green.png')),
            "5_green": ImageTk.PhotoImage(Image.open('image/line/color/green/5_green.png')),
            "9_green": ImageTk.PhotoImage(Image.open('image/line/color/green/9_green.png')),
            "10_green": ImageTk.PhotoImage(Image.open('image/line/color/green/10_green.png')),
            "11_green": ImageTk.PhotoImage(Image.open('image/line/color/green/11_green.png')),
            "12_green": ImageTk.PhotoImage(Image.open('image/line/color/green/12_green.png')),
            "13_green": ImageTk.PhotoImage(Image.open('image/line/color/green/13_green.png')),
            "14_green": ImageTk.PhotoImage(Image.open('image/line/color/green/14_green.png'))
        },
        "red": {
            "1_red": ImageTk.PhotoImage(Image.open('image/line/color/red/1_red.png')),
            "2_red": ImageTk.PhotoImage(Image.open('image/line/color/red/2_red.png')),
            "4_red": ImageTk.PhotoImage(Image.open('image/line/color/red/4_red.png')),
            "5_red": ImageTk.PhotoImage(Image.open('image/line/color/red/5_red.png')),
            "9_red": ImageTk.PhotoImage(Image.open('image/line/color/red/9_red.png')),
            "10_red": ImageTk.PhotoImage(Image.open('image/line/color/red/10_red.png')),
            "11_red": ImageTk.PhotoImage(Image.open('image/line/color/red/11_red.png')),
            "12_red": ImageTk.PhotoImage(Image.open('image/line/color/red/12_red.png')),
            "13_red": ImageTk.PhotoImage(Image.open('image/line/color/red/13_red.png')),
            "14_red": ImageTk.PhotoImage(Image.open('image/line/color/red/14_red.png'))
        },
        "multi": {
            "3_black_green": ImageTk.PhotoImage(Image.open('image/line/color/multi/3_black_green.png')),
            "3_black_red": ImageTk.PhotoImage(Image.open('image/line/color/multi/3_black_red.png')),
            "3_green_black": ImageTk.PhotoImage(Image.open('image/line/color/multi/3_green_black.png')),
            "3_green_green": ImageTk.PhotoImage(Image.open('image/line/color/multi/3_green_green.png')),
            "3_green_red": ImageTk.PhotoImage(Image.open('image/line/color/multi/3_green_red.png')),
            "3_red_black": ImageTk.PhotoImage(Image.open('image/line/color/multi/3_red_black.png')),
            "3_red_green": ImageTk.PhotoImage(Image.open('image/line/color/multi/3_red_green.png')),
            "3_red_red": ImageTk.PhotoImage(Image.open('image/line/color/multi/3_red_red.png')),

            "6_black_green": ImageTk.PhotoImage(Image.open('image/line/color/multi/6_black_green.png')),
            "6_black_red": ImageTk.PhotoImage(Image.open('image/line/color/multi/6_black_red.png')),
            "6_green_black": ImageTk.PhotoImage(Image.open('image/line/color/multi/6_green_black.png')),
            "6_green_green": ImageTk.PhotoImage(Image.open('image/line/color/multi/6_green_green.png')),
            "6_green_red": ImageTk.PhotoImage(Image.open('image/line/color/multi/6_green_red.png')),
            "6_red_black": ImageTk.PhotoImage(Image.open('image/line/color/multi/6_red_black.png')),
            "6_red_green": ImageTk.PhotoImage(Image.open('image/line/color/multi/6_red_green.png')),
            "6_red_red": ImageTk.PhotoImage(Image.open('image/line/color/multi/6_red_red.png')),

            "7_black_green": ImageTk.PhotoImage(Image.open('image/line/color/multi/7_black_green.png')),
            "7_black_red": ImageTk.PhotoImage(Image.open('image/line/color/multi/7_black_red.png')),
            "7_green_black": ImageTk.PhotoImage(Image.open('image/line/color/multi/7_green_black.png')),
            "7_green_green": ImageTk.PhotoImage(Image.open('image/line/color/multi/7_green_green.png')),
            "7_green_red": ImageTk.PhotoImage(Image.open('image/line/color/multi/7_green_red.png')),
            "7_red_black": ImageTk.PhotoImage(Image.open('image/line/color/multi/7_red_black.png')),
            "7_red_green": ImageTk.PhotoImage(Image.open('image/line/color/multi/7_red_green.png')),
            "7_red_red": ImageTk.PhotoImage(Image.open('image/line/color/multi/7_red_red.png')),

            "8_black_green": ImageTk.PhotoImage(Image.open('image/line/color/multi/8_black_green.png')),
            "8_black_red": ImageTk.PhotoImage(Image.open('image/line/color/multi/8_black_red.png')),
            "8_green_black": ImageTk.PhotoImage(Image.open('image/line/color/multi/8_green_black.png')),
            "8_green_green": ImageTk.PhotoImage(Image.open('image/line/color/multi/8_green_green.png')),
            "8_green_red": ImageTk.PhotoImage(Image.open('image/line/color/multi/8_green_red.png')),
            "8_red_black": ImageTk.PhotoImage(Image.open('image/line/color/multi/8_red_black.png')),
            "8_red_green": ImageTk.PhotoImage(Image.open('image/line/color/multi/8_red_green.png')),
            "8_red_red": ImageTk.PhotoImage(Image.open('image/line/color/multi/8_red_red.png'))
        }

    }
}

gates_styles = {
    "ansi": {
        "not": ImageTk.PhotoImage(Image.open('image/ansi/not.png')),
        "buf": ImageTk.PhotoImage(Image.open('image/ansi/buf.png')),
        "and": ImageTk.PhotoImage(Image.open('image/ansi/and.png')),
        "nand": ImageTk.PhotoImage(Image.open('image/ansi/nand.png')),
        "nor": ImageTk.PhotoImage(Image.open('image/ansi/nor.png')),
        "xnor": ImageTk.PhotoImage(Image.open('image/ansi/xnor.png')),
        "xor": ImageTk.PhotoImage(Image.open('image/ansi/xor.png')),
        "or": ImageTk.PhotoImage(Image.open('image/ansi/or.png'))
    },
    "iec": {
        "not": ImageTk.PhotoImage(Image.open('image/iec/not.png')),
        "buf": ImageTk.PhotoImage(Image.open('image/iec/buf.png')),
        "and": ImageTk.PhotoImage(Image.open('image/iec/and.png')),
        "nand": ImageTk.PhotoImage(Image.open('image/iec/nand.png')),
        "nor": ImageTk.PhotoImage(Image.open('image/iec/nor.png')),
        "xnor": ImageTk.PhotoImage(Image.open('image/iec/xnor.png')),
        "xor": ImageTk.PhotoImage(Image.open('image/iec/xor.png')),
        "or": ImageTk.PhotoImage(Image.open('image/iec/or.png'))
    },
    "log": {
        "not": ImageTk.PhotoImage(Image.open('image/letter/not.png')),
        "buf": ImageTk.PhotoImage(Image.open('image/letter/buf.png')),
        "and": ImageTk.PhotoImage(Image.open('image/letter/and.png')),
        "nand": ImageTk.PhotoImage(Image.open('image/letter/nand.png')),
        "nor": ImageTk.PhotoImage(Image.open('image/letter/nor.png')),
        "xnor": ImageTk.PhotoImage(Image.open('image/letter/xnor.png')),
        "xor": ImageTk.PhotoImage(Image.open('image/letter/xor.png')),
        "or": ImageTk.PhotoImage(Image.open('image/letter/or.png'))
    }
}

truth_table = {
        "not": ImageTk.PhotoImage(Image.open('information/image/not.png')),
        "buf": ImageTk.PhotoImage(Image.open('information/image/buf.png')),
        "and": ImageTk.PhotoImage(Image.open('information/image/and.png')),
        "nand": ImageTk.PhotoImage(Image.open('information/image/nand.png')),
        "nor": ImageTk.PhotoImage(Image.open('information/image/nor.png')),
        "xnor": ImageTk.PhotoImage(Image.open('information/image/xnor.png')),
        "xor": ImageTk.PhotoImage(Image.open('information/image/xor.png')),
        "or": ImageTk.PhotoImage(Image.open('information/image/or.png')),
        "menu": ImageTk.PhotoImage(Image.open('information/image/menu.png')),
        "settings": ImageTk.PhotoImage(Image.open('information/image/settings.png')),
        "reference": ImageTk.PhotoImage(Image.open('information/image/reference.png')),
}

# Инициализация глобальных переменных и временных хранилищ
style = "ansi"  # Метка используемого вида обозначений
type_of_task = ""  # Метка задания
type_of_random = False
training_mode = None  # может принимать значения: None, 'learning', 'training, 'control'

#  Временные значения программы
temporary_data = []  # Хранилище временных данных: [str], bool*4
temporary_index = []  # Хранение координат для скрытого элемента
temporary_elements_and_index = []  # Хранит вентили и их координаты
all_incoming_results = []  # Хранит все значения входящих переменных
elements_of_gate = []  # Хранит все вентили в том порядке, в котором изначально задавались
y_in_task_2 = []
number_of_pattern = 0  # Номер используемого шаблона в задании 2

temporary_data_for_task_3 = {}  # Хранение значений промежуточных элементов
answer_user_for_task_3 = {}  # Хранение цветов на промежуточных элементах от пользователя

# СЧЕТЧИКИ              (возможно поменять на словарь)
number_of_try = 0  # Количество попыток прохождения тестирования
max_task_in_control = 20
time_start = None
time_stop = None

number_of_tasks = 0  # Пройденых заданий
right_answers = 0  # Правильные ответы
number_of_intermediate_elements = 0  # Количество пройденых промежуточных элементовё
right_intermediate_answers = 0  # Правильные промежуточные ответы

type_1 = 0  # Количество пройденых заданий 1 типа
type_2 = 0  # Количество пройденых заданий 2 типа
type_3 = 0  # Количество пройденых заданий 3 типа

right_answers_type_1 = 0  # Правильные ответы на 1 тип заданий
right_answers_type_2 = 0  # Правильные ответы на 2 тип заданий
right_answers_type_3 = 0  # Правильные ответы на 3 тип заданий

counters = {
    "max_number_of_type_1": 6,  # Настройка количества заданий 1 типа
    "max_number_of_type_2": 6,  # Настройка количества заданий 2 типа
    "max_number_of_type_3": 8,  # Настройка количества заданий 3 типа
    "min_percent_for_middle": 50,
    "min_percent_for_good": 65,
    "min_percent_for_best": 85,
}

input_field_1 = None
input_field_2 = None
input_field_3 = None
input_field_4 = None
input_field_5 = None
input_field_6 = None


def check_settings():
    """ Проверяет наличие файла с настройками, если его нет, устанавливает значения по умолчанию """

    with open('files/settings.txt', 'r') as save_settings:
        try:
            counters["max_number_of_type_1"] = int(save_settings.readline())
            counters["max_number_of_type_2"] = int(save_settings.readline())
            counters["max_number_of_type_3"] = int(save_settings.readline())
            counters["min_percent_for_middle"] = int(save_settings.readline())
            counters["min_percent_for_good"] = int(save_settings.readline())
            counters["min_percent_for_best"] = int(save_settings.readline())
        except ValueError:
            pass


def pattern_1(call_type="generate") -> tuple:
    """ Шаблон 1 """

    global all_incoming_results
    global elements_of_gate
    global y_in_task_2

    ans_elements = []
    a = b = c = None

    elements = ['?' for i in range(5)]

    if call_type == "generate":
        a = random.choice(true_false)
        b = random.choice(true_false)
        c = random.choice(true_false)

        all_incoming_results.append(a)
        all_incoming_results.append(b)
        all_incoming_results.append(c)

        elements[0] = random.choice(gates_for_1)
        elements[1] = random.choice(gates_for_1)
        elements[2] = random.choice(gates_for_2)
        elements[3] = random.choice(gates_for_2)
        elements[4] = random.choice(gates_for_2)

        for elem in elements:
            elements_of_gate.append(elem)

    elif call_type == "calculated":
        vari = 0  # Указатель элемента в массиве элементов
        lost_element = temporary_data[0]  # int номер неизвестного входящего значения

        for elem in elements_of_gate:
            elements[vari] = elem
            vari += 1

        if lost_element == 1:
            a = not all_incoming_results[0]
            b = all_incoming_results[1]
            c = all_incoming_results[2]

        elif lost_element == 2:
            a = all_incoming_results[0]
            b = not all_incoming_results[1]
            c = all_incoming_results[2]

        else:
            a = all_incoming_results[0]
            b = all_incoming_results[1]
            c = not all_incoming_results[2]
    else:
        pass

    temp = solution(elements[0], a)
    ans_elements.append(temp)

    temp = solution(elements[1], b)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0], ans_elements[1])
    ans_elements.append(temp)

    temp = solution(elements[3], b, c)
    ans_elements.append(temp)

    temp = solution(elements[4], ans_elements[2], ans_elements[3])
    ans_elements.append(temp)

    if call_type == "generate":
        y_in_task_2.append(ans_elements[-1])

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_2(call_type="generate") -> tuple:
    """ Шаблон 2 """

    global all_incoming_results
    global elements_of_gate
    global y_in_task_2

    ans_elements = []
    a = b = c = None

    elements = ['?' for i in range(4)]

    if call_type == "generate":
        a = random.choice(true_false)
        b = random.choice(true_false)
        c = random.choice(true_false)

        all_incoming_results.append(a)
        all_incoming_results.append(b)
        all_incoming_results.append(c)

        elements[0] = random.choice(gates_for_2)
        elements[1] = random.choice(gates_for_2)
        elements[2] = random.choice(gates_for_1)
        elements[3] = random.choice(gates_for_2)

        elements_of_gate = []
        for elem in elements:
            elements_of_gate.append(elem)

    elif call_type == "calculated":
        vari = 0  # Указатель элемента в массиве элементов
        lost_element = temporary_data[0]  # int номер неизвестного входящего значения

        for elem in elements_of_gate:
            elements[vari] = elem
            vari += 1

        if lost_element == 1:
            a = not all_incoming_results[0]
            b = all_incoming_results[1]
            c = all_incoming_results[2]

        elif lost_element == 2:
            a = all_incoming_results[0]
            b = not all_incoming_results[1]
            c = all_incoming_results[2]

        else:
            a = all_incoming_results[0]
            b = all_incoming_results[1]
            c = not all_incoming_results[2]
    else:
        pass

    temp = solution(elements[0], a, b)
    ans_elements.append(temp)

    temp = solution(elements[1], b, c)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0])
    ans_elements.append(temp)

    temp = solution(elements[3], ans_elements[2], ans_elements[1])
    ans_elements.append(temp)

    if call_type == "generate":
        y_in_task_2.append(ans_elements[-1])

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_3(call_type='generate') -> tuple:
    """ Шаблон 3 """

    global all_incoming_results
    global elements_of_gate
    global y_in_task_2

    ans_elements = []
    a = b = c = None

    elements = ['?' for i in range(5)]

    if call_type == "generate":
        a = random.choice(true_false)
        b = random.choice(true_false)
        c = random.choice(true_false)

        all_incoming_results.append(a)
        all_incoming_results.append(b)
        all_incoming_results.append(c)

        elements[0] = random.choice(gates_for_2)
        elements[1] = random.choice(gates_for_2)
        elements[2] = random.choice(gates_for_1)
        elements[3] = random.choice(gates_for_1)
        elements[4] = random.choice(gates_for_2)

        for elem in elements:
            elements_of_gate.append(elem)

    elif call_type == "calculated":
        vari = 0  # Указатель элемента в массиве элементов
        lost_element = temporary_data[0]  # int номер неизвестного входящего значения

        for elem in elements_of_gate:
            elements[vari] = elem
            vari += 1

        if lost_element == 1:
            a = not all_incoming_results[0]
            b = all_incoming_results[1]
            c = all_incoming_results[2]

        elif lost_element == 2:
            a = all_incoming_results[0]
            b = not all_incoming_results[1]
            c = all_incoming_results[2]

        else:
            a = all_incoming_results[0]
            b = all_incoming_results[1]
            c = not all_incoming_results[2]
    else:
        pass
    temp = solution(elements[0], a, b)
    ans_elements.append(temp)

    temp = solution(elements[1], b, c)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0])
    ans_elements.append(temp)

    temp = solution(elements[3], ans_elements[1])
    ans_elements.append(temp)

    temp = solution(elements[4], ans_elements[2], ans_elements[3])
    ans_elements.append(temp)

    if call_type == "generate":
        y_in_task_2.append(ans_elements[-1])

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_4(call_type="generate") -> tuple:
    """ Шаблон 4 """

    global all_incoming_results
    global elements_of_gate
    global y_in_task_2

    ans_elements = []
    a = b = c = None

    elements = ['?' for i in range(5)]

    if call_type == "generate":

        a = random.choice(true_false)
        b = random.choice(true_false)
        c = random.choice(true_false)

        all_incoming_results.append(a)
        all_incoming_results.append(b)
        all_incoming_results.append(c)

        elements[0] = random.choice(gates_for_2)
        elements[1] = random.choice(gates_for_2)
        elements[2] = random.choice(gates_for_2)
        elements[3] = random.choice(gates_for_1)
        elements[4] = random.choice(gates_for_2)

        for elem in elements:
            elements_of_gate.append(elem)

    elif call_type == "calculated":
        vari = 0  # Указатель элемента в массиве элементов
        lost_element = temporary_data[0]  # int номер неизвестного входящего значения

        for elem in elements_of_gate:
            elements[vari] = elem
            vari += 1

        if lost_element == 1:
            a = not all_incoming_results[0]
            b = all_incoming_results[1]
            c = all_incoming_results[2]

        elif lost_element == 2:
            a = all_incoming_results[0]
            b = not all_incoming_results[1]
            c = all_incoming_results[2]

        else:
            a = all_incoming_results[0]
            b = all_incoming_results[1]
            c = not all_incoming_results[2]
    else:
        pass

    temp = solution(elements[0], a, b)
    ans_elements.append(temp)

    temp = solution(elements[1], b, c)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0], ans_elements[1])
    ans_elements.append(temp)

    temp = solution(elements[3], b)
    ans_elements.append(temp)

    temp = solution(elements[4], ans_elements[2], ans_elements[3])
    ans_elements.append(temp)

    if call_type == "generate":
        y_in_task_2.append(ans_elements[-1])

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_5(call_type="generate") -> tuple:
    """ Шаблон 5 """

    global all_incoming_results
    global elements_of_gate
    global y_in_task_2

    ans_elements = []
    a = b = c = None

    elements = ['?' for i in range(5)]

    if call_type == "generate":
        a = random.choice(true_false)
        b = random.choice(true_false)
        c = random.choice(true_false)

        all_incoming_results.append(a)
        all_incoming_results.append(b)
        all_incoming_results.append(c)

        elements[0] = random.choice(gates_for_2)
        elements[1] = random.choice(gates_for_2)
        elements[2] = random.choice(gates_for_1)
        elements[3] = random.choice(gates_for_2)
        elements[4] = random.choice(gates_for_1)

        for elem in elements:
            elements_of_gate.append(elem)

    elif call_type == "calculated":
        vari = 0  # Указатель элемента в массиве элементов
        lost_element = temporary_data[0]  # int номер неизвестного входящего значения

        for elem in elements_of_gate:
            elements[vari] = elem
            vari += 1

        if lost_element == 1:
            a = not all_incoming_results[0]
            b = all_incoming_results[1]
            c = all_incoming_results[2]

        elif lost_element == 2:
            a = all_incoming_results[0]
            b = not all_incoming_results[1]
            c = all_incoming_results[2]

        else:
            a = all_incoming_results[0]
            b = all_incoming_results[1]
            c = not all_incoming_results[2]
    else:
        pass

    temp = solution(elements[0], a, b)
    ans_elements.append(temp)

    temp = solution(elements[1], b, c)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0])
    ans_elements.append(temp)

    temp = solution(elements[3], ans_elements[2], ans_elements[1])
    ans_elements.append(temp)

    temp = solution(elements[4], ans_elements[3])
    ans_elements.append(temp)

    if call_type == "generate":
        y_in_task_2.append(ans_elements[-1])

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_6(call_type="generate") -> tuple:
    """ Шаблон 6 """

    global all_incoming_results
    global elements_of_gate
    global y_in_task_2

    ans_elements = []
    a = b = c = None

    elements = ['?' for i in range(4)]

    if call_type == "generate":
        a = random.choice(true_false)
        b = random.choice(true_false)
        c = random.choice(true_false)

        all_incoming_results.append(a)
        all_incoming_results.append(b)
        all_incoming_results.append(c)

        elements[0] = random.choice(gates_for_2)
        elements[1] = random.choice(gates_for_1)
        elements[2] = random.choice(gates_for_2)
        elements[3] = random.choice(gates_for_2)

        for elem in elements:
            elements_of_gate.append(elem)

    elif call_type == "calculated":
        vari = 0  # Указатель элемента в массиве элементов
        lost_element = temporary_data[0]  # int номер неизвестного входящего значения

        for elem in elements_of_gate:
            elements[vari] = elem
            vari += 1

        if lost_element == 1:
            a = not all_incoming_results[0]
            b = all_incoming_results[1]
            c = all_incoming_results[2]

        elif lost_element == 2:
            a = all_incoming_results[0]
            b = not all_incoming_results[1]
            c = all_incoming_results[2]

        else:
            a = all_incoming_results[0]
            b = all_incoming_results[1]
            c = not all_incoming_results[2]
    else:
        pass

    temp = solution(elements[0], a, b)
    ans_elements.append(temp)

    temp = solution(elements[1], c)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0], ans_elements[1])
    ans_elements.append(temp)

    temp = solution(elements[3], a, ans_elements[2])
    ans_elements.append(temp)

    if call_type == "generate":
        y_in_task_2.append(ans_elements[-1])

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_7(call_type="generate") -> tuple:
    """ Шаблон 7 """

    global all_incoming_results
    global elements_of_gate
    global y_in_task_2

    ans_elements = []
    a = b = c = None

    elements = ['?' for i in range(6)]

    if call_type == "generate":
        a = random.choice(true_false)
        b = random.choice(true_false)
        c = random.choice(true_false)

        all_incoming_results.append(a)
        all_incoming_results.append(b)
        all_incoming_results.append(c)

        elements[0] = random.choice(gates_for_1)
        elements[1] = random.choice(gates_for_1)
        elements[2] = random.choice(gates_for_2)
        elements[3] = random.choice(gates_for_2)
        elements[4] = random.choice(gates_for_2)
        elements[5] = random.choice(gates_for_2)

        for elem in elements:
            elements_of_gate.append(elem)

    elif call_type == "calculated":
        vari = 0  # Указатель элемента в массиве элементов
        lost_element = temporary_data[0]  # int номер неизвестного входящего значения

        for elem in elements_of_gate:
            elements[vari] = elem
            vari += 1

        if lost_element == 1:
            a = not all_incoming_results[0]
            b = all_incoming_results[1]
            c = all_incoming_results[2]

        elif lost_element == 2:
            a = all_incoming_results[0]
            b = not all_incoming_results[1]
            c = all_incoming_results[2]

        else:
            a = all_incoming_results[0]
            b = all_incoming_results[1]
            c = not all_incoming_results[2]
    else:
        pass

    temp = solution(elements[0], a)
    ans_elements.append(temp)

    temp = solution(elements[1], a)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[1], b)
    ans_elements.append(temp)

    temp = solution(elements[3], ans_elements[0], ans_elements[2])
    ans_elements.append(temp)

    temp = solution(elements[4], b, c)
    ans_elements.append(temp)

    temp = solution(elements[5], ans_elements[3], ans_elements[4])
    ans_elements.append(temp)

    if call_type == "generate":
        y_in_task_2.append(ans_elements[-1])

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_8(call_type="generate") -> tuple:
    """ Шаблон 8 """

    global all_incoming_results
    global elements_of_gate
    global y_in_task_2

    ans_elements = []
    a = b = c = None

    elements = ['?' for i in range(5)]

    if call_type == "generate":
        a = random.choice(true_false)
        b = random.choice(true_false)
        c = random.choice(true_false)

        all_incoming_results.append(a)
        all_incoming_results.append(b)
        all_incoming_results.append(c)

        elements[0] = random.choice(gates_for_2)
        elements[1] = random.choice(gates_for_2)
        elements[2] = random.choice(gates_for_1)
        elements[3] = random.choice(gates_for_2)
        elements[4] = random.choice(gates_for_2)

        for elem in elements:
            elements_of_gate.append(elem)

    elif call_type == "calculated":
        vari = 0  # Указатель элемента в массиве элементов
        lost_element = temporary_data[0]  # int номер неизвестного входящего значения

        for elem in elements_of_gate:
            elements[vari] = elem
            vari += 1

        if lost_element == 1:
            a = not all_incoming_results[0]
            b = all_incoming_results[1]
            c = all_incoming_results[2]

        elif lost_element == 2:
            a = all_incoming_results[0]
            b = not all_incoming_results[1]
            c = all_incoming_results[2]

        else:
            a = all_incoming_results[0]
            b = all_incoming_results[1]
            c = not all_incoming_results[2]
    else:
        pass

    temp = solution(elements[0], a, b)
    ans_elements.append(temp)

    temp = solution(elements[1], b, c)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0])
    ans_elements.append(temp)

    temp = solution(elements[3], b, ans_elements[1])
    ans_elements.append(temp)

    temp = solution(elements[4], ans_elements[2], ans_elements[3])
    ans_elements.append(temp)

    if call_type == "generate":
        y_in_task_2.append(ans_elements[-1])

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_9(call_type="generate") -> tuple:
    """ Шаблон 9 """

    global all_incoming_results
    global elements_of_gate
    global y_in_task_2

    ans_elements = []
    a = b = c = None

    elements = ['?' for i in range(6)]

    if call_type == "generate":

        a = random.choice(true_false)
        b = random.choice(true_false)
        c = random.choice(true_false)

        all_incoming_results.append(a)
        all_incoming_results.append(b)
        all_incoming_results.append(c)

        elements[0] = random.choice(gates_for_1)
        elements[1] = random.choice(gates_for_2)
        elements[2] = random.choice(gates_for_2)
        elements[3] = random.choice(gates_for_2)
        elements[4] = random.choice(gates_for_1)
        elements[5] = random.choice(gates_for_2)

        for elem in elements:
            elements_of_gate.append(elem)

    elif call_type == "calculated":
        vari = 0  # Указатель элемента в массиве элементов
        lost_element = temporary_data[0]  # int номер неизвестного входящего значения

        for elem in elements_of_gate:
            elements[vari] = elem
            vari += 1

        if lost_element == 1:
            a = not all_incoming_results[0]
            b = all_incoming_results[1]
            c = all_incoming_results[2]

        elif lost_element == 2:
            a = all_incoming_results[0]
            b = not all_incoming_results[1]
            c = all_incoming_results[2]

        else:
            a = all_incoming_results[0]
            b = all_incoming_results[1]
            c = not all_incoming_results[2]
    else:
        pass

    temp = solution(elements[0], a)
    ans_elements.append(temp)

    temp = solution(elements[1], a, b)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0], ans_elements[1])
    ans_elements.append(temp)

    temp = solution(elements[3], b, c)
    ans_elements.append(temp)

    temp = solution(elements[4], ans_elements[3])
    ans_elements.append(temp)

    temp = solution(elements[5], ans_elements[2], ans_elements[4])
    ans_elements.append(temp)

    if call_type == "generate":
        y_in_task_2.append(ans_elements[-1])

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_10(call_type="generate") -> tuple:
    """ Шаблон 10 """

    global all_incoming_results
    global elements_of_gate
    global y_in_task_2

    ans_elements = []
    a = b = c = None

    elements = ['?' for i in range(5)]

    if call_type == "generate":

        a = random.choice(true_false)
        b = random.choice(true_false)
        c = random.choice(true_false)

        all_incoming_results.append(a)
        all_incoming_results.append(b)
        all_incoming_results.append(c)

        elements[0] = random.choice(gates_for_2)
        elements[1] = random.choice(gates_for_2)
        elements[2] = random.choice(gates_for_2)
        elements[3] = random.choice(gates_for_1)
        elements[4] = random.choice(gates_for_2)

        for elem in elements:
            elements_of_gate.append(elem)

    elif call_type == "calculated":
        vari = 0  # Указатель элемента в массиве элементов
        lost_element = temporary_data[0]  # int номер неизвестного входящего значения

        for elem in elements_of_gate:
            elements[vari] = elem
            vari += 1

        if lost_element == 1:
            a = not all_incoming_results[0]
            b = all_incoming_results[1]
            c = all_incoming_results[2]

        elif lost_element == 2:
            a = all_incoming_results[0]
            b = not all_incoming_results[1]
            c = all_incoming_results[2]

        else:
            a = all_incoming_results[0]
            b = all_incoming_results[1]
            c = not all_incoming_results[2]
    else:
        pass

    temp = solution(elements[0], a, b)
    ans_elements.append(temp)

    temp = solution(elements[1], ans_elements[0], c)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0], ans_elements[1])
    ans_elements.append(temp)

    temp = solution(elements[3], c)
    ans_elements.append(temp)

    temp = solution(elements[4], ans_elements[2], ans_elements[3])
    ans_elements.append(temp)

    if call_type == "generate":
        y_in_task_2.append(ans_elements[-1])

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_11(call_type="generate") -> tuple:
    """ Шаблон 11 """

    global all_incoming_results
    global elements_of_gate
    global y_in_task_2

    ans_elements = []
    a = b = c = None

    elements = ['?' for i in range(5)]

    if call_type == "generate":
        a = random.choice(true_false)
        b = random.choice(true_false)
        c = random.choice(true_false)

        all_incoming_results.append(a)
        all_incoming_results.append(b)
        all_incoming_results.append(c)

        elements[0] = random.choice(gates_for_2)
        elements[1] = random.choice(gates_for_2)
        elements[2] = random.choice(gates_for_1)
        elements[3] = random.choice(gates_for_2)
        elements[4] = random.choice(gates_for_2)

        for elem in elements:
            elements_of_gate.append(elem)

    elif call_type == "calculated":
        vari = 0  # Указатель элемента в массиве элементов
        lost_element = temporary_data[0]  # int номер неизвестного входящего значения

        for elem in elements_of_gate:
            elements[vari] = elem
            vari += 1

        if lost_element == 1:
            a = not all_incoming_results[0]
            b = all_incoming_results[1]
            c = all_incoming_results[2]

        elif lost_element == 2:
            a = all_incoming_results[0]
            b = not all_incoming_results[1]
            c = all_incoming_results[2]

        else:
            a = all_incoming_results[0]
            b = all_incoming_results[1]
            c = not all_incoming_results[2]
    else:
        pass

    temp = solution(elements[0], a, b)
    ans_elements.append(temp)

    temp = solution(elements[1], b, c)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0])
    ans_elements.append(temp)

    temp = solution(elements[3], ans_elements[0], ans_elements[1])
    ans_elements.append(temp)

    temp = solution(elements[4], ans_elements[2], ans_elements[3])
    ans_elements.append(temp)

    if call_type == "generate":
        y_in_task_2.append(ans_elements[-1])

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_12() -> tuple:
    """ Шаблон 12 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = ['?' for i in range(6)]

    elements[0] = random.choice(gates_for_1)
    elements[1] = random.choice(gates_for_2)
    elements[2] = random.choice(gates_for_1)
    elements[3] = random.choice(gates_for_2)
    elements[4] = random.choice(gates_for_2)
    elements[5] = random.choice(gates_for_2)

    ans_elements = []

    temp = solution(elements[0], a)
    ans_elements.append(temp)

    temp = solution(elements[1], a, b)
    ans_elements.append(temp)

    temp = solution(elements[2], b)
    ans_elements.append(temp)

    temp = solution(elements[3], ans_elements[0], ans_elements[1])
    ans_elements.append(temp)

    temp = solution(elements[4], ans_elements[1], ans_elements[2])
    ans_elements.append(temp)

    temp = solution(elements[5], ans_elements[3], ans_elements[4])
    ans_elements.append(temp)

    return elements, a, b, c, ans_elements[-1], ans_elements


def solution(operation, enter_a, enter_b=True, enter_c=True) -> bool:
    """ Решение выражения с заданным действием и параметрами """

    # Выражения с 1 входящим значением
    if operation == 'not':
        return lg.log_NOT(enter_a)
    elif operation == 'buf':
        return lg.log_BUF(enter_a)

    # Выражения с 2 входящими значениеми
    elif operation == 'and':
        return lg.log_AND(enter_a, enter_b)
    elif operation == 'or':
        return lg.log_OR(enter_a, enter_b)
    elif operation == 'xor':
        return lg.log_XOR(enter_a, enter_b)
    elif operation == 'nand':
        return lg.log_NAND(enter_a, enter_b)
    elif operation == 'nor':
        return lg.log_NOR(enter_a, enter_b)
    elif operation == 'xnor':
        return lg.log_XNOR(enter_a, enter_b)

    # Выражения с 3 входящими значениеми
    else:
        return lg.log_NOR3(enter_a, enter_b, enter_c)


def reference_call(logic_gate: str, name_reference: str):
    """ Вывод справки по определенному элементу
        Принимает фактическое название элемента и название элемента в системе """

    for widget in frame_reference.winfo_children():
        widget.destroy()

    frame_reference.config(relief=RIDGE, borderwidth=2)
    Label(frame_reference, text=name_reference, font="Arial 15").grid(column=0, row=0, columnspan=2, sticky="we")
    Label(frame_reference, text="Обозначения", font="Arial 13").grid(column=0, row=1)
    Label(frame_reference, text="Таблица истинности:", font="Arial 13", padx=7, pady=5).grid(column=1, row=1)

    Label(frame_reference, image=gates_styles["iec"][logic_gate], padx=7, pady=5).grid(column=0, row=2)
    Label(frame_reference, image=gates_styles["ansi"][logic_gate], padx=7, pady=5).grid(column=0, row=3)
    Label(frame_reference, image=gates_styles["log"][logic_gate], padx=7, pady=5).grid(column=0, row=4)
    Label(frame_reference, image=truth_table[logic_gate], padx=7, pady=5).grid(column=1, row=2)


def reference_buf(_):  # event
    """ Справка buf """

    reference_call(logic_gate="buf", name_reference="БУФФЕР")


def reference_not(_):
    """ Справка not """

    reference_call(logic_gate="not", name_reference="НЕ")


def reference_and(_):
    """ Справка and """

    reference_call(logic_gate="and", name_reference="И")


def reference_or(_):
    """ Справка or """

    reference_call(logic_gate="or", name_reference="ИЛИ")


def reference_xor(_):
    """ Справка xor """

    reference_call(logic_gate="xor", name_reference="Исключающее ИЛИ")


def reference_nand(_):
    """ Справка nand """

    reference_call(logic_gate="nand", name_reference="И-НЕ")


def reference_nor(_):
    """ Справка nor """

    reference_call(logic_gate="nor", name_reference="ИЛИ-НЕ")


def reference_xnor(_):
    """ Справка xnor """

    reference_call(logic_gate="xnor", name_reference="Исключающее ИЛИ-НЕ")


def choice_from_gates(element: str, index_1: int, index_2: int, ans_element=True, call_type=1):
    """ Определяет какой элемент отрисовывать и настраивает нажание на объект """

    global temporary_elements_and_index
    elements = {
        'buf': "buf",
        'not': "not",
        'and': "and",
        'or': "or",
        'xor': "xor",
        'nand': "nand",
        'nor': "nor",
        'xnor': "xnor"
    }

    commands = {
        'buf': reference_buf,
        'not': reference_not,
        'and': reference_and,
        'or': reference_or,
        'xor': reference_xor,
        'nand': reference_nand,
        'nor': reference_nor,
        'xnor': reference_xnor
    }

    if call_type == 1:
        temporary_elements_and_index.append(element)
        temporary_elements_and_index.append(index_1)
        temporary_elements_and_index.append(index_2)

    name = str(index_1) + '_' + str(index_2)
    global temporary_data_for_task_3
    temporary_data_for_task_3[name] = [ans_element, index_1, index_2]

    lbl = Label(frame_gates, image=gates_styles[style][elements[element]])
    lbl.grid(row=index_1, column=index_2)
    if training_mode == "learning" or training_mode == "training":
        lbl.bind("<Button-1>", commands[element])


def contact_drawing(number: int, index_1: int, index_2: int):
    """ Отрисовка контактов """
    lines = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "11",
        12: "12",
        13: "13",
        14: "14"
    }

    image_number = lines[number]

    lbl = Label(frame_gates, image=image_of_lines["basic"][image_number])
    lbl.image_number = image_number  # Записывает в объект номер базовой картинки
    lbl.image_last_word = ""  # Записывает в объект окончание названия (для базового он пуст)
    lbl.image_index_1 = index_1
    lbl.image_index_2 = index_2

    lbl.grid(row=index_1, column=index_2)
    lbl.bind("<Button-1>", change_to_true)
    lbl.bind("<Button-3>", change_to_false)


def change_to_true(event):
    """ Изменение цвета элемента при нажатии на левую кнопку мыши
        true-true -> true-false -> false-true -> false-false
        true -> false """

    num = event.widget.image_number  # Возвращает номер используемой картинки
    last = event.widget.image_last_word  # Возвращает цвет текущей картинки, если он есть
    index_1 = event.widget.image_index_1
    index_2 = event.widget.image_index_2
    global answer_user_for_task_3

    if num not in ["3", "6", "7", "8"]:
        if last == "" or last == "_red":
            a = num + "_green"
            event.widget.image_last_word = "_green"
            event.widget["image"] = image_of_lines["color"]["green"][a]
        elif last == "_green":
            a = num + "_red"
            event.widget.image_last_word = "_red"
            event.widget["image"] = image_of_lines["color"]["red"][a]
        else:
            pass

        name = str(index_1) + '_' + str(index_2 - 1)
        if last == "_green":
            answer_user_for_task_3[name] = [False, index_1, index_2 - 1]
        else:
            answer_user_for_task_3[name] = [True, index_1, index_2 - 1]

    # Обработка элемента с 2 линиями
    array_of_last_word = ["_green_green", "_green_red", "_red_green", "_red_red"]

    if num in ["3", "6", "7", "8"]:
        if last == "" or last == array_of_last_word[3]:
            a = num + "_green_green"
            event.widget.image_last_word = "_green_green"
            event.widget["image"] = image_of_lines["color"]["multi"][a]
        elif last == array_of_last_word[0]:
            a = num + "_green_red"
            event.widget.image_last_word = "_green_red"
            event.widget["image"] = image_of_lines["color"]["multi"][a]
        elif last == array_of_last_word[1]:
            a = num + "_red_green"
            event.widget.image_last_word = "_red_green"
            event.widget["image"] = image_of_lines["color"]["multi"][a]
        elif last == array_of_last_word[2]:
            a = num + "_red_red"
            event.widget.image_last_word = "_red_red"
            event.widget["image"] = image_of_lines["color"]["multi"][a]
        else:
            pass


def change_to_false(event):
    """ Изменение цвета элемента при нажатии на правую кнопку мыши """

    num = event.widget.image_number  # Возвращает номер используемой картинки
    index_1 = event.widget.image_index_1
    index_2 = event.widget.image_index_2

    event.widget.image_last_word = ""
    event.widget["image"] = image_of_lines["basic"][num]

    # Удалить из словаря
    name = str(index_1) + '_' + str(index_2 - 1)
    global answer_user_for_task_3
    del answer_user_for_task_3[name]
    print(answer_user_for_task_3)


def choice_from_0_1(vari: bool, index_1: int, index_2: int):
    """ Определяет какой элемент отрисовывать на входах и выходе """

    if vari:
        Label(frame_gates, image=image_of_gates["true"]).grid(row=index_1, column=index_2)
    elif not vari:
        Label(frame_gates, image=image_of_gates["false"]).grid(row=index_1, column=index_2)
    else:
        pass


def writing_to_temporary_data(a: bool, b: bool, c: bool, y: bool):
    """ В зависимости от необходимого входа или выхода помещает в временное хранилище нужное значение"""

    if type_of_task == "task_1" or type_of_task == "task_3":
        temporary_data.append(y)
    elif type_of_task == "task_2":
        if temporary_data[0] == 1:
            temporary_data.append(a)
        elif temporary_data[0] == 2:
            temporary_data.append(b)
        else:
            temporary_data.append(c)
    else:
        pass


def choice_from_signal_image(index_1: int, index_2: int, signal: bool, this_letter: int):
    """ Отрисовка входящих или выходящего сигнала в заданиях """

    if (type_of_task == "task_1" or type_of_task == "task_3") and this_letter == 4:
        Label(frame_gates, image=image_of_gates["y"]).grid(row=index_1, column=index_2)
        temporary_index.append(index_1)
        temporary_index.append(index_2)
    elif (type_of_task == "task_1" or type_of_task == "task_3") and this_letter != 4:
        choice_from_0_1(signal, index_1, index_2)

    elif type_of_task == "task_2":
        if temporary_data[0] == this_letter:
            Label(frame_gates, image=image_of_gates["question"]).grid(row=index_1, column=index_2)
            temporary_index.append(index_1)
            temporary_index.append(index_2)
        else:
            choice_from_0_1(signal, index_1, index_2)


def circuit_1():
    """ Прорисовка 1 варианта """

    elements_in_circuit = pattern_1()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    ans_elements = elements_in_circuit[5]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(index_1=0, index_2=0, signal=a, this_letter=1)
    contact_drawing(number=1, index_1=0, index_2=1)
    choice_from_gates(elements[0], 0, 2, ans_elements[0])
    contact_drawing(number=2, index_1=0, index_2=3)

    # 2 строка
    contact_drawing(number=3, index_1=1, index_2=3)
    choice_from_gates(elements[2], 1, 4, ans_elements[2])
    contact_drawing(number=2, index_1=1, index_2=5)

    # 3 строка
    choice_from_signal_image(2, 0, b, 2)
    contact_drawing(number=4, index_1=2, index_2=1)
    choice_from_gates(elements[1], 2, 2, ans_elements[1])
    contact_drawing(number=5, index_1=2, index_2=3)
    contact_drawing(number=3, index_1=2, index_2=5)
    choice_from_gates(elements[4], 2, 6, ans_elements[4])
    contact_drawing(number=1, index_1=2, index_2=7)
    choice_from_signal_image(2, 8, y, 4)

    # 4 строка
    contact_drawing(number=12, index_1=3, index_2=1)
    contact_drawing(number=1, index_1=3, index_2=2)
    contact_drawing(number=2, index_1=3, index_2=3)
    contact_drawing(11, 3, 5)

    # 5 строка
    contact_drawing(number=3, index_1=4, index_2=3)
    choice_from_gates(elements[3], 4, 4, ans_elements[3])
    contact_drawing(number=5, index_1=4, index_2=5)

    # 6 строка
    choice_from_signal_image(5, 0, c, 3)
    contact_drawing(number=1, index_1=5, index_2=1)
    contact_drawing(number=1, index_1=5, index_2=2)
    contact_drawing(number=5, index_1=5, index_2=3)


def circuit_2():
    """ Прорисовка 2 варианта """

    elements_in_circuit = pattern_2()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    ans_elements = elements_in_circuit[5]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    contact_drawing(number=1, index_1=0, index_2=1)
    contact_drawing(number=2, index_1=0, index_2=2)

    # 2 строка
    contact_drawing(number=3, index_1=1, index_2=2)
    choice_from_gates(elements[0], 1, 3, ans_elements[0])
    contact_drawing(number=1, index_1=1, index_2=4)
    choice_from_gates(elements[2], 1, 5, ans_elements[2])
    contact_drawing(number=2, index_1=1, index_2=6)

    # 3 строка
    choice_from_signal_image(2, 0, b, 2)
    contact_drawing(number=4, index_1=2, index_2=1)
    contact_drawing(number=5, index_1=2, index_2=2)
    contact_drawing(number=3, index_1=2, index_2=6)
    choice_from_gates(elements[3], 2, 7, ans_elements[3])
    contact_drawing(number=1, index_1=2, index_2=8)
    choice_from_signal_image(2, 9, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, c, 3)
    contact_drawing(number=6, index_1=3, index_2=1)
    choice_from_gates(elements[1], 3, 2, ans_elements[1])
    contact_drawing(number=1, index_1=3, index_2=3)
    contact_drawing(number=1, index_1=3, index_2=4)
    contact_drawing(number=1, index_1=3, index_2=5)
    contact_drawing(number=5, index_1=3, index_2=6)


def circuit_3():
    """ Прорисовка 3 варианта """

    elements_in_circuit = pattern_3()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    ans_elements = elements_in_circuit[5]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    contact_drawing(number=7, index_1=0, index_2=1)
    choice_from_gates(elements[0], 0, 2, ans_elements[0])
    contact_drawing(number=1, index_1=0, index_2=3)
    choice_from_gates(elements[2], 0, 4, ans_elements[2])
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    contact_drawing(number=10, index_1=1, index_2=1)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[4], 1, 6, ans_elements[4])
    contact_drawing(number=1, index_1=1, index_2=7)
    choice_from_signal_image(1, 8, y, 4)

    # 3 строка
    choice_from_signal_image(2, 0, c, 3)
    contact_drawing(number=6, index_1=2, index_2=1)
    choice_from_gates(elements[1], 2, 2, ans_elements[1])
    contact_drawing(number=1, index_1=2, index_2=3)
    choice_from_gates(elements[3], 2, 4, ans_elements[3])
    contact_drawing(number=5, index_1=2, index_2=5)


def circuit_4():
    """ Прорисовка 4 варианта """

    elements_in_circuit = pattern_4()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    ans_elements = elements_in_circuit[5]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    contact_drawing(number=7, index_1=0, index_2=1)
    choice_from_gates(elements[0], 0, 2, ans_elements[0])
    contact_drawing(number=1, index_1=0, index_2=3)
    contact_drawing(number=1, index_1=0, index_2=4)
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    contact_drawing(number=11, index_1=1, index_2=1)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[2], 1, 6, ans_elements[2])
    contact_drawing(number=2, index_1=1, index_2=7)

    # 3 строка
    contact_drawing(number=11, index_1=2, index_2=1)
    choice_from_signal_image(2, 2, c, 3)
    contact_drawing(number=7, index_1=2, index_2=3)
    choice_from_gates(elements[1], 2, 4, ans_elements[1])
    contact_drawing(number=5, index_1=2, index_2=5)
    contact_drawing(number=3, index_1=2, index_2=7)
    choice_from_gates(elements[4], 2, 8, ans_elements[4])
    contact_drawing(number=1, index_1=2, index_2=9)
    choice_from_signal_image(2, 10, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, b, 2)
    contact_drawing(number=9, index_1=3, index_2=1)
    contact_drawing(number=1, index_1=3, index_2=2)
    contact_drawing(number=9, index_1=3, index_2=3)
    contact_drawing(number=1, index_1=3, index_2=4)
    choice_from_gates(elements[3], 3, 5, ans_elements[3])
    contact_drawing(number=1, index_1=3, index_2=6)
    contact_drawing(number=5, index_1=3, index_2=7)


def circuit_5():
    """ Прорисовка 5 варианта """

    elements_in_circuit = pattern_5()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    ans_elements = elements_in_circuit[5]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    contact_drawing(number=7, index_1=0, index_2=1)
    choice_from_gates(elements[0], 0, 2, ans_elements[0])
    contact_drawing(number=1, index_1=0, index_2=3)
    choice_from_gates(elements[2], 0, 4, ans_elements[2])
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    contact_drawing(number=10, index_1=1, index_2=1)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[3], 1, 6, ans_elements[3])
    contact_drawing(number=1, index_1=1, index_2=7)
    choice_from_gates(elements[4], 1, 8, ans_elements[4])
    contact_drawing(number=1, index_1=1, index_2=9)
    choice_from_signal_image(1, 10, y, 4)

    # 3 строка
    choice_from_signal_image(2, 0, c, 3)
    contact_drawing(number=6, index_1=2, index_2=1)
    choice_from_gates(elements[1], 2, 2, ans_elements[1])
    contact_drawing(number=1, index_1=2, index_2=3)
    contact_drawing(number=1, index_1=2, index_2=4)
    contact_drawing(number=5, index_1=2, index_2=5)


def circuit_6():
    """ Прорисовка 6 варианта """

    elements_in_circuit = pattern_6()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    ans_elements = elements_in_circuit[5]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    contact_drawing(number=4, index_1=0, index_2=1)
    contact_drawing(number=1, index_1=0, index_2=2)
    contact_drawing(number=1, index_1=0, index_2=3)
    contact_drawing(number=1, index_1=0, index_2=4)
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    contact_drawing(number=3, index_1=1, index_2=1)
    choice_from_gates(elements[0], 1, 2, ans_elements[0])
    contact_drawing(number=2, index_1=1, index_2=3)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[3], 1, 6, ans_elements[3])
    contact_drawing(number=1, index_1=1, index_2=7)
    choice_from_signal_image(1, 8, y, 4)

    # 3 строка
    choice_from_0_1(b, 3, 0)
    choice_from_signal_image(2, 0, b, 2)
    contact_drawing(number=5, index_1=2, index_2=1)
    contact_drawing(number=3, index_1=2, index_2=3)
    choice_from_gates(elements[2], 2, 4, ans_elements[2])
    contact_drawing(number=5, index_1=2, index_2=5)

    # 4 строка
    choice_from_0_1(c, 3, 0)
    choice_from_signal_image(3, 0, c, 3)
    contact_drawing(number=1, index_1=3, index_2=1)
    choice_from_gates(elements[1], 3, 2, ans_elements[1])
    contact_drawing(number=5, index_1=3, index_2=3)


def circuit_7():
    """ Прорисовка 7 варианта """

    elements_in_circuit = pattern_7()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    ans_elements = elements_in_circuit[5]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    contact_drawing(number=13, index_1=0, index_2=1)
    contact_drawing(number=1, index_1=0, index_2=2)
    choice_from_gates(elements[0], 0, 3, ans_elements[0])
    contact_drawing(number=1, index_1=0, index_2=4)
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    choice_from_signal_image(1, 0, a, 1)
    contact_drawing(number=9, index_1=1, index_2=1)
    choice_from_gates(elements[1], 1, 2, ans_elements[1])
    contact_drawing(number=2, index_1=1, index_2=3)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[3], 1, 6, ans_elements[3])
    contact_drawing(number=2, index_1=1, index_2=7)

    # 3 строка
    contact_drawing(number=3, index_1=2, index_2=3)
    choice_from_gates(elements[2], 2, 4, ans_elements[2])
    contact_drawing(number=5, index_1=2, index_2=5)
    contact_drawing(number=3, index_1=2, index_2=7)
    choice_from_gates(elements[5], 2, 8, ans_elements[5])
    contact_drawing(number=1, index_1=2, index_2=9)
    choice_from_signal_image(2, 10, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, b, 2)
    contact_drawing(number=4, index_1=3, index_2=1)
    contact_drawing(number=1, index_1=3, index_2=2)
    contact_drawing(number=5, index_1=3, index_2=3)
    contact_drawing(number=11, index_1=3, index_2=7)

    # 5 строка
    choice_from_signal_image(4, 0, c, 3)
    contact_drawing(number=6, index_1=4, index_2=1)
    choice_from_gates(elements[4], 4, 2, ans_elements[4])
    contact_drawing(number=1, index_1=4, index_2=3)
    contact_drawing(number=1, index_1=4, index_2=4)
    contact_drawing(number=1, index_1=4, index_2=5)
    contact_drawing(number=1, index_1=4, index_2=6)
    contact_drawing(number=5, index_1=4, index_2=7)


def circuit_8():
    """ Прорисовка 8 варианта """

    elements_in_circuit = pattern_8()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    ans_elements = elements_in_circuit[5]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    contact_drawing(number=7, index_1=0, index_2=1)
    choice_from_gates(elements[0], 0, 2, ans_elements[0])
    contact_drawing(number=1, index_1=0, index_2=3)
    choice_from_gates(elements[2], 0, 4, ans_elements[2])
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    contact_drawing(number=14, index_1=1, index_2=1)
    contact_drawing(number=1, index_1=1, index_2=2)
    contact_drawing(number=2, index_1=1, index_2=3)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[4], 1, 6, ans_elements[4])
    contact_drawing(number=1, index_1=1, index_2=7)
    choice_from_signal_image(1, 8, y, 4)

    # 3 строка
    contact_drawing(number=11, index_1=2, index_2=1)
    contact_drawing(number=3, index_1=2, index_2=3)
    choice_from_gates(elements[3], 2, 4, ans_elements[3])
    contact_drawing(number=5, index_1=2, index_2=5)

    # 4 строка
    choice_from_signal_image(3, 0, c, 3)
    contact_drawing(number=6, index_1=3, index_2=1)
    choice_from_gates(elements[1], 3, 2, ans_elements[1])
    contact_drawing(number=5, index_1=3, index_2=3)


def circuit_9():
    """ Прорисовка 9 варианта """

    elements_in_circuit = pattern_9()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    ans_elements = elements_in_circuit[5]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    contact_drawing(number=13, index_1=0, index_2=1)
    choice_from_gates(elements[0], 0, 2, ans_elements[0])
    contact_drawing(number=2, index_1=0, index_2=3)

    # 2 строка
    choice_from_signal_image(1, 0, a, 1)
    contact_drawing(number=10, index_1=1, index_2=1)
    contact_drawing(number=3, index_1=1, index_2=3)
    choice_from_gates(elements[2], 1, 4, ans_elements[2])
    contact_drawing(number=2, index_1=1, index_2=5)

    # 3 строка
    contact_drawing(number=3, index_1=2, index_2=1)
    choice_from_gates(elements[1], 2, 2, ans_elements[1])
    contact_drawing(number=5, index_1=2, index_2=3)
    contact_drawing(number=3, index_1=2, index_2=5)
    choice_from_gates(elements[5], 2, 6, ans_elements[5])
    contact_drawing(number=1, index_1=2, index_2=7)
    choice_from_signal_image(2, 8, y, 4)
    choice_from_signal_image(3, 0, b, 2)

    # 5 строка
    contact_drawing(number=10, index_1=3, index_2=1)
    contact_drawing(number=11, index_1=3, index_2=5)

    # 5 строка
    choice_from_signal_image(4, 0, c, 3)
    contact_drawing(number=6, index_1=4, index_2=1)
    choice_from_gates(elements[3], 4, 2, ans_elements[3])
    contact_drawing(number=1, index_1=4, index_2=3)
    choice_from_gates(elements[4], 4, 4, ans_elements[4])
    contact_drawing(number=5, index_1=4, index_2=5)


def circuit_10():
    """ Прорисовка 10 варианта """

    elements_in_circuit = pattern_10()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    ans_elements = elements_in_circuit[5]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    contact_drawing(number=7, index_1=0, index_2=1)
    choice_from_gates(elements[0], 0, 2, ans_elements[0])
    contact_drawing(number=4, index_1=0, index_2=3)
    contact_drawing(number=1, index_1=0, index_2=4)
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    contact_drawing(number=5, index_1=1, index_2=1)
    contact_drawing(number=11, index_1=1, index_2=3)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[2], 1, 6, ans_elements[2])
    contact_drawing(number=2, index_1=1, index_2=7)

    # 3 строка
    contact_drawing(number=3, index_1=2, index_2=3)
    choice_from_gates(elements[1], 2, 4, ans_elements[1])
    contact_drawing(number=5, index_1=2, index_2=5)
    contact_drawing(number=3, index_1=2, index_2=7)
    choice_from_gates(elements[4], 2, 8, ans_elements[4])
    contact_drawing(number=1, index_1=2, index_2=9)
    choice_from_signal_image(2, 10, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, c, 3)
    contact_drawing(number=1, index_1=3, index_2=1)
    contact_drawing(number=1, index_1=3, index_2=2)
    contact_drawing(number=10, index_1=3, index_2=3)
    contact_drawing(number=11, index_1=3, index_2=7)

    # 5 строка
    contact_drawing(number=12, index_1=4, index_2=3)
    contact_drawing(number=1, index_1=4, index_2=4)
    choice_from_gates(elements[3], 4, 5, ans_elements[3])
    contact_drawing(number=1, index_1=4, index_2=6)
    contact_drawing(number=5, index_1=4, index_2=7)


def circuit_11():
    """ Прорисовка 11 варианта """

    elements_in_circuit = pattern_11()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    ans_elements = elements_in_circuit[5]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    contact_drawing(number=7, index_1=0, index_2=1)
    choice_from_gates(elements[0], 0, 2, ans_elements[0])
    contact_drawing(number=4, index_1=0, index_2=3)
    choice_from_gates(elements[2], 0, 4, ans_elements[2])
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    contact_drawing(number=10, index_1=1, index_2=1)
    contact_drawing(number=11, index_1=1, index_2=3)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[4], 1, 6, ans_elements[4])
    contact_drawing(number=1, index_1=1, index_2=7)
    choice_from_signal_image(1, 8, y, 4)

    # 3 строка
    contact_drawing(number=11, index_1=2, index_2=1)
    contact_drawing(number=3, index_1=2, index_2=3)
    choice_from_gates(elements[3], 2, 4, ans_elements[3])
    contact_drawing(number=5, index_1=2, index_2=5)

    # 4 строка
    choice_from_signal_image(3, 0, c, 3)
    contact_drawing(number=6, index_1=3, index_2=1)
    choice_from_gates(elements[1], 3, 2, ans_elements[1])
    contact_drawing(number=5, index_1=3, index_2=3)


def circuit_12():
    """ Прорисовка 12 варианта """

    elements_in_circuit = pattern_12()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    ans_elements = elements_in_circuit[5]

    if type_of_task == "task_1" or type_of_task == "task_3":
        temporary_data.append(y)
    elif type_of_task == "task_2":
        if temporary_data[0] == 1:
            temporary_data.append(a)
        elif temporary_data[0] == 2:
            temporary_data.append(b)
        else:
            temporary_data.append(c)
    else:
        pass

    # 1 строка
    contact_drawing(number=13, index_1=0, index_2=1)
    choice_from_gates(elements[0], 0, 2, ans_elements[0])
    contact_drawing(number=2, index_1=0, index_2=3)

    # 2 строка
    choice_from_signal_image(1, 0, a, 1)
    contact_drawing(number=10, index_1=1, index_2=1)
    contact_drawing(number=3, index_1=1, index_2=3)
    choice_from_gates(elements[3], 1, 4, ans_elements[3])
    contact_drawing(number=2, index_1=1, index_2=5)

    # 3 строка
    contact_drawing(number=3, index_1=2, index_2=1)
    choice_from_gates(elements[1], 2, 2, ans_elements[1])
    contact_drawing(number=10, index_1=2, index_2=3)
    contact_drawing(number=3, index_1=2, index_2=5)
    choice_from_gates(elements[5], 2, 6, ans_elements[5])
    contact_drawing(number=1, index_1=2, index_2=7)
    choice_from_signal_image(2, 8, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, b, 2)
    contact_drawing(number=10, index_1=3, index_2=1)
    contact_drawing(number=3, index_1=3, index_2=3)
    choice_from_gates(elements[4], 3, 4, ans_elements[4])
    contact_drawing(number=5, index_1=3, index_2=5)

    # 5 строка
    contact_drawing(number=12, index_1=4, index_2=1)
    choice_from_gates(elements[2], 4, 2, ans_elements[2])
    contact_drawing(number=5, index_1=4, index_2=3)


def answer_user_true():
    """ Вызывает функцию обработки ответа с True """

    answer_user(True)


def answer_user_false():
    """ Вызывает функцию обработки ответа с False """

    answer_user(False)


def answer_user(answer: bool):
    """ Принимает ответ пользователя из формы """

    global right_answers
    global number_of_tasks
    global number_of_intermediate_elements
    global right_intermediate_answers
    global right_answers_type_1
    global right_answers_type_2
    global right_answers_type_3

    for widget in frame_task.winfo_children():
        widget.destroy()

    """ Реакция на ответ 1 задания """
    if type_of_task == "task_1" and (training_mode == 'learning' or training_mode == 'training'):
        if answer == temporary_data[-1]:
            right_answers += 1
            Label(frame_task,
                  text='Ответ верный', font="Arial 15").grid(row=0, column=0, sticky="nw", padx=20, pady=20)
        else:
            Label(frame_task,
                  text='Ответ неверный', font="Arial 15").grid(row=0, column=0, sticky="nw", padx=20, pady=20)
        if temporary_data[-1]:
            Label(frame_gates, image=image_of_gates["true"]).grid(row=temporary_index[0], column=temporary_index[1])
        else:
            Label(frame_gates, image=image_of_gates["false"]).grid(row=temporary_index[0], column=temporary_index[1])

    elif type_of_task == "task_1" and training_mode == 'control':
        if answer == temporary_data[-1]:
            right_answers += 1
            right_answers_type_1 += 1

    """ Реакция на ответ 2 задания """
    if type_of_task == "task_2":
        if answer == temporary_data[-1]:  # Если ответ пользователя совпал с правильным ответом
            right_answers += 1
            if training_mode == 'control':
                right_answers_type_2 += 1
            if training_mode == 'learning' or training_mode == 'training':
                Label(frame_task,
                      text='Ответ верный', font="Arial 15").grid(row=0, column=0, sticky="nw", padx=20, pady=20)

                if temporary_data[-1]:
                    Label(frame_gates, image=image_of_gates["true"]).grid(row=temporary_index[0], column=temporary_index[1])
                else:
                    Label(frame_gates, image=image_of_gates["false"]).grid(row=temporary_index[0], column=temporary_index[1])

        else:  # Ответ пользоваетеля не совпал
            patterns = {
                1: pattern_1,
                2: pattern_2,
                3: pattern_3,
                4: pattern_4,
                5: pattern_5,
                6: pattern_6,
                7: pattern_7,
                8: pattern_8,
                9: pattern_9,
                10: pattern_10,
                11: pattern_11,
                12: pattern_12
            }

            output_from_function = patterns[number_of_pattern](call_type="calculated")

            if output_from_function[4] == y_in_task_2[-1]:  # Если перерасчет одинаков
                right_answers += 1
                if training_mode == 'control':
                    right_answers_type_2 += 1
                if training_mode == 'learning' or training_mode == 'training':
                    Label(frame_task,
                          text='Ответ верный', font="Arial 15").grid(row=0, column=0, sticky="nw", padx=20, pady=20)
                    if answer:
                        Label(frame_gates, image=image_of_gates["true"]).grid(row=temporary_index[0], column=temporary_index[1])
                    else:
                        Label(frame_gates, image=image_of_gates["false"]).grid(row=temporary_index[0], column=temporary_index[1])

            else:  # Если перерасчет не одинаков
                if training_mode == 'learning' or training_mode == 'training':
                    Label(frame_task,
                          text='Ответ неверный', font="Arial 15").grid(row=0, column=0, sticky="nw", padx=20, pady=20)
                    if temporary_data[-1]:
                        Label(frame_gates, image=image_of_gates["true"]).grid(row=temporary_index[0], column=temporary_index[1])
                    else:
                        Label(frame_gates, image=image_of_gates["false"]).grid(row=temporary_index[0], column=temporary_index[1])

    """ Реакция на  ответ 3 задания """
    if type_of_task == "task_3":

        right_answer = 0  # Счетчик правильных промежуточных ответов
        max_y = -1  # Y координата последнего элемента
        intermediate_elements = len(list(temporary_data_for_task_3.keys())) - 1  # Количество промежуточных элементов
        keys = list(temporary_data_for_task_3.keys())

        # Вычисляет максимальное y
        try:
            for key in keys:
                max_y_in_temp = temporary_data_for_task_3[key][2]
                if max_y_in_temp > max_y:
                    max_y = max_y_in_temp
        except KeyError:
            pass

        # Проверяет ответы пользователя по индексам
        for key in keys:
            try:
                temp = temporary_data_for_task_3[key][2]
                if temporary_data_for_task_3[key] == answer_user_for_task_3[key] and temp != max_y:
                    right_answer += 1
            except KeyError:
                right_answer += 0

        if answer == temporary_data[-1]:
            if training_mode == 'control' and (right_answer == intermediate_elements):
                right_answers_type_3 += 1
                right_answers += 1
            if training_mode == 'learning' or training_mode == 'training':
                right_answers += 1
                Label(frame_task,
                      text='Ответ верный', font="Arial 15").grid(row=0, column=0, sticky="nw", padx=20, pady=10)
        else:
            if training_mode == 'learning' or training_mode == 'training':
                Label(frame_task,
                      text='Ответ неверный', font="Arial 15").grid(row=0, column=0, sticky="nw", padx=20, pady=10)
                if temporary_data[-1]:
                    Label(frame_gates, image=image_of_gates["true"]).grid(row=temporary_index[0], column=temporary_index[1])
                else:
                    Label(frame_gates, image=image_of_gates["false"]).grid(row=temporary_index[0], column=temporary_index[1])

        if training_mode == 'learning' or training_mode == 'training':
            Label(frame_task,
                  text=f'Промежуточных ответов правильно: {right_answer} из {intermediate_elements}',
                  font="Arial 15").grid(row=1, column=0, sticky="nw", padx=20, pady=15)
            if temporary_data[-1]:
                Label(frame_gates, image=image_of_gates["true"]).grid(row=temporary_index[0], column=temporary_index[1])
            else:
                Label(frame_gates, image=image_of_gates["false"]).grid(row=temporary_index[0], column=temporary_index[1])

        elif training_mode == 'control':
            number_of_intermediate_elements += intermediate_elements
            right_intermediate_answers += right_answer

    button = ''  # Без изначального инициализирования ругается

    if training_mode == 'training':
        number_of_tasks += 1
        button = Button(frame_task, text="Следующее задание", font="Arial 15", command=training)
        try:
            for widget in frame_counter.winfo_children():
                widget.destroy()
        except AttributeError:
            pass
        Label(frame_counter,
              text=f'Правильных ответов {right_answers} из {number_of_tasks}',
              font="Arial 15").grid(row=0, column=0, sticky="we", padx=30)
    elif training_mode == 'control':
        try:
            for widget in frame_counter.winfo_children():
                widget.destroy()
        except:
            pass
        max_number = counters["max_number_of_type_1"] + counters["max_number_of_type_2"] + counters["max_number_of_type_3"]

        Label(frame_counter,
              text=f'Задание {number_of_tasks} из {max_number}',
              font="Arial 15").grid(row=0, column=0, sticky="we", padx=50)

        if number_of_tasks == max_number + 1:  # Счетчик обновляется после ответа и не запускает 20 вопрос без проверки на 21
            end_test()
        else:
            control()

    else:
        if type_of_task == "task_1":
            button = Button(frame_task, text="Следующее задание", font="Arial 15", command=task_1)
        elif type_of_task == "task_2":
            button = Button(frame_task, text="Следующее задание", font="Arial 15", command=task_2)
        elif type_of_task == "task_3":
            button = Button(frame_task, text="Следующее задание", font="Arial 15", command=task_3)
    try:
        button.grid(column=0, row=2, sticky="sw", padx=20, pady=10)
    except:
        pass


def choice_task_1():
    """ Запуск 1 режима тренажера "Learning" с 1 заданием """

    global type_of_random
    global training_mode
    global number_of_tasks
    global right_answers
    global frame_counter

    try:
        for widget in frame_counter.winfo_children():
            widget.destroy()
    except:
        pass

    number_of_tasks = 0
    right_answers = 0
    type_of_random = False
    training_mode = 'learning'
    task_1()


def choice_task_2():
    """ Запуск 1 режима тренажера "Learning" с 2 заданием """

    global type_of_random
    global training_mode
    global number_of_tasks
    global right_answers
    global frame_counter

    try:
        for widget in frame_counter.winfo_children():
            widget.destroy()
    except:
        pass

    number_of_tasks = 0
    right_answers = 0
    training_mode = 'learning'
    type_of_random = False
    task_2()


def choice_task_3():
    """ Запуск 1 режима тренажера "Learning" с 3 заданием """

    global type_of_random
    global training_mode
    global number_of_tasks
    global right_answers
    global frame_counter

    try:
        for widget in frame_counter.winfo_children():
            widget.destroy()
    except:
        pass

    right_answers = 0
    number_of_tasks = 0
    training_mode = 'learning'
    type_of_random = False
    task_3()


def choice_mode_training():
    """ Настройка приложения в режиме тренировки """

    global type_of_random
    global training_mode
    global right_answers
    global number_of_tasks
    global frame_counter

    type_of_random = True
    training_mode = 'training'
    right_answers = 0
    number_of_tasks = 0

    frame_counter = Frame(frame_button)
    frame_counter.grid(row=0, column=6)
    Label(frame_counter, text=f'Правильных ответов {right_answers} из {number_of_tasks}', font="Arial 15").grid(row=0, column=0, sticky="we", padx=30)
    training()


def choice_mode_control():
    """ Настройка приложения для работы в режиме тестирования """

    global type_of_random
    global training_mode
    global number_of_try
    global time_start
    global frame_counter
    global number_of_tasks
    global right_answers
    global type_1
    global type_2
    global type_3
    global right_answers_type_1
    global right_answers_type_2
    global right_answers_type_3
    global number_of_intermediate_elements
    global right_intermediate_answers

    training_mode = 'control'
    type_of_random = True
    number_of_try += 1
    number_of_tasks = 1
    right_answers = 0
    type_1 = 0
    type_2 = 0
    type_3 = 0
    right_answers_type_1 = 0
    right_answers_type_2 = 0
    right_answers_type_3 = 0
    right_intermediate_answers = 0
    number_of_intermediate_elements = 0
    max_number = counters["max_number_of_type_1"] + counters["max_number_of_type_2"] + counters["max_number_of_type_3"]
    now = datetime.now()
    time_start = now.strftime("%H:%M:%S")

    try:
        for widget in frame_counter.winfo_children():
            widget.destroy()
    except:
        pass

    for widget in frame_button.winfo_children():
        widget.destroy()
    frame_counter = Frame(frame_button)
    frame_counter.grid(row=0, column=2)
    lbl = Label(frame_counter, text=f"Задание {number_of_tasks} из {max_number}", font="Arial 15")
    lbl.grid(row=0, column=0, sticky="we", padx=50)

    button = Button(frame_button, text="Завершить тестирование", command=choice_end, font="Arial 10", width=20)
    button.grid(row=0, column=0, padx=5, sticky="we")

    control()


def choice_end():
    """ Запуск функции завершения попытки """

    answer = messagebox.askyesno(title="Предупреждение", message="Вы хотите закончить попытку досрочно?")
    if answer:
        end_test()


def end_test():
    """ Выход из тестирования и демонстрация статистики прохждения попытки """

    global frame_counter
    global training_mode

    training_mode = None

    for widget in frame_button.winfo_children():
        widget.destroy()

    frame_counter = Frame(frame_button)
    frame_counter.grid(row=0, column=6)

    spawn_buttons()

    for widget in frame_task.winfo_children():
        widget.destroy()
    for widget in frame_gates.winfo_children():
        widget.destroy()

    # Сбор информации
    global time_stop

    now = datetime.now()
    time_stop = now.strftime("%H:%M:%S")

    percent_of_right = right_answers / max_task_in_control * 100
    percent_of_right = round(percent_of_right, 2)

    Label(frame_gates, text=f"Попытка № {number_of_try}", font="Arial 18", padx=550, pady=15). grid(row=0, column=0, sticky="w")

    Label(frame_gates, text=f"Время начала {time_start}", font="Arial 16", pady=7, padx=550).grid(row=1, column=0, sticky="w")
    Label(frame_gates, text=f"Время окончания {time_stop}", font="Arial 16", pady=7, padx=550).grid(row=2, column=0, sticky="w")

    Label(frame_gates, text="Статистика:", font="Arial 18", pady=15, padx=550).grid(row=3, column=0, sticky="w")

    if percent_of_right >= counters["min_percent_for_best"]:
        Label(frame_gates, text=f"Процент правильных ответов: {percent_of_right}%",
              font="Arial 16", pady=7, padx=550, fg='#009900').grid(row=4, column=0, sticky="w")
    elif percent_of_right >= counters["min_percent_for_good"]:
        Label(frame_gates, text=f"Процент правильных ответов: {percent_of_right}%",
              font="Arial 16", pady=7, padx=550, fg='#66cc00').grid(row=4, column=0, sticky="w")
    elif percent_of_right >= counters["min_percent_for_middle"]:
        Label(frame_gates, text=f"Процент правильных ответов: {percent_of_right}%",
              font="Arial 16", pady=7, padx=550, fg='#ff9900').grid(row=4, column=0, sticky="w")
    else:
        Label(frame_gates, text=f"Процент правильных ответов: {percent_of_right}%",
              font="Arial 16", pady=7, padx=550, fg='#ff3300').grid(row=4, column=0, sticky="w")

    Label(frame_gates, text=f'Задание 1: {right_answers_type_1} из {counters["max_number_of_type_1"]}',
          font="Arial 16", pady=7, padx=550).grid(row=5, column=0, sticky="w")

    Label(frame_gates, text=f'Задание 2: {right_answers_type_2} из {counters["max_number_of_type_2"]}',
          font="Arial 16", pady=7, padx=550).grid(row=6, column=0, sticky="w")

    Label(frame_gates, text=f'Задание 3: {right_answers_type_3} из {counters["max_number_of_type_3"]}',
          font="Arial 16", pady=7, padx=550).grid(row=7, column=0, sticky="w")

    with open('files/log.txt', 'a+') as save_log:
        save_log.write(f"Попытка: {number_of_try}" + "\n")
        save_log.write(f"Время начала: {time_start}" + "\n")
        save_log.write(f"Время окончания {time_stop}" + "\n")
        save_log.write(f"Процент правильных ответов: {percent_of_right}" + "%\n")
        save_log.write(f'Задание 1: {right_answers_type_1} из {counters["max_number_of_type_1"]}' + '\n')
        save_log.write(f'Задание 2: {right_answers_type_2} из {counters["max_number_of_type_2"]}' + '\n')
        save_log.write(f'Задание 3: {right_answers_type_3} из {counters["max_number_of_type_3"]}' + '\n')
        save_log.write(f'---------------------------------------------------------' + '\n')


def task_1():
    """ Задание, где пользователю не известен вывод при всех остальных известных значениях """

    global type_of_task
    type_of_task = "task_1"
    if training_mode == 'control':
        global type_1
        type_1 += 1

    for widget in frame_gates.winfo_children():
        widget.destroy()
    for widget in frame_task.winfo_children():
        widget.destroy()
    for widget in frame_reference.winfo_children():
        widget.destroy()
    frame_reference.config(borderwidth=0)

    global temporary_data
    global temporary_index
    global temporary_elements_and_index
    global temporary_data_for_task_3
    global answer_user_for_task_3
    global all_incoming_results
    global elements_of_gate
    global style
    global number_of_tasks

    temporary_data = []
    temporary_index = []
    temporary_elements_and_index = []
    all_incoming_results = []
    elements_of_gate = []
    temporary_data_for_task_3 = {}
    answer_user_for_task_3 = {}

    if training_mode == 'training' or training_mode == 'control':
        type_of_style = random.randint(1, 3)
        styles = {
            1: "ansi",
            2: "iec",
            3: "log",
        }
        style = styles[type_of_style]

    if training_mode == 'control':
        number_of_tasks += 1

    pattern = random.randint(1, 11)
    patterns = {
        1: circuit_1,
        2: circuit_2,
        3: circuit_3,
        4: circuit_4,
        5: circuit_5,
        6: circuit_6,
        7: circuit_7,
        8: circuit_8,
        9: circuit_9,
        10: circuit_10,
        11: circuit_11,
        12: circuit_12,
    }
    patterns[pattern]()

    Label(frame_task,
          text='Какой логический сигнал появится на выходе?',
          font="Arial 14").grid(row=0, column=0, sticky="sw", padx=20, pady=20)

    button = Button(frame_task, text="True", font="Arial 14", command=answer_user_true, width=8)
    button.grid(column=0, row=1, sticky="ws", padx=20, pady=10)
    button = Button(frame_task, text="False", font="Arial 14", command=answer_user_false, width=8)
    button.grid(column=0, row=2, sticky="sw", padx=20, pady=10)


def task_2():
    """ Задание, где пользователю не известен один сигнал на входе при всех остальных известных значениях """

    global type_of_task
    type_of_task = "task_2"
    if training_mode == 'control':
        global type_2
        type_2 += 1

    for widget in frame_gates.winfo_children():
        widget.destroy()
    for widget in frame_task.winfo_children():
        widget.destroy()
    for widget in frame_reference.winfo_children():
        widget.destroy()
    frame_reference.config(borderwidth=0)

    global temporary_data
    global temporary_index
    global temporary_elements_and_index
    global temporary_data_for_task_3
    global answer_user_for_task_3
    global all_incoming_results
    global elements_of_gate
    global y_in_task_2
    global number_of_pattern
    global style
    global number_of_tasks

    temporary_data_for_task_3 = {}
    answer_user_for_task_3 = {}
    temporary_data = []
    temporary_index = []
    temporary_elements_and_index = []
    all_incoming_results = []
    elements_of_gate = []
    y_in_task_2 = []
    number_of_pattern = 0

    if training_mode == 'training' or training_mode == 'control':
        type_of_style = random.randint(1, 3)
        styles = {
            1: "ansi",
            2: "iec",
            3: "log",
        }
        style = styles[type_of_style]

    if training_mode == 'control':
        number_of_tasks += 1
    inter_var = random.randint(1, 3)
    temporary_data.append(inter_var)

    pattern = random.randint(1, 11)
    patterns = {
        1: circuit_1,
        2: circuit_2,
        3: circuit_3,
        4: circuit_4,
        5: circuit_5,
        6: circuit_6,
        7: circuit_7,
        8: circuit_8,
        9: circuit_9,
        10: circuit_10,
        11: circuit_11
    }
    number_of_pattern = pattern
    patterns[pattern]()

    Label(frame_task,
          text='При каком значении неизвестного сигнала на входе данная схема будеть верной?',
          font="Arial 14").grid(row=0, column=0, sticky="sw", padx=20, pady=20)

    button = Button(frame_task, text="True", font="Arial 14", command=answer_user_true, width=8)
    button.grid(row=1, column=0, sticky="ws", padx=20, pady=10)
    button = Button(frame_task, text="False", font="Arial 14", command=answer_user_false, width=8)
    button.grid(row=2, column=0, sticky="sw", padx=20, pady=10)


def task_3():
    """ Задание, где пользователю не известен вывод при всех остальных известных значениях """

    global type_of_task
    type_of_task = "task_3"
    if training_mode == 'control':
        global type_3
        type_3 += 1

    for widget in frame_gates.winfo_children():
        widget.destroy()
    for widget in frame_task.winfo_children():
        widget.destroy()
    for widget in frame_reference.winfo_children():
        widget.destroy()
    frame_reference.config(borderwidth=0)

    global temporary_data
    global temporary_index
    global temporary_elements_and_index
    global temporary_data_for_task_3
    global answer_user_for_task_3
    global all_incoming_results
    global elements_of_gate
    global style
    global number_of_tasks

    temporary_data = []
    temporary_index = []
    temporary_elements_and_index = []
    all_incoming_results = []
    elements_of_gate = []
    temporary_data_for_task_3 = {}
    answer_user_for_task_3 = {}

    if training_mode == 'training' or training_mode == 'control':
        type_of_style = random.randint(1, 3)
        styles = {
            1: "ansi",
            2: "iec",
            3: "log",
        }
        style = styles[type_of_style]

    if training_mode == 'control':
        number_of_tasks += 1
    pattern = random.randint(1, 11)
    patterns = {
        1: circuit_1,
        2: circuit_2,
        3: circuit_3,
        4: circuit_4,
        5: circuit_5,
        6: circuit_6,
        7: circuit_7,
        8: circuit_8,
        9: circuit_9,
        10: circuit_10,
        11: circuit_11,
        12: circuit_12,
    }
    patterns[pattern]()

    Label(frame_task,
          text='Какой логический сигнал появится на выходе схемы?',
          font="Arial 14").grid(row=0, column=0, sticky="sw", padx=20, pady=7)

    Label(frame_task,
          text='В ответе учитываются значения промежуточных элементов',
          font="Arial 13").grid(row=1, column=0, sticky="sw", padx=20, pady=5)

    button = Button(frame_task, text="True", font="Arial 14", command=answer_user_true, width=8)
    button.grid(column=0, row=2, sticky="ws", padx=20, pady=10)
    button = Button(frame_task, text="False", font="Arial 14", command=answer_user_false, width=8)
    button.grid(column=0, row=3, sticky="sw", padx=20, pady=10)


def training():
    """ 2 режим тренажера "Training":
        * Задания выдаются случайно
        * Нотация выбирается случайно, но пользователь может ее изменить
        * Пользователь может смотреть подсказки
        * Ведется учет правильных ответов пользователя
        * Пользователь может спокойно перейти в любой другой режим """

    number_of_task = random.randint(1, 3)
    tasks = {
        1: task_1,
        2: task_2,
        3: task_3,
    }
    tasks[number_of_task]()


def control():
    """ 3 режим тренажера "Control":
        * Выдается определенное количество заданий: 20
        * Задания выбираются случайно
        * 3 тип задания встречается 8 раз
        * Ведется учет всех заданий
        * Нотация выбирается случайно и пользователь не может ее менять
        * Пользователь не может смотреть подсказки
        * Ведется учет правильных ответов
        * Пользователь может только завершить тестирование
        * После завершения тестирования показывается результат

     """

    global counters

    number_of_task = random.randint(1, 3)
    tasks = {
        1: task_1,
        2: task_2,
        3: task_3,
    }

    if number_of_task == 1 and type_1 < counters["max_number_of_type_1"]:
        tasks[number_of_task]()
    elif number_of_task == 2 and type_2 < counters["max_number_of_type_2"]:
        tasks[number_of_task]()
    elif number_of_task == 3 and type_3 < counters["max_number_of_type_3"]:
        tasks[number_of_task]()
    else:
        control()


def spawn_buttons():
    """ Вывод кнопок на верхнюю панель """

    button = Button(frame_button, text="Тип задания 1", command=choice_task_1, font="Arial 10", width=12)
    button.grid(row=0, column=1, padx=1, sticky="we")
    button = Button(frame_button, text="Тип задания 2", command=choice_task_2, font="Arial 10", width=12)
    button.grid(row=0, column=2, padx=1, sticky="we")
    button = Button(frame_button, text="Тип задания 3", command=choice_task_3, font="Arial 10", width=12)
    button.grid(row=0, column=3, padx=1, sticky="we")
    button = Button(frame_button, text="Тренировка", command=choice_mode_training, font="Arial 10", width=12)
    button.grid(row=0, column=4, padx=1, sticky="we")
    button = Button(frame_button, text="Тестирование", command=choice_mode_control, font="Arial 10", width=12)
    button.grid(row=0, column=5, padx=1, sticky="we")


def redrawing_of_gates():
    """ При изменении нотации перерисовывает все элементы """

    array = temporary_elements_and_index
    for element in range(0, len(array) - 1, 3):
        choice_from_gates(element=array[element], index_1=array[element+1], index_2=array[element+2], call_type=2)


def delete_log():
    """ Очищает файл с логами.
        Если такого файла нет, то создает его """
    answer = messagebox.askyesno(title="Предупреждение", message="Вы действительно хотите очистить файл сохранений?")
    customizing_window.focus_set()
    if answer:
        with open('files/log.txt', 'w+') as file_log:
            file_log.write("")


def types_of_tasks():
    """ Справка о типах заданий """
    global help_window

    help_window.geometry('800x555')
    for widget in help_window.winfo_children():
        widget.destroy()

    frame_text = Frame(help_window)
    frame_text.grid(column=0, row=1, columnspan=3, sticky="wne", padx=10)

    name_title = Label(help_window, text="Типы заданий", font="Aria 17")
    name_title.grid(row=0, column=0, padx=20, pady=15, sticky="w")

    button = Button(help_window, text="Меню", font="Arial 13", command=help_user, width=8)
    button.grid(row=0, column=2, sticky="n", pady=15, padx=508)

    with open('information/task.txt', 'r', encoding='utf-8') as show_help:
        help_text = show_help.readlines()  # type list

    aaa = " ".join(help_text)  # Преобразует в строку
    text = Text(frame_text, width=83, height=12,
                cursor="arrow", pady=5, padx=10, font="Aria 13",
                autoseparators=False, exportselection=False, spacing1=10,
                spacing2=5, spacing3=10, wrap="word")  # Размер текстового поля

    text.insert(INSERT, aaa)  # Вписать в окно текст
    text.configure(state='disabled')
    text.grid(column=0, row=1, sticky="we", padx=10)  # pack(side=LEFT)


def notations():
    """ Справка о нотациях """

    global help_window

    help_window.geometry('710x540')
    for widget in help_window.winfo_children():
        widget.destroy()

    frame_image = Frame(help_window)
    frame_image.grid(column=0, row=1, sticky="w")
    frame_text = Frame(help_window)
    frame_text.grid(column=1, row=0, rowspan=2, sticky="nw", columnspan=2, padx=10)
    frame_buttons = Frame(help_window)
    frame_buttons.grid(column=0, row=0, sticky="n")

    name_title = Label(frame_buttons, text="Нотации", font="Aria 17")
    name_title.grid(row=0, column=0, padx=20, pady=15)

    lbl_image = Label(frame_image, image=truth_table["menu"])
    lbl_image.grid(row=0, column=0, pady=10, padx=5)

    lbl_image = Label(frame_image, image=gates_styles["ansi"]["not"])
    lbl_image.grid(row=1, column=0, pady=10)

    lbl_image = Label(frame_image, image=gates_styles["iec"]["not"])
    lbl_image.grid(row=2, column=0, pady=10)

    lbl_image = Label(frame_image, image=gates_styles["log"]["not"])
    lbl_image.grid(row=3, column=0, pady=10)

    button = Button(frame_text, text="Меню", font="Arial 13", command=help_user, width=8)
    button.grid(row=0, column=0, sticky="ne", pady=5, padx=435)

    with open('information/notations.txt', 'r', encoding='utf-8') as show_help:
        help_text = show_help.readlines()  # type list

    aaa = " ".join(help_text)  # Преобразует в строку
    text = Text(frame_text, width=55, height=12,
                cursor="arrow", pady=5, padx=10, font="Aria 13",
                autoseparators=False, exportselection=False, spacing1=10,
                spacing2=10, spacing3=10, wrap="word")  # Размер текстового поля

    text.insert(INSERT, aaa)  # Вписать в окно текст
    text.configure(state='disabled')
    text.grid(column=0, row=1, sticky="w")  # pack(side=LEFT)


def hints():
    """ Справка о подсказках """

    global help_window

    help_window.geometry('610x395')
    for widget in help_window.winfo_children():
        widget.destroy()

    frame_image = Frame(help_window)
    frame_image.grid(column=0, row=1, sticky="w")
    frame_text = Frame(help_window)
    frame_text.grid(column=1, row=0, rowspan=2, sticky="nw", columnspan=2, padx=10)
    frame_buttons = Frame(help_window)
    frame_buttons.grid(column=0, row=0, sticky="n")

    name_title = Label(frame_buttons, text="Подсказки", font="Aria 17")
    name_title.grid(row=0, column=0, padx=20, pady=15)

    lbl_image = Label(frame_image, image=truth_table["reference"])
    lbl_image.grid(row=0, column=0, padx=5, sticky="n")

    lbl_image = Label(frame_image, image=gates_styles["ansi"]["or"])
    lbl_image.grid(row=1, column=0, pady=10, sticky="n")

    button = Button(frame_text, text="Меню", font="Arial 13", command=help_user, width=8)
    button.grid(row=0, column=0, sticky="ne", pady=5, padx=327)

    with open('information/hints.txt', 'r', encoding='utf-8') as show_help:
        help_text = show_help.readlines()  # type list

    aaa = " ".join(help_text)  # Преобразует в строку
    text = Text(frame_text, width=43, height=8,
                cursor="arrow", pady=5, padx=10, font="Aria 13",
                autoseparators=False, exportselection=False, spacing1=10,
                spacing2=5, spacing3=10, wrap="word")  # Размер текстового поля

    text.insert(INSERT, aaa)  # Вписать в окно текст
    text.configure(state='disabled')
    text.grid(column=0, row=1, sticky="w")  # pack(side=LEFT)


def line_of_communication():
    """ Справка о линиях связи """

    global help_window

    help_window.geometry('860x470')
    for widget in help_window.winfo_children():
        widget.destroy()

    frame_image = Frame(help_window)
    frame_image.grid(column=0, row=1, sticky="w")
    frame_text = Frame(help_window)
    frame_text.grid(column=1, row=0, rowspan=2, sticky="nw", columnspan=2, padx=10)
    frame_buttons = Frame(help_window)
    frame_buttons.grid(column=0, row=0, sticky="n")

    name_title = Label(frame_buttons, text="Линии связи", font="Aria 17")
    name_title.grid(row=0, column=0, padx=20, pady=15)

    lbl_image = Label(frame_image, image=image_of_lines["basic"]["1"])
    lbl_image.grid(row=0, column=0, pady=5, padx=50, sticky="we")

    lbl_image = Label(frame_image, image=image_of_lines["color"]["green"]["1_green"])
    lbl_image.grid(row=1, column=0, pady=5, padx=50, sticky="we")

    lbl_image = Label(frame_image, image=image_of_lines["basic"]["3"])
    lbl_image.grid(row=2, column=0, pady=5, padx=50, sticky="we")

    lbl_image = Label(frame_image, image=image_of_lines["color"]["multi"]["3_red_green"])
    lbl_image.grid(row=3, column=0, pady=5, padx=50, sticky="we")

    button = Button(frame_text, text="Меню", font="Arial 13", command=help_user, width=8)
    button.grid(row=0, column=0, sticky="ne", pady=5, padx=570)

    with open('information/lines.txt', 'r', encoding='utf-8') as show_help:
        help_text = show_help.readlines()  # type list

    aaa = " ".join(help_text)  # Преобразует в строку
    text = Text(frame_text, width=70, height=10,
                cursor="arrow", pady=5, padx=10, font="Aria 13",
                autoseparators=False, exportselection=False, spacing1=10,
                spacing2=5, spacing3=10, wrap="word")  # Размер текстового поля

    text.insert(INSERT, aaa)  # Вписать в окно текст
    text.configure(state='disabled')
    text.grid(column=0, row=1, sticky="w")  # pack(side=LEFT)


def settings_test():
    """ Справка о настройках теста """

    global help_window

    help_window.geometry('890x390')
    for widget in help_window.winfo_children():
        widget.destroy()

    frame_image = Frame(help_window, )
    frame_image.grid(column=0, row=1, sticky="n")
    frame_text = Frame(help_window,)
    frame_text.grid(column=1, row=0, rowspan=2, sticky="nw", padx=10)
    frame_buttons = Frame(help_window)
    frame_buttons.grid(column=0, row=0, sticky="n")

    name_title = Label(frame_buttons, text="Настройки теста", font="Aria 17")
    name_title.grid(row=0, column=0, padx=20, pady=15)

    lbl_image = Label(frame_image, image=truth_table["settings"])
    lbl_image.grid(row=1, column=0, pady=10, sticky="n")

    button = Button(frame_text, text="Меню", font="Arial 13", command=help_user, width=8)
    button.grid(row=0, column=0, sticky="ne", pady=5, padx=480)

    with open('information/settings.txt', 'r', encoding='utf-8') as show_help:
        help_text = show_help.readlines()  # type list

    aaa = " ".join(help_text)  # Преобразует в строку
    text = Text(frame_text, width=60, height=8,
                cursor="arrow", pady=5, padx=10, font="Aria 13",
                autoseparators=False, exportselection=False, spacing1=10,
                spacing2=5, spacing3=10, wrap="word")  # Размер текстового поля

    text.insert(INSERT, aaa)  # Вписать в окно текст
    text.configure(state='disabled')
    text.grid(column=0, row=1, sticky="w")  # pack(side=LEFT)


def simulator_modes():
    """ Справка о режимах тренажера """

    global help_window

    help_window.geometry('930x595')
    for widget in help_window.winfo_children():
        widget.destroy()

    frame_text = Frame(help_window)
    frame_text.grid(column=0, row=1, columnspan=3, sticky="wne", padx=10)

    name_title = Label(help_window, text="Режимы тренажера", font="Aria 17")
    name_title.grid(row=0, column=0, padx=20, pady=15, sticky="w")

    button = Button(help_window, text="Меню", font="Arial 13", command=help_user, width=8)
    button.grid(row=0, column=2, sticky="n", pady=15, padx=578)

    with open('information/mods.txt', 'r', encoding='utf-8') as show_help:
        help_text = show_help.readlines()  # type list

    aaa = " ".join(help_text)  # Преобразует в строку
    text = Text(frame_text, width=97, height=13,
                cursor="arrow", pady=5, padx=10, font="Aria 13",
                autoseparators=False, exportselection=False, spacing1=10,
                spacing2=5, spacing3=10, wrap="word")  # Размер текстового поля

    text.insert(INSERT, aaa)  # Вписать в окно текст
    text.configure(state='disabled')
    text.grid(column=0, row=1, sticky="we", padx=10)  # pack(side=LEFT)


# Меню
def swap_iec():
    """ Меняет нотацию на IEC """

    if training_mode == 'learning' or training_mode == 'training' or training_mode is None:
        global style
        style = "iec"
        notation_menu.entryconfig(4, label="Выбран IEC")
        redrawing_of_gates()
    else:
        messagebox.showwarning('Предупреждение', 'В режиме тестирования смена нотации невозможна')


def swap_ansi():
    """ Меняет нотацию на логические ANSI """

    if training_mode == 'learning' or training_mode == 'training' or training_mode is None:
        global style
        style = "ansi"
        notation_menu.entryconfig(4, label="Выбран ANSI")
        redrawing_of_gates()
    else:
        messagebox.showwarning('Предупреждение', 'В режиме тестирования смена нотации невозможна')


def swap_letter():
    """ Меняет нотацию на логические выражения """

    if training_mode == 'learning' or training_mode == 'training' or training_mode is None:
        global style
        style = "log"
        notation_menu.entryconfig(4, label="Выбран Letter")
        redrawing_of_gates()
    else:
        messagebox.showwarning('Предупреждение', 'В режиме тестирования смена нотации невозможна')


def choice_help():
    """ Запуск справки по приложению """

    global help_window

    help_window = Toplevel(root)
    help_window.geometry('700x500')
    help_window.title('Помощь')
    help_window.resizable(width=False, height=False)
    help_window.focus_set()

    help_user()


def help_user():
    """ Вывод справочной информации по использованию приложения """

    global help_window

    for widget in help_window.winfo_children():
        widget.destroy()
    help_window.geometry('240x400')

    name = Label(help_window, text="Справка", font="Aria 17")
    name.grid(row=0, column=0, sticky="we", padx=30, pady=10)

    button_1 = Button(help_window, text="Типы заданий", font="Arial 13", width=18, command=types_of_tasks)
    button_1.grid(row=1, column=0, sticky="we", padx=30, pady=10)

    button_2 = Button(help_window, text="Нотации", font="Arial 13", width=18, command=notations)
    button_2.grid(row=2, column=0, sticky="we", padx=30, pady=10)

    button_3 = Button(help_window, text="Подсказки", font="Arial 13", width=18, command=hints)
    button_3.grid(row=3, column=0, sticky="we", padx=30, pady=10)

    button_4 = Button(help_window, text="Линии связи", font="Arial 13", width=18, command=line_of_communication)
    button_4.grid(row=4, column=0, sticky="we", padx=30, pady=10)

    button_5 = Button(help_window, text="Режимы тренажера", font="Arial 13", width=18, command=simulator_modes)
    button_5.grid(row=5, column=0, sticky="we", padx=30, pady=10)

    button_6 = Button(help_window, text="Настройки теста", font="Arial 13", width=18, command=settings_test)
    button_6.grid(row=6, column=0, sticky="we", padx=30, pady=10)


def choice_settings():
    """ Вызов окна с настройками """

    if training_mode == 'control':
        messagebox.showwarning('Предупреждение', 'В режиме тестирования настройка невозможна')
    else:
        customization()


def customization():
    """ Окно с настройками теста.
        Позволяет настраивать количество вопросов в тесте
        и процент правильных ответов для каждой оценки """

    global customizing_window

    customizing_window = Toplevel(root)
    customizing_window.geometry('550x415')
    customizing_window.title('Настройка теста')

    message_in_type1 = StringVar()
    message_in_type1.set(counters["max_number_of_type_1"])

    message_in_type2 = StringVar()
    message_in_type2.set(counters["max_number_of_type_2"])

    message_in_type3 = StringVar()
    message_in_type3.set(counters["max_number_of_type_3"])

    message_in_type4 = StringVar()
    message_in_type4.set(counters["min_percent_for_middle"])

    message_in_type5 = StringVar()
    message_in_type5.set(counters["min_percent_for_good"])

    message_in_type6 = StringVar()
    message_in_type6.set(counters["min_percent_for_best"])

    global input_field_1
    global input_field_2
    global input_field_3
    global input_field_4
    global input_field_5
    global input_field_6

    Label(customizing_window, text="Настройки",
          font="Arial 15").grid(row=0, column=0, columnspan=2, sticky="we", padx=50, pady=7)

    Label(customizing_window, text="Первый тип заданий:",
          font="Arial 13").grid(row=1, column=0, sticky="w", padx=20, pady=10)
    input_field_1 = Entry(customizing_window,
                          width=10, bd=3, textvariable=message_in_type1, justify="center")
    input_field_1.grid(row=1, column=1, sticky="w", padx=20, pady=10)

    Label(customizing_window, text="Второй тип заданий:",
          font="Arial 13").grid(row=2, column=0, sticky="w", padx=20, pady=10)
    input_field_2 = Entry(customizing_window,
                          width=10, bd=3, textvariable=message_in_type2, justify="center")
    input_field_2.grid(row=2, column=1, sticky="w", padx=20, pady=10)

    Label(customizing_window, text="Третий тип заданий:",
          font="Arial 13").grid(row=3, column=0, sticky="w", padx=20, pady=10)
    input_field_3 = Entry(customizing_window,
                          width=10, bd=3, textvariable=message_in_type3, justify="center")
    input_field_3.grid(row=3, column=1, sticky="w", padx=20, pady=10)

    Label(customizing_window, text="Минимальный процент для \"Удовлетворительно\":",
          font="Arial 13").grid(row=4, column=0, sticky="w", padx=20, pady=10)
    input_field_4 = Entry(customizing_window,
                          width=10, bd=3, textvariable=message_in_type4, justify="center")
    input_field_4.grid(row=4, column=1, sticky="w", padx=20, pady=10)

    Label(customizing_window, text="Минимальный процент для \"Хорошо\":",
          font="Arial 13").grid(row=5, column=0, sticky="w", padx=20, pady=10)
    input_field_5 = Entry(customizing_window,
                          width=10, bd=3, textvariable=message_in_type5, justify="center")
    input_field_5.grid(row=5, column=1, sticky="w", padx=20, pady=10)

    Label(customizing_window, text="Минимальный процент для \"Отлично\":",
          font="Arial 13").grid(row=6, column=0, sticky="w", padx=20, pady=10)
    input_field_6 = Entry(customizing_window,
                          width=10, bd=3, textvariable=message_in_type6, justify="center")
    input_field_6.grid(row=6, column=1, sticky="w", padx=20, pady=10)

    button = Button(customizing_window, text="Применить", font="Arial 13", width=12, command=swap_settings)
    button.grid(row=7, column=0, columnspan=2, pady=12)

    button = Button(customizing_window, text="Очистить логи", font="Arial 13", width=15, command=delete_log)
    button.grid(row=8, column=0, columnspan=2, pady=7, sticky="e")


def swap_settings():
    """ Применение и запись настроек """

    global counters

    num_in_ent = []

    try:
        num_in_ent.append(int(input_field_1.get()))
        num_in_ent.append(int(input_field_2.get()))
        num_in_ent.append(int(input_field_3.get()))
        num_in_ent.append(int(input_field_4.get()))  # Минимальный порог оценки
        num_in_ent.append(int(input_field_5.get()))
        num_in_ent.append(int(input_field_6.get()))

        for num in range(len(num_in_ent)-1):
            if num_in_ent[num] < 0 and num <= 2:
                num_in_ent[num] = 0
            counters["max_number_of_type_" + str(num + 1)] = num_in_ent[num]

        if (num_in_ent[4] - num_in_ent[3] > 2) and (num_in_ent[5] - num_in_ent[4] > 2) and num_in_ent[3] >= 1:
            counters["min_percent_for_middle"] = num_in_ent[3]
            counters["min_percent_for_good"] = num_in_ent[4]
            counters["min_percent_for_best"] = num_in_ent[5]
            with open('files/settings.txt', 'w+') as save_settings:
                save_settings.write(f"{num_in_ent[0]}" + "\n")
                save_settings.write(f"{num_in_ent[1]}" + "\n")
                save_settings.write(f"{num_in_ent[2]}" + "\n")
                save_settings.write(f"{num_in_ent[3]}" + "\n")
                save_settings.write(f"{num_in_ent[4]}" + "\n")
                save_settings.write(f"{num_in_ent[5]}")
                customizing_window.destroy()
        else:
            messagebox.showerror('Ошибка', 'Неправильно задан минимальный процент для оценок')
            customizing_window.focus_set()
    except:
        messagebox.showerror('Ошибка', 'Неверно введены настройки')
        customizing_window.focus_set()


if __name__ == "__main__":
    main_menu.add_cascade(label="Нотация", menu=notation_menu)
    notation_menu.add_command(label="ANSI", command=swap_ansi)
    notation_menu.add_command(label="IEC", command=swap_iec)
    notation_menu.add_command(label="Letter", command=swap_letter)
    notation_menu.add_separator()
    notation_menu.add_command(label="Выбрано ANSI")
    main_menu.add_command(label='Помощь', command=choice_help)
    main_menu.add_command(label='Настройки', command=choice_settings)

    spawn_buttons()
    check_settings()
    root.mainloop()
