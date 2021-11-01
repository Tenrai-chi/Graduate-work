import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

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
root.title('????????????')  # Заголовок окна
root.geometry('1500x1200')  # Размер окна


# Подгрузка и преобразование изображений
im_true = ImageTk.PhotoImage(Image.open('image/true.png'))
im_false = ImageTk.PhotoImage(Image.open('image/false.png'))
im_answer = ImageTk.PhotoImage(Image.open('image/y.png'))
im_a = ImageTk.PhotoImage(Image.open('image/a.png'))
im_b = ImageTk.PhotoImage(Image.open('image/b.png'))
im_c = ImageTk.PhotoImage(Image.open('image/c.png'))


# Буквенное

'''im_not = ImageTk.PhotoImage(Image.open('image/not.png'))
im_buf = ImageTk.PhotoImage(Image.open('image/buf.png'))
im_and = ImageTk.PhotoImage(Image.open('image/and.png'))
im_nand = ImageTk.PhotoImage(Image.open('image/nand.png'))
im_nor = ImageTk.PhotoImage(Image.open('image/nor.png'))
im_xnor = ImageTk.PhotoImage(Image.open('image/xnor.png'))
im_xor = ImageTk.PhotoImage(Image.open('image/xor.png'))
im_or = ImageTk.PhotoImage(Image.open('image/or.png'))'''

# Символьное

im_not = ImageTk.PhotoImage(Image.open('image/new/not.png'))
im_buf = ImageTk.PhotoImage(Image.open('image/new/buf.png'))
im_and = ImageTk.PhotoImage(Image.open('image/new/and.png'))
im_nand = ImageTk.PhotoImage(Image.open('image/new/nand.png'))
im_nor = ImageTk.PhotoImage(Image.open('image/new/nor.png'))
im_xnor = ImageTk.PhotoImage(Image.open('image/new/xnor.png'))
im_xor = ImageTk.PhotoImage(Image.open('image/new/xor.png'))
im_or = ImageTk.PhotoImage(Image.open('image/new/or.png'))


im_1 = ImageTk.PhotoImage(Image.open('image/1.png'))
im_2 = ImageTk.PhotoImage(Image.open('image/2.png'))
im_3 = ImageTk.PhotoImage(Image.open('image/3.png'))
im_4 = ImageTk.PhotoImage(Image.open('image/4.png'))
im_5 = ImageTk.PhotoImage(Image.open('image/5.png'))
im_6 = ImageTk.PhotoImage(Image.open('image/6.png'))
im_7 = ImageTk.PhotoImage(Image.open('image/7.png'))
im_8 = ImageTk.PhotoImage(Image.open('image/8.png'))
im_9 = ImageTk.PhotoImage(Image.open('image/9.png'))
im_10 = ImageTk.PhotoImage(Image.open('image/10.png'))
im_11 = ImageTk.PhotoImage(Image.open('image/11.png'))
im_12 = ImageTk.PhotoImage(Image.open('image/12.png'))
im_13 = ImageTk.PhotoImage(Image.open('image/13.png'))


def log_NOT(a: bool) -> bool:
    """ Вентилль НЕ
        Возвращает инвертированное значение входящей переменной """
    y = not a

    return y


def log_BUF(a: bool) -> bool:
    """ Вентиль БУФФЕР
        Возвращает входящее значение """
    y = a

    return y


def log_AND(a, b: bool) -> bool:
    """ Вентиль И
        Возвращает истину, если лба входящих значения истины """
    y = a and b

    return y


def log_OR(a, b: bool) -> bool:
    """ Вентиль ИЛИ
        Возвращает истину, если хотя бы 1 входящее значение истино """
    y = a or b

    return y


def log_XOR(a, b: bool) -> bool:
    """ Вентиль ИСКЛЮЧАЮЩЕЕ ИЛИ
        Возвращает истину, если один из входящих значений истино, а другой ложно """
    if a == True and b == False or a == False and b == True:
        y = True
    else:
        y = False

    return y


def log_NAND(a, b: bool) -> bool:
    """ Вентиль И-НЕ
        Возвращает истиннцу, если хотя бы один из входящих значений ложно
        Инвертирует значения вентиля И """
    if a == False or b == False:
        y = True
    else:
        y = False

    return y


