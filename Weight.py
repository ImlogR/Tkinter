from tkinter import *

window= Tk()

def kg2o():
    grams=float(in1_value.get())*1000
    pounds=float(in1_value.get())*2.205
    tons=float(in1_value.get())/1000
    o1.delete("1.0", END)
    o1.insert(END, grams)
    o2.delete("1.0", END)
    o2.insert(END, pounds)
    o3.delete("1.0", END)
    o3.insert(END, tons)

window.wm_title("Weight converter")

w1= Label(window, text="kilos:")
w1.grid(row=0, column=0)

in1_value= StringVar()
in1=Entry(window, textvariable=in1_value)
in1.grid(row=0, column=1)


b1=Button(window, text="Convert", command=kg2o)
b1.grid(row=0, column=2)

w2=Label(window, text="Grams:")
w2.grid(row=1, column=0)

w3=Label(window, text="Pounds:")
w3.grid(row=1, column=1)

w4=Label(window, text="Tons:")
w4.grid(row=1, column=2)

o1=Text(window, height=1, width=20)
o1.grid(row=2, column=0)

o2=Text(window, height=1, width=20)
o2.grid(row=2, column=1)

o3=Text(window, height=1, width=20)
o3.grid(row=2, column=2)


window.mainloop()