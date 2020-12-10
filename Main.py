import tkinter as tk
from tkinter import filedialog as f
from tkinter import messagebox as mb
from tkinter.colorchooser import askcolor
from io import open

font= "Calibri"
tamaño = "12"
titleName =("Nuevo Documento"+".jmc")
colorType= "#000000"
colorTypeAct = colorType
ColorFondo = "#ffffff"
colorFondoAct = ColorFondo
url_file = ""

ventanaTamañoAct = False
ventanaAct = False
titleVarAct = False

def tamaño_letra():
    global ventanaTamañoAct
    def cambio(x):
        global texto, font, tamaño, ventanaTamañoAct
        texto.config(font=(font, x))
        tamaño = x
        ventanaTamañoAct = False
        ventanaTamaño.destroy()
    ventanaTamaño = tk.Tk()
    ventanaTamañoAct = ventanaTamaño
    ventanaTamaño.resizable(False, False)
    ventanaTamaño.title("Tamaño de la letra")
    ventanaTamaño.geometry("500x200")
    
    title = tk.Label(ventanaTamaño, text="Elija el Tamaño de la Letra:", font=("Calibri", 15))
    title.pack()
    
    tamaño= tk.Entry(ventanaTamaño, width=15)
    tamaño.place(x=200, y=100)
    
    changeButton = tk.Button(ventanaTamaño, bg="green", fg="white", text="Cambiar", font=("Calibri", 10), command= lambda: cambio(tamaño.get()))
    changeButton.place(x=215, y=150)
    
    
def tipo_letra():
    global ventanaAct
    ventana = tk.Tk()
    ventanaAct = ventana
    ventana.title("Tipo de Letra")
    ventana.geometry("500x200")
    ventana.resizable(False, False)
    
    def cambio(x):
        global texto, font, tamaño, ventanaAct
        texto.config(font=(x, tamaño))
        font= x
        ventanaAct = False
        ventana.destroy()
    
    
    title = tk.Label(ventana, text="Tipos de letra", font=("Calibri", 15))
    title.pack()

    
    arialButton = tk.Button(ventana, text="Arial", bg="green", fg="white", font=("Arial", 10), width="10", command= lambda: cambio("Arial"))
    arialButton.place(x=10, y=50)
    
    calibriButton = tk.Button(ventana, text="Calibri", bg="green", fg="white", font=("Calibri", 10), width="10", command= lambda: cambio("Calibri"))
    calibriButton.place(x=125, y=50)
    
    comicButton = tk.Button(ventana, text="Comic Sans", bg="green", fg="white", font=("Comic Sans MS", 9), width="10", command= lambda: cambio("Comic Sans MS"))
    comicButton.place(x=235, y=50)
    
    georgiaButton = tk.Button(ventana, text="Georgia", bg="green", fg="white", font=("Georgia", 10), width="10", command= lambda: cambio("Georgia"))
    georgiaButton.place(x=345, y=50)
    
    romanButton = tk.Button(ventana, text="Times New Roman", bg="green", fg="white", font=("Arial", 10), width="20", command= lambda: cambio("Times New Roman"))
    romanButton.place(x=167, y=100)


def finish():
    root.destroy()
        
def closeVerify():
   if mb.askyesno(message="¿Desea salir? Perderá los datos que no haya guardado.", title="Salir", default="no"):
       finish()
   else:
       pass

def newVerify():
   if mb.askyesno(message="¿Desea abrir un nuevo documento? Perderá los datos que no haya guardado.", title="Nuevo Documento", default="no"):
       nuevoArchivo()
   else:
       pass

def abrir():
    global url_file, tamaño, font, colorType, ColorFondo
    
    url_file = f.askopenfilename(initialdir = ".", filetype = ((
            "Archivo de Texto","*.jmc" 
            ),), title = "Abrir archivo/")
    if url_file != "":
        file = open(url_file,"r")
        contenido = file.read()
        texto.delete(1.0,"end")
        partes=contenido.split(":cutdownIntoSpace:")
        texto.insert("insert",partes[4])
        font=partes[0]
        tamaño=partes[1]
        colorType=partes[2]
        ColorFondo=partes[3]
        texto.config(font=(partes[0], partes[1]), fg=partes[2], bg=partes[3])
        root.geometry(partes[5])
        file.close()
        root.title(url_file)
    
