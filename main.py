import random

qua_size = 3  # Количество переменных
max_operations = 4

task = []


""" def transformation(task: str, separator=' ') -> str:
     Преобразует изначальную строку в строку, которую понимает интерпритатор

    task_final = task.split(separator)  # Разделение строки по пробелу в список

    ''' Замена операций '''
    for i in range(len(task_final)):
        if task_final[i] == '*':
            task_final[i] = 'and'
        elif task_final[i] == '+':
            task_final[i] = 'or'
        elif task_final[i] == '-':
            task_final[i] = 'not'

    task_final = ' '.join(task_final)  # Конечный вариант строки, которая обрабатывается интерпритатором

    return task_final """


def matrix_calculation(size: int) -> tuple:
    """Рассчет и заполнение матрицы истинности операндов"""

    '''Рассчет размера матрицы'''
    matrix_height = 2 ** size  # Количество строк
    matrix_width = size + 1  # Количество колонок

    '''Создание матрицы'''
    matrix = [['?' for i in range(matrix_width)] for j in range(matrix_height)]

    '''Присвоение таблице истинности 0 и 1'''
    for i in range(matrix_height):
        for j in range(3):
            if j == 0 and i <= 3:
                matrix[i][j] = False
            elif j == 0 and i > 3:
                matrix[i][j] = True

            if j == 2 and i % 2 == 0:
                matrix[i][j] = False
            elif j == 2 and i % 2 == 1:
                matrix[i][j] = True

    for i in range(0, matrix_height, 4):
        matrix[i][1] = False
        matrix[i + 1][1] = False

    for i in range(2, matrix_height, 4):
        matrix[i][1] = True
        matrix[i + 1][1] = True


    return matrix, matrix_height, matrix_width



def solution() -> list:
    """ Решение матрицы """
    matrix, height, width = matrix_calculation(qua_size)
    task = generation(max_operations)

    for row in range(height):
        a = matrix[row][0]
        b = matrix[row][1]
        c = matrix[row][2]
        matrix[row][width-1] = eval(task)
    print(task)

    return matrix




def show_matrix():
    """Решение и вывод матрицы на экран"""
    matrix = solution()
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()



def generation(max_operation: int) -> list:
    operation = 0
    exam_a = 0
    exam_b = 0
    exam_c = 0

    task_original11 = []
    oper_and_var = ['a', 'b', 'c', 'not']
    vari = ['a', 'b', 'c']
    oper = ['or', 'and']
    not_and_var = ['not', 'a', 'b', 'c']
    while operation < max_operation:
        if task_original11 == []:
            task_original11.append(random.choice(oper_and_var))
        else:
            if task_original11[-1] == 'not':
                task_original11.append(random.choice(vari))
            elif task_original11[-1] in 'abc':
                task_original11.append(random.choice(oper))
                operation += 1
            else:
                task_original11.append(random.choice(not_and_var))

        if task_original11[-1] == 'a':
            exam_a += 1
        elif task_original11[-1] == 'b':
            exam_b += 1
        elif task_original11[-1] == 'c':
            exam_c += 1



    if exam_a == 0:
        task_original11.append('a')
    elif exam_b == 0:
        task_original11.append('b')
    elif exam_b == 0:
        task_original11.append('c')
    else:
        task_original11.append(random.choice(vari))

    task_original11 = ' '.join(task_original11)  # Конечный вариант строки, которая обрабатывается интерпритатором

    
    return task_original11



def examination():
    """ Создает матрицу, с которой будет работать пользователь """

    exam_matrix, height, width = matrix_calculation(qua_size)
    print(exam_matrix)




def main():
    """ Основная функция программы """
    show_matrix()




main()

