from tkinter import *

#ventana
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("310x400")
ventana.configure(background="#333")
ventana.resizable(False, False)

#Entrada
pantalla = Entry(ventana, font=("calibri", 20), bd=10, relief=RIDGE, justify=RIGHT)
pantalla.grid(row=0,column=0, columnspan=4, padx=10, pady=10)

#funciones
def presionar(boton):
    pantalla.insert(END, boton)


def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, END)
        pantalla.insert(END, resultado)
    except:
        pantalla.delete(0, END)
        pantalla.insert(END, "error")
        

def limpiar():
    pantalla.delete(0 ,END)


#botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
]

for (texto, fila, columna) in botones:
    Button(ventana, text=texto, font=("calibri", 18), command=lambda t=texto: presionar(t)).grid(row=fila, column=columna, padx=5, pady=5)


Button(ventana, text="C", font=("Arial", 18), bg="red", fg="white", command=limpiar).grid(row=4, column=3, padx=5, pady=5)
Button(ventana, text="=", font=("Arial", 18), bg="green", fg="white", command=calcular).grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

            
ventana.mainloop()



