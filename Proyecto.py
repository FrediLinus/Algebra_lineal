import tkinter as tk
import numpy as np 

ventana = tk.Tk()
ventana.title("Proyecto Algebra Digital")
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
            return
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
            return
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
def calcular_2x2(a1, b1, c1, a2, b2, c2, resultado):
    try:
        a1 = float(a1.get())
        b1 = float(b1.get())
        c1 = float(c1.get())
        a2 = float(a2.get())
        b2 = float(b2.get())
        c2 = float(c2.get())

        det = a1*b2 - a2*b1

        if det == 0:
            resultado.config(text="No tiene solución única")
            return

        x = (c1*b2 - c2*b1) / det
        y = (a1*c2 - a2*c1) / det

        resultado.config(text=f"x = {x:.2f}, y = {y:.2f}")

    except:
        resultado.config(text="Error en datos")


#logica 3x3

def calcular_3x3(x1,y1,z1,r1,x2,y2,z2,r2,x3,y3,z3,r3,resultado):
    try:
        x1 = float(x1.get())
        y1 = float(y1.get())
        z1 = float(z1.get())
        x2 = float(x2.get())
        y2 = float(y2.get())
        z2 = float(z2.get())
        x3 = float(x3.get())
        y3 = float(y3.get())
        z3 = float(z3.get())
        r1 =float(r1.get())
        r2 =float(r2.get())
        r3 =float(r3.get())

        array = np.array([
            [x1,y1,z1],
            [x2,y2,z2],
            [x3,y3,z3]
        ])

        total = np.array([r1,r2,r3])
        solucion  = np.linalg.solve(array, total)

        resultado.config(text=f"x={solucion[0]:.2f}, y={solucion[1]:.2f}, z={solucion[2]:.2f}")

    except:
        resultado.config(text="Error: datos inválidos")

#generar matrices 

# GENERAR MATRICES Y SUMAR

def calcular_matriz_suma(
    entry_filas,
    entry_columnas,
    ventana_suma_matrices
):

    try:

        filas = int(entry_filas.get())
        columnas = int(entry_columnas.get())

        entradas_a = []
        entradas_b = []

        # ------------------------
        # MATRIZ A
        # ------------------------

        titulo_a = tk.Label(
            ventana_suma_matrices,
            text="Matriz A"
        )
        titulo_a.pack()

        frame_a = tk.Frame(ventana_suma_matrices)
        frame_a.pack(pady=10)

        for i in range(filas):

            fila_a = []

            for j in range(columnas):

                entrada_a = tk.Entry(
                    frame_a,
                    width=5
                )

                entrada_a.grid(
                    row=i,
                    column=j,
                    padx=5,
                    pady=5
                )

                fila_a.append(entrada_a)

            entradas_a.append(fila_a)

        # ------------------------
        # MATRIZ B
        # ------------------------

        titulo_b = tk.Label(
            ventana_suma_matrices,
            text="Matriz B"
        )
        titulo_b.pack()

        frame_b = tk.Frame(ventana_suma_matrices)
        frame_b.pack(pady=10)

        for i in range(filas):

            fila_b = []

            for j in range(columnas):

                entrada_b = tk.Entry(
                    frame_b,
                    width=5
                )

                entrada_b.grid(
                    row=i,
                    column=j,
                    padx=5,
                    pady=5
                )

                fila_b.append(entrada_b)

            entradas_b.append(fila_b)

        # ------------------------
        # RESULTADO
        # ------------------------

        resultado = tk.Label(
            ventana_suma_matrices,
            text="Resultado:"
        )

        resultado.pack(pady=10)

        # ------------------------
        # FUNCIÓN SUMAR
        # ------------------------

        def sumar():

            try:

                matriz_resultado = []

                for i in range(filas):

                    fila_resultado = []

                    for j in range(columnas):

                        valor_a = float(
                            entradas_a[i][j].get()
                        )

                        valor_b = float(
                            entradas_b[i][j].get()
                        )

                        suma = valor_a + valor_b

                        fila_resultado.append(suma)

                    matriz_resultado.append(
                        fila_resultado
                    )

                resultado.config(
                    text=f"Resultado:\n{matriz_resultado}"
                )

            except:

                resultado.config(
                    text="Error: revisa los datos"
                )

        # ------------------------
        # BOTÓN SUMAR
        # ------------------------

        btn_sumar = tk.Button(
            ventana_suma_matrices,
            text="Sumar matrices",
            command=sumar
        )

        btn_sumar.pack(pady=10)

    except:

        error = tk.Label(
            ventana_suma_matrices,
            text="Error en filas o columnas"
        )

        error.pack()


# ABRIR VENTANA SUMA MATRICES

