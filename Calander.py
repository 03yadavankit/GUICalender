from tkinter import *
import calendar

def showCalendar():
    year = int(year_field.get())
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar for the Year")
    gui.geometry("550x600")
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.grid(row=5, column=1, padx=20)
    gui.mainloop()

if __name__ == '__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calendar")
    new.geometry("250x140")

    cal = Label(new, text="Calendar", bg='grey', font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg='dark grey')
    year_field = Entry(new)
    button = Button(new, text='Show Calendar', fg='Black', bg='Blue', command=showCalendar)
    exit_button = Button(new, text='Exit', fg='Black', bg='Red', command=new.destroy)

    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    exit_button.grid(row=5, column=1)

    new.mainloop()