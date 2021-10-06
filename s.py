from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def on_closing():
    """ закрытие приложения """

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

im_not = ImageTk.PhotoImage(Image.open('image/not.png'))
im_buf = ImageTk.PhotoImage(Image.open('image/buf.png'))
im_and = ImageTk.PhotoImage(Image.open('image/and.png'))
im_nand = ImageTk.PhotoImage(Image.open('image/nand.png'))
im_nor = ImageTk.PhotoImage(Image.open('image/nor.png'))
im_xnor = ImageTk.PhotoImage(Image.open('image/xnor.png'))
im_xor = ImageTk.PhotoImage(Image.open('image/xor.png'))
im_or = ImageTk.PhotoImage(Image.open('image/or.png'))

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


def circuit_1():
    """ Прорисовка 1 варианта """

    # 1 строка
    Label(root, image=im_a).grid(row=0, column=0)
    Label(root, image=im_1).grid(row=0, column=1)
    Label(root, image=im_not).grid(row=0, column=2)
    Label(root, image=im_2).grid(row=0, column=3)

    # 2 строка
    Label(root, image=im_3).grid(row=1, column=3)
    Label(root, image=im_and).grid(row=1, column=4)
    Label(root, image=im_2).grid(row=1, column=5)

    # 3 строка
    Label(root, image=im_b).grid(row=2, column=0)
    Label(root, image=im_4).grid(row=2, column=1)
    Label(root, image=im_buf).grid(row=2, column=2)
    Label(root, image=im_5).grid(row=2, column=3)
    Label(root, image=im_3).grid(row=2, column=5)
    Label(root, image=im_nand).grid(row=2, column=6)
    Label(root, image=im_1).grid(row=2, column=7)
    Label(root, image=im_answer).grid(row=2, column=8)

    # 4 строка
    Label(root, image=im_12).grid(row=3, column=1)
    Label(root, image=im_1).grid(row=3, column=2)
    Label(root, image=im_2).grid(row=3, column=3)
    Label(root, image=im_11).grid(row=3, column=5)

    # 5 строка
    Label(root, image=im_3).grid(row=4, column=3)
    Label(root, image=im_xnor).grid(row=4, column=4)
    Label(root, image=im_5).grid(row=4, column=5)

    # 6 строка
    Label(root, image=im_c).grid(row=5, column=0)
    Label(root, image=im_1).grid(row=5, column=1)
    Label(root, image=im_1).grid(row=5, column=2)
    Label(root, image=im_5).grid(row=5, column=3)


def circuit_2():
    """ Прорисовка 2 варианта """

    # 1 строка
    Label(root, image=im_a).grid(row=0, column=0)
    Label(root, image=im_1).grid(row=0, column=1)
    Label(root, image=im_2).grid(row=0, column=2)

    # 2 строка
    Label(root, image=im_3).grid(row=1, column=2)
    Label(root, image=im_and).grid(row=1, column=3)
    Label(root, image=im_1).grid(row=1, column=4)
    Label(root, image=im_not).grid(row=1, column=5)
    Label(root, image=im_2).grid(row=1, column=6)

    # 3 строка
    Label(root, image=im_b).grid(row=2, column=0)
    Label(root, image=im_4).grid(row=2, column=1)
    Label(root, image=im_5).grid(row=2, column=2)
    Label(root, image=im_3).grid(row=2, column=6)
    Label(root, image=im_nand).grid(row=2, column=7)
    Label(root, image=im_1).grid(row=2, column=8)
    Label(root, image=im_answer).grid(row=2, column=9)

    # 4 строка
    Label(root, image=im_c).grid(row=3, column=0)
    Label(root, image=im_6).grid(row=3, column=1)
    Label(root, image=im_and).grid(row=3, column=2)
    Label(root, image=im_1).grid(row=3, column=3)
    Label(root, image=im_1).grid(row=3, column=4)
    Label(root, image=im_1).grid(row=3, column=5)
    Label(root, image=im_5).grid(row=3, column=6)


