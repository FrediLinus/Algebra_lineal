import tkinter as tk

ventana = tk.Tk()
ventana.title("Proyecto Álgebra Digital")
ventana.geometry("800x700")

#Título
titulo = tk.Label(ventana, text="ALGEBRA DIGITAL", font=("Arial", 18))
titulo.pack(pady=20)

#Logica suma vectores

def calcular_suma_vectores(entry_a, entry_b, resultado):
    try:
        # Convertir texto a lista de números
        vector_a = list(map(float, entry_a.get().split(",")))
        vector_b = list(map(float, entry_b.get().split(",")))
        suma = []
        if len(vector_a) != 2 or len(vector_b) != 2:
            resultado.config(text="Error: ingresa solo 2 valores en cada vector")
        # Sumar vectores
        for a,b in zip(vector_a,vector_b):
            suma.append(a+b)


        resultado.config(text=f"Resultado: \n x - y \n {suma}")

    except:
        resultado.config(text="Error: revisa los datos")

#logica restaq vectores
def calcular_resta_vectores(entry_a,entry_b,resultado):
    try:
        vector_a = list(map(float, entry_a.get().split(",")))
        vector_b = list(map(float, entry_b.get().split(",")))
        resta = []
        if len(vector_a) != 2 or len(vector_b) != 2:
            resultado.config(text="Error: ingresa solo 2 valores en cada vector")
        for a,b in zip(vector_a,vector_b):
            resta.append(a-b)
        resultado.config(text=f"Resultado: \n x - y \n {resta}")

    except:
        resultado.config(text="Error: revisa los datos")


#logica producto punto
def calcular_producto_punto_vectores(entry_a,entry_b, resultado):
    try:
        vector_a = list(map(float,entry_a.get().split(",")))
        vector_b = list(map(float,entry_b.get().split(",")))

        producto = []
        producto_punto = 0
        if len(vector_a ) != 3 or len(vector_b) != 3 :
            resultado.config(text="Error: ingresa solo 3 valores en cada vector")

        for a,b in zip(vector_a,vector_b):
            producto.append(a*b)

        for a in producto:
            producto_punto += a
        resultado.config(text=f"Resultado: \n x - y \n {producto_punto}")
        
    except:
        resultado.config(text="Error, revisa los datos")

# LOGICAS DEL SEGUNDO TEMA 

#Logica de 2x2
"""
def calcular_ecuacion_2x2(entry_a,entry_b,entry_c,resultado):
    try:
        valor_x = float(entry_a.get())
        valor_y = float(entry_b.get())
        valor_r = float(entry_c.get())

        multiplicacion =  

"""
#Funciones primer tema
def abrir_vectores():
    ventana_vectores = tk.Toplevel()
    ventana_vectores.title("Vectores")
    ventana_vectores.geometry("600x500")

    titulo = tk.Label(ventana_vectores, text="Operaciones con vectores", font=("Arial", 14))
    titulo.pack(pady=20)

    #Sub menus 

    #Boton 1 
    btn_suma = tk.Button(ventana_vectores, text="Suma de vectores", command= abrir_suma_vectores)
    btn_suma.pack(pady=10)

    #Boton 2r.ap
    btn_resta = tk.Button(ventana_vectores, text="Resta de vectores",command= abrir_resta_vectores)
    btn_resta.pack(pady=10)

    #Boton 3
    btn_producto = tk.Button(ventana_vectores, text="Producto punto", command= abrir_punto_vectores)
    btn_producto.pack(pady=10)



def abrir_suma_vectores():
    ventana_vectores_suma = tk.Toplevel()
    ventana_vectores_suma.title("Suma Vectores")
    ventana_vectores_suma.geometry("600x500")

    titulo = tk.Label(ventana_vectores_suma, text="Operaciones con vectores suma", font=("Arial", 14))
    titulo.pack(pady=20)

    # Vector A
    label_a = tk.Label(ventana_vectores_suma, text="Vector A (ej: 1,2,3):")
    label_a.pack()
    entry_a = tk.Entry(ventana_vectores_suma)
    entry_a.pack()

    # Vector B
    label_b = tk.Label(ventana_vectores_suma, text="Vector B (ej: 4,5,6):")
    label_b.pack()
    entry_b = tk.Entry(ventana_vectores_suma)
    entry_b.pack()

    # Resultado
    resultado = tk.Label(ventana_vectores_suma, text="Resultado: ")
    resultado.pack(pady=10)

    # Botón calcular
    btn_calcular = tk.Button(
        ventana_vectores_suma,
        text="Calcular",
        command=lambda: calcular_suma_vectores(entry_a, entry_b, resultado)
    )
    btn_calcular.pack(pady=10)