def abrir_suma():

    ventana_suma_matrices = tk.Toplevel()

    ventana_suma_matrices.title("Matriz Suma")

    ventana_suma_matrices.geometry("600x500")

    titulo = tk.Label(
        ventana_suma_matrices,
        text="Matrices Suma a realizar",
        font=("Arial", 14)
    )

    titulo.pack(pady=20)

    # FILAS

    label_filas = tk.Label(
        ventana_suma_matrices,
        text="Numero de filas"
    )

    label_filas.pack()

    entry_filas = tk.Entry(
        ventana_suma_matrices
    )

    entry_filas.pack()

    # COLUMNAS

    label_columnas = tk.Label(
        ventana_suma_matrices,
        text="Numero de columnas"
    )

    label_columnas.pack()

    entry_columnas = tk.Entry(
        ventana_suma_matrices
    )

    entry_columnas.pack()

    # BOTÓN

    btn = tk.Button(
        ventana_suma_matrices,
        text="Generar matrices",
        command=lambda:
        calcular_matriz_suma(
            entry_filas,
            entry_columnas,
            ventana_suma_matrices
        )
    )

    btn.pack(pady=10)


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
    ventana = tk.Toplevel()
    ventana.title("Ecuaciones 2x2")
    ventana.geometry("600x500")

    titulo = tk.Label(ventana, text="Sistema de ecuaciones 2x2", font=("Arial",14))
    titulo.pack(pady=20)

    #ECUACIÓN 1
    tk.Label(ventana, text="Ecuación 1: x + y = r").pack()

    a1 = tk.Entry(ventana)
    a1.pack()
    b1 = tk.Entry(ventana)
    b1.pack()
    c1 = tk.Entry(ventana)
    c1.pack()

    #ECUACIÓN 2
    tk.Label(ventana, text="Ecuación 2: x + y = r").pack()

    a2 = tk.Entry(ventana)
    a2.pack()
    b2 = tk.Entry(ventana)
    b2.pack()
    c2 = tk.Entry(ventana)
    c2.pack()

    resultado = tk.Label(ventana, text="Resultado:")
    resultado.pack(pady=10)

    btn = tk.Button(
        ventana,
        text="Calcular",
        command=lambda: calcular_2x2(a1,b1,c1,a2,b2,c2,resultado)
    )
    btn.pack(pady=10)

def abrir_ecuaciones3X3():
    ventana_ecuaciones_3x3 = tk.Toplevel()
    ventana_ecuaciones_3x3.title("Ecuaciones 3x3")
    ventana_ecuaciones_3x3.geometry("600x500")

    titulo = tk.Label(ventana_ecuaciones_3x3,text="Ecuaciones 3x3 Realizar", font=("Arial, 14"))
    titulo.pack(pady=20)

    #Ecuacion1 
    ecuacion = tk.Label(ventana_ecuaciones_3x3, text="Ecuación 2: x + y = r")
    ecuacion.pack()

    x1 = tk.Entry(ventana_ecuaciones_3x3)
    x1.pack()
    y1 = tk.Entry(ventana_ecuaciones_3x3)
    y1.pack()
    z1 = tk.Entry(ventana_ecuaciones_3x3)
    z1.pack()
    r1 = tk.Entry(ventana_ecuaciones_3x3)
    r1.pack()

    #ecuacion 2
    ecuacion2 = tk.Label(ventana_ecuaciones_3x3, text="Ecuación 2: x + y = r")
    ecuacion2.pack()
    

    x2 = tk.Entry(ventana_ecuaciones_3x3)
    x2.pack()
    y2 = tk.Entry(ventana_ecuaciones_3x3)
    y2.pack()
    z2 = tk.Entry(ventana_ecuaciones_3x3)
    z2.pack()

    r2 = tk.Entry(ventana_ecuaciones_3x3)
    r2.pack()

    #ecuacion 3
    ecuacion3 = tk.Label(ventana_ecuaciones_3x3, text="Ecuación 3: x + y = r")
    ecuacion3.pack()

    x3 = tk.Entry(ventana_ecuaciones_3x3)
    x3.pack()
    y3 = tk.Entry(ventana_ecuaciones_3x3)
    y3.pack()
    z3 = tk.Entry(ventana_ecuaciones_3x3)
    z3.pack()

    r3 = tk.Entry(ventana_ecuaciones_3x3)
    r3.pack()

    resultado = tk.Label(ventana_ecuaciones_3x3, text="Resultado")
    resultado.pack(pady=20)

    btn = tk.Button(
        ventana_ecuaciones_3x3,
        text="Calcular",
        command=lambda:calcular_3x3(x1,y1,z1,r1,x2,y2,z2,r2,x3,y3,z3,r3,resultado)
    )
    btn.pack(pady=5)



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

    label_filas = tk.Label(
        ventana_suma_matrices, 
        text="Numero de filas"
    )
    label_filas.pack()

    entry_filas = tk.Entry(ventana_suma_matrices)
    entry_filas.pack()

    label_columnas = tk.Label(
        ventana_suma_matrices, 
        text="Numero de columnas"
    )
    label_columnas.pack()

    entry_columnas = tk.Entry(ventana_suma_matrices)
    entry_columnas.pack()

    btn = tk.Button(
        ventana_suma_matrices,
        text="Calcular",
        command=lambda:calcular_matriz_suma(entry_filas,entry_columnas,ventana_suma_matrices)
    )
    btn.pack(pady=5)

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