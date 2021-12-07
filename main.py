import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import logic_gates as lg


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
root.geometry('1920x1080')  # Размер окна

main_menu = Menu(root)
root.config(menu=main_menu)
notation_menu = Menu(main_menu, tearoff=0)

# Создание фреймов
frame_button = Frame(root)  # Фрейм с кнопками
frame_button.grid(column=0, row=0, sticky="nw", columnspan=2)
frame_gates = Frame(root)  # Фрейм с схемой relief=RIDGE, borderwidth=10, width=700, # height=660
frame_gates.grid(column=1, row=1, sticky="nw", padx=20, pady=20)
frame_task = Frame(root)  # Фрейм с заданием
frame_task.grid(column=1, row=2, sticky="sw")
frame_empty = Frame(root, width=50, height=850)  # Пустой фрейм, чтобы фрейм с заданием не скакал по экрану
frame_empty.grid(column=0, row=1, rowspan=2, sticky="w")

# Подгрузка и преобразование изображений в словарь
image_of_gates = {
    "im_true": ImageTk.PhotoImage(Image.open('image/input/true.png')),
    "im_false": ImageTk.PhotoImage(Image.open('image/input/false.png')),
    "im_question": ImageTk.PhotoImage(Image.open('image/input/qest.png')),
    "im_a": ImageTk.PhotoImage(Image.open('image/input/a.png')),
    "im_b": ImageTk.PhotoImage(Image.open('image/input/b.png')),
    "im_c": ImageTk.PhotoImage(Image.open('image/input/c.png')),
    "im_y": ImageTk.PhotoImage(Image.open('image/input/y.png')),
    "im_1": ImageTk.PhotoImage(Image.open('image/line/1.png')),
    "im_2": ImageTk.PhotoImage(Image.open('image/line/2.png')),
    "im_3": ImageTk.PhotoImage(Image.open('image/line/3.png')),
    "im_4": ImageTk.PhotoImage(Image.open('image/line/4.png')),
    "im_5": ImageTk.PhotoImage(Image.open('image/line/5.png')),
    "im_6": ImageTk.PhotoImage(Image.open('image/line/6.png')),
    "im_7": ImageTk.PhotoImage(Image.open('image/line/7.png')),
    "im_8": ImageTk.PhotoImage(Image.open('image/line/8.png')),
    "im_9": ImageTk.PhotoImage(Image.open('image/line/9.png')),
    "im_10": ImageTk.PhotoImage(Image.open('image/line/10.png')),
    "im_11": ImageTk.PhotoImage(Image.open('image/line/11.png')),
    "im_12": ImageTk.PhotoImage(Image.open('image/line/12.png')),
    "im_13": ImageTk.PhotoImage(Image.open('image/line/13.png')),
    "im_14": ImageTk.PhotoImage(Image.open('image/line/14.png'))
}

#Запись картинок в словари стилей
gates_styles = {
    "ansi": {  # ANSI
        "im_not": ImageTk.PhotoImage(Image.open('image/ansi/not.png')),
        "im_buf": ImageTk.PhotoImage(Image.open('image/ansi/buf.png')),
        "im_and": ImageTk.PhotoImage(Image.open('image/ansi/and.png')),
        "im_nand": ImageTk.PhotoImage(Image.open('image/ansi/nand.png')),
        "im_nor": ImageTk.PhotoImage(Image.open('image/ansi/nor.png')),
        "im_xnor": ImageTk.PhotoImage(Image.open('image/ansi/xnor.png')),
        "im_xor": ImageTk.PhotoImage(Image.open('image/ansi/xor.png')),
        "im_or": ImageTk.PhotoImage(Image.open('image/ansi/or.png'))
    },
    "iec": {  # ГОСТ
        "im_not": ImageTk.PhotoImage(Image.open('image/iec/not.png')),
        "im_buf": ImageTk.PhotoImage(Image.open('image/iec/buf.png')),
        "im_and": ImageTk.PhotoImage(Image.open('image/iec/and.png')),
        "im_nand": ImageTk.PhotoImage(Image.open('image/iec/nand.png')),
        "im_nor": ImageTk.PhotoImage(Image.open('image/iec/nor.png')),
        "im_xnor": ImageTk.PhotoImage(Image.open('image/iec/xnor.png')),
        "im_xor": ImageTk.PhotoImage(Image.open('image/iec/xor.png')),
        "im_or": ImageTk.PhotoImage(Image.open('image/iec/or.png'))
    },
    "log": {  # Логические обозначения
        "im_not": ImageTk.PhotoImage(Image.open('image/letter/not.png')),
        "im_buf": ImageTk.PhotoImage(Image.open('image/letter/buf.png')),
        "im_and": ImageTk.PhotoImage(Image.open('image/letter/and.png')),
        "im_nand": ImageTk.PhotoImage(Image.open('image/letter/nand.png')),
        "im_nor": ImageTk.PhotoImage(Image.open('image/letter/nor.png')),
        "im_xnor": ImageTk.PhotoImage(Image.open('image/letter/xnor.png')),
        "im_xor": ImageTk.PhotoImage(Image.open('image/letter/xor.png')),
        "im_or": ImageTk.PhotoImage(Image.open('image/letter/or.png'))
    }
}

