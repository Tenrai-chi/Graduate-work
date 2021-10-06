from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def on_closing():
    if messagebox.askokcancel('Выход из приложения', 'Хотите выйти из приложения?'):
        root.destroy()


root = Tk()
root.protocol('WM_DELETE_WINDOW', on_closing)
root.title('????????????')  # Заголовок окна
root.geometry('1200x900')


# создаем рабочую область
#frame = Frame(root)
#frame.grid()


# Подгрузка изображений
'''
im_true = PhotoImage(file="image/true.png")
im_false = Image.open("image/false.png")
im_answer = Image.open("image/y.png")
im_a = Image.open("image/a.png")
im_b = Image.open("image/b.png")
im_c = Image.open("image/c.png")

im_and = Image.open("image/and.png")
im_buf = Image.open("image/buf.png")
im_nand = Image.open("image/nand.png")
im_nor = Image.open("image/nor.png")
im_not = Image.open("image/not.png")
im_or = Image.open("image/or.png")
im_xnor = Image.open("image/xnor.png")
im_xor = Image.open("image/xor.png")

im_1 = Image.open("image/1.png")
im_2 = Image.open("image/2.png")
im_3 = Image.open("image/3.png")
im_4 = Image.open("image/4.png")
im_5 = Image.open("image/5.png")
im_6 = Image.open("image/6.png")
im_7 = Image.open("image/7.png")
im_8 = Image.open("image/8.png")
im_9 = Image.open("image/9.png")
im_10 = Image.open("image/10.png")
im_11 = Image.open("image/11.png")'''

'''
im_true = PhotoImage(file="image/true.png")
im_label = Label(root)
im_label.image = im_true
im_label['image'] = im_label.image
im_label.grid(row=0, column=0)
'''

'''
im_true = Image.open('image/true.png')
im_true = ImageTk.PhotoImage(im_true)
im_label = Label(image=im_true)
im_label.image = im_true
im_label.grid(row=0, column=0)
'''

'''
im_true = Image.open('image/true.png')
im_true = ImageTk.PhotoImage(im_true)
im_id = frame.create_image(0, 0, achor='nw', image=im_true)
im_id.grid(row=0, column=0)
'''

#  Преобразование пикчи
im_true = Image.open('image/true.png')
im_true = ImageTk.PhotoImage(im_true)
Label(root, image=im_true).grid(row=0, column=0)


im_not = Image.open('image/not.png')
im_not = ImageTk.PhotoImage(im_not)
Label(root, image=im_not).grid(row=1, column=1)


im_5 = Image.open('image/5.png')
im_5 = ImageTk.PhotoImage(im_5)
Label(root, image=im_5).grid(row=1, column=2)

'''im_true = Image.open('image/true.png')
im_true = ImageTk.PhotoImage(im_true)'''
Label(root, image=im_true).grid(row=2, column=2)


root.mainloop()
