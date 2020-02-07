##crea nuestra pantalla
from tkinter import *
from time import sleep
from tkinter import ttk
from tkinter import messagebox
##Conexion a Base de Datos
import pymysql
conn=pymysql.connect(host='localhost', user='root', passwd='', db='test')
cursor=conn.cursor()
##realiza el diseño del gato
gato=Tk()
gato.resizable(1,1)
gato.title("El Gato")
gato.geometry("600x500")
gato.config(bg="red")
turno=StringVar()
turno.set("P")
mensaje=StringVar()
mensaje.set(" ")
##Será el contador del empate
cont_empate=StringVar()
cont_empate.set("9")
numero=StringVar()
numero.set("1")

##Será el contador de P
cont_perro=StringVar()
cont_perro.set("0")
numperro=StringVar()
numperro.set("1")


##Será el contador de G
cont_gato=StringVar()
cont_gato.set("0")
numgato=StringVar()
numgato.set("1")

## Nombre del primer usuario
def nombre1(event):
	tc.config(state=DISABLED)
## Nombre del segundo usuario
def nombre2(event):
	bn.config(state=DISABLED)

## Combo de Usuarios
cursor.execute('select Nom_usuario from usuarios')
tcs=[]

##Se definen las variables de las posiciones para hacer validas las combinaciones
b1=StringVar()
b1.set("1")
b2=StringVar()
b2.set("2")
b3=StringVar()
b3.set("3")
b4=StringVar()
b4.set("4")
b5=StringVar()
b5.set("5")
b6=StringVar()
b6.set("6")
b7=StringVar()
b7.set("7")
b8=StringVar()
b8.set("8")
b9=StringVar()
b9.set("9")

##da valor alas imagenes de cada jugador 
perro2=PhotoImage(file="perro12.gif")
hola=PhotoImage(file="hola1.gif")
gato1=PhotoImage(file="gato1.gif")
extra=PhotoImage(file="huella12.gif")
##Formas de ganar
def ganador():
	## priemra fila
	if (b1.get() == b2.get() and b1.get() == b3.get()):
		if b1.get() == "P":
			messagebox.showinfo(message="GANO "+bn.get(), title="gana")
			celebra_perro()
			cont_perro.set(int(cont_perro.get())+int(numperro.get()))
		else:
			messagebox.showinfo(message="GANO "+tc.get(), title="gana")
			celebra_gato()
			cont_gato.set(int(cont_gato.get())+int(numgato.get()))
		cierra()
	## segunda fila
	if (b4.get() == b5.get() and b4.get() == b6.get()):
		if b4.get() == "P":
			messagebox.showinfo(message="GANO "+bn.get(), title="gana")
			celebra_perro()
			cont_perro.set(int(cont_perro.get())+int(numperro.get()))
		else:
			messagebox.showinfo(message="GANO "+tc.get(), title="gana")
			celebra_gato()
			cont_gato.set(int(cont_gato.get())+int(numgato.get()))
		cierra()
	##tercera fila
	if (b7.get() == b8.get() and b7.get() == b9.get()):
		if b7.get() == "P":
			messagebox.showinfo(message="GANO "+bn.get(), title="gana")
			celebra_perro()
			cont_perro.set(int(cont_perro.get())+int(numperro.get()))
		else:
			messagebox.showinfo(message="GANO "+tc.get(), title="gana")
			celebra_gato()
			cont_gato.set(int(cont_gato.get())+int(numgato.get()))
		cierra()
	## primera columna
	if (b1.get() == b4.get() and b1.get() == b7.get()):
		if b1.get() == "p":
			messagebox.showinfo(message="GANO"+bn.get(), title="gana")
			celebra_perro()
			cont_perro.set(int(cont_perro.get())+int(numperro.get()))
		else:
			messagebox.showinfo(message="GANO "+tc.get(), title="gana")
			celebra_gato()
			cont_gato.set(int(cont_gato.get())+int(numgato.get()))
		cierra()
	## segunda columna
	if (b2.get() == b5.get() and b2.get() == b8.get()):
		if b2.get() == "P":
			messagebox.showinfo(message="GANO "+bn.get(), title="gana")
			celebra_perro()
			cont_perro.set(int(cont_perro.get())+int(numperro.get()))
		else:
			messagebox.showinfo(message="GANO "+tc.get(), title="gana")
			celebra_gato()
			cont_gato.set(int(cont_gato.get())+int(numgato.get()))
		cierra()
	## tercera columna
	if (b3.get() == b6.get() and b3.get() == b9.get()):
		if b3.get() == "P": 
			messagebox.showinfo(message="GANO "+bn.get(), title="gana")
			celebra_perro()
			cont_perro.set(int(cont_perro.get())+int(numperro.get()))
		else:
			messagebox.showinfo(message="GANO "+tc.get(), title="gana")
			celebra_gato()
			cont_gato.set(int(cont_gato.get())+int(numgato.get()))
		cierra()
	## diagonal
	if (b1.get() == b5.get() and b1.get() == b9.get()):
		if b1.get() == "P":
			messagebox.showinfo(message="GANO "+bn.get(), title="gana")
			celebra_perro()
			cont_perro.set(int(cont_perro.get())+int(numperro.get()))
		else:
			messagebox.showinfo(message="GANO "+tc.get(), title="gana")
			celebra_gato()
			cont_gato.set(int(cont_gato.get())+int(numgato.get()))
		cierra()
	##diagonal
	if (b3.get() == b5.get() and b3.get() == b7.get()):
		if b3.get() == "P":
			messagebox.showinfo(message="GANO "+bn.get(), title="gana")
			celebra_perro()
			cont_perro.set(int(cont_perro.get())+int(numperro.get()))
		else:
			messagebox.showinfo(message="GANO "+tc.get(), title="gana")
			celebra_gato()
			cont_gato.set(int(cont_gato.get())+int(numgato.get()))
		cierra()
	elif cont_empate.get()=="0":
		messagebox.showinfo(message="empate ", title="gana")
		celebra_empate()
		
