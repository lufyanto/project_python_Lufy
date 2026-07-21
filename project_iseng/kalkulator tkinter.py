from tkinter import *


window = Tk()
window.geometry("354x460")
window.title("Kalkulator sederhana")
windowlabel = Label(window, text="Kalkulator Sederhana", bg="dark blue", font=("arial",17), fg="white")
windowlabel.pack(side=TOP)

textin = StringVar()
operator = ""

"""Definisi (Fungsi)"""

#Input Angka / Operator

def angka(number):
    global operator
    operator = operator + str(number)
    textin.set(operator)

# Menghitung Hasil
def hitung():
    global operator
    try:
        add = str(eval(operator))
        textin.set(add)
        operator = add
    except Exception:
        textin.set("Error")
        operator = ""

# Reset operator
def clrbut ():
    global operator
    operator = ""
    textin.set("Hidup Jokowiii !!")


""" Tampilan """

windowtext = Entry(window, font=("arial", 12, "bold"), textvariable=textin, width=25, bd=5, bg="light green")
windowtext.pack()

but1 = Button(window, padx=14, pady=14, bd=4, bg="white", command=lambda: angka(1), text="1", font=("Courier New", 14))
but1.place(x=10, y=100)

but2 = Button(window, padx=14, pady=14, bd=4, bg="white", command=lambda: angka(2), text="2", font=("Courier New", 14))
but2.place(x=75, y=100)

but3 = Button(window, padx=14, pady=14, bd=4, bg="white", command=lambda: angka(3), text="3", font=("Courier New", 14))
but3.place(x=140, y=100)

but4 = Button(window, padx=14, pady=14, bd=4, bg="white", command=lambda: angka(4), text="4", font=("Courier New", 14))
but4.place(x=10, y=170)

but5 = Button(window, padx=14, pady=14, bd=4, bg="white", command=lambda: angka(5), text="5", font=("Courier New", 14))
but5.place(x=75, y=170)

but6 = Button(window, padx=14, pady=14, bd=4, bg="white", command=lambda: angka(6), text="6", font=("Courier New", 14))
but6.place(x=140, y=170)

but7 = Button(window, padx=14, pady=14, bd=4, bg="white", command=lambda: angka(7), text="7", font=("Courier New", 14))
but7.place(x=10, y=240)

but8 = Button(window, padx=14, pady=14, bd=4, bg="white", command=lambda: angka(8), text="8", font=("Courier New", 14))
but8.place(x=75, y=240)

but9 = Button(window, padx=14, pady=14, bd=4, bg="white", command=lambda: angka(9), text="9", font=("Courier New", 14))
but9.place(x=140, y=240)

but0 = Button(window, padx=14, pady=14, bd=4, bg="white", command=lambda: angka(0), text="0", font=("Courier New", 14))
but0.place(x=10, y=310)

butdot = Button(window, padx=14, pady=14, bd=4, bg="white", command=lambda: angka("."), text=".", font=("Courier New", 14))
butdot.place(x=75, y=310)

butpl = Button(window, padx=14, pady=14, bd=4, bg='white', text="+", command=lambda: angka("+"), font=("Courier New", 16, 'bold'))
butpl.place(x=205, y=100)

butsub = Button(window, padx=14, pady=14, bd=4, bg='white', text="-", command=lambda: angka("-"), font=("Courier New", 16, 'bold'))
butsub.place(x=205, y=170)

butml = Button(window, padx=14, pady=14, bd=4, bg='white', text="*", command=lambda: angka("*"), font=("Courier New", 16, 'bold'))
butml.place(x=205, y=240)

butdiv = Button(window, padx=14, pady=14, bd=4, bg='white', text="/", command=lambda: angka("/"), font=("Courier New", 16, 'bold'))
butdiv.place(x=205, y=310)

butclear = Button(window, padx=14, pady=119, bd=4, bg='white', text="CE", command=clrbut, font=("Courier New", 16, 'bold'))
butclear.place(x=270, y=100)

butequal = Button(window, padx=151, pady=14, bd=4, bg='white', command=hitung, text="=", font=("Courier New", 16, 'bold'))
butequal.place(x=10, y=380)

window.mainloop()
