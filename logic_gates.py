import random

gates_for_1 = ['not', 'buf']
gates_for_2 = ['and', 'or', 'xor', 'nand', 'nor', 'xnor']
gates_for_3 = ['nor3']
true_false = [True, False]


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
    print(elements, a, b, c)

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

    print(ans_elements)


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
    print(elements, a, b, c)

    ans_elements = []

    temp = solution(elements[0], a, b)
    ans_elements.append(temp)

    temp = solution(elements[1], b, c)
    ans_elements.append(temp)

    temp = solution(elements[2], ans_elements[0])
    ans_elements.append(temp)

    temp = solution(elements[3], ans_elements[2], ans_elements[1])
    ans_elements.append(temp)

    print(ans_elements)


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
    print(elements, a, b, c)

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

    print(ans_elements)


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
    print(elements, a, b, c)

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

    print(ans_elements)


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
    print(elements, a, b, c)

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

    print(ans_elements)


def solution(operation, enter_a, enter_b=True, enter_c=True) -> bool:
    """ решение выражения с заданным действием и параметрами """
    #Выражения с 1 входящим значением
    if operation == 'not':
        return log_NOT(enter_a)
    elif operation == 'buf':
        return log_BUF(enter_a)

    #Выражения с 2 входящими значениеми
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

    #Выражения с 3 входящими значениеми  '''
    else:
        return log_NOR3(enter_a, enter_b, enter_c)


pattern_5()