##sustitulle las imagenes del gato y el perro
def bot1():
	if turno.get()=="P":
		boton1.config(image=perro2)
		boton1.config(state=DISABLED)
		turno.set("G")
		b1.set("P")
	else:
		boton1.config(image=gato1)
		boton1.config(state=DISABLED)
		turno.set("P")
		b1.set("G")
	cont_empate.set(int(cont_empate.get())-int(numero.get()))
	ganador()
##sustitulle las imagenes del gato y el perro
def bot2():
	if turno.get()=="P":
		boton2.config(image=perro2)
		boton2.config(state=DISABLED)
		turno.set("G")
		b2.set("P")
	else:
		boton2.config(image=gato1)
		boton2.config(state=DISABLED)
		turno.set("P")
		b2.set("G")
	cont_empate.set(int(cont_empate.get())-int(numero.get()))
	ganador()
##sustitulle las imagenes del gato y el perro
def bot3():
	if turno.get()=="P":
		boton3.config(image=perro2)
		boton3.config(state=DISABLED)
		turno.set("G")
		b3.set("P")
	else:
		boton3.config(image=gato1)
		boton3.config(state=DISABLED)
		turno.set("P")
		b3.set("G")
	cont_empate.set(int(cont_empate.get())-int(numero.get()))
	ganador()
##sustitulle las imagenes del gato y el perro
def bot4():
	if turno.get()=="P":
		boton4.config(image=perro2)
		boton4.config(state=DISABLED)
		turno.set("G")
		b4.set("P")
	else:
		boton4.config(image=gato1)
		boton4.config(state=DISABLED)
		turno.set("P")
		b4.set("G")
	cont_empate.set(int(cont_empate.get())-int(numero.get()))
	ganador()
##sustitulle las imagenes del gato y el perro
def bot5():
	if turno.get()=="P":
		boton5.config(image=perro2)
		boton5.config(state=DISABLED)
		turno.set("G")
		b5.set("P")
	else:
		boton5.config(image=gato1)
		boton5.config(state=DISABLED)
		turno.set("P")
		b5.set("G")
	cont_empate.set(int(cont_empate.get())-int(numero.get()))
	ganador()