def log_NOR(a, b: bool) -> bool:
    """ Вентиль ИЛИ-НЕ
        Возвращает истиннцу, если оба входящих значения ложны
        Инвертирует значения вентиля ИЛИ """
    if a == False and b == False:
        y = True
    else:
        y = False

    return y


def log_XNOR(a, b: bool) -> bool:
    """ Вентиль ИСКЛЮЧАЮЩЕЕ ИЛИ_НЕ
     Возвращает истину, если входящие значения равно между собой """
    if a == True and b == True or a == False and b == False:
        y = True
    else:
        y = False

    return y


def log_NOR3(a, b, c: bool) -> bool:
    """ Вентиль ИЛИ-НЕ с 3 входами
        Возвращает истину, только если все входящие значения ложны"""
    if a == False and b == False and c == False:
        y = True
    else:
        y = False
    return y


def pattern_1():
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


def pattern_2():
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


def pattern_3():
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


def pattern_4():
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


def pattern_5():
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


def pattern_6():
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


def pattern_7():
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


def pattern_8():
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
    """ решение выражения с заданным действием и параметрами """

    # Выражения с 1 входящим значением
    if operation == 'not':
        return log_NOT(enter_a)
    elif operation == 'buf':
        return log_BUF(enter_a)

    # Выражения с 2 входящими значениеми
    elif operation == 'and':
        return log_AND(enter_a, enter_b)
    elif operation == 'or':
        return log_OR(enter_a, enter_b)
    elif operation == 'xor':
        return log_XOR(enter_a, enter_b)
    elif operation == 'nand':
        return log_NAND(enter_a, enter_b)
    elif operation == 'nor':
        return log_NOR(enter_a, enter_b)
    elif operation == 'xnor':
        return log_XNOR(enter_a, enter_b)

    # Выражения с 3 входящими значениеми
    else:
        return log_NOR3(enter_a, enter_b, enter_c)


def choice_from_gates_1(element: str, index_1: int, index_2: int):
    """ Определяет какой элемент отрисовывать при 1 входном сигнале """

    if element == 'buf':
        Label(root, image=im_buf).grid(row=index_1, column=index_2)
    else:
        Label(root, image=im_not).grid(row=index_1, column=index_2)


def choice_from_gates_2(element: str, index_1: int, index_2: int):
    """ Определяет какой элемент отрисовывать при двух входных сигналах """

    if element == 'and':
        Label(root, image=im_and).grid(row=index_1, column=index_2)
    elif element == 'or':
        Label(root, image=im_or).grid(row=index_1, column=index_2)
    elif element == 'xor':
        Label(root, image=im_xor).grid(row=index_1, column=index_2)
    elif element == 'nand':
        Label(root, image=im_nand).grid(row=index_1, column=index_2)
    elif element == 'nor':
        Label(root, image=im_nor).grid(row=index_1, column=index_2)
    else:
        Label(root, image=im_xnor).grid(row=index_1, column=index_2)


def choice_from_0_1(vari: bool, index_1: int, index_2: int):
    """ Определяет какой элемент отрисовывать на входах и выходе """

    if vari:
        Label(root, image=im_true).grid(row=index_1, column=index_2)
    else:
        Label(root, image=im_false).grid(row=index_1, column=index_2)