style = "ansi"  # Метка используемого вида обозначений
temporary_data = []  # Хранилище временных данных: [str], bool*4
temporary_index = []  # Хранение координат
type_of_task = "task_1"  # Метка задания


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

    return elements, a, b, c, ans_elements[-1]


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

    return elements, a, b, c, ans_elements[-1]


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

    return elements, a, b, c, ans_elements[-1]


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

    return elements, a, b, c, ans_elements[-1]


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

    return elements, a, b, c, ans_elements[-1]


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

    return elements, a, b, c, ans_elements[-1]


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

    return elements, a, b, c, ans_elements[-1]


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

    return elements, a, b, c, ans_elements[-1]


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

    return elements, a, b, c, ans_elements[-1]


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

    return elements, a, b, c, ans_elements[-1]


def pattern_11() -> tuple:
    """ Шаблон 1 """

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

    return elements, a, b, c, ans_elements[-1]


def pattern_12() -> tuple:
    """ Шаблон 8 """

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
    elements[5] = random.choice(gates_for_1)

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

    return elements, a, b, c, ans_elements[-1]


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


def choice_from_gates_1(element: str, index_1: int, index_2: int):
    """ Определяет какой элемент отрисовывать при 1 входном сигнале """

    if element == 'buf':
        Label(frame_gates, image=gates_styles[style]["im_buf"]).grid(row=index_1, column=index_2)
    elif element == 'not':
        Label(frame_gates, image=gates_styles[style]["im_not"]).grid(row=index_1, column=index_2)
    else:
        print('Error in choice_from_gates_1')


def choice_from_gates_2(element: str, index_1: int, index_2: int):
    """ Определяет какой элемент отрисовывать при двух входных сигналах """

    if element == 'and':
        Label(frame_gates, image=gates_styles[style]["im_and"]).grid(row=index_1, column=index_2)
    elif element == 'or':
        Label(frame_gates, image=gates_styles[style]["im_or"]).grid(row=index_1, column=index_2)
    elif element == 'xor':
        Label(frame_gates, image=gates_styles[style]["im_xor"]).grid(row=index_1, column=index_2)
    elif element == 'nand':
        Label(frame_gates, image=gates_styles[style]["im_nand"]).grid(row=index_1, column=index_2)
    elif element == 'nor':
        Label(frame_gates, image=gates_styles[style]["im_nor"]).grid(row=index_1, column=index_2)
    elif element == 'xnor':
        Label(frame_gates, image=gates_styles[style]["im_nor"]).grid(row=index_1, column=index_2)
    else:
        print('Error in choice_from_gates_2')


def choice_from_0_1(vari: bool, index_1: int, index_2: int):
    """ Определяет какой элемент отрисовывать на входах и выходе """

    if vari:
        Label(frame_gates, image=image_of_gates["im_true"]).grid(row=index_1, column=index_2)
    elif not vari:
        Label(frame_gates, image=image_of_gates["im_false"]).grid(row=index_1, column=index_2)
    else:
        print('Error in choice_from_0_1')