##sustitulle las imagenes del gato y el perro
def bot6():
	if turno.get()=="P":
		boton6.config(image=perro2)
		boton6.config(state=DISABLED)
		turno.set("G")
		b6.set("P")
	else:
		boton6.config(image=gato1)
		boton6.config(state=DISABLED)
		turno.set("P")
		b6.set("G")
	cont_empate.set(int(cont_empate.get())-int(numero.get()))
	ganador()
##sustitulle las imagenes del gato y el perro
def bot7():
	if turno.get()=="P":
		boton7.config(image=perro2)
		boton7.config(state=DISABLED)
		turno.set("G")
		b7.set("P")
	else:
		boton7.config(image=gato1)
		boton7.config(state=DISABLED)
		turno.set("P")
		b7.set("G")
	cont_empate.set(int(cont_empate.get())-int(numero.get()))
	ganador()
##sustitulle las imagenes del gato y el perro
def bot8():
	if turno.get()=="P":
		boton8.config(image=perro2)
		boton8.config(state=DISABLED)
		turno.set("G")
		b8.set("P")
	else:
		boton8.config(image=gato1)
		boton8.config(state=DISABLED)
		turno.set("P")
		b8.set("G")
	cont_empate.set(int(cont_empate.get())-int(numero.get()))
	ganador()
##sustitulle las imagenes del gato y el perro
def bot9():
	if turno.get()=="P":
		boton9.config(image=perro2)
		boton9.config(state=DISABLED)
		turno.set("G")
		b9.set("P")
	else:
		boton9.config(image=gato1)
		boton9.config(state=DISABLED)
		turno.set("P")
		b9.set("G")
	cont_empate.set(int(cont_empate.get())-int(numero.get()))
	ganador()
##Inhabilita los botones
def cierra():
	boton1.config(state=DISABLED)
	boton2.config(state=DISABLED)
	boton3.config(state=DISABLED)
	boton4.config(state=DISABLED)
	boton5.config(state=DISABLED)
	boton6.config(state=DISABLED)
	boton7.config(state=DISABLED)
	boton8.config(state=DISABLED)
	boton9.config(state=DISABLED)

def nuevo_jugador():
	tc.config(state=NORMAL)
	bn.config(state=NORMAL)

##Crea un nuevo juego
def nuevo():
	boton1.config(state=NORMAL)
	boton2.config(state=NORMAL)
	boton3.config(state=NORMAL)
	boton4.config(state=NORMAL)
	boton5.config(state=NORMAL)
	boton6.config(state=NORMAL)
	boton7.config(state=NORMAL)
	boton8.config(state=NORMAL)
	boton9.config(state=NORMAL)

	boton1.config(bg="white")
	boton2.config(bg="white")
	boton3.config(bg="white")
	boton4.config(bg="white")
	boton5.config(bg="white")
	boton6.config(bg="white")
	boton7.config(bg="white")
	boton8.config(bg="white")
	boton9.config(bg="white")
##pone la imagen de fondo cuando se reinicia el juego
	boton1.config(image=hola)
	boton2.config(image=hola)
	boton3.config(image=hola)
	boton4.config(image=hola)
	boton5.config(image=hola)
	boton6.config(image=hola)
	boton7.config(image=hola)
	boton8.config(image=hola)
	boton9.config(image=hola)

	b1.set("1")
	b2.set("2")
	b3.set("3")
	b4.set("4")
	b5.set("5")
	b6.set("6")
	b7.set("7")
	b8.set("8")
	b9.set("9")
    ##Pone valores iniciales del turno y del mensaje
	turno.set("P")
	mensaje.set(" ")

    ##Pone los valores iniciales del empate
	cont_empate.set("9")
	numero.set("1")

##Reinicia los contadores
def nuevo_cont():
	cont_perro.set("0")
	numperro.set("1")
	cont_gato.set("0")
	numgato.set("1")