def circuit_1():
    """ Прорисовка 1 варианта """

    elements_in_circuit = pattern_1()
    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    # 1 строка
    choice_from_0_1(a, 0, 0)
    Label(root, image=im_1).grid(row=0, column=1)
    choice_from_gates_1(elements[0], 0, 2)
    Label(root, image=im_2).grid(row=0, column=3)

    # 2 строка
    Label(root, image=im_3).grid(row=1, column=3)
    choice_from_gates_2(elements[2], 1, 4)
    Label(root, image=im_2).grid(row=1, column=5)

    # 3 строка
    choice_from_0_1(b, 2, 0)
    Label(root, image=im_4).grid(row=2, column=1)
    choice_from_gates_1(elements[1], 2, 2)
    Label(root, image=im_buf).grid(row=2, column=2)
    Label(root, image=im_5).grid(row=2, column=3)
    Label(root, image=im_3).grid(row=2, column=5)
    choice_from_gates_2(elements[4], 2, 6)
    Label(root, image=im_1).grid(row=2, column=7)
    choice_from_0_1(y, 2, 8)

    # 4 строка
    Label(root, image=im_12).grid(row=3, column=1)
    Label(root, image=im_1).grid(row=3, column=2)
    Label(root, image=im_2).grid(row=3, column=3)
    Label(root, image=im_11).grid(row=3, column=5)

    # 5 строка
    Label(root, image=im_3).grid(row=4, column=3)
    choice_from_gates_2(elements[3], 4, 4)
    Label(root, image=im_xnor).grid(row=4, column=4)
    Label(root, image=im_5).grid(row=4, column=5)

    # 6 строка
    choice_from_0_1(c, 5, 0)
    Label(root, image=im_1).grid(row=5, column=1)
    Label(root, image=im_1).grid(row=5, column=2)
    Label(root, image=im_5).grid(row=5, column=3)


def circuit_2():
    """ Прорисовка 2 варианта """

    elements_in_circuit = pattern_2()
    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    # 1 строка
    choice_from_0_1 (a, 0, 0)
    Label(root, image=im_1).grid(row=0, column=1)
    Label(root, image=im_2).grid(row=0, column=2)

    # 2 строка
    Label(root, image=im_3).grid(row=1, column=2)
    choice_from_gates_2(elements[0], 1, 3)
    Label(root, image=im_1).grid(row=1, column=4)
    choice_from_gates_1(elements[2], 1, 5)
    Label(root, image=im_2).grid(row=1, column=6)

    # 3 строка
    choice_from_0_1(b, 2, 0)
    Label(root, image=im_4).grid(row=2, column=1)
    Label(root, image=im_5).grid(row=2, column=2)
    Label(root, image=im_3).grid(row=2, column=6)
    choice_from_gates_2(elements[3], 2, 7)
    Label(root, image=im_1).grid(row=2, column=8)
    choice_from_0_1(y, 2, 9)

    # 4 строка
    choice_from_0_1(c, 3, 0)
    Label(root, image=im_6).grid(row=3, column=1)
    choice_from_gates_2(elements[3], 3, 2)
    Label(root, image=im_1).grid(row=3, column=3)
    Label(root, image=im_1).grid(row=3, column=4)
    Label(root, image=im_1).grid(row=3, column=5)
    Label(root, image=im_5).grid(row=3, column=6)


def circuit_3():
    """ Прорисовка 3 варианта """

    elements_in_circuit = pattern_3()
    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    # 1 строка
    choice_from_0_1(a, 0, 0)
    Label(root, image=im_7).grid(row=0, column=1)
    choice_from_gates_2(elements[0], 0, 2)
    Label(root, image=im_1).grid(row=0, column=3)
    choice_from_gates_1(elements[2], 0, 4)
    Label(root, image=im_2).grid(row=0, column=5)

    # 2 строка
    choice_from_0_1(b, 1, 0)
    Label(root, image=im_10).grid(row=1, column=1)
    Label(root, image=im_3).grid(row=1, column=5)
    choice_from_gates_2(elements[4], 1, 6)
    Label(root, image=im_1).grid(row=1, column=7)
    choice_from_0_1(y, 1, 8)

    # 3 строка
    choice_from_0_1(c, 2, 0)
    Label(root, image=im_6).grid(row=2, column=1)
    choice_from_gates_2(elements[1], 2, 2)
    Label(root, image=im_1).grid(row=2, column=3)
    choice_from_gates_1(elements[3], 2, 4)
    Label(root, image=im_5).grid(row=2, column=5)


