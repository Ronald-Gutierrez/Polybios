import tkinter as tk

def quitar_tildes_y_caracteres_especiales(texto):
    caracteres_especiales = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ü': 'u', 'Ü': 'U', 'ñ': 'n', 'Ñ': 'N',
    }

    for especial, normal in caracteres_especiales.items():
        texto = texto.replace(especial, normal)

    return texto

def cifrar_polybios(texto):
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    resultado = []

    texto = quitar_tildes_y_caracteres_especiales(texto)
    
    for letra in texto:
        if letra.isalpha():
            letra = letra.upper()  # Asegúrate de que la letra esté en mayúscula
            if letra == 'J':
                resultado.append((2, 4))  # Cifra 'J' como '24'
            elif letra in alfabeto:
                index = alfabeto.index(letra)
                fila = (index // 5) + 1
                columna = (index % 5) + 1
                resultado.append((fila, columna))
        else:
            resultado.append(' ')

    return resultado


def descifrar_polybios(texto_cifrado):
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    resultado = []

    i = 0
    while i < len(texto_cifrado):
        if i + 1 < len(texto_cifrado) and texto_cifrado[i].isdigit() and texto_cifrado[i + 1].isdigit():
            fila = int(texto_cifrado[i])
            columna = int(texto_cifrado[i + 1])
            if fila > 0 and fila < 6 and columna > 0 and columna < 6:
                index = (fila - 1) * 5 + (columna - 1)
                resultado.append(alfabeto[index])
                i += 2
            else:
                resultado.append(texto_cifrado[i])
                i += 1
        else:
            resultado.append(texto_cifrado[i])
            i += 1

    return resultado

def procesar():
    texto = entrada_texto.get()
    if operacion.get() == "Cifrar":
        resultado = cifrar_polybios(texto)
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        for elemento in resultado:
            if elemento == ' ':
                resultado_texto.insert(tk.END, ' ')
            else:
                resultado_texto.insert(tk.END, f"{elemento[0]}{elemento[1]}")
        resultado_texto.insert(tk.END, '\n')  # Agregar un salto de línea entre palabras
        resultado_texto.config(state=tk.DISABLED)
    else:
        resultado = descifrar_polybios(texto)
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        for elemento in resultado:
            resultado_texto.insert(tk.END, elemento)
        resultado_texto.config(state=tk.DISABLED)

def copiar():
    resultado = resultado_texto.get("1.0", tk.END)
    ventana.clipboard_clear()
    ventana.clipboard_append(resultado)
    ventana.update()

ventana = tk.Tk()
ventana.title("Cifrado y Descifrado de Polybios")
ventana.geometry("800x400")
ventana.configure(bg='#87CEEB')

etiqueta = tk.Label(ventana, text="Texto:", bg='#87CEEB')
etiqueta.pack()

entrada_texto = tk.Entry(ventana)
entrada_texto.pack()

operacion = tk.StringVar()
operacion.set("Cifrar")

opcion_cifrar = tk.Radiobutton(ventana, text="Cifrar", variable=operacion, value="Cifrar", bg='#87CEEB')
opcion_descifrar = tk.Radiobutton(ventana, text="Descifrar", variable=operacion, value="Descifrar", bg='#87CEEB')
opcion_cifrar.pack()
opcion_descifrar.pack()

boton_procesar = tk.Button(ventana, text="Procesar", command=procesar, bg='#32CD32')
boton_procesar.pack()

resultado_texto = tk.Text(ventana, height=10, width=40, state=tk.DISABLED)
resultado_texto.pack()

boton_copiar = tk.Button(ventana, text="Copiar Resultado", command=copiar, bg='#32CD32')
boton_copiar.pack()

ancho_ventana = ventana.winfo_reqwidth()
alto_ventana = ventana.winfo_reqheight()
pos_x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
pos_y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}')

ventana.mainloop()
