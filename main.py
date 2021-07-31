qua_size = 3  # Количество переменных
#task_original = 'a * b + - c'  # Задание
#task_original = '- a + a * c + b'  # Задание
#task_original = 'a + b * c'  # Задание пройдено
task_original = 'a * c + b'  # Задание


def transformation(task: str, separator=' ') -> str:
    """ Преобразует изначальную строку в строку, которую понимает интерпритатор"""

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

    return task_final


def matrix_calculation(size: int) -> tuple:
    """Рассчет и заполнение маьтрицы истинности операндов"""

    '''Рассчет размера матрицы'''
    matrix_heigh = 2 ** size  # Количество строк
    matrix_width = size + 1  # Количество колонок

    '''Создание матрицы'''
    matrix = [['?' for i in range(matrix_width)] for j in range(matrix_heigh)]

    ''' Присвоение таблице истинности 0 и 1'''
    for i in range(matrix_heigh):
        for j in range(3):
            if j == 0 and i <= 3:
                matrix[i][j] = False
            elif j == 0 and i > 3:
                matrix[i][j] = True

            if j == 2 and i % 2 == 0:
                matrix[i][j] = False
            elif j == 2 and i % 2 == 1:
                matrix[i][j] = True

    for i in range(0, matrix_heigh, 4):
        matrix[i][1] = False
        matrix[i + 1][1] = False

    for i in range(2, matrix_heigh, 4):
        matrix[i][1] = True
        matrix[i + 1][1] = True


    return matrix, matrix_heigh, matrix_width



def solution():
    matrix, heigh, width = matrix_calculation(qua_size)
    task = transformation(task_original)

    for row in range(heigh):
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




def main():
    """Основная функция программы"""
    show_matrix()

main()