def circuit_4():
    """ Прорисовка 4 варианта """

    elements_in_circuit = pattern_4()
    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    # 1 строка
    choice_from_0_1(a, 0, 0)
    Label(root, image=im_7).grid(row=0, column=1)
    choice_from_gates_2(elements[0], 0, 2)
    Label(root, image=im_1).grid(row=0, column=3)
    Label(root, image=im_1).grid(row=0, column=4)
    Label(root, image=im_2).grid(row=0, column=5)

    # 2 строка
    Label(root, image=im_11).grid(row=1, column=1)
    Label(root, image=im_3).grid(row=1, column=5)
    choice_from_gates_2(elements[0], 1, 6)
    Label(root, image=im_2).grid(row=1, column=7)

    # 3 строка
    Label(root, image=im_11).grid(row=2, column=1)
    choice_from_0_1(c, 2, 2)
    Label(root, image=im_7).grid(row=2, column=3)
    choice_from_gates_2(elements[1], 2, 4)
    Label(root, image=im_5).grid(row=2, column=5)
    Label(root, image=im_3).grid(row=2, column=7)
    choice_from_gates_2(elements[4], 2, 8)
    Label(root, image=im_xor).grid(row=2, column=8)
    Label(root, image=im_1).grid(row=2, column=9)
    choice_from_0_1(y, 2, 10)

    # 4 строка
    choice_from_0_1(b, 3, 0)
    Label(root, image=im_9).grid(row=3, column=1)
    Label(root, image=im_1).grid(row=3, column=2)
    Label(root, image=im_9).grid(row=3, column=3)
    Label(root, image=im_1).grid(row=3, column=4)
    choice_from_gates_1(elements[3], 3, 5)
    Label(root, image=im_1).grid(row=3, column=6)
    Label(root, image=im_5).grid(row=3, column=7)


def circuit_5():
    """ Прорисовка 5 варианта """

    elements_in_circuit = pattern_5()
    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    # 1 строка
    choice_from_0_1(a, 0, 0)
    Label(root, image=im_7).grid(row=0, column=1)
    choice_from_gates_2(elements[0], 0, 2)
    Label(root, image=im_1).grid(row=0, column=3)
    choice_from_gates_1(elements[2], 0, 4)
    Label(root, image=im_2).grid(row=0, column=5)

    # 2 строка
    choice_from_0_1(b, 1, 0)
    Label(root, image=im_10).grid(row=1, column=1)
    Label(root, image=im_3).grid(row=1, column=5)
    choice_from_gates_2(elements[3], 1, 6)
    Label(root, image=im_1).grid(row=1, column=7)
    choice_from_gates_1(elements[4], 1, 8)
    Label(root, image=im_1).grid(row=1, column=9)
    choice_from_0_1(y, 1, 10)

    # 3 строка
    choice_from_0_1(c, 2, 0)
    Label(root, image=im_6).grid(row=2, column=1)
    choice_from_gates_2(elements[1], 2, 2)
    Label(root, image=im_1).grid(row=2, column=3)
    Label(root, image=im_1).grid(row=2, column=4)
    Label(root, image=im_5).grid(row=2, column=5)


def circuit_6():
    """ Прорисовка 6 варианта """

    elements_in_circuit = pattern_6()
    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    # 1 строка
    choice_from_0_1(a, 0, 0)
    Label(root, image=im_4).grid(row=0, column=1)
    Label(root, image=im_1).grid(row=0, column=2)
    Label(root, image=im_1).grid(row=0, column=3)
    Label(root, image=im_1).grid(row=0, column=4)
    Label(root, image=im_2).grid(row=0, column=5)

    # 2 строка
    Label(root, image=im_3).grid(row=1, column=1)
    choice_from_gates_2(elements[0], 1, 2)
    Label(root, image=im_2).grid(row=1, column=3)
    Label(root, image=im_3).grid(row=1, column=5)
    choice_from_gates_2(elements[3], 1, 6)
    Label(root, image=im_1).grid(row=1, column=7)
    choice_from_0_1(y, 1, 8)

    # 3 строка
    choice_from_0_1(b, 2, 0)
    Label(root, image=im_5).grid(row=2, column=1)
    Label(root, image=im_3).grid(row=2, column=3)
    choice_from_gates_2(elements[2], 2, 4)
    Label(root, image=im_5).grid(row=2, column=5)

    # 4 строка
    choice_from_0_1(c, 3, 0)
    Label(root, image=im_1).grid(row=3, column=1)
    choice_from_gates_1(elements[1], 3, 2)
    Label(root, image=im_5).grid(row=3, column=3)


