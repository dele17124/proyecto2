# -*- coding: cp1252 -*-
#Proyecto final Rony Schumann y Luis Fernando de león

#importar librerias
from Tkinter import *
import serial
import time
import sys
#from PIL import Image, ImageTk

Grabar_ = 0
Playstation = 0
Manual = 1
Rutina_1 = 0
Rutina_2 = 0
#lista1.append()

def Stop_():
    global Grabar_
    global Playstation
    global Manual
    global Rutina_1
    global Rutina_2
    Grabar_ = 0
    Playstation = 0
    Manual = 1
    Rutina_1 = 0
    Rutina_2 = 0

def play_1():
    global Grabar_
    global Playstation
    global Manual
    global Rutina_1
    global Rutina_2
    Grabar_ = 0
    Playstation = 1
    Manual = 0
    Rutina_1 = 1
    Rutina_2 = 0

def play_2():
    global Grabar_
    global Playstation
    global Manual
    global Rutina_1
    global Rutina_2
    Grabar_ = 0
    Playstation = 1
    Manual = 0
    Rutina_1 = 0
    Rutina_2 = 1

def play_3():
    global Grabar_
    global Playstation
    global Manual
    global Rutina_1
    global Rutina_2
    Grabar_ = 0
    Playstation = 1
    Manual = 0
    Rutina_1 = 0
    Rutina_2 = 0
    
def rec_1():
    global Grabar_
    global Playstation
    global Manual
    global Rutina_1
    global Rutina_2
    Grabar_ = 1
    Playstation = 0
    Manual = 0
    Rutina_1 = 1
    Rutina_2 = 0

def rec_2():
    global Grabar_
    global Playstation
    global Manual
    global Rutina_1
    global Rutina_2
    Grabar_ = 1
    Playstation = 0
    Manual = 0
    Rutina_1 = 0
    Rutina_2 = 1

def rec_3():
    global Grabar_
    global Playstation
    global Manual
    global Rutina_1
    global Rutina_2
    Grabar_ = 1
    Playstation = 0
    Manual = 0
    Rutina_1 = 0
    Rutina_2 = 0


#VENTANA
ventana = Tk()
ventana.geometry("450x350")
ventana.title("Proyecto final")
ventana.configure(bg = '#CED8F6')
#NOMBRES
Nombre = Label(ventana, text = "Rony Schumann 17232", bg = '#CED8F6', font=("Times", 10))
Nombre.grid(row=0, column=0)
Nombre2 = Label(ventana, text = "Tusitar de León 17124", bg = '#CED8F6', font=("Times", 10))
Nombre2.grid(row=1, column=0,pady=(1, 50))

#FILA1
texto2 = Label(ventana, text = "Rutina 1", bg = '#CED8F6',font=("Times", 14, "bold"))
texto2.grid(row=2, column=0,padx=(75, 10))
#BOTONES 1
boton2 = Button(ventana, text = 'Grabar', command = rec_1, bd = 10)
boton2.grid(row=2, column=1)
boton2_2 = Button(ventana, command = play_1, text = 'Reproducir', bd = 10)
boton2_2.grid(row=2, column=2,padx=10, pady=10)
boton2_3 = Button(ventana, text="Parar", command = Stop_, bd = 10)
boton2_3.grid(row=2, column=3)

#FILA2
texto3 = Label(ventana, text = "Rutina 2", bg = '#CED8F6', font=("Times", 14, "bold"))
texto3.grid(row=3, column=0,padx=(75, 10))
#BOTONES 2
boton3 = Button(ventana, text="Grabar", command = rec_2, bd = 10)
boton3.grid(row=3, column=1)
boton3_2 = Button(ventana, text="Reproducir", command = play_2, bd = 10)
boton3_2.grid(row=3, column=2,padx=10, pady=10)
boton3_3 = Button(ventana, text="Parar", command = Stop_ , bd = 10)
boton3_3.grid(row=3, column=3)

#FILA3
texto1 = Label(ventana, text = "Rutina 3", bg = '#CED8F6', font=("Times", 14, "bold"))
texto1.grid(row=4, column=0,padx=(75, 10))
#BOTONES 3
boton1 = Button(ventana, text="Grabar", command = rec_3, bd = 10)
boton1.grid(row=4, column=1)
boton1_2 = Button(ventana, text="Reproducir", command = play_3, bd = 10)
boton1_2.grid(row=4, column=2,padx=10, pady=10)
boton1_3 = Button(ventana, text="Parar", command = Stop_, bd = 10)
boton1_3.grid(row=4, column=3)


#LOOPS
#ser= serial.Serial(port='COM5',baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=0)
while 1:
    while Manual == 1:
       print 'dele_duro'
       ventana.update()
        
    while Grabar_ == 1:
        
        print 'grabe'
        ventana.update()
        
    while Playstation == 1:
        print 'play'
        ventana.update()

