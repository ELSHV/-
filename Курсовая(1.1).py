from tkinter import*
root = Tk()
root.title('Меню Курсовой Работы')
root.geometry('400x300')
root.configure(bg = "lightblue")
var = IntVar()
var.set(0)

#-----------------------------------------------------------------------------------------------------------#
def integral():
    win = Toplevel(root)
    win.geometry('500x400')
    win.resizable(height = False,width = False)
    win.title('Интегралы')
    win.configure(bg = 'lightblue')
    
    lbl_A= Label(win,text ='a',bg = 'lightblue')
    lbl_A.place(x = 270,y = 145)
    
    Entry_A = Entry(win,width = 15)
    Entry_A.place(x = 285,y = 145)
    
    lbl_B = Label(win,text ='b',bg = 'lightblue')
    lbl_B.place(x = 270,y = 180)
    
    Entry_B = Entry(win,width = 15)
    Entry_B.place(x = 285,y = 180)
    
    lbl_N = Label(win,text ='n',bg = 'lightblue')
    lbl_N.place(x = 270,y = 220)
    
    Entry_N = Entry(win,width = 15)
    Entry_N.place(x = 285,y = 220)
    
    lbl_Lprmk = Label(win,text ='Левые прямоугольники',bg = 'lightblue')
    lbl_Lprmk.place(x = 5,y = 145)
    
    Entry_Lprmk = Entry(win,width = 15)
    Entry_Lprmk.place(x = 150,y = 145)
    
    lbl_Pprmk = Label(win,text ='Правые прямоугольники',bg = 'lightblue')
    lbl_Pprmk.place(x = 5,y = 185)
    
    Entry_Pprmk = Entry(win,width = 15)
    Entry_Pprmk.place(x = 150,y = 185)
    
    lbl_Trapezia = Label(win,text ='Трапеция',bg = 'lightblue')
    lbl_Trapezia.place(x = 5,y = 225)
    
    Entry_Trapezia = Entry(win,width = 15)
    Entry_Trapezia.place(x = 150,y = 225)
    
    lbl_Simpson= Label(win,text ='Симпсон',bg = 'lightblue')
    lbl_Simpson.place(x = 5,y = 230)
    
    Entry_Simpson = Entry(win,width = 15)
    Entry_Simpson.place(x = 150,y = 225)
    
    lbl_n_min = Label(win,text ='n_min',bg = 'lightblue')
    lbl_n_min.place(x = 5,y = 280)
    
    Entry_n_min = Entry(win,width = 15)
    Entry_n_min.place(x = 150,y = 280)

    btn_save = Button(win,text = 'Считать',width = 30,height = 2)
    btn_save.place(x = 270,y = 260)
    
    btn_save = Button(win,text = 'Рунге',width = 30,height = 2)
    btn_save.place(x = 270,y = 305)
    
    btn_save = Button(win,text = 'Найти n_min',width = 33,height = 2)
    btn_save.place(x = 5,y = 305)
    
    btn_save = Button(win,text = 'Выйти',width = 30,height = 2)
    btn_save.place(x = 270,y = 350)

btn_Integral = Button(root,text = 'Интегралы',width = 30,height = 2,command = integral)
btn_Integral.place(x = 100,y = 5)
#-----------------------------------------------------------------------------------------------------------#

def nellin():
    win = Toplevel(root)
    win.geometry('400x400')
    win.resizable(height = False,width = False)
    win.title('Нелинейные уравнения')
    win.configure(bg = 'lightblue')

btn_nellin = Button(root,text = 'НУ',width = 30,height = 2,command = nellin)
btn_nellin.place(x = 100,y = 55,)

#-----------------------------------------------------------------------------------------------------------#

def polinom():
    win = Toplevel(root)
    win.geometry('400x400')
    win.resizable(height = False,width = False)
    win.title('Полиномы')
    win.configure(bg = 'lightblue')

btn_polinom = Button(root,text = 'Полиномы',width = 30,height = 2,command = polinom)
btn_polinom.place(x = 100,y = 105)

#-----------------------------------------------------------------------------------------------------------#

def MNK():
    win = Toplevel(root)
    win.geometry('400x400')
    win.resizable(height = False,width = False)
    win.title('МНК')
    win.configure(bg = 'lightblue')

btn_MNK = Button(root,text = 'МНК',width = 30,height = 2,command = MNK)
btn_MNK.place(x = 100,y = 160)

#-----------------------------------------------------------------------------------------------------------#

def MKR():
    win = Toplevel(root)
    win.geometry('400x400')
    win.resizable(height = False,width = False)
    win.title('МКР')
    win.configure(bg = 'lightblue')

btn_MKR= Button(root,text = 'МКР',width = 30,height = 2,command = MKR)
btn_MKR.place(x = 100,y = 215)

#-----------------------------------------------------------------------------------------------------------#

def author():
    win = Toplevel(root)
    win.geometry('400x400')
    win.resizable(height = False,width = False)
    win.title('От Автора')
    win.configure(bg = 'lightblue')

btn_author = Button(root,text = 'От Автора',command = author)
btn_author.place(x = 5,y = 270)

#-----------------------------------------------------------------------------------------------------------#    
    
root.mainloop()