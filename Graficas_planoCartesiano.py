from tkinter import Tk, Label, Button, Canvas, Frame, BOTH, IntVar, Entry, LabelFrame

BASE = 600
ALTURA = 600
BASE1 = 600
ALTURA1 = 600

ventana_prn = Tk()
ventana_prn.resizable(False,False)
ventana_prn.geometry("800x600")
ventana_prn.config(bg = "lightblue3")
ventana_prn.title("Graficador de funciones")

frame_graficacion = Frame(ventana_prn)
frame_graficacion.config(bg="white", width=580, height=580)
frame_graficacion.place(x=10, y=10)

frame_datos = Frame(ventana_prn)
frame_datos.config(bg="gray90", width=190, height=580)
frame_datos.place(x=600, y=10)

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.place(x=0, y=0)

ejey = c.create_line(BASE/2, 0, BASE/2, ALTURA, fill="black")
ejex= c.create_line(0, ALTURA/2, BASE, ALTURA/2, fill="black")

texto1 = c.create_text(BASE/2 + 10, 10, anchor="center", text="Y", font=("Arial", "10", "bold"), fill="black")
texto2 = c.create_text(BASE - 30, ALTURA/2 - 10, anchor="center", text="X", font=("Arial", "10", "bold"), fill="black")


x1 = IntVar()
y1 = IntVar()
x2 = IntVar()
y2 = IntVar()

y2_label = Label(frame_datos, text= "y2= ",bg="dim gray", font=("Arial", "8"))
y2_label.place(x=10 ,y=130)
Entry_y2 = Entry(frame_datos,textvariable=y2,width=5)
Entry_y2.place(x=35 ,y=130)
x2_label = Label(frame_datos, text= "x2= ",bg="dim gray", font=("Arial", "8"))
x2_label.place(x=10 , y=90)
Entry_x2 = Entry(frame_datos,textvariable=x2,width=5)
Entry_x2.place(x=35 ,y= 90)
y1_label = Label(frame_datos, text= "y1= ",bg="dim gray", font=("Arial", "8"))
y1_label.place(x=10 ,y= 50)
Entry_y1 = Entry(frame_datos,textvariable=y1, width=5)
Entry_y1.place(x=35 ,y= 50)    
x1_label = Label(frame_datos, text= "x1= ",bg="dim gray", font=("Arial", "8"))
x1_label.place(x=10 ,y= 10)
Entry_x1 = Entry(frame_datos,textvariable=x1,width=5)
Entry_x1.place(x=35 ,y= 10)

def graficar():
    recta = c.create_line(x1.get(), y1.get, x2.get(), y2.get(), fill="black")



    


graf = Button(frame_datos, text="graficar", command=graficar)
graf.place(x=10, y=300)
graf.config(bg="navajowhite2")
pend = Button(frame_datos, text="pendiente", command=graficar)
pend.place(x=80, y=300)
pend.config(bg="navajowhite2")



ventana_prn.mainloop()