##pone el gif cuando gana el gato
def celebra_gato():
	img=[PhotoImage(file="./gato bailarin/gar1.gif")]
	img.append(PhotoImage(file="./gato bailarin/gar2.gif"))
	img.append(PhotoImage(file="./gato bailarin/gar1.gif"))
	img.append(PhotoImage(file="./gato bailarin/gar2.gif"))
	img.append(PhotoImage(file="./gato bailarin/gar1.gif"))
	img.append(PhotoImage(file="./gato bailarin/gar2.gif"))
	img.append(PhotoImage(file="./gato bailarin/gar1.gif"))
	img.append(PhotoImage(file="./gato bailarin/gar2.gif"))
	img.append(PhotoImage(file="./gato bailarin/gar1.gif"))
	img.append(PhotoImage(file="./gato bailarin/gar2.gif"))
	for a in range(0,10):
		imagen.config(image=img[a])
		gato.update()
		sleep(.2)
	imagen.config(image=extra)
	gato.update()
##pone el gif cuando gana el perro
def celebra_perro():
	img1=[PhotoImage(file="./perro bailarin/odi1.gif")]
	img1.append(PhotoImage(file="./perro bailarin/odi2.gif"))
	img1.append(PhotoImage(file="./perro bailarin/odi3.gif"))
	img1.append(PhotoImage(file="./perro bailarin/odi4.gif"))
	img1.append(PhotoImage(file="./perro bailarin/odi1.gif"))
	img1.append(PhotoImage(file="./perro bailarin/odi2.gif"))
	img1.append(PhotoImage(file="./perro bailarin/odi3.gif"))
	img1.append(PhotoImage(file="./perro bailarin/odi4.gif"))
	img1.append(PhotoImage(file="./perro bailarin/odi1.gif"))
	img1.append(PhotoImage(file="./perro bailarin/odi2.gif"))
	img1.append(PhotoImage(file="./perro bailarin/odi3.gif"))
	img1.append(PhotoImage(file="./perro bailarin/odi4.gif"))
	for a in range(0,12):
		imagen1.config(image=img1[a])
		gato.update()
		sleep(.2)
	imagen1.config(image=extra)
	gato.update()
##pone el gif cuando nadie gana 
def celebra_empate():
	img2=[PhotoImage(file="./empate bailarin/emp1.gif")]
	img2.append(PhotoImage(file="./empate bailarin/emp2.gif"))
	img2.append(PhotoImage(file="./empate bailarin/emp1.gif"))
	img2.append(PhotoImage(file="./empate bailarin/emp2.gif"))
	img2.append(PhotoImage(file="./empate bailarin/emp1.gif"))
	img2.append(PhotoImage(file="./empate bailarin/emp2.gif"))
	img2.append(PhotoImage(file="./empate bailarin/emp1.gif"))
	img2.append(PhotoImage(file="./empate bailarin/emp2.gif"))

	for a in range(0,6):
		imagen2.config(image=img2[a])
		gato.update()
		sleep(.2)
	imagen2.config(image=extra)
	gato.update()

def lista_usuarios():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='test')
	cursor=conn.cursor()
	cursor.execute('select Nom_usuario from usuarios')
	tcs = []
	for row in cursor:
		tcs.append(row)
	cursor.close
	conn.close()
	return tcs

def nuevo_usuario():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='test')
	cursor=conn.cursor()
	sql= 'insert into usuarios(Nom_usuario)values(%s)'
	datos=str(str_nombre.get())
	cursor.execute(sql, datos)
	conn.commit()
	cursor.close()
	conn.close()
	lista = lista_usuarios()
	tc['values'] = lista
	bn['values'] = lista

def marcador_usuario():
	global ganador
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='test')
	cursor1=conn.cursor()
	sql = 'update usuarios set puntos=puntos+1 where nom_usuario'
	datos=ganador
	cursor1.execute(sql, datos)
	conn.commit
	cursor1.close()
	conn.close()