def abrir_resta_vectores():
    ventana_vectores_resta = tk.Toplevel()
    ventana_vectores_resta.title("Resta de Vectores")
    ventana_vectores_resta.geometry("600x500")

    titulo = tk.Label(ventana_vectores_resta, text="Operaciones con vectores resta1", font=("Arial", 14))
    titulo.pack(pady=20)

    #bector A
    label_a = tk.Label(ventana_vectores_resta, text="Vector A (ej: 1,2,3):")
    label_a.pack()
    entry_a = tk.Entry(ventana_vectores_resta)
    entry_a.pack()

    #vector B
    label_b = tk.Label(ventana_vectores_resta, text = "Vector B (ej: 1,2,3):")
    label_b.pack()
    entry_b = tk.Entry(ventana_vectores_resta,text = "Vector B (ej: 1,2,3):")
    entry_b.pack()

    #res
    resultado = tk.Label(ventana_vectores_resta, text="Resultado:")
    resultado.pack(pady=10)

    btn_calcular = tk.Button(
        ventana_vectores_resta,
        text="Calcular",
        command=lambda: calcular_resta_vectores(entry_a, entry_b, resultado)
    )
    btn_calcular.pack(pady=10)



def abrir_punto_vectores():
    ventana_vectores_punto = tk.Toplevel()
    ventana_vectores_punto.title("Punto Vectores")
    ventana_vectores_punto.geometry("600x500")

    titulo = tk.Label(ventana_vectores_punto, text="Operaciones con vectores punto", font=("Arial", 14))
    titulo.pack(pady=20)

    #bector A
    label_a = tk.Label(ventana_vectores_punto, text="Vector A (ej: 1,2,3):")
    label_a.pack()
    entry_a = tk.Entry(ventana_vectores_punto)
    entry_a.pack()

    #vector b
    label_b = tk.Label(ventana_vectores_punto,text="Vector B (ej: 1,2,3):")
    label_b.pack()
    entry_b = tk.Entry(ventana_vectores_punto)
    entry_b.pack()

    resultado = tk.Label(ventana_vectores_punto, text="Resultado: ")
    resultado.pack(pady=10)
    btn_calcular = tk.Button(
        ventana_vectores_punto,
        text =" calcular",
        command=lambda:calcular_producto_punto_vectores(entry_a, entry_b, resultado)
    )
    btn_calcular.pack(pady=10)

#Funciones segundo tema

def abrir_resolucion_ecuaciones():
    ventana_resolucion_ecuaciones = tk.Toplevel()
    ventana_resolucion_ecuaciones.title("Ecuaciones")
    ventana_resolucion_ecuaciones.geometry("600x500")

    titulo = tk.Label(ventana_resolucion_ecuaciones, text = "Operaciones con Ecuaciones", font=("Arial", 14))
    titulo.pack(pady=20)

    #BTNs news 
    btn_2x2 = tk.Button(ventana_resolucion_ecuaciones, text="Ecuaciones 2x2", command= abrir_ecuaciones2X2)
    btn_2x2.pack(pady=10)

    btn_3x3 = tk.Button(ventana_resolucion_ecuaciones, text= "Ecuaciones 3x3",command= abrir_ecuaciones3X3)
    btn_3x3.pack(pady=10)

def abrir_ecuaciones2X2():
    ventana_ecuaciones_2X2 = tk.Toplevel()
    ventana_ecuaciones_2X2.title("Ecuaciones 2x2")
    ventana_ecuaciones_2X2.geometry("600x500")
    
    titulo = tk.Label(ventana_ecuaciones_2X2, text = "Ecuaciones 2x2 realizar", font=( "Arial",14))
    titulo.pack(pady=20)

    # X
    label_x = tk.Label(ventana_ecuaciones_2X2, text="Ingrese valor de X")
    label_x.pack()
    entry_x = tk.Entry(ventana_ecuaciones_2X2)
    entry_x.pack()

    # Y
    label_y = tk.Label(ventana_ecuaciones_2X2, text="Ingrese valor de Y")
    label_y.pack()
    entry_y = tk.Entry(ventana_ecuaciones_2X2)
    entry_y.pack()

    # Resultado
    label_r = tk.Label(ventana_ecuaciones_2X2, text="Ingrese valor del resultado")
    label_r.pack()
    entry_r = tk.Entry(ventana_ecuaciones_2X2)
    entry_r.pack()

    resultado = tk.Label(ventana_ecuaciones_2X2, text="Resultado: ")
    resultado.pack(pady=10)
    btn_calcular = tk.Button(
        ventana_ecuaciones_2X2,
        text =" calcular ecuacion",
        command=lambda:calcular_producto_punto_vectores(entry_x, entry_y,entry_r, resultado)
    ) 
    btn_calcular.pack(pady=10)


