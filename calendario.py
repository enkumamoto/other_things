import calendar
from tkinter import *

def showcal():
    new_gui = Tk()
    new_gui.config(background = 'white')
    new_gui.title('Calendário')
    new_gui.geometry('640x640')

    fetch_year = int(year_field.get())

    cal_content = calendar.calendar(fetch_year)

    cal_year = Label(new_gui, text = cal_content, font = ('Consolas', 10, 'bold'))

    cal_year.grid(row=5,column=1, padx=20)
    new_gui.mainloop()

if __name__ == '__main__':
    gui = Tk()
    gui.config(background='white')
    gui.title('Calendário')
    gui.geometry('250x150')

    cal = Label(gui, text = 'Calendário', bg = 'dark gray', font = ('time',28,'bold'))
    year = Label(gui, text = 'Enter Year', bg = 'light green')

    year_field = Entry(gui)

    Show = Button(gui, text = 'Mostrar Calendário', fg = "Black", bg = 'Red', command = showcal)

    Exit = Button(gui, text = 'Sair', fg = "Black", bg = 'Red', command = exit)

    cal.grid(row=1,column=1)
    year.grid(row=2,column=1)
    year_field.grid(row=3,column=1)
    Show.grid(row=4,column=1)
    Exit.grid(row=6,column=1)

    gui.mainloop()