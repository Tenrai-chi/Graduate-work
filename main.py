
def print_matrix():
    """Вывод таблицы значения"""
    print('x y w z')
    for x in range(2):
        for y in range(2):
            for w in range(2):
                for z in range(2):
                    if ((y <= w) == (x <= (not z))) and (x or w):
                        print(x, y, w, z)


qua_size = 3  # Количество переменных


def transformation(size: int, separator=' ') -> tuple:
    """ Преобразует изначальную строку в список и создает размерность матрицы"""

    task = 'a * b + - c'  # Задание
    #task = '- a + a * c + b'  # Задание
    task_final = task.split(separator)  # Разделение строки по пробелу

    test = 'abc'
    operations = 0

    '''Оценка количества операндов'''
    for symbol in task_final:
        if symbol in test:
            operations += 1

    operations = len(task_final) - operations

    '''Рассчет размера матрицы'''
    matrix_rows = 2 ** size  # Количество строк
    matrix_columns = size + operations  # Количество колонок
    size_matrix = matrix_rows, matrix_columns

    return task_final, size_matrix



def show():
    task, size = transformation(qua_size)
    height = size[0]
    width = size[1]

    '''Создание матрицы'''

    matrix = [['?' for i in range(width)] for j in range(height)]


    for i in range(height):
        for j in range(3):
            if j == 0 and i <= 3:
                matrix[i][j] = False
            elif j == 0 and i > 3 :
                matrix[i][j] = True

            if j == 2 and i % 2 == 0:
                matrix[i][j] = False
            elif j == 2 and i % 2 == 1:
                matrix[i][j] = True

    for i in range(0, height, 4):
        matrix[i][1] = False
        matrix[i+1][1] = False

    for i in range(2, height, 4):
        matrix[i][1] = True
        matrix[i+1][1] = True



    '''Вывод матрицы'''
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()


def main():
    """ Основная функция программы """
    show()


main()