def writing_to_temporary_data(a: bool, b: bool, c: bool, y: bool):
    """ В зависимости от необходимого входа или выхода помещает в временное хранилище нужное значение"""

    if type_of_task == "task_1":
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

    if type_of_task == "task_1" and this_letter == 4:
        Label(frame_gates, image=image_of_gates["im_y"]).grid(row=index_1, column=index_2)
        temporary_index.append(index_1)
        temporary_index.append(index_2)
    elif type_of_task == "task_1" and this_letter != 4:
        choice_from_0_1(signal, index_1, index_2)

    elif type_of_task == "task_2":
        if temporary_data[0] == this_letter:
            Label(frame_gates, image=image_of_gates["im_question"]).grid(row=index_1, column=index_2)
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

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=1)
    choice_from_gates_1(elements[0], 0, 2)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=0, column=3)

    # 2 строка
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=3)
    choice_from_gates_2(elements[2], 1, 4)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=1, column=5)

    # 3 строка
    choice_from_signal_image(2, 0, b, 2)
    Label(frame_gates, image=image_of_gates["im_4"]).grid(row=2, column=1)
    choice_from_gates_1(elements[1], 2, 2)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=2, column=3)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=5)
    choice_from_gates_2(elements[4], 2, 6)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=2, column=7)
    choice_from_signal_image(2, 8, y, 4)

    # 4 строка
    Label(frame_gates, image=image_of_gates["im_12"]).grid(row=3, column=1)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=3, column=2)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=3, column=3)
    Label(frame_gates, image=image_of_gates["im_11"]).grid(row=3, column=5)

    # 5 строка
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=4, column=3)
    choice_from_gates_2(elements[3], 4, 4)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=4, column=5)

    # 6 строка
    choice_from_signal_image(5, 0, c, 3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=5, column=1)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=5, column=2)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=5, column=3)


def circuit_2():
    """ Прорисовка 2 варианта """

    elements_in_circuit = pattern_2()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=1)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=0, column=2)

    # 2 строка
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=2)
    choice_from_gates_2(elements[0], 1, 3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=1, column=4)
    choice_from_gates_1(elements[2], 1, 5)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=1, column=6)

    # 3 строка
    choice_from_signal_image(2, 0, b, 2)
    Label(frame_gates, image=image_of_gates["im_4"]).grid(row=2, column=1)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=2, column=2)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=6)
    choice_from_gates_2(elements[3], 2, 7)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=2, column=8)
    choice_from_signal_image(2, 9, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, c, 3)
    Label(frame_gates, image=image_of_gates["im_6"]).grid(row=3, column=1)
    choice_from_gates_2(elements[3], 3, 2)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=3, column=3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=3, column=4)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=3, column=5)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=3, column=6)


def circuit_3():
    """ Прорисовка 3 варианта """

    elements_in_circuit = pattern_3()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    Label(frame_gates, image=image_of_gates["im_7"]).grid(row=0, column=1)
    choice_from_gates_2(elements[0], 0, 2)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=3)
    choice_from_gates_1(elements[2], 0, 4)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=0, column=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    Label(frame_gates, image=image_of_gates["im_10"]).grid(row=1, column=1)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=5)
    choice_from_gates_2(elements[4], 1, 6)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=1, column=7)
    choice_from_signal_image(1, 8, y, 4)

    # 3 строка
    choice_from_signal_image(2, 0, c, 3)
    Label(frame_gates, image=image_of_gates["im_6"]).grid(row=2, column=1)
    choice_from_gates_2(elements[1], 2, 2)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=2, column=3)
    choice_from_gates_1(elements[3], 2, 4)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=2, column=5)


def circuit_4():
    """ Прорисовка 4 варианта """

    elements_in_circuit = pattern_4()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    Label(frame_gates, image=image_of_gates["im_7"]).grid(row=0, column=1)
    choice_from_gates_2(elements[0], 0, 2)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=4)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=0, column=5)

    # 2 строка
    Label(frame_gates, image=image_of_gates["im_11"]).grid(row=1, column=1)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=5)
    choice_from_gates_2(elements[0], 1, 6)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=1, column=7)

    # 3 строка
    Label(frame_gates, image=image_of_gates["im_11"]).grid(row=2, column=1)
    choice_from_signal_image(2, 2, c, 3)
    Label(frame_gates, image=image_of_gates["im_7"]).grid(row=2, column=3)
    choice_from_gates_2(elements[1], 2, 4)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=2, column=5)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=7)
    choice_from_gates_2(elements[4], 2, 8)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=2, column=9)
    choice_from_signal_image(2, 10, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, b, 2)
    Label(frame_gates, image=image_of_gates["im_9"]).grid(row=3, column=1)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=3, column=2)
    Label(frame_gates, image=image_of_gates["im_9"]).grid(row=3, column=3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=3, column=4)
    choice_from_gates_1(elements[3], 3, 5)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=3, column=6)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=3, column=7)


