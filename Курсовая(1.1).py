from tkinter import *
import customtkinter as CTk
from PIL import Image, ImageTk

Button_Width, Button_Height = 200, 50
Button_Font = ("Arial", 15, "bold")
FG_Colour = "#080871"

Button_Width2, Button_Height2 = 200, 30
Button_Font2 = ("Arial", 15, "bold")
FG_Colour2 = "#080871"


class SecondWindow(CTk.CTkToplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("Интеграл")
        self.geometry("650x400")
        self.resizable(False, False)

        self.count_button = CTk.CTkButton(master=self, text="СЧИТАТЬ", width=Button_Width2,
                                          height=Button_Height2, font=Button_Font2, fg_color=FG_Colour2, corner_radius=15)
        self.count_button.place(x=430, y=295)

        self.count_button = CTk.CTkButton(master=self, text="МЕТОД РУНГЕ", width=Button_Width2,
                                          height=Button_Height2, font=Button_Font2, fg_color=FG_Colour2, corner_radius=15)
        self.count_button.place(x=430, y=330)

        self.count_button = CTk.CTkButton(master=self, text="N_MIN", width=Button_Width2,
                                          height=Button_Height2, font=Button_Font2, fg_color=FG_Colour2,
                                          corner_radius=15)
        self.count_button.place(x=430, y=365)

        # Кнопка назад(в меню вкладки Интегралы)
        self.back_button = CTk.CTkButton(master=self, text="НАЗАД", width=10,
                                         height=Button_Height2, font=Button_Font2, fg_color=FG_Colour2, corner_radius=15,
                                         command=self.close)
        self.back_button.place(x=10, y=365)

        self.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        self.parent.deiconify()
        self.destroy()


class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("460x400")
        self.title("Курсовая работа")
        self.resizable(False, False)
        self.configure(fg_color="#2C2C2F")

        # Интерфейс главного меню и меню вкладки Интегралы
        # _____________________________________________________________________________________________________________#
        self.Menu = CTk.CTkButton(master=self, text="ГЛАВНОЕ МЕНЮ", font=("Arial", 25, "bold"), fg_color=FG_Colour)
        self.Menu.place(x=125, y=-4)

        self.integral = CTk.CTkButton(master=self, text="ИНТЕГРАЛЫ", width=Button_Width,
                                      height=Button_Height, font=Button_Font, fg_color=FG_Colour,
                                      corner_radius=15, command=self.second_window)
        self.integral.place(x=10, y=70)

        # Интерфейс вкладки Полиномы
        # _____________________________________________________________________________________________________________#
        self.Polinom = CTk.CTkButton(master=self, text="ПОЛИНОМЫ", width=Button_Width,
                                     height=Button_Height, font=Button_Font, fg_color=FG_Colour, corner_radius=15)
        self.Polinom.place(x=10, y=130)

        # Интерфейс вкладки Н/У (Нелинейные уравнения )
        # _____________________________________________________________________________________________________________#
        self.N_Y = CTk.CTkButton(master=self, text="Н/У", width=Button_Width,
                                 height=Button_Height, font=Button_Font, fg_color=FG_Colour, corner_radius=15)
        self.N_Y.place(x=10, y=190)

        # Интерфейс вкладки МНК ()
        # _____________________________________________________________________________________________________________#
        self.MNK = CTk.CTkButton(master=self, text="МНК", width=Button_Width,
                                 height=Button_Height, font=Button_Font, fg_color=FG_Colour, corner_radius=15)
        self.MNK.place(x=250, y=70)

        # Интерфейс вкладки МКР ()
        # _____________________________________________________________________________________________________________#
        self.MKR = CTk.CTkButton(master=self, text="МКР", width=Button_Width,
                                 height=Button_Height, font=Button_Font, fg_color=FG_Colour, corner_radius=15)
        self.MKR.place(x=250, y=130)

        # Интерфейс вкладки От Автора
        # _____________________________________________________________________________________________________________#
        self.Author = CTk.CTkButton(master=self, text="ОТ АВТОРА", width=Button_Width,
                                    height=Button_Height, font=Button_Font, fg_color=FG_Colour, corner_radius=15)
        self.Author.place(x=250, y=190)

        # Кнопка Выйти (ЗАкрыть полность Окно с ГИ)
        # _____________________________________________________________________________________________________________#
        self.Exit = CTk.CTkButton(master=self, text="ВЫЙТИ", width=20,
                                  height=40, font=Button_Font, fg_color=FG_Colour,
                                  corner_radius=15, command=self.destroy)
        self.Exit.place(x=10, y=350)

    def second_window(self):
        self.withdraw()
        second_window = SecondWindow(self)


if __name__ == '__main__':
    app = App()
    app.mainloop()