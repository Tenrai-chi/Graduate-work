import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import logic_gates as lg

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
root.title('Я не знаю что это такое')  # Заголовок окна
root.geometry('1600x1000')  # Размер окна 1920x1080

main_menu = Menu(root)
root.config(menu=main_menu)
notation_menu = Menu(main_menu, tearoff=0)

# Создание фреймов
frame_button = Frame(root)  # Фрейм с кнопками
frame_button.grid(column=0, row=0, sticky="nw", columnspan=2)

frame_gates = Frame(root)  # Фрейм с схемой relief=RIDGE, borderwidth=10, width=700, # height=660
frame_gates.grid(column=1, row=1, sticky="w", padx=20, pady=20)

frame_task = Frame(root)  # Фрейм с заданием   relief=RIDGE, borderwidth=2
frame_task.grid(column=1, row=2, sticky="sw")

frame_empty = Frame(root, width=50, height=900)  # Пустой фрейм, чтобы фрейм с заданием не скакал по экрану
frame_empty.grid(column=0, row=1, rowspan=2, sticky="w")

frame_reference = Frame(root, width=500, height=700)  # Фрейм с справка   relief=RIDGE, borderwidth=2
frame_reference.grid(column=2, row=1, rowspan=2, sticky="ne")
#-------------------------------------------------------------------------------------------------------------

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
    "color": {  # Линии после взаимодействия с пользователем
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
    "ansi": {  # ANSI
        "not": ImageTk.PhotoImage(Image.open('image/ansi/not.png')),
        "buf": ImageTk.PhotoImage(Image.open('image/ansi/buf.png')),
        "and": ImageTk.PhotoImage(Image.open('image/ansi/and.png')),
        "nand": ImageTk.PhotoImage(Image.open('image/ansi/nand.png')),
        "nor": ImageTk.PhotoImage(Image.open('image/ansi/nor.png')),
        "xnor": ImageTk.PhotoImage(Image.open('image/ansi/xnor.png')),
        "xor": ImageTk.PhotoImage(Image.open('image/ansi/xor.png')),
        "or": ImageTk.PhotoImage(Image.open('image/ansi/or.png'))
    },
    "iec": {  # ГОСТ
        "not": ImageTk.PhotoImage(Image.open('image/iec/not.png')),
        "buf": ImageTk.PhotoImage(Image.open('image/iec/buf.png')),
        "and": ImageTk.PhotoImage(Image.open('image/iec/and.png')),
        "nand": ImageTk.PhotoImage(Image.open('image/iec/nand.png')),
        "nor": ImageTk.PhotoImage(Image.open('image/iec/nor.png')),
        "xnor": ImageTk.PhotoImage(Image.open('image/iec/xnor.png')),
        "xor": ImageTk.PhotoImage(Image.open('image/iec/xor.png')),
        "or": ImageTk.PhotoImage(Image.open('image/iec/or.png'))
    },
    "log": {  # Логические обозначения
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
        "or": ImageTk.PhotoImage(Image.open('information/image/or.png'))
}
#-------------------------------------------------------------------------------------------------------------

# Инициализация глобальных переменных и временных хранилищ

style = "ansi"  # Метка используемого вида обозначений
type_of_task = "task_1"  # Метка задания

#  Временные значения программы
temporary_data = []  # Хранилище временных данных: [str], bool*4
temporary_index = []  # Хранение координат для скрытого элемента
temporary_elements_and_index = []  # Хранит вентили и их координаты

temporary_data_for_task_3 = {}  # Хранение значений промежуточных элементов
answer_user_for_task_3 = {}  # Хранение цветов на промежуточных элементах от пользователя


def pattern_1() -> tuple:
    """ Шаблон 1 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = []
    for i in range(5):
        elements.append('?')

    elements[0] = random.choice(gates_for_1)
    elements[1] = random.choice(gates_for_1)
    elements[2] = random.choice(gates_for_2)
    elements[3] = random.choice(gates_for_2)
    elements[4] = random.choice(gates_for_2)

    ans_elements = []
    for x in range(2):
        temp = solution(elements[x], a, b, c)
        ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0], ans_elements[1])
    ans_elements.append(temp)

    temp = solution(elements[3], b, c)
    ans_elements.append(temp)

    temp = solution(elements[4], ans_elements[2], ans_elements[3])
    ans_elements.append(temp)

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_2() -> tuple:
    """ Шаблон 2 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = []
    for i in range(4):
        elements.append('?')

    elements[0] = random.choice(gates_for_2)
    elements[1] = random.choice(gates_for_2)
    elements[2] = random.choice(gates_for_1)
    elements[3] = random.choice(gates_for_2)

    ans_elements = []

    temp = solution(elements[0], a, b)
    ans_elements.append(temp)

    temp = solution(elements[1], b, c)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0])
    ans_elements.append(temp)

    temp = solution(elements[3], ans_elements[2], ans_elements[1])
    ans_elements.append(temp)

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_3() -> tuple:
    """ Шаблон 3 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = []
    for i in range(5):
        elements.append('?')

    elements[0] = random.choice(gates_for_2)
    elements[1] = random.choice(gates_for_2)
    elements[2] = random.choice(gates_for_1)
    elements[3] = random.choice(gates_for_1)
    elements[4] = random.choice(gates_for_2)

    ans_elements = []
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

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_4() -> tuple:
    """ Шаблон 4 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = []
    for i in range(5):
        elements.append('?')

    elements[0] = random.choice(gates_for_2)
    elements[1] = random.choice(gates_for_2)
    elements[2] = random.choice(gates_for_2)
    elements[3] = random.choice(gates_for_1)
    elements[4] = random.choice(gates_for_2)

    ans_elements = []
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

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_5() -> tuple:
    """ Шаблон 5 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = []
    for i in range(5):
        elements.append('?')

    elements[0] = random.choice(gates_for_2)
    elements[1] = random.choice(gates_for_2)
    elements[2] = random.choice(gates_for_1)
    elements[3] = random.choice(gates_for_2)
    elements[4] = random.choice(gates_for_1)

    ans_elements = []

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

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_6() -> tuple:
    """ Шаблон 6 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = []
    for i in range(4):
        elements.append('?')

    elements[0] = random.choice(gates_for_2)
    elements[1] = random.choice(gates_for_1)
    elements[2] = random.choice(gates_for_2)
    elements[3] = random.choice(gates_for_2)

    ans_elements = []

    temp = solution(elements[0], a, b)
    ans_elements.append(temp)

    temp = solution(elements[1], c)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0], ans_elements[1])
    ans_elements.append(temp)

    temp = solution(elements[3], a, ans_elements[2])
    ans_elements.append(temp)

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_7() -> tuple:
    """ Шаблон 7 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = []
    for i in range(6):
        elements.append('?')

    elements[0] = random.choice(gates_for_1)
    elements[1] = random.choice(gates_for_1)
    elements[2] = random.choice(gates_for_2)
    elements[3] = random.choice(gates_for_2)
    elements[4] = random.choice(gates_for_2)
    elements[5] = random.choice(gates_for_2)

    ans_elements = []

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

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_8() -> tuple:
    """ Шаблон 8 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = []
    for i in range(5):
        elements.append('?')

    elements[0] = random.choice(gates_for_2)
    elements[1] = random.choice(gates_for_2)
    elements[2] = random.choice(gates_for_1)
    elements[3] = random.choice(gates_for_2)
    elements[4] = random.choice(gates_for_2)

    ans_elements = []
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

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_9() -> tuple:
    """ Шаблон 9 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = []
    for i in range(6):
        elements.append('?')

    elements[0] = random.choice(gates_for_1)
    elements[1] = random.choice(gates_for_2)
    elements[2] = random.choice(gates_for_2)
    elements[3] = random.choice(gates_for_2)
    elements[4] = random.choice(gates_for_1)
    elements[5] = random.choice(gates_for_2)

    ans_elements = []
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

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_10() -> tuple:
    """ Шаблон 10 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = []
    for i in range(5):
        elements.append('?')

    elements[0] = random.choice(gates_for_2)
    elements[1] = random.choice(gates_for_2)
    elements[2] = random.choice(gates_for_2)
    elements[3] = random.choice(gates_for_1)
    elements[4] = random.choice(gates_for_2)

    ans_elements = []

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

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_11() -> tuple:
    """ Шаблон 11 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = []
    for i in range(5):
        elements.append('?')

    elements[0] = random.choice(gates_for_2)
    elements[1] = random.choice(gates_for_2)
    elements[2] = random.choice(gates_for_1)
    elements[3] = random.choice(gates_for_2)
    elements[4] = random.choice(gates_for_2)

    ans_elements = []

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

    return elements, a, b, c, ans_elements[-1], ans_elements


def pattern_12() -> tuple:
    """ Шаблон 12 """

    a = random.choice(true_false)
    b = random.choice(true_false)
    c = random.choice(true_false)

    elements = []
    for i in range(6):
        elements.append('?')

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


def reference_buf(event):
    """ Справка buf """
    reference_call(logic_gate="buf", name_reference="БУФФЕР")


def reference_not(event):
    """ Справка not """
    reference_call(logic_gate="not", name_reference="НЕ")


def reference_and(event):
    """ Справка and """

    reference_call(logic_gate="and", name_reference="И")


def reference_or(event):
    """ Справка or """

    reference_call(logic_gate="or", name_reference="ИЛИ")


def reference_xor(event):
    """ Справка xor """

    reference_call(logic_gate="xor", name_reference="Исключающее ИЛИ")


def reference_nand(event):
    """ Справка nand """

    reference_call(logic_gate="nand", name_reference="И-НЕ")


def reference_nor(event):
    """ Справка nor """

    reference_call(logic_gate="nor", name_reference="ИЛИ-НЕ")


def reference_xnor(event):
    """ Справка xnor """

    reference_call(logic_gate="xnor", name_reference="Исключающее ИЛИ-НЕ")


def choice_from_gates(element: str, ans_element: bool, index_1: int, index_2: int, call_type=1):
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

    #Label(frame_gates, image=image_of_lines["basic"][lines[number]]).grid(row=index_1, column=index_2)


def change_to_true(event):
    """ Изменение цвета элемента при нажатии на левую кнопку мыши """
    num = event.widget.image_number  # Возвращает номер используемой картинки
    last = event.widget.image_last_word  # Возвращает цвет текущей картинки, если он есть
    index_1 = event.widget.image_index_1
    index_2 = event.widget.image_index_2

    if num not in ["3", "6", "7", "8"]:
        name = str(index_1) + '_' + str(index_2-1)
        global answer_user_for_task_3
        answer_user_for_task_3[name] = [True, index_1, index_2 - 1]

    array_of_last_word = ["_green_green", "_green_red", "_red_green", "_red_red"]

    # Если была базовая с 1 входом
    a = num + "_green"
    if a in image_of_lines["color"]["green"]:
        event.widget["image"] = image_of_lines["color"]["green"][a]

    if num in ["3", "6", "7", "8"]:
        if last == "" or last == array_of_last_word[3]:
            lbl = Label(frame_gates, image=image_of_lines["color"]["multi"][num+"_green_green"])
            lbl.image_last_word = "_green_green"  # Записывает в объект окончание названия (для базового он пуст)
        elif last == array_of_last_word[0]:
            lbl = Label(frame_gates, image=image_of_lines["color"]["multi"][num + array_of_last_word[1]])
            lbl.image_last_word = "_green_red"  # Записывает в объект окончание названия (для базового он пуст)
        elif last == array_of_last_word[1]:
            lbl = Label(frame_gates, image=image_of_lines["color"]["multi"][num + array_of_last_word[2]])
            lbl.image_last_word = "_red_green"  # Записывает в объект окончание названия (для базового он пуст)
        elif last == array_of_last_word[2]:
            lbl = Label(frame_gates, image=image_of_lines["color"]["multi"][num + array_of_last_word[3]])
            lbl.image_last_word = "_red_red"  # Записывает в объект окончание названия (для базового он пуст)
        else:
            print("mda")

        lbl.image_number = num  # Записывает в объект номер базовой картинки
        lbl.image_index_1 = index_1
        lbl.image_index_2 = index_2

        lbl.grid(row=index_1, column=index_2)
        lbl.bind("<Button-1>", change_to_true)
        lbl.bind("<Button-3>", change_to_false)


def change_to_false(event):
    """ Изменение цвета элемента при нажатии на правую кнопку мыши """
    num = event.widget.image_number  # Возвращает номер используемой картинки
    index_1 = event.widget.image_index_1
    index_2 = event.widget.image_index_2
    a = num + "_red"
    if a in image_of_lines["color"]["red"]:
        event.widget["image"] = image_of_lines["color"]["red"][a]

    if num not in ["3", "6", "7", "8"]:
        name = str(index_1) + '_' + str(index_2-1)
        global answer_user_for_task_3
        answer_user_for_task_3[name] = [False, index_1, index_2 - 1]


def choice_from_0_1(vari: bool, index_1: int, index_2: int):
    """ Определяет какой элемент отрисовывать на входах и выходе """

    if vari:
        Label(frame_gates, image=image_of_gates["true"]).grid(row=index_1, column=index_2)
    elif not vari:
        Label(frame_gates, image=image_of_gates["false"]).grid(row=index_1, column=index_2)
    else:
        print('Error in choice_from_0_1')


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
        print('Error in writing_to_temporary_data')


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
    choice_from_gates(elements[0], ans_elements[0], 0, 2)
    contact_drawing(number=2, index_1=0, index_2=3)

    # 2 строка
    contact_drawing(number=3, index_1=1, index_2=3)
    choice_from_gates(elements[2], ans_elements[2], 1, 4)
    contact_drawing(number=2, index_1=1, index_2=5)

    # 3 строка
    choice_from_signal_image(2, 0, b, 2)
    contact_drawing(number=4, index_1=2, index_2=1)
    choice_from_gates(elements[1], ans_elements[1], 2, 2)
    contact_drawing(number=5, index_1=2, index_2=3)
    contact_drawing(number=3, index_1=2, index_2=5)
    choice_from_gates(elements[4], ans_elements[4], 2, 6)
    contact_drawing(number=1, index_1=2, index_2=7)
    choice_from_signal_image(2, 8, y, 4)

    # 4 строка
    contact_drawing(number=12, index_1=3, index_2=1)
    contact_drawing(number=1, index_1=3, index_2=2)
    contact_drawing(number=2, index_1=3, index_2=3)
    contact_drawing(11, 3, 5)

    # 5 строка
    contact_drawing(number=3, index_1=4, index_2=3)
    choice_from_gates(elements[3], ans_elements[3], 4, 4)
    contact_drawing(number=5, index_1=4, index_2=5)

    # 6 строка
    choice_from_signal_image(5, 0, c, 3)
    contact_drawing(number=1, index_1=5, index_2=1)
    contact_drawing(number=1, index_1=5, index_2=2)
    contact_drawing(number=5, index_1=5, index_2=3)


# Посмотреть вывод правильных ответов
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
    choice_from_gates(elements[0], ans_elements[0], 1, 3)
    contact_drawing(number=1, index_1=1, index_2=4)
    choice_from_gates(elements[2], ans_elements[2], 1, 5)
    contact_drawing(number=2, index_1=1, index_2=6)

    # 3 строка
    choice_from_signal_image(2, 0, b, 2)
    contact_drawing(number=4, index_1=2, index_2=1)
    contact_drawing(number=5, index_1=2, index_2=2)
    contact_drawing(number=3, index_1=2, index_2=6)
    choice_from_gates(elements[3], ans_elements[3], 2, 7)
    contact_drawing(number=1, index_1=2, index_2=8)
    choice_from_signal_image(2, 9, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, c, 3)
    contact_drawing(number=6, index_1=3, index_2=1)
    choice_from_gates(elements[1], ans_elements[1], 3, 2)
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
    choice_from_gates(elements[0], ans_elements[0], 0, 2)
    contact_drawing(number=1, index_1=0, index_2=3)
    choice_from_gates(elements[2], ans_elements[2], 0, 4)
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    contact_drawing(number=10, index_1=1, index_2=1)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[4], ans_elements[4], 1, 6)
    contact_drawing(number=1, index_1=1, index_2=7)
    choice_from_signal_image(1, 8, y, 4)

    # 3 строка
    choice_from_signal_image(2, 0, c, 3)
    contact_drawing(number=6, index_1=2, index_2=1)
    choice_from_gates(elements[1], ans_elements[1], 2, 2)
    contact_drawing(number=1, index_1=2, index_2=3)
    choice_from_gates(elements[3], ans_elements[3], 2, 4)
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
    choice_from_gates(elements[0], ans_elements[0], 0, 2)
    contact_drawing(number=1, index_1=0, index_2=3)
    contact_drawing(number=1, index_1=0, index_2=4)
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    contact_drawing(number=11, index_1=1, index_2=1)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[2], ans_elements[2], 1, 6)
    contact_drawing(number=2, index_1=1, index_2=7)

    # 3 строка
    contact_drawing(number=11, index_1=2, index_2=1)
    choice_from_signal_image(2, 2, c, 3)
    contact_drawing(number=7, index_1=2, index_2=3)
    choice_from_gates(elements[1], ans_elements[1], 2, 4)
    contact_drawing(number=5, index_1=2, index_2=5)
    contact_drawing(number=3, index_1=2, index_2=7)
    choice_from_gates(elements[4], ans_elements[4], 2, 8)
    contact_drawing(number=1, index_1=2, index_2=9)
    choice_from_signal_image(2, 10, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, b, 2)
    contact_drawing(number=9, index_1=3, index_2=1)
    contact_drawing(number=1, index_1=3, index_2=2)
    contact_drawing(number=9, index_1=3, index_2=3)
    contact_drawing(number=1, index_1=3, index_2=4)
    choice_from_gates(elements[3], ans_elements[3], 3, 5)
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
    choice_from_gates(elements[0], ans_elements[0], 0, 2)
    contact_drawing(number=1, index_1=0, index_2=3)
    choice_from_gates(elements[2], ans_elements[2], 0, 4)
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    contact_drawing(number=10, index_1=1, index_2=1)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[3], ans_elements[3], 1, 6)
    contact_drawing(number=1, index_1=1, index_2=7)
    choice_from_gates(elements[4], ans_elements[4], 1, 8)
    contact_drawing(number=1, index_1=1, index_2=9)
    choice_from_signal_image(1, 10, y, 4)

    # 3 строка
    choice_from_signal_image(2, 0, c, 3)
    contact_drawing(number=6, index_1=2, index_2=1)
    choice_from_gates(elements[1], ans_elements[1], 2, 2)
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
    choice_from_gates(elements[0], ans_elements[0], 1, 2)
    contact_drawing(number=2, index_1=1, index_2=3)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[3], ans_elements[3], 1, 6)
    contact_drawing(number=1, index_1=1, index_2=7)
    choice_from_signal_image(1, 8, y, 4)

    # 3 строка
    choice_from_0_1(b, 3, 0)
    choice_from_signal_image(2, 0, b, 2)
    contact_drawing(number=5, index_1=2, index_2=1)
    contact_drawing(number=3, index_1=2, index_2=3)
    choice_from_gates(elements[2], ans_elements[2], 2, 4)
    contact_drawing(number=5, index_1=2, index_2=5)

    # 4 строка
    choice_from_0_1(c, 3, 0)
    choice_from_signal_image(3, 0, c, 3)
    contact_drawing(number=1, index_1=3, index_2=1)
    choice_from_gates(elements[1], ans_elements[1], 3, 2)
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
    choice_from_gates(elements[0], ans_elements[0], 0, 3)
    contact_drawing(number=1, index_1=0, index_2=4)
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    choice_from_signal_image(1, 0, a, 1)
    contact_drawing(number=9, index_1=1, index_2=1)
    choice_from_gates(elements[1], ans_elements[1], 1, 2)
    contact_drawing(number=2, index_1=1, index_2=3)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[3], ans_elements[3], 1, 6)
    contact_drawing(number=2, index_1=1, index_2=7)

    # 3 строка
    contact_drawing(number=3, index_1=2, index_2=3)
    choice_from_gates(elements[2], ans_elements[2], 2, 4)
    contact_drawing(number=5, index_1=2, index_2=5)
    contact_drawing(number=3, index_1=2, index_2=7)
    choice_from_gates(elements[5], ans_elements[5], 2, 8)
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
    choice_from_gates(elements[4], ans_elements[4], 4, 2)
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
    choice_from_gates(elements[0], ans_elements[0], 0, 2)
    contact_drawing(number=1, index_1=0, index_2=3)
    choice_from_gates(elements[2], ans_elements[2], 0, 4)
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    contact_drawing(number=14, index_1=1, index_2=1)
    contact_drawing(number=1, index_1=1, index_2=2)
    contact_drawing(number=2, index_1=1, index_2=3)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[4], ans_elements[4], 1, 6)
    contact_drawing(number=1, index_1=1, index_2=7)
    choice_from_signal_image(1, 8, y, 4)

    # 3 строка
    contact_drawing(number=11, index_1=2, index_2=1)
    contact_drawing(number=3, index_1=2, index_2=3)
    choice_from_gates(elements[3], ans_elements[3], 2, 4)
    contact_drawing(number=5, index_1=2, index_2=5)

    # 4 строка
    choice_from_signal_image(3, 0, c, 3)
    contact_drawing(number=6, index_1=3, index_2=1)
    choice_from_gates(elements[1], ans_elements[1], 3, 2)
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
    choice_from_gates(elements[0], ans_elements[0], 0, 2)
    contact_drawing(number=2, index_1=0, index_2=3)

    # 2 строка
    choice_from_signal_image(1, 0, a, 1)
    contact_drawing(number=10, index_1=1, index_2=1)
    contact_drawing(number=3, index_1=1, index_2=3)
    choice_from_gates(elements[2], ans_elements[2], 1, 4)
    contact_drawing(number=2, index_1=1, index_2=5)

    # 3 строка
    contact_drawing(number=3, index_1=2, index_2=1)
    choice_from_gates(elements[1], ans_elements[1], 2, 2)
    contact_drawing(number=5, index_1=2, index_2=3)
    contact_drawing(number=3, index_1=2, index_2=5)
    choice_from_gates(elements[5], ans_elements[5], 2, 6)
    contact_drawing(number=1, index_1=2, index_2=7)
    choice_from_signal_image(2, 8, y, 4)
    choice_from_signal_image(3, 0, b, 2)

    # 5 строка
    contact_drawing(number=10, index_1=3, index_2=1)
    contact_drawing(number=11, index_1=3, index_2=5)

    # 5 строка
    choice_from_signal_image(4, 0, c, 3)
    contact_drawing(number=6, index_1=4, index_2=1)
    choice_from_gates(elements[3], ans_elements[3], 4, 2)
    contact_drawing(number=1, index_1=4, index_2=3)
    choice_from_gates(elements[4], ans_elements[4], 4, 4)
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
    choice_from_gates(elements[0], ans_elements[0], 0, 2)
    contact_drawing(number=4, index_1=0, index_2=3)
    contact_drawing(number=1, index_1=0, index_2=4)
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    contact_drawing(number=5, index_1=1, index_2=1)
    contact_drawing(number=11, index_1=1, index_2=3)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[2], ans_elements[2], 1, 6)
    contact_drawing(number=2, index_1=1, index_2=7)

    # 3 строка
    contact_drawing(number=3, index_1=2, index_2=3)
    choice_from_gates(elements[1], ans_elements[1], 2, 4)
    contact_drawing(number=5, index_1=2, index_2=5)
    contact_drawing(number=3, index_1=2, index_2=7)
    choice_from_gates(elements[4], ans_elements[4], 2, 8)
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
    choice_from_gates(elements[3], ans_elements[3], 4, 5)
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
    choice_from_gates(elements[0], ans_elements[0], 0, 2)
    contact_drawing(number=4, index_1=0, index_2=3)
    choice_from_gates(elements[2], ans_elements[2], 0, 4)
    contact_drawing(number=2, index_1=0, index_2=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    contact_drawing(number=10, index_1=1, index_2=1)
    contact_drawing(number=11, index_1=1, index_2=3)
    contact_drawing(number=3, index_1=1, index_2=5)
    choice_from_gates(elements[4], ans_elements[4], 1, 6)
    contact_drawing(number=1, index_1=1, index_2=7)
    choice_from_signal_image(1, 8, y, 4)

    # 3 строка
    contact_drawing(number=11, index_1=2, index_2=1)
    contact_drawing(number=3, index_1=2, index_2=3)
    choice_from_gates(elements[3], ans_elements[3], 2, 4)
    contact_drawing(number=5, index_1=2, index_2=5)

    # 4 строка
    choice_from_signal_image(3, 0, c, 3)
    contact_drawing(number=6, index_1=3, index_2=1)
    choice_from_gates(elements[1], ans_elements[1], 3, 2)
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
        print('Error')

    # 1 строка
    contact_drawing(number=13, index_1=0, index_2=1)
    choice_from_gates(elements[0], ans_elements[0], 0, 2)
    contact_drawing(number=2, index_1=0, index_2=3)

    # 2 строка
    choice_from_signal_image(1, 0, a, 1)
    contact_drawing(number=10, index_1=1, index_2=1)
    contact_drawing(number=3, index_1=1, index_2=3)
    choice_from_gates(elements[3], ans_elements[3], 1, 4)
    contact_drawing(number=2, index_1=1, index_2=5)

    # 3 строка
    contact_drawing(number=3, index_1=2, index_2=1)
    choice_from_gates(elements[1], ans_elements[1], 2, 2)
    contact_drawing(number=10, index_1=2, index_2=3)
    contact_drawing(number=3, index_1=2, index_2=5)
    choice_from_gates(elements[5], ans_elements[5], 2, 6)
    contact_drawing(number=1, index_1=2, index_2=7)
    choice_from_signal_image(2, 8, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, b, 2)
    contact_drawing(number=10, index_1=3, index_2=1)
    contact_drawing(number=3, index_1=3, index_2=3)
    choice_from_gates(elements[4], ans_elements[4], 3, 4)
    contact_drawing(number=5, index_1=3, index_2=5)

    # 5 строка
    contact_drawing(number=12, index_1=4, index_2=1)
    choice_from_gates(elements[2], ans_elements[2], 4, 2)
    contact_drawing(number=5, index_1=4, index_2=3)


def answer_user_true():
    """ Вызывает функцию обработки ответа с True """
    answer_user(True)


def answer_user_false():
    """ Вызывает функцию обработки ответа с False """
    answer_user(False)


def answer_user(answer: bool):
    """ Принимает ответ пользователя из формы """

    right_answer = 0

    for widget in frame_task.winfo_children():
        widget.destroy()

    if type_of_task == "task_3":
        try:
            keys = list(temporary_data_for_task_3.keys())
            for key in keys:
                if temporary_data_for_task_3[key] == answer_user_for_task_3[key]:
                    right_answer += 1
        except KeyError:
            right_answer += 0

    if answer == temporary_data[-1]:
        Label(frame_task,
              text='Ответ верный', font="Arial 15").grid(row=0, column=0, sticky="nw", padx=20, pady=20)
    else:
        Label(frame_task,
              text='Ответ неверный', font="Arial 15").grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    Label(frame_task,
          text=f'Промежуточных ответов правильно: {right_answer}', font="Arial 15").grid(row=1, column=0, sticky="nw", padx=20, pady=20)

    button = ''  # Без изначального инициализирования ругается
    if type_of_task == "task_1":
        button = Button(frame_task, text="Следующее задание", font="Arial 15", command=task_1)
    elif type_of_task == "task_2":
        button = Button(frame_task, text="Следующее задание", font="Arial 15", command=task_2)
    elif type_of_task == "task_3":
        button = Button(frame_task, text="Следующее задание", font="Arial 15", command=task_3)
    button.grid(column=0, row=2, sticky="nw", padx=20, pady=10)

    if temporary_data[-1]:
        Label(frame_gates, image=image_of_gates["true"]).grid(row=temporary_index[0], column=temporary_index[1])
    else:
        Label(frame_gates, image=image_of_gates["false"]).grid(row=temporary_index[0], column=temporary_index[1])


def task_1():
    """ Задание, где пользователю не известен вывод при всех остальных известных значениях """
    global type_of_task
    type_of_task = "task_1"

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

    temporary_data = []
    temporary_index = []
    temporary_elements_and_index = []
    temporary_data_for_task_3 = {}
    answer_user_for_task_3 = {}

    Label(frame_task,
          text='Какой логический сигнал появится на выходе схемы после подачи заданных вдохящих значений?',
          font="Arial 15").grid(row=0, column=0, sticky="sw", padx=20, pady=20)

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
    #circuit_12()

    button = Button(frame_task, text="True", font="Arial 15", command=answer_user_true, width=8)  # relief="flat" для более стильного дизайна
    button.grid(column=0, row=1, sticky="ws", padx=20, pady=10)
    button = Button(frame_task, text="False", font="Arial 15", command=answer_user_false, width=8)
    button.grid(column=0, row=2, sticky="sw", padx=20, pady=10)


def task_2():
    """ Задание, где пользователю не известен один сигнал на входе при всех остальных известных значениях """
    global type_of_task
    type_of_task = "task_2"

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

    temporary_data_for_task_3 = {}
    answer_user_for_task_3 = {}
    temporary_data = []
    temporary_index = []
    temporary_elements_and_index = []

    Label(frame_task,
          text='При каком значении неизвестного сигнала на входе данная схема будеть верной?',
          font="Arial 15").grid(row=0, column=0, sticky="sw", padx=20, pady=20)

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
    patterns[pattern]()

    #circuit_2()

    button = Button(frame_task, text="True", font="Arial 15", command=answer_user_true, width=8)  # relief="flat" для более стильного дизайна
    button.grid(row=1, column=0, sticky="ws", padx=20, pady=10)
    button = Button(frame_task, text="False", font="Arial 15", command=answer_user_false, width=8)
    button.grid(row=2, column=0, sticky="sw", padx=20, pady=10)


def task_3():
    """ Задание, где пользователю не известен вывод при всех остальных известных значениях """
    global type_of_task
    type_of_task = "task_3"

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

    temporary_data = []
    temporary_index = []
    temporary_elements_and_index = []
    temporary_data_for_task_3 = {}
    answer_user_for_task_3 = {}

    Label(frame_task,
          text='Какой логический сигнал появится на выходе схемы после подачи заданных вдохящих значений?',
          font="Arial 15").grid(row=0, column=0, sticky="sw", padx=20, pady=10)

    Label(frame_task,
          text='В ответе учитываются значения промежуточных элементов',
          font="Arial 13").grid(row=1, column=0, sticky="sw", padx=20, pady=10)

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
    # circuit_11()

    button = Button(frame_task, text="True", font="Arial 15", command=answer_user_true, width=8)  # relief="flat" для более стильного дизайна
    button.grid(column=0, row=2, sticky="ws", padx=20, pady=10)
    button = Button(frame_task, text="False", font="Arial 15", command=answer_user_false, width=8)
    button.grid(column=0, row=3, sticky="sw", padx=20, pady=10)


def random_task():
    number_of_task = random.randint(1, 2)
    if number_of_task == 1:
        task_1()
    else:
        task_2()


def spawn_buttons():
    button = Button(frame_button, text="Задание 1", command=task_1, font="Arial 10", width=9)
    button.grid(row=0, column=1, padx=1, sticky="we")
    button = Button(frame_button, text="Задание 2", command=task_2, font="Arial 10", width=9)
    button.grid(row=0, column=2, padx=1, sticky="we")
    button = Button(frame_button, text="Задание 3", command=task_3, font="Arial 10", width=9)
    button.grid(row=0, column=3, padx=1, sticky="we")
    #button = Button(frame_button, text="Random", command=size, font="Arial 10", width=9)
    #button.grid(column=3, row=0, padx=1)


def redrawing_of_gates():
    array = temporary_elements_and_index
    for element in range(0, len(array) - 1, 3):
        choice_from_gates(element=array[element], index_1=array[element+1], index_2=array[element+2], call_type=2)


# Меню
def swap_iec():
    """ Меняет нотацию на IEC """

    global style
    style = "iec"
    notation_menu.entryconfig(4, label="Выбран IEC")
    redrawing_of_gates()


def swap_ansi():
    """ Меняет нотацию на логические ANSI """

    global style
    style = "ansi"
    notation_menu.entryconfig(4, label="Выбран ANSI")
    redrawing_of_gates()


def swap_letter():
    """ Меняет нотацию на логические выражения """

    global style
    style = "log"
    notation_menu.entryconfig(4, label="Выбран Letter")
    redrawing_of_gates()


if __name__ == "__main__":
    main_menu.add_cascade(label="Нотация", menu=notation_menu)
    notation_menu.add_command(label="ANSI", command=swap_ansi)
    notation_menu.add_command(label="IEC", command=swap_iec)
    notation_menu.add_command(label="Letter", command=swap_letter)
    notation_menu.add_separator()
    notation_menu.add_command(label="Выбрано ANSI")

    spawn_buttons()
    root.mainloop()
