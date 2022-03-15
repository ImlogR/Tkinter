from tkinter import *

window =Tk()

def kmTo():
    metre = float(e1_value.get())*1000
    centimetre=float(e1_value.get())*100000
    miles = float(e1_value.get())/1.6
    t1.delete("1.0", END)
    t1.insert(END, metre)
    t2.delete("1.0", END)
    t2.insert(END, centimetre)
    t3.delete("1.0", END)
    t3.insert(END, miles)

window.wm_title("Length Converter")

e0= Label(window, text="km::")
e0.grid(row=0, column=1)


e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=2)

e2 = Label(window, text="Metres:")
e2.grid(row=1, column=1)

e3 = Label(window, text="Centimetres:")
e3.grid(row=1, column=2)


e4 = Label(window, text="Miles:")
e4.grid(row=1, column=3)

e5= Label(window, text="Maile nai banako ho!!")
e5.grid(row=3, column=1)

b1 = Button(window, text="Convert", command=kmTo)
b1.grid(row=0, column=3)

t1= Text(window, height=1, width=20)
t1.grid(row=2, column=1)

t2= Text(window, height=1, width=20)
t2.grid(row=2, column=2)

t3= Text(window, height=1, width=20)
t3.grid(row=2, column=3)
window.mainloop()