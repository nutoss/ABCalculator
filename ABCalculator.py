#A/B калькулятор 

import tkinter as tk
from tkinter import messagebox as mb
import os
import math
from scipy.stats import norm

#Функция закрытия программы
def do_close():
    root.destroy()
#Функция форматирования процентов
def num_persent(num):
    return "{:.2f}".format(num*100).rjust(10) + '%'
    
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
    window.geometry("500x500")
    window.title("A/B результат")
    
    #Добавление окна вывода текста
    txtOutput = tk.Text(window, font = ('Courier New', 10, 'bold'))
    txtOutput.place(x=15, y=115, width=470, height=300)
    
    #Добавление заголовка
    txtOutput.insert(tk.END,'                    Контрольная    Тестовая' + os.linesep)
    txtOutput.insert(tk.END,'                    группа         группа' + os.linesep)
    txtOutput.insert(tk.END,'-------------------------------------------------' + os.linesep)
    
    #Добавление авывода конверсии и стандартного отклонения
    p1 = c1/n1
    p2 = c2/n2
    txtOutput.insert(tk.END, 'Конверсия              ' + num_persent(p1)
        +'      ' + num_persent(p2)+ os.linesep)
        
    sigma1 = math.sqrt(p1*(1-p1)/n1)
    sigma2 = math.sqrt(p2*(1-p2)/n2)
    
    txtOutput.insert(tk.END, 'Стандартное отклонение ' + num_persent(sigma1)
        +'      ' + num_persent(sigma2)+ os.linesep)    
    txtOutput.insert(tk.END, '-------------------------------------------------' + os.linesep) 
      
     #Добавление вывода ложных разбросов
    z1 = 1.96
    lower1_95 = p1-z1*sigma1
    if lower1_95 < 0:
        lower1_95 = 0 
    upper1_95 = p1+z1*sigma1
    if upper1_95 > 1: 
        upper1_95  = 1 
        
    lower2_95 = p2-z1*sigma2
    if lower2_95 < 0:
        lower2_95 = 0 
    upper2_95 = p2+z1*sigma2
    if upper2_95 > 1: 
        upper2_95  = 1 
    
    txtOutput.insert(tk.END, '95% Возможный разброс  ' + os.linesep)
    txtOutput.insert(tk.END, '                  От   ' + num_persent(lower1_95) 
        + num_persent(lower2_95)+ os.linesep) 
    txtOutput.insert(tk.END, '                  До   ' + num_persent(upper1_95) 
        + num_persent(upper2_95)+ os.linesep) 
    txtOutput.insert(tk.END, '---------------------------------------------------------- ' + os.linesep)
   
    z2 = 2.575
    lower1_99 = p1-z2*sigma1
    if lower1_99 < 0:
        lower1_99 = 0 
    upper1_99 = p1+z2*sigma1
    if upper1_99 > 1: 
        upper1_99  = 1 
        
    lower2_99 = p2-z2*sigma2
    if lower2_99 < 0:
        lower2_99 = 0 
    upper2_99 = p2+z2*sigma2
    if upper2_99 > 1: 
        upper2_99  = 1 
    
    txtOutput.insert(tk.END, '99% Возможный разброс  ' + os.linesep)
    txtOutput.insert(tk.END, '                  От   ' + num_persent(lower1_99) 
        + num_persent(lower2_99)+ os.linesep) 
    txtOutput.insert(tk.END, '                  До   ' + num_persent(upper1_99) 
        + num_persent(upper2_99)+ os.linesep) 
    txtOutput.insert(tk.END, '---------------------------------------------------------- ' + os.linesep)
     
    #Вычисление Z и P
    z_score = (p2-p1)/math.sqrt(sigma1*sigma1*sigma2*sigma2)
    txtOutput.insert(tk.END, 'Z = '+"{:.7f}".format(z_score) + os.linesep)
    
    p_value = norm.sf(x=z_score, loc=0, scale=1)
    txtOutput.insert(tk.END, 'P = '+"{:.7f}".format(p_value) + os.linesep)
    
    #Добавление оценки результатов 
    confidence_95 = False
    if p_value < 0.025 or p-value >0.975:
        confidence_95 = True
        
    confidence_99 = False
    if p_value < 0.005 or p-value >0.995:
        confidence_99 = True
    
    lblComment95 = tk.Label(window, text = "95% уверенность:", font = ('Helvetica',10, 'bold'))
    lblComment95.place(x=25, y=25)
    
    if confidence_95:
        lblResult95 = tk.Label(window, text = "ДА", font = ('Helvetica',12, 'bold'), fg = '#008800')
        lblResult95.place(x=160, y=25)
    else: 
        lblResult95 = tk.Label(window, text = "НЕТ", font = ('Helvetica',12, 'bold'), fg = '#ff0000')
        lblResult95.place(x=160, y=25)
        
    lblComment99 = tk.Label(window, text = "99% уверенность:", font = ('Helvetica',10, 'bold'))
    lblComment99.place(x=25, y=65)
    
    if confidence_99:
        lblResult99 = tk.Label(window, text = "ДА", font = ('Helvetica',12, 'bold'), fg = '#008800')
        lblResult99.place(x=160, y=65)
    else:
        lblResult99 = tk.Label(window, text = "НЕТ", font = ('Helvetica',12, 'bold'), fg = '#ff0000')
        lblResult99.place(x=160, y=65)
        
    
    #Добавлени кнопки закрытия окна
    btnClosePopup = tk.Button(window, text = "Закрыть", font = ('Helvetica',10, 'bold'), command=window.destroy)
    btnClosePopup.place(x=190, y=450, width=90, height=30)
    
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