def circuit_5():
    """ Прорисовка 5 варианта """

    elements_in_circuit = pattern_5()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    Label(frame_gates, image=image_of_gates["im_7"]).grid(row=0, column=1)
    choice_from_gates_2(elements[0], 0, 2)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=3)
    choice_from_gates_1(elements[2], 0, 4)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=0, column=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    Label(frame_gates, image=image_of_gates["im_10"]).grid(row=1, column=1)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=5)
    choice_from_gates_2(elements[3], 1, 6)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=1, column=7)
    choice_from_gates_1(elements[4], 1, 8)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=1, column=9)
    choice_from_signal_image(1, 10, y, 4)

    # 3 строка
    choice_from_signal_image(2, 0, c, 3)
    Label(frame_gates, image=image_of_gates["im_6"]).grid(row=2, column=1)
    choice_from_gates_2(elements[1], 2, 2)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=2, column=3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=2, column=4)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=2, column=5)


def circuit_6():
    """ Прорисовка 6 варианта """

    elements_in_circuit = pattern_6()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    Label(frame_gates, image=image_of_gates["im_4"]).grid(row=0, column=1)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=2)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=4)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=0, column=5)

    # 2 строка
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=1)
    choice_from_gates_2(elements[0], 1, 2)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=1, column=3)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=5)
    choice_from_gates_2(elements[3], 1, 6)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=1, column=7)
    choice_from_signal_image(1, 8, y, 4)

    # 3 строка
    choice_from_0_1(b, 3, 0)
    choice_from_signal_image(2, 0, b, 2)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=2, column=1)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=3)
    choice_from_gates_2(elements[2], 2, 4)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=2, column=5)

    # 4 строка
    choice_from_0_1(c, 3, 0)
    choice_from_signal_image(3, 0, c, 3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=3, column=1)
    choice_from_gates_1(elements[1], 3, 2)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=3, column=3)


def circuit_7():
    """ Прорисовка 7 варианта """

    elements_in_circuit = pattern_7()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]
    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    Label(frame_gates, image=image_of_gates["im_13"]).grid(row=0, column=1)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=2)
    choice_from_gates_1(elements[0], 0, 3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=4)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=0, column=5)

    # 2 строка
    choice_from_signal_image(1, 0, a, 1)
    Label(frame_gates, image=image_of_gates["im_9"]).grid(row=1, column=1)
    choice_from_gates_1(elements[1], 1, 2)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=1, column=3)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=5)
    choice_from_gates_2(elements[3], 1, 6)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=1, column=7)

    # 3 строка
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=3)
    choice_from_gates_2(elements[2], 2, 4)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=2, column=5)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=7)
    choice_from_gates_2(elements[5], 2, 8)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=2, column=9)
    choice_from_signal_image(2, 10, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, b, 2)
    Label(frame_gates, image=image_of_gates["im_4"]).grid(row=3, column=1)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=3, column=2)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=3, column=3)
    Label(frame_gates, image=image_of_gates["im_11"]).grid(row=3, column=7)

    # 5 строка
    choice_from_signal_image(4, 0, c, 3)
    Label(frame_gates, image=image_of_gates["im_6"]).grid(row=4, column=1)
    choice_from_gates_2(elements[4], 4, 2)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=4, column=3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=4, column=4)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=4, column=5)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=4, column=6)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=4, column=7)


def circuit_8():
    """ Прорисовка 8 варианта """

    elements_in_circuit = pattern_8()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    Label(frame_gates, image=image_of_gates["im_7"]).grid(row=0, column=1)
    choice_from_gates_2(elements[0], 0, 2)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=3)
    choice_from_gates_1(elements[2], 0, 4)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=0, column=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    Label(frame_gates, image=image_of_gates["im_14"]).grid(row=1, column=1)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=1, column=2)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=1, column=3)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=5)
    choice_from_gates_2(elements[4], 1, 6)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=1, column=7)
    choice_from_signal_image(1, 8, y, 4)

    # 3 строка
    Label(frame_gates, image=image_of_gates["im_11"]).grid(row=2, column=1)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=3)
    choice_from_gates_2(elements[3], 2, 4)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=2, column=5)

    # 4 строка
    choice_from_signal_image(3, 0, c, 3)
    Label(frame_gates, image=image_of_gates["im_6"]).grid(row=3, column=1)
    choice_from_gates_2(elements[1], 3, 2)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=3, column=3)