def ventana():
	##pone le diseño de la nueva ventana 
	gato1=Tk()
	gato1.resizable(1,1)
	gato1.title("ventanita")
	gato1.geometry("500x500")
	gato1.config(bg="dark turquoise")

	##pone el boton
	ven=Button(gato1, text="insertar" , font = 'Helectiva 18 bold').place(x=1 , y=200)

	##pone las etiquetas
	ventanita=Label(gato1, bg="dark turquoise" ,text="id_usuario" , font = 'Helectiva 18 bold').place(x=1 , y=1)
	ventanita2=Label(gato1, bg="dark turquoise" , text="nom_usuario" , font = 'Helectiva 18 bold').place(x=1 , y=50)
	ventanita3=Label(gato1, bg="dark turquoise" , text="puntos" , font = 'Helectiva 18 bold').place(x=1 , y=100)
    
    ##pone las cajas de texto
	vent=Label(gato1, font = 'Helectiva 18 bold',state=DISABLED,text="0", width=10)
	vent.place(x=150 , y=1)
	vent1=Entry(gato1, font = 'Helectiva 18 bold',  width=10)
	vent1.place(x=180 , y=50)
	vent2=Label(gato1,font = 'Helectiva 18 bold',state=DISABLED,text="0", width=10)
	vent2.place(x=130 , y=100)

##pone los combobox 
bn=ttk.Combobox(gato)
bn.place(x=250 , y=100)
contadorperro=Label(gato, bg="red" , text="0" , font = 'Helectiva 18 bold' , width=3 , textvariable=cont_perro).place(x=250 , y=135)
##pone los combobox 
tc=ttk.Combobox(gato)
tc.place(x=400, y=100)
contadorgato=Label(gato, bg="red" , text="0" , font = 'Helectiva 18 bold' , width=3 , textvariable=cont_gato).place(x=400 , y=135)



##se crean etiquetas para el turno
etiqueta1=Label(gato, bg="red" , text="TURNO" , font='Helectiva 18 bold').place(x=360 , y=10)
etiquetaxd=Label(gato, bg="red" , font='Helectiva 16 bold' , width=3 , textvariable=turno).place(x=379 , y=50)
##reinicia los contadores
reiniciarjuego=Button(gato, command=nuevo , bg="lavender" , text="Nuevo Juego" , font = 'Helectiva 18 bold').place(x=43 , y=270)
##reinicia los botones
reiniciar1=Button(gato, command=nuevo_cont, bg="lavender" , text="Reiniciar contadores" , font = 'Helectiva 18 bold').place(x=280 , y=190)
##reinicia los jugadores 
reiniciaj=Button(gato, command=nuevo_jugador, bg="lavender" , text="Reiniciar jugadores" , font = 'Helectiva 18 bold').place(x=285 , y=270)
##pone una nueva ventana 
ventana=Button(gato, command=ventana, bg="lavender" , text="ventana" , font = 'Helectiva 18 bold').place(x=350 , y=350)



##pone las imagenes de fondo en cada boton 
boton1=Button(gato, command=bot1 , image=hola , relief="flat" , textvariable=b1)
boton1.place(x=20 , y=20)

boton2=Button(gato, command=bot2 , image=hola , relief="flat" , textvariable=b2)
boton2.place(x=95 , y=20)

boton3=Button(gato, command=bot3 , image=hola , relief="flat" , textvariable=b3)
boton3.place(x=170 , y=20)

boton4=Button(gato, command=bot4 , image=hola, relief="flat" , textvariable=b4)
boton4.place(x=20 , y=90)

boton5=Button(gato, command=bot5 , image=hola , relief="flat" , textvariable=b5)
boton5.place(x=95 , y=90)

boton6=Button(gato, command=bot6 , image=hola , relief="flat" , textvariable=b6)
boton6.place(x=170 , y=90)

boton7=Button(gato, command=bot7 , image=hola , relief="flat" , textvariable=b7)
boton7.place(x=20 , y=160)

boton8=Button(gato, command=bot8 , image=hola , relief="flat" , textvariable=b8)
boton8.place(x=95 , y=160)

boton9=Button(gato, command=bot9 , image=hola , relief="flat" , textvariable=b9)
boton9.place(x=170 , y=160)

imagen1=Label(gato, image=extra)
imagen1.place(x=1,y=1)
imagen=Label(gato, image=extra)
imagen.place(x=1,y=1)
imagen2=Label(gato, image=extra)
imagen2.place(x=1,y=1)


for row in cursor:
	tcs.append(row)

cursor.close()
conn.close()
tc['values']=tcs
bn['values']=tcs
tc.bind("<<ComboboxSelected>>",nombre1)
bn.bind("<<ComboboxSelected>>",nombre2)

gato.mainloop()