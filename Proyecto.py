# -*- coding: cp1252 -*-
#Proyecto final Rony Schumann y Luis Fernando de león

#importar librerias
from Tkinter import *
import serial
import time
import sys
#from PIL import Image, ImageTk

lista1 = []
lista2 = []
lista3 = []

Manual = 1
Pleito = 0
Grabar = 0
Rut1 = 1
Rut2 = 0
Rut3 = 0


#lista1.append()

def cambio(var_1, var_2, var_3, var_4, var_5, var_6):
    var_1 = 1
    var_2 = 1
    var_3 = 0
    var_4 = 0
    var_5 = 0
    var_6 = 0
    

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
boton2 = Button(ventana, text = 'Grabar', command = "funcion", bd = 10)
boton2.grid(row=2, column=1)
boton2_2 = Button(ventana, command = "funcion", text = "Reproducir", bd = 10)
boton2_2.grid(row=2, column=2,padx=10, pady=10)
boton2_3 = Button(ventana, text="Parar", command = cambio(Manual, ), bd = 10)
boton2_3.grid(row=2, column=3)

#FILA2
texto3 = Label(ventana, text = "Rutina 2", bg = '#CED8F6', font=("Times", 14, "bold"))
texto3.grid(row=3, column=0,padx=(75, 10))
#BOTONES 2
boton3 = Button(ventana, text="Grabar", command = "funcion", bd = 10)
boton3.grid(row=3, column=1)
boton3_2 = Button(ventana, text="Reproducir", command = "funcion", bd = 10)
boton3_2.grid(row=3, column=2,padx=10, pady=10)
boton3_3 = Button(ventana, text="Parar", command = "funcion", bd = 10)
boton3_3.grid(row=3, column=3)

#FILA3
texto1 = Label(ventana, text = "Rutina 3", bg = '#CED8F6', font=("Times", 14, "bold"))
texto1.grid(row=4, column=0,padx=(75, 10))
#BOTONES 3
boton1 = Button(ventana, text="Grabar", command = "funcion", bd = 10)
boton1.grid(row=4, column=1)
boton1_2 = Button(ventana, text="Reproducir", command = "funcion", bd = 10)
boton1_2.grid(row=4, column=2,padx=10, pady=10)
boton1_3 = Button(ventana, text="Parar", command = "funcion", bd = 10)
boton1_3.grid(row=4, column=3)


#LOOPS
ser= serial.Serial(port='COM5',baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=0)

while Manual == 1:
   print 'hola'
   ventana.update()
    
while Pleito == 1:
    print 'adios'
    ventana.update()










