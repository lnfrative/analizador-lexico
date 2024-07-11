import tkinter as tk
from main import *

def onValidar():    
    messages.clear()

    codigo = entrada.get("1.0", tk.END)  

    parser.parse(codigo, lexer=lexer)

    if len(messages) == 0:
        messages.append('Validación completada.')
    
    output = '\n'.join(messages)

    resultado.config(text=f"{output}")

ventana = tk.Tk()
ventana.title("Validador de Texto")

recuadro_entrada = tk.LabelFrame(ventana, text="Ingrese texto:")
recuadro_entrada.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entrada = tk.Text(recuadro_entrada)
entrada.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

boton_validar = tk.Button(ventana, text="Validar", command=onValidar)
boton_validar.pack(pady=10)

recuadro_salida = tk.LabelFrame(ventana, text="Salida:")
recuadro_salida.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

resultado = tk.Label(recuadro_salida, text="")  
resultado.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

ventana.mainloop() 