def abrir_ecuaciones3X3():
    ventana_ecuaciones_3x3 = tk.Toplevel()
    ventana_ecuaciones_3x3.title("Ecuaciones 3x3")
    ventana_ecuaciones_3x3.geometry("600x500")

    titulo = tk.Label(ventana_ecuaciones_3x3,text="Ecuaciones 3x3 Realizar", font=("Arial, 14"))
    titulo.pack(pady=20)



#Funciones tercer tema a usar
def abrir_algebra_matrices():
    ventana_resolucion_algebra = tk.Toplevel()
    ventana_resolucion_algebra.title("Ecuaciones Matrices Algebra")
    ventana_resolucion_algebra.geometry("600x500")

    titulo = tk.Label(ventana_resolucion_algebra,text= "Operaciones de Algebra", font =( "Arial", 13) )
    titulo.pack(pady=20)


    #BTNs news
    btn_suma = tk.Button(ventana_resolucion_algebra,text = "matriz Suma", command=abrir_suma)
    btn_suma.pack(pady=20)

    btn_resta = tk.Button(ventana_resolucion_algebra, text = " Matriz resta", command=abrir_resta)
    btn_resta.pack(pady=20)

    btn_producto = tk.Button(ventana_resolucion_algebra, text = " Matriz producto", command=abrir_producto)
    btn_producto.pack(pady=20)


def abrir_suma():
    ventana_suma_matrices = tk.Toplevel()
    ventana_suma_matrices.title(" Matriz Suma")
    ventana_suma_matrices.geometry("600x500")


    titulo = tk.Label(ventana_suma_matrices,text="Matricez Suma a realizar ",font= ("Arial",14))
    titulo.pack(pady=20)

def abrir_resta():
    ventana_resta_matrices = tk.Toplevel()
    ventana_resta_matrices.title("Matriz Resta")
    ventana_resta_matrices.geometry("600x500")

    titulo = tk.Label(ventana_resta_matrices, text="Matricez Resta a realizar", font=("Arial",14 ))
    titulo.pack(pady=20)


def abrir_producto():
    ventana_producto_matricez = tk.Toplevel()
    ventana_producto_matricez.title("Matriz Producto")
    ventana_producto_matricez.geometry("600x500")

    titulo = tk.Label(ventana_producto_matricez,text="Matrices producto a realizar", font=("Arial",14))
    titulo.pack(pady=20)





#Funciones cuarto tema a usar
def abrir_matriz_inversa():
    ventana_matriz_inversa = tk.Toplevel()
    ventana_matriz_inversa.title("Matrices Inversas")
    ventana_matriz_inversa.geometry("600x500")

    titulo = tk.Label(ventana_matriz_inversa,text="Operaciones de Matrices Inversas", font=("Arial",14 ))
    titulo.pack(pady=20)

    #BTNs news
    btn_inversa_2x2 = tk.Button(ventana_matriz_inversa,text = "matriz Invrsa 2x2", command=abrir_inversa_2x2)
    btn_inversa_2x2.pack(pady=20)

    btn_inversa_3x3 = tk.Button(ventana_matriz_inversa, text="Matriz Inversa 3x3",command=abrir_inversa_3x3)
    btn_inversa_3x3.pack(pady=20)


def abrir_inversa_2x2():
    ventana_inversa_2x2 = tk.Toplevel()
    ventana_inversa_2x2.title("Inversa 2x2")
    ventana_inversa_2x2.geometry("600x500")

    titulo = tk.Label(ventana_inversa_2x2,text="Ingreso matriz inversa 2x2",font=("Arial",14))
    titulo.pack(pady=20)


def abrir_inversa_3x3():
    ventana_inversa_3x3 = tk.Toplevel()
    ventana_inversa_3x3.title(" Inversa 3x3")
    ventana_inversa_3x3.geometry("600x500")

    titulo = tk.Label(ventana_inversa_3x3,text="INgreso matriz inversa 3x3", font=("Arial",14))
    titulo.pack(pady=20)


#BOTONES INICIALES DE MENU PRINCIPAL


# Boton 1
btn_vectores = tk.Button(ventana, text="Operaciones con vectores", command=abrir_vectores)
btn_vectores.pack(pady=10)

# Boton 2
btn_resolucion_ecuaciones = tk.Button(ventana,text = "Resolucion de ecuaciones", command=abrir_resolucion_ecuaciones)
btn_resolucion_ecuaciones.pack(pady=10)


#Boton 3 
btn_algebra_matrices = tk.Button(ventana, text="Álgebra de matrices",command=abrir_algebra_matrices)
btn_algebra_matrices.pack(pady=10)

#Boton 4
btn_matrices_inversas = tk.Button(ventana, text="Matrizes inversas", command=abrir_matriz_inversa)
btn_matrices_inversas.pack(pady=10)







ventana.mainloop() #siempre va de ultimo 