def guardar():
    global url_file, tamaño, font, colorType, ColorFondo, colorFondoAct
    if url_file != "":
        file = open(url_file,"w+")
        contenido=texto.get(1.0, "end")
        file.write(font)
        file.write(":cutdownIntoSpace:")
        file.write(tamaño)
        file.write(":cutdownIntoSpace:")
        if colorType == None:
            colorType = "#000000"
        file.write(colorType)
        file.write(":cutdownIntoSpace:")
        if ColorFondo == None:
            ColorFondo = "#ffffff"
        file.write(ColorFondo)
        file.write(":cutdownIntoSpace:")
        file.write(contenido)    
        file.write(":cutdownIntoSpace:")
        file.write(root.geometry())   
        root.title("Archivo guardado " + url_file)
        file.close()
        
    else:
        file =f.asksaveasfile(title = "Save file", mode = "w", defaultextension = ".jmc")
        if file is not None:
            url_file = file.name
            file = open(url_file,"w+")
            contenido=texto.get(1.0, "end")
            file.write(font)
            file.write(":cutdownIntoSpace:")
            file.write(tamaño)
            file.write(":cutdownIntoSpace:")
            if colorType == None:
                colorType = "#000000"
            file.write(colorType)
            file.write(":cutdownIntoSpace:")
            file.write(ColorFondo)
            file.write(":cutdownIntoSpace:")
            file.write(contenido)     
            file.write(":cutdownIntoSpace:")
            file.write(root.geometry()) 
            root.title("Archivo guardado " + url_file)
            file.close()
        else:
            url_file = ""
            root.title("No hay nada que guardar "+url_file)

    

def change_title():
    global titleName, titleVarAct
    titleVar = tk.Tk()
    titleVarAct = titleVar
    titleVar.title("Cambiar Nombre del documento")
    titleVar.geometry("500x250")
    titleVar.resizable(False, False)
    
    def change():
        global titleName, titleVarAct
        titleName = nombre.get()
        root.title(titleName+".jmc")
        titleVarAct = False
        titleVar.destroy()
    
    pres = tk.Label(titleVar, text="Cambiar el nombre del documento", font=("Georgia", 15))
    pres.pack()
    
    actual = tk.Label(titleVar, text=("Nombre Actual: "+titleName), font=("Calibri", 15))
    actual.place(x= 50, y=70)
    
    nuevoNombre = tk.Label(titleVar, text="Nuevo Nombre:", font=("Calibri", 15))
    nuevoNombre.place(x=50, y= 130)
    
    nombre = tk.Entry(titleVar, width=20)
    nombre.place(x=195, y=137)
    cambiar = tk.Button(titleVar, text="Cambiar", bg="green", fg="white", font=("Calibri", 10), width=15, command=change)
    cambiar.place(x=145, y=175)

def nuevoArchivo():
    global url_file, font, tamaño, colorType, ColorFondo
    url_file = "Nuevo archivo/"
    texto.delete(1.0,"end")
    url_file = ""
    font= "Calibri"
    tamaño = "12"
    titleName =("Nuevo Documento"+".jmc")
    colorType= "black"
    ColorFondo = "white"
    texto.config(font=(font, tamaño), fg=colorType, bg=ColorFondo)
    root.title(titleName)
    
def colorFont():
    global colorType, colorTypeAct
    result = askcolor(color=colorType, 
                      title = "Color del texto") 
    colorType=(result[1])
    texto.config(fg=colorType)
    if colorType != None:
        colorTypeAct = colorType
    else: 
        colorType = colorTypeAct

    
def colorFondo():
    global ColorFondo, colorFondoAct
    result = askcolor(color=ColorFondo, 
                      title = "Color del fondo") 
    ColorFondo=(result[1])
    texto.config(bg=ColorFondo)
    if ColorFondo != None:
        colorFondoAct = ColorFondo
    else: 
        ColorFondo = colorFondoAct
    
    
# Root
root = tk.Tk()
root.title(titleName)
root.iconbitmap("blocIcon.ico")
root.geometry("900x550")

# Texto

texto = tk.Text(root)

scroll = tk.Scrollbar(root, command = texto.yview)
scroll.pack(side="right", fill="y")

texto.config(font=(font, tamaño), fg=colorType, bg=ColorFondo, yscrollcommand = scroll.set)
texto.pack(side="left", fill="both", expand=1)
texto.config(bd = 0,padx = 6, pady = 5)


# Menu

menubar = tk.Menu(root)
root.config(menu = menubar)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo Archivo", command=newVerify)
filemenu.add_command(label="Guardar", command = guardar)
filemenu.add_command(label="Abrir", command = abrir)
filemenu.add_command(label="Nombre del documento", command = change_title)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=closeVerify)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Tamaño de letra", command=tamaño_letra)
editmenu.add_command(label="Tipos de letra", command=tipo_letra)
editmenu.add_command(label="Color del texto", command=colorFont)
editmenu.add_command(label="Color de fondo", command= colorFondo)

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)

root.mainloop()
