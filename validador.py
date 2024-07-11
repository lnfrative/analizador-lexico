import tkinter as tk
from main import *

def onValidar():
    codigo = entrada.get("1.0", tk.END)  # Obtener todo el texto del cuadro

    parser.parse(codigo, lexer=lexer)

    messages.append('Validación completada.')

    output = '\n'.join(messages)

    resultado.config(text=f"{output}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Validador de Texto")

# Recuadro para el input
recuadro_entrada = tk.LabelFrame(ventana, text="Ingrese texto:")
recuadro_entrada.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entrada = tk.Text(recuadro_entrada)  # Cuadro de texto para la entrada
entrada.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

# Botón "Validar"
boton_validar = tk.Button(ventana, text="Validar", command=onValidar)
boton_validar.pack(pady=10)

# Recuadro para el output
recuadro_salida = tk.LabelFrame(ventana, text="Salida:")
recuadro_salida.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

resultado = tk.Label(recuadro_salida, text="")  # Etiqueta para mostrar el resultado
resultado.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

ventana.mainloop()  # Inicia el bucle principal de la interfaz
