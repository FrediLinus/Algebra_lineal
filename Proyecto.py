import tkinter as tk

ventana = tk.Tk()
ventana.title("Proyecto Álgebra Digital")
ventana.geometry("800x700")

#Título
titulo = tk.Label(ventana, text="ÁLGEBRA DIGITAL", font=("Arial", 18))
titulo.pack(pady=20)

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

    #Boton 2
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

def abrir_resta_vectores():
    ventana_vectores_resta = tk.Toplevel()
    ventana_vectores_resta.title("Resta de Vectores")
    ventana_vectores_resta.geometry("600x500")

    titulo = tk.Label(ventana_vectores_resta, text="Operaciones con vectores resta1", font=("Arial", 14))
    titulo.pack(pady=20)


def abrir_punto_vectores():
    ventana_vectores_punto = tk.Toplevel()
    ventana_vectores_punto.title("Punto Vectores")
    ventana_vectores_punto.geometry("600x500")

    titulo = tk.Label(ventana_vectores_punto, text="Operaciones con vectores punto", font=("Arial", 14))
    titulo.pack(pady=20)

    

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

#Funcion 4 a usar
def abrir_matriz_inversa():
    ventana_matriz_inversa = tk.Toplevel()
    ventana_matriz_inversa.title("Matrices Inversas")
    ventana_matriz_inversa.geometry("600x500")

    titulo = tk.Label(ventana_matriz_inversa,text="Operaciones de Matrices Inversas", font=("Arial",14 ))
    titulo.pack(pady=20)



# Botón 1
btn_vectores = tk.Button(ventana, text="Operaciones con vectores", command=abrir_vectores)
btn_vectores.pack(pady=10)

# Botón 2
btn_resolucion_ecuaciones = tk.Button(ventana,text = "Resolucion de ecuaciones", command=abrir_resolucion_ecuaciones)
btn_resolucion_ecuaciones.pack(pady=10)


#Boton 3 
btn_algebra_matrices = tk.Button(ventana, text="Álgebra de matrices",command=abrir_algebra_matrices)
btn_algebra_matrices.pack(pady=10)

#Boton 4
btn_matrices_inversas = tk.Button(ventana, text="Matrizes inversas", command=abrir_matriz_inversa)
btn_matrices_inversas.pack(pady=10)







ventana.mainloop() #siempre va de ultimo 