def circuit_9():
    """ Прорисовка 9 варианта """

    elements_in_circuit = pattern_9()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    Label(frame_gates, image=image_of_gates["im_13"]).grid(row=0, column=1)
    choice_from_gates_1(elements[0], 0, 2)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=0, column=3)

    # 2 строка
    choice_from_signal_image(1, 0, a, 1)
    Label(frame_gates, image=image_of_gates["im_10"]).grid(row=1, column=1)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=3)
    choice_from_gates_2(elements[2], 1, 4)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=1, column=5)

    # 3 строка
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=1)
    choice_from_gates_2(elements[1], 2, 2)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=2, column=3)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=5)
    choice_from_gates_2(elements[5], 2, 6)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=2, column=7)
    choice_from_signal_image(2, 8, y, 4)
    choice_from_signal_image(3, 0, b, 2)

    Label(frame_gates, image=image_of_gates["im_10"]).grid(row=3, column=1)
    Label(frame_gates, image=image_of_gates["im_11"]).grid(row=3, column=5)

    # 4 строка
    choice_from_signal_image(4, 0, c, 3)
    Label(frame_gates, image=image_of_gates["im_6"]).grid(row=4, column=1)
    choice_from_gates_2(elements[3], 4, 2)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=4, column=3)
    choice_from_gates_1(elements[4], 4, 4)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=4, column=5)


def circuit_10():
    """ Прорисовка 10 варианта """

    elements_in_circuit = pattern_10()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    Label(frame_gates, image=image_of_gates["im_7"]).grid(row=0, column=1)
    choice_from_gates_2(elements[0], 0, 2)
    Label(frame_gates, image=image_of_gates["im_4"]).grid(row=0, column=3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=0, column=4)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=0, column=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=1, column=1)
    Label(frame_gates, image=image_of_gates["im_11"]).grid(row=1, column=3)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=5)
    choice_from_gates_2(elements[2], 1, 6)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=1, column=7)

    # 3 строка
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=3)
    choice_from_gates_2(elements[1], 2, 4)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=2, column=5)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=7)
    choice_from_gates_2(elements[4], 2, 8)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=2, column=9)
    choice_from_signal_image(2, 10, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, c, 3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=3, column=1)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=3, column=2)
    Label(frame_gates, image=image_of_gates["im_10"]).grid(row=3, column=3)
    Label(frame_gates, image=image_of_gates["im_11"]).grid(row=3, column=7)

    # 5 строка
    Label(frame_gates, image=image_of_gates["im_12"]).grid(row=4, column=3)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=4, column=4)
    choice_from_gates_1(elements[3], 4, 5)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=4, column=6)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=4, column=7)


def circuit_11():
    """ Прорисовка 11 варианта """

    elements_in_circuit = pattern_11()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    writing_to_temporary_data(a, b, c, y)

    # 1 строка
    choice_from_signal_image(0, 0, a, 1)
    Label(frame_gates, image=image_of_gates["im_7"]).grid(row=0, column=1)
    choice_from_gates_2(elements[0], 0, 2)
    Label(frame_gates, image=image_of_gates["im_4"]).grid(row=0, column=3)
    choice_from_gates_1(elements[2], 0, 4)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=0, column=5)

    # 2 строка
    choice_from_signal_image(1, 0, b, 2)
    Label(frame_gates, image=image_of_gates["im_10"]).grid(row=1, column=1)
    Label(frame_gates, image=image_of_gates["im_11"]).grid(row=1, column=3)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=5)
    choice_from_gates_2(elements[4], 1, 6)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=1, column=7)
    choice_from_signal_image(1, 8, y, 4)

    # 3 строка
    Label(frame_gates, image=image_of_gates["im_11"]).grid(row=2, column=1)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=3)
    choice_from_gates_2(elements[3], 2, 4)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=2, column=5)

    # 4 строка
    choice_from_signal_image(3, 0, c, 3)
    Label(frame_gates, image=image_of_gates["im_6"]).grid(row=3, column=1)
    choice_from_gates_2(elements[1], 3, 2)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=3, column=3)


def circuit_12():
    """ Прорисовка 8 варианта """

    elements_in_circuit = pattern_12()
    global temporary_data

    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    if type_of_task == "task_1":
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
    Label(frame_gates, image=image_of_gates["im_13"]).grid(row=0, column=1)
    choice_from_gates_1(elements[0], 0, 2)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=0, column=3)

    # 2 строка
    choice_from_signal_image(1, 0, a, 1)
    Label(frame_gates, image=image_of_gates["im_10"]).grid(row=1, column=1)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=1, column=3)
    choice_from_gates_2(elements[3], 1, 4)
    Label(frame_gates, image=image_of_gates["im_2"]).grid(row=1, column=5)

    # 3 строка
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=1)
    choice_from_gates_2(elements[1], 2, 2)
    Label(frame_gates, image=image_of_gates["im_10"]).grid(row=2, column=3)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=2, column=5)
    choice_from_gates_2(elements[5], 2, 6)
    Label(frame_gates, image=image_of_gates["im_1"]).grid(row=2, column=7)
    choice_from_signal_image(2, 8, y, 4)

    # 4 строка
    choice_from_signal_image(3, 0, b, 2)
    Label(frame_gates, image=image_of_gates["im_10"]).grid(row=3, column=1)
    Label(frame_gates, image=image_of_gates["im_3"]).grid(row=3, column=3)
    choice_from_gates_2(elements[4], 3, 4)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=3, column=5)

    # 5 строка
    Label(frame_gates, image=image_of_gates["im_12"]).grid(row=4, column=1)
    choice_from_gates_1(elements[2], 4, 2)
    Label(frame_gates, image=image_of_gates["im_5"]).grid(row=4, column=3)


