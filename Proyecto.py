# -*- coding: cp1252 -*-
#Proyecto final Rony Schumann y Luis Fernando de león

#importar librerias
from Tkinter import *
import serial
import time
import sys

Grabar_ = 0
Playstation = 0
Manual = 1
Rutina_1 = 0
Rutina_2 = 0
Lista1 = []
Lista2 = []
Lista3 = []

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
    ser.write(chr(255))

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
    ser.write(chr(255))

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
    ser.write(chr(255))
    
def rec_1():
    global Lista1
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
    Lista1 = []

def rec_2():
    global Lista2
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
    Lista2 = []

def rec_3():
    global Lista3
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
    Lista3 = []

def conv_def(datos, pot):
    if datos <=110:
        if pot >20:
            pot = pot -1
        else:
            pass
    elif datos >=140:
        if pot <80:
            pot = pot +1
        else:
            pass
    else:
        pass
    return pot

def conv_2(datos, pot):
    if datos <=110:
        if pot >1:
            pot = pot -1
        else:
            pass
    elif datos >=140:
        if pot <5:
            pot = pot +1
        else:
            pass
    else:
        pass
    return pot

def espere_mijo():
    while ser.inWaiting()==0:
        ventana.update()
    recibo = ser.read()
    Valor = ord(recibo)
    return Valor

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


Pot1 = 20
Pot2 = 20
Pot3 = 5
Pot4 = 5

#LOOPS
ser= serial.Serial(port='COM5',baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=0)
while 1:
    while Manual == 1:
        recibi = espere_mijo() #------motor 1
        Pot1 = conv_def(recibi, Pot1)
        envio = chr(Pot1)
        ser.write(envio)
        recibi = espere_mijo() #------motor 2
        Pot2 = conv_def(recibi, Pot2)
        envio = chr(Pot2)
        ser.write(envio)
        recibi = espere_mijo() #------motor 3
        Pot3 = conv_2(recibi, Pot3)
        envio = chr(Pot3)
        ser.write(envio)
        recibi = espere_mijo() #------motor 4
        Pot4 = conv_2(recibi, Pot4)
        envio = chr(Pot4)
        ser.write(envio)
    
    while Grabar_ == 1:
        if Rutina_1 == 1:
            recibi = espere_mijo() #------motor 1
            Pot1 = conv_def(recibi, Pot1)
            Lista1.append(Pot1)
            recibi = espere_mijo() #------motor 2
            Pot2 = conv_def(recibi, Pot2)
            Lista1.append(Pot2)
            recibi = espere_mijo() #------motor 3
            Pot3 = conv_2(recibi, Pot3)
            Lista1.append(Pot3)
            recibi = espere_mijo() #------motor 4
            Pot4 = conv_2(recibi, Pot4)
            Lista1.append(Pot4)
        elif Rutina_2 == 1:
            recibi = espere_mijo() #------motor 1
            Pot1 = conv_def(recibi, Pot1)
            Lista2.append(Pot1)
            recibi = espere_mijo() #------motor 2
            Pot2 = conv_def(recibi, Pot2)
            Lista2.append(Pot2)
            recibi = espere_mijo() #------motor 3
            Pot3 = conv_2(recibi, Pot3)
            Lista2.append(Pot3)
            recibi = espere_mijo() #------motor 4
            Pot4 = conv_2(recibi, Pot4)
            Lista2.append(Pot4)
        else:
            recibi = espere_mijo() #------motor 1
            Pot1 = conv_def(recibi, Pot1)
            Lista3.append(Pot1)
            recibi = espere_mijo() #------motor 2
            Pot2 = conv_def(recibi, Pot2)
            Lista3.append(Pot2)
            recibi = espere_mijo() #------motor 3
            Pot3 = conv_2(recibi, Pot3)
            Lista3.append(Pot3)
            recibi = espere_mijo() #------motor 4
            Pot4 = conv_2(recibi, Pot4)
            Lista3.append(Pot4)
        
    while Playstation == 1:
        time.sleep(.01)
        if Rutina_1 == 1:       #rutina 1
            for x in Lista1:
                envio = chr(x)
                ser.write(envio)
                time.sleep(0.01)
                ventana.update()
        elif Rutina_2 == 1:     #rutina 2
            for x in Lista2:
                envio = chr(x)
                ser.write(envio)
                time.sleep(0.01)
                ventana.update()
        else:
            for x in Lista3:    #rutina 3
                envio = chr(x)
                ser.write(envio)
                time.sleep(0.01)
                ventana.update()