def circuit_7():
    """ Прорисовка 7 варианта """

    elements_in_circuit = pattern_7()
    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    # 1 строка
    Label(root, image=im_13).grid(row=0, column=1)
    Label(root, image=im_1).grid(row=0, column=2)
    choice_from_gates_1(elements[0], 0, 3)
    Label(root, image=im_1).grid(row=0, column=4)
    Label(root, image=im_2).grid(row=0, column=5)

    # 2 строка
    choice_from_0_1(a, 1, 0)
    Label(root, image=im_9).grid(row=1, column=1)
    choice_from_gates_1(elements[1], 1, 2)
    Label(root, image=im_2).grid(row=1, column=3)
    Label(root, image=im_3).grid(row=1, column=5)
    choice_from_gates_2(elements[3], 1, 6)
    Label(root, image=im_2).grid(row=1, column=7)

    # 3 строка
    Label(root, image=im_3).grid(row=2, column=3)
    choice_from_gates_2(elements[2], 2, 4)
    Label(root, image=im_5).grid(row=2, column=5)
    Label(root, image=im_3).grid(row=2, column=7)
    choice_from_gates_2(elements[5], 2, 8)
    Label(root, image=im_1).grid(row=2, column=9)
    choice_from_0_1(y, 2, 10)

    # 4 строка
    choice_from_0_1(b, 3, 0)
    Label(root, image=im_4).grid(row=3, column=1)
    Label(root, image=im_1).grid(row=3, column=2)
    Label(root, image=im_5).grid(row=3, column=3)
    Label(root, image=im_11).grid(row=3, column=7)

    # 5 строка
    choice_from_0_1(c, 4, 0)
    Label(root, image=im_6).grid(row=4, column=1)
    choice_from_gates_2(elements[4], 4, 2)
    Label(root, image=im_1).grid(row=4, column=3)
    Label(root, image=im_1).grid(row=4, column=4)
    Label(root, image=im_1).grid(row=4, column=5)
    Label(root, image=im_1).grid(row=4, column=6)
    Label(root, image=im_5).grid(row=4, column=7)


def circuit_8():
    """ Прорисовка 8 варианта """

    elements_in_circuit = pattern_8()
    elements = elements_in_circuit[0]  # Элементы схемы
    a = elements_in_circuit[1]
    b = elements_in_circuit[2]
    c = elements_in_circuit[3]
    y = elements_in_circuit[4]

    # 1 строка
    Label(root, image=im_13).grid(row=0, column=1)
    choice_from_gates_1(elements[0], 0, 2)
    Label(root, image=im_2).grid(row=0, column=3)

    # 2 строка
    choice_from_0_1(a, 1, 0)
    Label(root, image=im_10).grid(row=1, column=1)
    Label(root, image=im_3).grid(row=1, column=3)
    choice_from_gates_2(elements[3], 1, 4)
    Label(root, image=im_2).grid(row=1, column=5)

    # 3 строка
    Label(root, image=im_3).grid(row=2, column=1)
    choice_from_gates_2(elements[1], 2, 2)
    Label(root, image=im_10).grid(row=2, column=3)
    Label(root, image=im_3).grid(row=2, column=5)
    choice_from_gates_2(elements[5], 2, 6)
    Label(root, image=im_1).grid(row=2, column=7)
    choice_from_0_1(y, 2, 8)

    # 4 строка
    choice_from_0_1(b, 3, 0)
    Label(root, image=im_10).grid(row=3, column=1)
    Label(root, image=im_3).grid(row=3, column=3)
    choice_from_gates_2(elements[4], 3, 4)
    Label(root, image=im_5).grid(row=3, column=5)

    # 5 строка
    Label(root, image=im_12).grid(row=4, column=1)
    choice_from_gates_1(elements[2], 4, 2)
    Label(root, image=im_5).grid(row=4, column=3)


def main():
    """ Основной цикл программы """

    pattern = random.randint(1, 8)
    if pattern == 1:
        circuit_1()
    elif pattern ==2:
        circuit_2()
    elif pattern == 3:
        circuit_3()
    elif pattern == 4:
        circuit_4()
    elif pattern == 5:
        circuit_5()
    elif pattern == 6:
        circuit_6()
    elif pattern == 7:
        circuit_7()
    else:
        circuit_8()

    #circuit_8()

main()
root.mainloop()
