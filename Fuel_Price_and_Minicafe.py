from tkinter import *

tk = Tk()
coke = 2
burg = 2
fri = 4
cola = 1
cizburg = 3

while True:
    tk.configure(background="light blue")
    tk.maxsize(900,700)
    tk.minsize(900,700)
    tk.title("Fuel Price and Minicafe")
    tk.wm_iconbitmap('fuel.ico')
    title = Label(text="Benzin", font=("Courier", 40), bg="light blue")
    def cal():
        if str(aznbox.get()) == "":
            hesabfuel.configure(text="Etibarlı bir dəyər daxil edin")
        else:
            hesabfuel.configure(text=str(round(int(aznbox.get()) / litrfuel,2))+ " Litr")
    def caltwo():
        if burgent.get() or cizburgent.get() or frient.get() or cokent.get() or colaent.get() == "":
            hesabkafe.configure(text="Etibarlı bir dəyər daxil edin")
        total = (int(burgent.get()) * burg) + (int(cizburgent.get()) * cizburg) + (int(frient.get()) * fri) + (int(cokent.get()) * coke) + (int(colaent.get()) * cola)
        hesabkafe.configure(text=str(total) + str(" AZN"))
    azn = Label(text="AZN:", font=("Arial", 17), bg="light blue")
    aznbox = Entry()
    button = Button(text="Hesabla", command=cal,bg="grey")
    button2 = Button(text="Hesabla",bg="blue",command=caltwo)
    title2 = Label(text="Minikafe",bg="light blue",font = ("Courier",40))
    hesabfuel = Label(text="",bg="light blue",font=("Arial", 17))
    hesabkafe = Label(text="",bg="light blue", font=("Arial", 17))
    burgent = Entry()
    frient = Entry()
    cizburgent = Entry()
    cokent = Entry()
    colaent = Entry()
    drinktxt = Label(text="İçkilər", bg="light blue", font=("Arial", 30))
    burgtxt = Label(text="Hamburger:2 AZN",bg="light blue",font = ("Arial",17))
    fritxt = Label(text="Fri:4 AZN",bg="light blue",font=("Arial", 16))
    cizburgtxt = Label(text="Çizburger:3 AZN",bg="light blue", font=("Arial", 16))
    coketxt = Label(text="Kokteyl:2 AZN", bg="light blue", font=("Arial", 16))
    colatxt = Label(text="Coca-Cola:1 AZN", bg="light blue", font=("Arial", 16))
    litrfuel = 1.50
    title.place(x=100, y=10)
    title2.place(x=450, y=10)
    azn.place(x = 100,y = 90)
    aznbox.place(x = 168,y = 98)
    button.place(x = 100,y = 160)
    button2.place(x = 450,y = 450)
    burgtxt.place(x = 450,y = 100)
    fritxt.place(x = 450,y = 150)
    cizburgtxt.place(x = 450,y = 200)
    drinktxt.place(x = 450, y = 250)
    coketxt.place(x = 450,y = 320)
    colatxt.place(x = 450,y = 365)
    hesabfuel.place(x = 100,y = 400)
    hesabkafe.place(x = 450, y = 500)
    burgent.place(x = 685,y = 107)
    frient.place(x = 578,y = 156)
    cizburgent.place(x = 665,y = 206)
    cokent.place(x = 635,y = 327)
    colaent.place(x = 670,y = 370)
    tk.mainloop()
