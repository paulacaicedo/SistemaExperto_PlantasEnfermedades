# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:54:03 2022

@author: LIGHT
"""

import tkinter as tk
from tkinter import ttk
from tkinter import *
 

def change_color(canvas,objeto):
    canvas.itemconfig(objeto, fill='green') 
    
def change_color1(canvas,objeto):
    canvas.itemconfig(objeto, fill='dark red') 
    
def cambio_texto(x):
    root = tk.Tk()
    root.geometry('750x100')
    root.title('Aplicacion')
    lab = ttk.Label(root, text=x).pack()
     
    root.mainloop()

def simulacion():
    #Actividad Principal
    master = tk.Tk()
    master.geometry('1000x700')
    master.title('Aplicacion')
    
    
    
    canvas = Canvas(master,width=1000, height=600, bg='white')
    canvas.pack(expand=YES, fill=BOTH)
    
     
    #AGENTES EXTERNOS
    #canvas.create_text(70, 20, text='Agentes Externos',)

    A1 = canvas.create_oval(50, 50, 80, 80, fill='dark red')
    canvas.create_text(75, 90, text='Humedad Ambiental Alta')
    
    A2 = canvas.create_oval(50, 110, 80, 140, fill='dark red')
    canvas.create_text(80, 150, text='Deficiencia en la Potasio')
    
    A3 = canvas.create_oval(50, 170, 80, 200, fill='dark red')
    canvas.create_text(89, 210, text='Condición Anormal de Nutrición')
    
    A4 = canvas.create_oval(50, 230, 80, 260, fill='dark red')
    canvas.create_text(90, 270, text='Deficit Hidrico(Largas Sequias)')
    
    A5 = canvas.create_oval(50, 290, 80, 320, fill='dark red')
    canvas.create_text(80, 330, text='Deficiencia de Magnesio')
    
    A6 = canvas.create_oval(50, 350, 80, 380, fill='dark red')
    canvas.create_text(80, 390, text='Deficiencia en la fertilizacion')
    
    A7 = canvas.create_oval(50, 410, 80, 440, fill='dark red')
    canvas.create_text(65, 450, text='Constitución Genetica')
    
    A8 = canvas.create_oval(50, 470, 80, 500, fill='dark red')
    canvas.create_text(65, 510, text='Suelos Arenosos')
    
    A9 = canvas.create_oval(50, 530, 80, 560, fill='dark red')
    canvas.create_text(65, 570, text='Fallas en la siembra')
    
    A10 = canvas.create_oval(50, 580, 80, 610, fill='dark red')
    canvas.create_text(90, 620, text='Mal drenaje de suelos compactos')
    
    #--------------------ENFERMEDADES -- REPRODUCCION DE HONGOS
    
    
    H1 = canvas.create_oval(220, 50, 250, 80, fill='dark red')
    x = "Manchas Oscuras en la punta de la hoja o borde de color marron, rodeada de por un halo o zona de transicion de color amarillento"
    button = ttk.Button(canvas,text = 'H1', command=lambda: cambio_texto(x))
    button.place(x=200, y=82)
    
    H2 = canvas.create_oval(220, 110, 250, 140, fill='dark red')
    x1 = "Manchas Translucidas de color marron claro, rodeadas por un borde amarillo palido"
    button = ttk.Button(canvas,text = 'H2', command=lambda: cambio_texto(x1))
    button.place(x=200, y=142) 
    
    H3 = canvas.create_oval(220, 170, 250, 200, fill='dark red')
    x2 = "Manchas Alargadas en medio de las nervaduras de color marron oscuro, rodeadas por bordes amarillos"
    button = ttk.Button(canvas,text = 'H3', command=lambda: cambio_texto(x2))
    button.place(x=200, y=202) 
    
    H4 = canvas.create_oval(220, 230, 250, 260, fill='dark red')
    x3 = "Manchas de color amarillento, translucidas y alargadas con borde amarillo rodeada de un anillo de color gris"
    button = ttk.Button(canvas,text = 'H4', command=lambda: cambio_texto(x3))
    button.place(x=200, y=262) 
    
    H5 = canvas.create_oval(220, 290, 250, 320, fill='dark red')
    x4 = "Manchas que primero son de color marron purpura, luego toman coloración marron claro y por ultimo es gris ceniza"
    button = ttk.Button(canvas,text = 'H5', command=lambda: cambio_texto(x4))
    button.place(x=200, y=322) 
    
    H6 = canvas.create_oval(220, 350, 250, 380, fill='dark red') 
    x5 = "Enves de los folios y manchas casi circulares de color oliva rodeada de bordes amarillos"
    button = ttk.Button(canvas,text = 'H6', command=lambda: cambio_texto(x5))
    button.place(x=200, y=382) 
    
    #AFECTACION EN TRONCOS Y RAICES
    
    H7 = canvas.create_oval(220, 410, 250, 440, fill='dark red') 
    x6 = "Coloración marron en raices"
    button = ttk.Button(canvas,text = 'H7', command=lambda: cambio_texto(x6))
    button.place(x=200, y=442)
    
    H8 = canvas.create_oval(220, 470, 250, 500, fill='dark red') 
    x7 = "Los tejidos bulbo toman un color marron claro se tornan marron oscuro con tintes azulados(tronco) "
    button = ttk.Button(canvas,text = 'H8', command=lambda: cambio_texto(x7))
    button.place(x=200, y=502)
    
    
    #AFECTACION DE FRUTOS
    
    H9 = canvas.create_oval(220, 530, 250, 560, fill='dark red') 
    x8 = "Frutos de Color blanco cerca al suelo que se semejan a orejas de palo"
    button = ttk.Button(canvas,text = 'H9', command=lambda: cambio_texto(x8))
    button.place(x=200, y=562)
    
    H10 = canvas.create_oval(220, 590, 250, 620, fill='dark red') 
    x9 = "Flechas permanecen cerrados y las hojas bajeras se tornan amarillentas y se secan"
    button = ttk.Button(canvas,text = 'H10', command=lambda: cambio_texto(x9))
    button.place(x=200, y=622)
    
     
    
                 
    
    #-------------
    
    E1 = canvas.create_oval(330, 60, 360, 90, fill='dark red')
    canvas.create_text(350, 100, text='Botryodipiodia')
    
    E2 = canvas.create_oval(330, 120, 360, 150, fill='dark red')
    canvas.create_text(350, 160, text='Melaconium')
    
    E3 = canvas.create_oval(330, 180, 360, 210, fill='dark red')
    canvas.create_text(350, 220, text='Glomeralla Cingulata')
    
    E4 = canvas.create_oval(330, 240, 360, 270, fill='dark red')
    canvas.create_text(350, 280, text='Curvalaria Maculans')
    
    E5 = canvas.create_oval(330, 300, 360, 330, fill='dark red')
    canvas.create_text(360, 340, text='Pestalotiopsis y/o Pestalotia')
    
    E6 = canvas.create_oval(330, 360, 360, 390, fill='dark red')
    canvas.create_text(350, 400, text='Thelaviopsis paradoxa')
    
    E7 = canvas.create_oval(330, 420, 360, 450, fill='dark red')
    canvas.create_text(350, 460, text='Ganoderma lucidum')
    
    
    
    #--------------INSECTOS AFECTACIONES
    
    I1 = canvas.create_oval(450, 50, 480, 80, fill='dark red')
    canvas.create_text(460, 100, text='A. Insecto Tigidae')
    
    I2 = canvas.create_oval(450, 120, 480, 150, fill='dark red')
    canvas.create_text(460, 160, text='A.Chinche Encaje')
    
    I3 = canvas.create_oval(450, 180, 480, 210, fill='dark red')
    canvas.create_text(470, 220, text='A. Varios Parasitos')
    
    I4 = canvas.create_oval(450, 240, 480, 270, fill='dark red')
    canvas.create_text(470, 280, text='A. Cucarron Picudo')
    
 
    #-------------------EDADES DE LAS PALMAS
    
    D1 = canvas.create_oval(450, 360, 480, 390, fill='dark red')
    d1 = "Palma Joven de 3 a 5 años"
    button = ttk.Button(canvas,text = 'Edad', command=lambda: cambio_texto(d1))
    button.place(x=430, y=392)
    
    D2 = canvas.create_oval(450, 420, 480, 450, fill='dark red')
    d2 = "Palma Joven +6 años"
    button = ttk.Button(canvas,text = 'Edad', command=lambda: cambio_texto(d2))
    button.place(x=430, y=452)
    
    D3 = canvas.create_oval(450, 480, 480, 510, fill='dark red')
    d3 = "Palma 2 y media de años"
    button = ttk.Button(canvas,text = 'Edad', command=lambda: cambio_texto(d3))
    button.place(x=430, y=512)
    
    D4 = canvas.create_oval(450, 540, 480, 570, fill='dark red')
    d4 = "Palma Mayores a 10 años"
    button = ttk.Button(canvas,text = 'Edad', command=lambda: cambio_texto(d4))
    button.place(x=430, y=572)
    
    #------------------- OTRAS HECHOS EN LAS HOJAS
    
    H11 = canvas.create_oval(570, 360, 600, 390, fill='dark red')
    y1 = "Hojas bajeras de color Amarillento"
    button = ttk.Button(canvas,text = 'H11', command=lambda: cambio_texto(y1))
    button.place(x=550, y=392)
    
    H12 = canvas.create_oval(570, 420, 600, 450, fill='dark red')
    y2 = "Tejido Marron oscuro y pudricion humeda y fetida"
    button = ttk.Button(canvas,text = 'H12', command=lambda: cambio_texto(y2))
    button.place(x=550, y=452)
    
    H13 = canvas.create_oval(570, 480, 600, 510, fill='dark red')
    y3 = "Secamiento Progresivo de las hojas centrales de la corona"
    button = ttk.Button(canvas,text = 'H13', command=lambda: cambio_texto(y3))
    button.place(x=550, y=512)
    
    H14 = canvas.create_oval(570, 540, 600, 570, fill='dark red')
    y4 = "Frutos Enfermos"
    button = ttk.Button(canvas,text = 'H14', command=lambda: cambio_texto(y4))
    button.place(x=550, y=572)
    
    H15 = canvas.create_oval(570, 600, 600, 630, fill='dark red')
    y5 = "Afectado por Hongo Marcimus"
    button = ttk.Button(canvas,text = 'H15', command=lambda: cambio_texto(y5))
    button.place(x=550, y=632)
    
    
    
    #--------------ENFERMEDADES PALMAS ADULTAS
    
    P1 = canvas.create_oval(630, 50, 660, 80, fill='dark red')
    canvas.create_text(650, 100, text='Añublo o Secamiento de Hojas')
    x10 = "Los mejores resultados en el control del insecto se han encontrado en las plantaciones del producto mediante inyección en el tronco. Entre los insecticidas empleados en esta forma está el Monocrotophos (4.8 a 8.4 gm. de ia.a./palma) y el Dicrotophos (6.5 a 7.8 gm. de ia.a./palma), con efectividad del 100°/o, en palmas mayores de 11 años y aplicados en un solo hueco, en el tronco."
    button = ttk.Button(canvas,text = 'T1', command=lambda: cambio_texto(x10))
    button.place(x=680, y=50)
    
    P2 = canvas.create_oval(630, 130, 660,160, fill='dark red')
    canvas.create_text(650, 180, text='Pudricion de Raices y Base del Tronco')
    x11 = "Se recomienda, para prevenir la enfermedad, el mejoramiento del drenaje a fin de facilitar la evacuación rápida y eficiente del exceso de agua en el suelo. "
    button = ttk.Button(canvas,text = 'T2', command=lambda: cambio_texto(x11))
    button.place(x=680, y=130)
    
    P5 = canvas.create_oval(630, 230, 660,260, fill='dark red')
    canvas.create_text(650, 280, text='Anillo Marron')
    x14 = "El tratamiento curativo del anillo marrón, mediante la aplicación de nematicidas en inyección al tronco, al suelo en la zona del plateo o por absorción a través de las raíces, ha dado hasta el presente, resultados erráticos  "
    button = ttk.Button(canvas,text = 'T5', command=lambda: cambio_texto(x14))
    button.place(x=680, y=230)
    
    
    
    
    P3 = canvas.create_oval(700, 360, 730,390, fill='dark red')
    canvas.create_text(750, 400, text='Amarillamiento  de  las  hojas  inferiores')
    x12 = "se sugirieron las siguientes dosis de fertilizantes por palma y por año: Urea : 1 Kg. en dos aplicaciones (0.5 + 0.5) Superfosfato triple : 1 Kg. Cloruro de potasio : 0.750 Kg. Borax : 75 Kg. Para las palmas que mostraban amarillamiento de las hojas inferiores, se sugirió añadir a los anteriores fertilizantes, 1 Kg. de kieserita u otra fuente de magnesio como sulfomag.  "
    button = ttk.Button(canvas,text = 'T3', command=lambda: cambio_texto(x12))
    button.place(x=760, y=360)
    
    P4 = canvas.create_oval(700, 420, 730,450, fill='dark red')
    canvas.create_text(750, 470, text='Pudricion Letal de la flecha y el cogollo')
    x13 = "El tratamiento de las palmas enfermas con una mezcla insecticida-fungicida, bactericida (Dipterex + Azul de Metileno), fue inefectivo. "
    button = ttk.Button(canvas,text = 'T4', command=lambda: cambio_texto(x13))
    button.place(x=760, y=420)
    
    
    P6 = canvas.create_oval(700, 540, 730,570, fill='dark red')
    canvas.create_text(750, 590, text='Pudricion de los Racimos')
    x15 = "Los racimos infectados deben retirarse de las palmas, así como también los restos de inflorescencias, mediante podas sanitarias regulares. Cuando sea necesario, debe efectuarse la polinización asistida para conseguir un mejor cuajamiento de los frutos, procurando una disminución del exceso de humedad ambiental, mediante un control de malezas y mejoramiento de las condiciones de drenaje   "
    button = ttk.Button(canvas,text = 'T6', command=lambda: cambio_texto(x15))
    button.place(x=760, y=540)
    
    
    
    #-----------------------------------------------------------------------------
    #REPRODUCCION DE ENFERMEDADES
    
    #AÑUBLO O SECAMIENTO DE LAS HOJAS
    #1. Humedad Ambiental Alta y Periodo Seco y Deficiencia de Magnesio
    #2. Manchas que son marron purpura, luego marron claro y se torna ceniza H5
    #2. Enves de Folios y manchas casi circulares H6
    #3. Afectado por hongo Pestalopsis 
    #3. Insecto, parasitos, chinche
    #4. Edad 2 y media de años
    #5. Añublo o secamiento de las hojas
    
    master.after(1000, lambda led=A1: change_color(canvas,led)) 
    master.after(17000, lambda led=A1: change_color1(canvas,led))
    
    master.after(1000, lambda led=A4: change_color(canvas,led)) 
    master.after(17000, lambda led=A4: change_color1(canvas,led))
    
    master.after(1000, lambda led=A5: change_color(canvas,led)) 
    master.after(17000, lambda led=A5: change_color1(canvas,led))
    
    master.after(4000, lambda led=H5: change_color(canvas,led)) 
    master.after(17000, lambda led=H5: change_color1(canvas,led))
    
    master.after(4000, lambda led=H6: change_color(canvas,led)) 
    master.after(17000, lambda led=H6: change_color1(canvas,led))
    
    master.after(7000, lambda led=E5: change_color(canvas,led)) 
    master.after(17000, lambda led=E5: change_color1(canvas,led))
    
    master.after(9000, lambda led=I1: change_color(canvas,led)) 
    master.after(17000, lambda led=I1: change_color1(canvas,led))
    
    master.after(9000, lambda led=I2: change_color(canvas,led)) 
    master.after(17000, lambda led=I2: change_color1(canvas,led))
    
    master.after(9000, lambda led=I3: change_color(canvas,led)) 
    master.after(17000, lambda led=I3: change_color1(canvas,led))
    
    master.after(12000, lambda led=D3: change_color(canvas,led)) 
    master.after(17000, lambda led=D3: change_color1(canvas,led))
    
    master.after(15000, lambda led=P1: change_color(canvas,led)) 
    master.after(17000, lambda led=P1: change_color1(canvas,led))
    
 
    #------------------------------------------------------
    # PUDRICION DE LAS RAICES Y DE LA BASE DEL TRONCO
    
    #1.Mal drenaje de suelos
    #2. Frutos de olor blanco cerca al suelo H9 y H10
    #3. Ganoderma lucidum E7
    #3. Tejidos bulbo toman color marron H8 y coloracion marron oscura H7
    #4. Planta Mayor a 6 años
    #5. Pudricion de Raices P2
    
    master.after(18000, lambda led=A10: change_color(canvas,led)) 
    master.after(30000, lambda led=A10: change_color1(canvas,led))
    
    master.after(20000, lambda led=H9: change_color(canvas,led)) 
    master.after(30000, lambda led=H9: change_color1(canvas,led))
    
    master.after(20000, lambda led=H10: change_color(canvas,led)) 
    master.after(30000, lambda led=H10: change_color1(canvas,led))
    
    master.after(21000, lambda led=E7: change_color(canvas,led)) 
    master.after(30000, lambda led=E7: change_color1(canvas,led))
    
    master.after(23000, lambda led=H8: change_color(canvas,led)) 
    master.after(30000, lambda led=H8: change_color1(canvas,led))
    
    master.after(23000, lambda led=H7: change_color(canvas,led)) 
    master.after(30000, lambda led=H7: change_color1(canvas,led))
    
    master.after(24000, lambda led=D2: change_color(canvas,led)) 
    master.after(30000, lambda led=D2: change_color1(canvas,led))
    
    master.after(26000, lambda led=P2: change_color(canvas,led)) 
    master.after(30000, lambda led=P2: change_color1(canvas,led))
    
    #---------------------------------------------------------------------
    #AMARILLAMIENTO DE LAS HOJAS INFERIORES
    
    #1. Retraso en el crecimiento A9 y A8, A6
    #2. Amarrillento en Hojas H11 y Folios Secos H10
    #2. Edad 3 a 5 años D11
    #3. P3 Amarillamiento de las hojas inferiores
    
    master.after(31000, lambda led=A9: change_color(canvas,led)) 
    master.after(37000, lambda led=A9: change_color1(canvas,led))
    
    master.after(31000, lambda led=A8: change_color(canvas,led)) 
    master.after(37000, lambda led=A8: change_color1(canvas,led))
    
    master.after(31000, lambda led=A6: change_color(canvas,led)) 
    master.after(37000, lambda led=A6: change_color1(canvas,led))
    
    master.after(33000, lambda led=H10: change_color(canvas,led)) 
    master.after(37000, lambda led=H10: change_color1(canvas,led))
    
    master.after(33000, lambda led=H11: change_color(canvas,led)) 
    master.after(37000, lambda led=H11: change_color1(canvas,led))
    
    master.after(34000, lambda led=D1: change_color(canvas,led)) 
    master.after(37000, lambda led=D1: change_color1(canvas,led))
    
    master.after(35000, lambda led=P3: change_color(canvas,led)) 
    master.after(37000, lambda led=P3: change_color1(canvas,led))
    
    #-----------------------------------------------------------------
    # PudricionLetal de la flecha y el cogollo 
    
    #1. Pisos secos A4, A6
    #2. H10 Secamiento Progresivo
    #2. Edad +6 Años
    #3. H13, H12
    #4. Pudricion P4
     
    master.after(39000, lambda led=A4: change_color(canvas,led)) 
    master.after(46000, lambda led=A4: change_color1(canvas,led))
    
    master.after(39000, lambda led=A6: change_color(canvas,led)) 
    master.after(46000, lambda led=A6: change_color1(canvas,led))
    
    master.after(40000, lambda led=H10: change_color(canvas,led)) 
    master.after(46000, lambda led=H10: change_color1(canvas,led))
    
    master.after(40000, lambda led=D2: change_color(canvas,led)) 
    master.after(46000, lambda led=D2: change_color1(canvas,led))
    
    master.after(43000, lambda led=H12: change_color(canvas,led)) 
    master.after(46000, lambda led=H12: change_color1(canvas,led))
    
    master.after(43000, lambda led=H13: change_color(canvas,led)) 
    master.after(46000, lambda led=H13: change_color1(canvas,led))
    
    master.after(44000, lambda led=P4: change_color(canvas,led)) 
    master.after(46000, lambda led=P4: change_color1(canvas,led))
    
    #-----------------------------------------------------------------------
    #ANILLO MARRON
    #1. A4, A6
    #2. H10, H11,H7
    #3. I4
    #4. P5
    
    master.after(48000, lambda led=A4: change_color(canvas,led)) 
    master.after(55000, lambda led=A4: change_color1(canvas,led))
    
    master.after(48000, lambda led=A6: change_color(canvas,led)) 
    master.after(55000, lambda led=A6: change_color1(canvas,led))
    
    master.after(49000, lambda led=H10: change_color(canvas,led)) 
    master.after(55000, lambda led=H10: change_color1(canvas,led))
    
    master.after(50000, lambda led=H11: change_color(canvas,led)) 
    master.after(55000, lambda led=H11: change_color1(canvas,led))
    
    master.after(50000, lambda led=H7: change_color(canvas,led)) 
    master.after(55000, lambda led=H7: change_color1(canvas,led))
    
    master.after(50000, lambda led=I4: change_color(canvas,led)) 
    master.after(55000, lambda led=I4: change_color1(canvas,led))
    
    master.after(52000, lambda led=P5: change_color(canvas,led)) 
    master.after(55000, lambda led=P5: change_color1(canvas,led))
    
    #----------------------------------------------------------------------------
    #PUDRICION DE LOS RACIMOS
    # 1.A1, A6
    # 2.H15
    # 2.H14
    # 3.D2
    # 4.P6
    
    master.after(57000, lambda led=A1: change_color(canvas,led)) 
    master.after(62000, lambda led=A1: change_color1(canvas,led))
    
    master.after(57000, lambda led=A6: change_color(canvas,led)) 
    master.after(62000, lambda led=A6: change_color1(canvas,led))
    
    master.after(58000, lambda led=H15: change_color(canvas,led)) 
    master.after(62000, lambda led=H15: change_color1(canvas,led))
    
    master.after(58000, lambda led=H14: change_color(canvas,led)) 
    master.after(62000, lambda led=H14: change_color1(canvas,led))
    
    master.after(59000, lambda led=D2: change_color(canvas,led)) 
    master.after(62000, lambda led=D2: change_color1(canvas,led))
    
    master.after(60000, lambda led=P6: change_color(canvas,led)) 
    master.after(62000, lambda led=P6: change_color1(canvas,led))



    master.mainloop()
    


#---------------------------------------------------



root = tk.Tk()
root.geometry('200x50')
root.title('Inicio')
button_atipico = tk.Button(root,text = 'Empezar Simulacion', command=simulacion)
button_atipico.place(x=30, y=10) 

root.mainloop()



