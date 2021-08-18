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
        Инвертирует значения вентиля И"""
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
