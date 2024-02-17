# -*- coding: utf-8 -*-
import sys
import tkinter as tk

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
        Шаблон программы с графикой tkinter
        
        В дальнейшем будет использован для разработки
        программы простого калькулятора

        В программе задействованы следующие функции:
        techinfo():
        def About():            Об авторе
        def Selfdoc():          самодокументирования 

        В программе задействованы следующие функции:
        def About():            Об авторе
        def Selfdoc():          самодокументирования 
        def inputFloat(prompt): Ввод вещ. числа с проверкой
        def Fn_Calc(A, op, B):  Функ вычисл. по аргументам A,B
                                где op ['+','-','*','/']
        def Work():             Функция где весь цикл работы
        def main():             Основная функция программы
    ========================================================== 
        Для создания приложения с графическим интерфейсом
        необходимо выполнить следующие этапы:
        • создать главное окно приложения;
        • создать необходимые виджеты и
          выполнить конфигурацию их свойств (опций);
        • определить события, на которые будет
          реагировать программа;
        • написать обработчики событий, т.е. программные коды,
          которые будут запускаться при наступлении
          того или иного события;
        • расположить виджеты в главном окне приложения;
        • запустить цикл обработки событий.
    ==========================================================
        За основу взяты уроки:
        https://python-scripts.com/tkinter-introduction
    ==========================================================
    '''
    )

# =====================================================
def Work():
    #--- Константы будут часто использоваться потом,
    #--- поэтому числа назначим только в одном месте
    #--- в самом начале программы
    WSIZE="800x600"
    WW=800
    WH=600
    
    #--- Создаем окно с заголовком и размерами WSIZE
    window = tk.Tk()   
    window.title("Программа вывода текста в главное окно") 
    window.geometry(WSIZE)
    
    Cap(window)        #--- Функция шапки принимает параметр - имя окна 
    PackExample()      #--- Пример расстановки меток с помощью pack()
    BtExit(window)
    
    window.mainloop()  #--- Главный цикл графического интерфейса окна
    
def Cap(win): #--- Функция шапки окна win программы
    lb_1=tk.Label(win,text="Уроки информатики",font = "Arial 16")
    lb_1.pack(side = tk.TOP)    
    lb_2=tk.Label(win,text="Язык Python",font = ("Arial",18,"bold") )
    lb_2.pack(padx = 20, pady = 10)
  
def PackExample(): #--- Функция работы примера расстановки меток 
    lab_1=tk.Label(width=8, height=3, bg='yellow',text="1")
    lab_2=tk.Label(width=8, height=3, bg='red',text="2")
    lab_3=tk.Label(width=8, height=3, bg='lightgreen',text="3")
    lab_4=tk.Label(width=8, height=3, bg='lightblue',text="4")
    lab_1.pack(side = tk.BOTTOM)
    lab_2.pack(side = tk.TOP)
    lab_3.pack(side = tk.LEFT)
    lab_4.pack(side = tk.RIGHT)
    
def BtExit(win): #--- Кнопка выхода из GUI-цикла win с пом. quit
    bt_exit=tk.Button(win,
                      bg="blue",fg="yellow",border=3,
                      text="Exit",font="Arial 16",
                      command=quit)
    bt_exit.pack(side = tk.BOTTOM)
    
# =====================================================
def main():
    techinfo()
    About()
    Selfdoc()
    Work()
    
# =====================================================
if __name__ == "__main__":
    main()