def circuit_3():
    """ Прорисовка 3 варианта """

    # 1 строка
    Label(root, image=im_a).grid(row=0, column=0)
    Label(root, image=im_7).grid(row=0, column=1)
    Label(root, image=im_and).grid(row=0, column=2)
    Label(root, image=im_1).grid(row=0, column=3)
    Label(root, image=im_not).grid(row=0, column=4)
    Label(root, image=im_2).grid(row=0, column=5)

    # 2 строка
    Label(root, image=im_b).grid(row=1, column=0)
    Label(root, image=im_10).grid(row=1, column=1)
    Label(root, image=im_3).grid(row=1, column=5)
    Label(root, image=im_nand).grid(row=1, column=6)
    Label(root, image=im_1).grid(row=1, column=7)
    Label(root, image=im_answer).grid(row=1, column=8)

    # 3 строка
    Label(root, image=im_c).grid(row=2, column=0)
    Label(root, image=im_6).grid(row=2, column=1)
    Label(root, image=im_xor).grid(row=2, column=2)
    Label(root, image=im_1).grid(row=2, column=3)
    Label(root, image=im_buf).grid(row=2, column=4)
    Label(root, image=im_5).grid(row=2, column=5)


def circuit_4():
    """ Прорисовка 4 варианта """

    # 1 строка
    Label(root, image=im_a).grid(row=0, column=0)
    Label(root, image=im_7).grid(row=0, column=1)
    Label(root, image=im_nand).grid(row=0, column=2)
    Label(root, image=im_1).grid(row=0, column=3)
    Label(root, image=im_1).grid(row=0, column=4)
    Label(root, image=im_2).grid(row=0, column=5)

    # 2 строка
    Label(root, image=im_11).grid(row=1, column=1)
    Label(root, image=im_3).grid(row=1, column=5)
    Label(root, image=im_or).grid(row=1, column=6)
    Label(root, image=im_2).grid(row=1, column=7)

    # 3 строка
    Label(root, image=im_11).grid(row=2, column=1)
    Label(root, image=im_c).grid(row=2, column=2)
    Label(root, image=im_7).grid(row=2, column=3)
    Label(root, image=im_nand).grid(row=2, column=4)
    Label(root, image=im_5).grid(row=2, column=5)
    Label(root, image=im_3).grid(row=2, column=7)
    Label(root, image=im_xor).grid(row=2, column=8)
    Label(root, image=im_1).grid(row=2, column=9)
    Label(root, image=im_answer).grid(row=2, column=10)

    # 4 строка
    Label(root, image=im_b).grid(row=3, column=0)
    Label(root, image=im_9).grid(row=3, column=1)
    Label(root, image=im_1).grid(row=3, column=2)
    Label(root, image=im_9).grid(row=3, column=3)
    Label(root, image=im_1).grid(row=3, column=4)
    Label(root, image=im_not).grid(row=3, column=5)
    Label(root, image=im_1).grid(row=3, column=6)
    Label(root, image=im_5).grid(row=3, column=7)


def circuit_5():
    """ Прорисовка 5 варианта """

    # 1 строка
    Label(root, image=im_a).grid(row=0, column=0)
    Label(root, image=im_7).grid(row=0, column=1)
    Label(root, image=im_xor).grid(row=0, column=2)
    Label(root, image=im_1).grid(row=0, column=3)
    Label(root, image=im_not).grid(row=0, column=4)
    Label(root, image=im_2).grid(row=0, column=5)

    # 2 строка
    Label(root, image=im_b).grid(row=1, column=0)
    Label(root, image=im_10).grid(row=1, column=1)
    Label(root, image=im_3).grid(row=1, column=5)
    Label(root, image=im_and).grid(row=1, column=6)
    Label(root, image=im_1).grid(row=1, column=7)
    Label(root, image=im_buf).grid(row=1, column=8)
    Label(root, image=im_1).grid(row=1, column=9)
    Label(root, image=im_answer).grid(row=1, column=10)

    # 3 строка
    Label(root, image=im_c).grid(row=2, column=0)
    Label(root, image=im_6).grid(row=2, column=1)
    Label(root, image=im_and).grid(row=2, column=2)
    Label(root, image=im_1).grid(row=2, column=3)
    Label(root, image=im_1).grid(row=2, column=4)
    Label(root, image=im_5).grid(row=2, column=5)


circuit_5()
root.mainloop()
