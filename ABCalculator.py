#A/B калькулятор 

import tkinter as tk
from tkinter import messagebox as mb

#Функция закрытия программы
def do_close():
    root.destroy()
    
def do_processing():
    #Считывание данных из полей ввода
    n1 = int(entVisitors1.get())
    c1 = int(entConversions1.get())
    n2 = int(entVisitors2.get())
    c2 = int(entConversions2.get())
    
    #Проверка данных из полей ввода
    if n1<=0 or n2<=0:
        mb.showerror(title="Ошибка", message="Неверное количество посетителей")
        return
    
    popup_window(n1, c1, n2, c2)
    
    #Функция вызова окна результатов
def popup_window(n1, c1, n2, c2):
    window = tk.Toplevel()
    window.geometry("280x300")
    window.title("A/B результат")
    
    #Добавлени кнопки закрытия окна
    btnClosePopup = tk.Button(window, text = "Закрыть", font = ('Helvetica',10, 'bold'), command=window.destroy)
    btnClosePopup.place(x=160, y=250, width=90, height=30)
    
    #Перевод фокуса на созданное окно
    window.focus_force()

#Создание главного окна
root=tk.Tk()
root.geometry("280x300")
root.title ("A/B калькулятор")

#Добавление метки заголовка
lbtTitle = tk.Label(text = "A/B калькулятор", font = ('Helvetica',16, 'bold'), fg = '#0000cc')
lbtTitle.place(x=55, y=20)

#Добавление метки заголовка контрольной группы
lbtTitle1 = tk.Label(text = "Контрольная группа", font = ('Helvetica',12, 'bold'), fg = '#0066ff')
lbtTitle1.place(x=25, y=55)

#Добавление полей ввода контрольной группы
lblVisitors1 = tk.Label(text = "Посетители", font = ('Helvetica',10, 'bold'))
lblVisitors1.place(x=25, y=85)


entVisitors1 = tk.Entry(font = ('Helvetica',10, 'bold'), justify = 'center') #justify вырав по центру
entVisitors1.place(x=115, y=85, width=90, height=20)
entVisitors1.insert(tk.END, '0')

lblConversions1 = tk.Label(text = "Конверсии", font = ('Helvetica',10, 'bold'))
lblConversions1.place(x=25, y=115)

entConversions1 = tk.Entry(font = ('Helvetica',10, 'bold'), justify = 'center')
entConversions1.place(x=115, y=115, width=90, height=20)
entConversions1.insert(tk.END, '0')

#Добавление метки заголовка тестовой группы
lbtTitle2 = tk.Label(text = "Тестовая группа", font = ('Helvetica',12, 'bold'), fg = '#008800')
lbtTitle2.place(x=25, y=145)

#Добавление полей ввода контрольной группы
lblVisitors2 = tk.Label(text = "Посетители", font = ('Helvetica',10, 'bold'))
lblVisitors2.place(x=25, y=175)

entVisitors2 = tk.Entry(font = ('Helvetica',10, 'bold'), justify = 'center')
entVisitors2.place(x=115, y=175, width=90, height=20)
entVisitors2.insert(tk.END, '0')

lblConversions2 = tk.Label(text = "Конверсии", font = ('Helvetica',10, 'bold'))
lblConversions2.place(x=25, y=205)

entConversions2 = tk.Entry(font = ('Helvetica',10, 'bold'), justify = 'center')
entConversions2.place(x=115, y=205, width=90, height=20)
entConversions2.insert(tk.END, '0')


#Добавление кнопки Рассчитать
btnProcess = tk.Button(root, text = "Рассчитать", font = ('Helvetica',10, 'bold'), command=do_processing)
btnProcess.place(x=25, y=250, width=90, height=30)

#Добавление кнопки закрытия программы
btnClose = tk.Button(root, text = "Закрыть", font = ('Helvetica',10, 'bold'), command=do_close)
btnClose.place(x=160, y=250, width=90, height=30)


#Запуск цикла mainloop
root.mainloop()

