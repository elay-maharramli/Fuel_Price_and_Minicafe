from tkinter import *

tk = Tk()
while True:
    tk.configure(background="light blue")
    tk.maxsize(900,700)
    tk.minsize(900,700)
    tk.title("Fuel System")
    tk.wm_iconbitmap('fuel.ico')
    title = Label(text="Fuel", font=("Courier", 40), bg="light blue")
    def cal():
        if str(aznbox.get()) == "":
            hesabfuel.configure(text="Please enter valid nummber")
        else:
            hesabfuel.configure(text=str(round(int(aznbox.get()) / litrfuel,2))+ " Liter")
    litr = Label(text="USD", font=("Arial", 17), bg="light blue")
    aznbox = Entry()
    button = Button(text="Calculate", command=cal,bg="grey")
    title2 = Label(text="Minicafe",bg="light blue",font = ("Courier",40))
    hesabfuel = Label(text="",bg="light blue",font=("Arial", 17))
    burgent = Entry()
    frient = Entry()
    burgent.insert(0, "Enter the number")
    frient.insert(0, "Enter the number")
    burgtxt = Label(text="Hamburger:2USD",bg="light blue",font = ("Arial",17))
    fritxt = Label(text="French fries:3USD",bg="light blue",font=("Arial", 16))
    litrfuel = 1.50
    burger = 2
    fri = 3
    title.place(x=100, y=10)
    title2.place(x=450, y=10)
    litr.place(x = 100,y = 90)
    aznbox.place(x = 166,y = 98)
    button.place(x = 100,y = 160)
    burgtxt.place(x = 450,y = 100)
    fritxt.place(x = 450,y = 150)
    hesabfuel.place(x = 100,y = 400)
    burgent.place(x = 680,y = 107)
    frient.place(x = 680,y = 156)
    tk.mainloop()
