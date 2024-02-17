#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import tkinter as tk
from tkinter import Frame, BOTH

def techinfo():
    print("__________________________")
    print("Сведения о платформе:")
    print(sys.version_info)
    print(sys.version)
    print("__________________________\n")

# --- Функция выводит информацию об авторе
def About():
    print(
    """
    Привет!
    _______________________________
    author: Anna Starmark
            class  8
            school 242
    e-mail: nn.starmark@gmail.com
    github: github.com/AnnaStarmark
    date:   16-02-2024    17:48:00
    _______________________________
    """
    )
    
def Selfdoc():
    print(
    ''' 
    ==========================================================           
        Шаблон программы с графикой tkinter применяя классы
        
        В дальнейшем будет использован для разработки
        программы простого калькулятора

        В программе задействованы следующие функции:
        techinfo():
        def About():            Об авторе
        def Selfdoc():          самодокументирования 

        class Work():           Вся работа построения окна
                                с методами класса
            def __init__(self, parent):  
            def centerWindow(self):
            def Cap(self):        
            def PackExample(self):
            def BtExit(self):
        
        А также, стандарт запуска GUI части программы:        
        root = tk.Tk()
        ex = Work(root)
        root.mainloop()

        def main():             Основная функция программы
    ========================================================== 
        Для приложения с графическим интерфейсом
        с применением классов необходимо выполнить этапы:
        
        • создать класс главного окна приложения и экземпляр;
        • В классе создать необходимые виджеты и
          выполнить конфигурацию их свойств (опций);
        • В классе определить события, на которые будет
          реагировать программа;
        • В классе написать обработчики событий,
          т.е. программные коды, которые будут запускаться
          при наступлении того или иного события;
        • В классе расположить виджеты в гл. окне приложения;
        
        В гл. функции main():
        
        • Создать root = tk.Tk()
        • Создать экземпляр класса  ex = Work(root)
        • root.mainloop() запустить цикл обработки событий.
    ==========================================================
        За основу взяты уроки:
        https://python-scripts.com/tkinter-introduction
    ==========================================================
    '''
    )



#--- Вместо процедурной программы с вызовами не связанных функций
#--- можно создать класс, где все элементы и методы будут там
#--- описаны, а при создании экземпляра класса все это оживет.
#--- В момент создания экземпляра класса
#--- ему будет передан параметр Frame -> вот так: ex=Work(root)
class Work(Frame):
    
    #--- Главный метод-конструктор экземпляра класса
    def __init__(self, parent):
        self.PROGNAME="Программа вывода текста в главное окно"
        self.WW=800
        self.WH=600
    
        Frame.__init__(self,parent,background="gray")
        self.parent=parent
        self.parent.title(self.PROGNAME)
        self.pack(fill=BOTH, expand=1)
        
        self.centerWindow()
        self.Cap()
        self.PackExample()
        
        self.BtExit()
        
    #--- Метод для опред. размера окна и размер экрана, чтобы центрировать окно    
    def centerWindow(self):
        
        #--- Это значения ширины и высоты окна нашего приложения
        w=self.WW
        h=self.WH
        
        #--- С помощью этого кода мы определяем ширину и высоту экрана.
        sw=self.parent.winfo_screenwidth()
        sh=self.parent.winfo_screenheight()
        
        #--- Теперь мы рассчитываем необходимые координаты «x» и «y».
        x=(sw-w)/2
        y=(sh-h)/2
        
        #--- используем метод geometry(), чтобы центрировать окно на экране.
        self.parent.geometry('%dx%d+%d+%d' % (w,h,x,y))
        
    def Cap(self): #--- Метод шапки окна экземпляра класса
        lb_1=tk.Label(self,bg='gray',text="Уроки информатики",font = "Arial 16")
        lb_1.pack(side = tk.TOP)    
        lb_2=tk.Label(self,bg='gray',text="Язык Python",font = ("Arial",18,"bold") )
        lb_2.pack(padx = 20, pady = 10)
        
    def PackExample(self): #--- Метод екземпляра класса расстановки меток 
        lab_1=tk.Label(width=8, height=3, bg='yellow',text="1")
        lab_2=tk.Label(width=8, height=3, bg='red',text="2")
        lab_3=tk.Label(width=8, height=3, bg='lightgreen',text="3")
        lab_4=tk.Label(width=8, height=3, bg='lightblue',text="4")
        lab_1.pack(side = tk.BOTTOM)
        lab_2.pack(side = tk.TOP)
        lab_3.pack(side = tk.LEFT)
        lab_4.pack(side = tk.RIGHT)

    def BtExit(self): #--- Метод выхода из GUI-цикла с пом. quit
        bt_exit=tk.Button(self,bg="blue",fg="yellow",border=3,
                          text="Exit",font="Arial 16",
                          command=quit)
        bt_exit.pack(side = tk.TOP)
        
# =====================================================
def main():
    techinfo()
    About()
    Selfdoc()
    
    #--- Созд. окно с заголовком и размерами по центру
    #--- относительно root
    #--- И запускаем главный цикл mainloop() для root
    root = tk.Tk()
    ex = Work(root)
    root.mainloop()
    
# =====================================================
if __name__ == "__main__":
    main()