def answer_user_true():
    """ Вызывает функцию с обработкой ответа с True """
    answer_user(True)


def answer_user_false():
    """ Вызывает функцию с обработкой ответа с False """
    answer_user(False)


def answer_user(answer: bool):
    """ Принимает ответ пользователя из формы """

    for widget in frame_task.winfo_children():
        widget.destroy()

    if answer == temporary_data[-1]:
        Label(frame_task,
              text='Ответ верный', font="Arial 15").grid(row=0, column=0, sticky="nw", padx=20, pady=20)
    else:
        Label(frame_task,
              text='Ответ неверный', font="Arial 15").grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    button = ''  # Без изначального инициализирования ругается
    if type_of_task == "task_1":
        button = Button(frame_task, text="Следующее задание", font="Arial 15", command=task_1)
    elif type_of_task == "task_2":
        button = Button(frame_task, text="Следующее задание", font="Arial 15", command=task_2)
    button.grid(column=0, row=1, sticky="nw", padx=20, pady=10)

    if temporary_data[-1]:
        Label(frame_gates, image=image_of_gates["im_true"]).grid(row=temporary_index[0], column=temporary_index[1])
    else:
        Label(frame_gates, image=image_of_gates["im_false"]).grid(row=temporary_index[0], column=temporary_index[1])


def task_1():
    """ Задание, где пользователю не известен вывод при всех остальных известных значениях """
    global type_of_task
    type_of_task = "task_1"

    for widget in frame_gates.winfo_children():
        widget.destroy()
    for widget in frame_task.winfo_children():
        widget.destroy()

    global temporary_data
    global temporary_index
    temporary_data = []
    temporary_index = []

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

    global temporary_data
    global temporary_index
    temporary_data = []
    temporary_index = []

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

    #circuit_12()

    button = Button(frame_task, text="True", font="Arial 15", command=answer_user_true, width=8)  # relief="flat" для более стильного дизайна
    button.grid(column=0, row=1, sticky="ws", padx=20, pady=10)
    button = Button(frame_task, text="False", font="Arial 15", command=answer_user_false, width=8)
    button.grid(column=0, row=2, sticky="sw", padx=20, pady=10)


def random_task():
    number_of_task = random.randint(1, 2)
    if number_of_task == 1:
        task_1()
    else:
        task_2()


def spawn_buttons():
    button = Button(frame_button, text="Задание 1", command=task_1, font="Arial 10", width=9)
    button.grid(column=1, row=0, padx=1)
    button = Button(frame_button, text="Задание 2", command=task_2, font="Arial 10", width=9)
    button.grid(column=2, row=0, padx=1)
    #button = Button(frame_button, text="Random", command=random_task, font="Arial 10", width=9)
    #button.grid(column=3, row=0, padx=1)


# Меню
def swap_iec():
    """ Меняет нотацию на IEC """

    global style
    style = "iec"
    notation_menu.entryconfig(4, label="Выбран IEC")


def swap_ansi():
    """ Меняет нотацию на логические ANSI """

    global style
    style = "ansi"
    notation_menu.entryconfig(4, label="Выбран ANSI")


def swap_letter():
    """ Меняет нотацию на логические выражения """

    global style
    style = "log"
    notation_menu.entryconfig(4, label="Выбран Letter")


main_menu.add_cascade(label="Нотация", menu=notation_menu)
notation_menu.add_command(label="IEC", command=swap_iec)
notation_menu.add_command(label="ANSI", command=swap_ansi)
notation_menu.add_command(label="Letter", command=swap_letter)
notation_menu.add_separator()
notation_menu.add_command(label="Выбрано ANSI")


spawn_buttons()
root.mainloop()
