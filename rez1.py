from tkinter import *


def open_file():
    open_f = askopenfilename()
    text_area.delete("1.0", END)

    for i in fileinput.input(open_f):
        text_area.insert(END, i)

def save_file():
    save_f = asksaveasfilename(filetypes=(("Text Documents", "*.txt"), ("all files", "*.*")))
    # відкриття діалогового вікна для збереження
    if save_f:
        letter = str(text_area.get(1.0, END)) # зберегли весь текст з текстареа
        f = open(save_f, "w") # вікдрили файл для запису
        f.write(letter) # записали у файл текст
        f.close() # закрили файл у який записували

def change_col():
    (triple, h) = askcolor()
    if h:
        text_area.config(fg = h)

def change_size(mode):
    global style, font_size
    if mode == 1:
        font_size = font_size - 1
        style  = "Arial" + str(font_size)
        text_area.config(font=style)
    elif mode == 0:
        font_size = font_size + 1
        style  = "Arial" + str(font_size)
        text_area.config(font=style)

def change_bg():
    (triple, h) = askcolor()
    if h:
        text_area.config(fg = h)

def new_f():
    text_area.delete("1.0", End)


window = Tk()
window.geometry()

main_menu = Menu(window) # створення головного меню
file_m = Menu(main_menu, tearoff=False)  # створення менюшки файл
edit_m = Menu(main_menu, tearoff=False)  # створення менюшки едіт

main_menu.add_cascade(label="File", menu=file_m) # підключення менюшки до головного меню
file_m.add_command(label="Save", command=save_file)
file_m.add_command(label="Open", command=open_file)
file_m.add_command(label="New", command=new_f)
file_m.add_separator()
file_m.add_command(label="Exit", command=lambda: window.destroy())

main_menu.add_cascade(label="Edit", menu=edit_m)
edit_m.add_command(label="Change color bg", command=change_bg)
edit_m.add_command(label="Change color", command=change_col)
edit_m.add_command(label="Size text +", command=lambda: change_size(0))
edit_m.add_command(label="Size text -", command=lambda: change_size(1))
 
text_area = Text(window)
text_area.pack(expand=YES, fill=BOTH)


window.config(menu=main_menu)
window.mainloop()
