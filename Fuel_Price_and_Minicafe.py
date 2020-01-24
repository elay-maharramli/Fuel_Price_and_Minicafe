from tkinter import *

tk = Tk()
while True:
    tk.configure(background="light blue")
    tk.maxsize(900,700)
    tk.minsize(900,700)
    tk.title("Fuel Price and Minicafe")
    tk.wm_iconbitmap('fuel.ico')
    title = Label(text="Benzin", font=("Courier", 40), bg="light blue")
    def cal():
        if str(aznbox.get()) == "":
            hesabfuel.configure(text="Zəhmət olmasa etibarlı bir dəyər daxil edin")
        else:
            hesabfuel.configure(text=str(round(int(aznbox.get()) / litrfuel,2))+ " Litr")
    azn = Label(text="AZN:", font=("Arial", 17), bg="light blue")
    aznbox = Entry()
    button = Button(text="Hesabla", command=cal,bg="grey")
    title2 = Label(text="Minikafe",bg="light blue",font = ("Courier",40))
    hesabfuel = Label(text="",bg="light blue",font=("Arial", 17))
    burgent = Entry()
    frient = Entry()
    cizburgent = Entry()
    burgent.insert(0, "Say daxil edin")
    frient.insert(0, "Say daxil edin")
    cizburgent.insert(0, "Say daxil edin")
    drinktxt = Label(text="İçkilər", bg="light blue", font=("Arial", 30))
    burgtxt = Label(text="Hamburger:2 AZN",bg="light blue",font = ("Arial",17))
    fritxt = Label(text="Fri:4 AZN",bg="light blue",font=("Arial", 16))
    cizburgtxt = Label(text="Çizburger:3 AZN",bg="light blue", font=("Arial", 16))
    litrfuel = 1.50
    burger = 2
    fri = 3
    title.place(x=100, y=10)
    title2.place(x=450, y=10)
    azn.place(x = 100,y = 90)
    aznbox.place(x = 168,y = 98)
    button.place(x = 100,y = 160)
    burgtxt.place(x = 450,y = 100)
    fritxt.place(x = 450,y = 150)
    cizburgtxt.place(x = 450,y = 200)
    drinktxt.place(x = 450, y = 250)
    hesabfuel.place(x = 100,y = 400)
    burgent.place(x = 685,y = 107)
    frient.place(x = 578,y = 156)
    cizburgent.place(x = 665,y = 206)
    tk.mainloop()
