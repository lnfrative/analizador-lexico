import os
from datetime import datetime

# Variables globales
filename = None
username = None

def logger(lexer):
    global filename, username  # Declarar las variables globales para modificarlas dentro de la función
    username = input("Por favor, introduce tu nombre de usuario: ")

    now = datetime.now()
    timestamp = now.strftime("%d%m%Y-%Hh%M")

    log_dir = "./log"
    filename = f"{log_dir}/lexico-{username}-{timestamp}.txt"

    # Verifica y crea el directorio si no existe
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with open(filename, 'w') as f:
        while True:
            tok = lexer.token()
            if not tok:
                break
            f.write(str(tok) + '\n')

def t_error(t):
    global filename  # Declarar la variable global para modificarla dentro de la función

    if filename:  # Asegurarse de que el archivo de log esté definido
        with open(filename, 'a') as f:
            error_message = f"Illegal character '{t.value[0]}' at line {t.lineno}\n"
            f.write(error_message)
            print(error_message)
    t.lexer.skip(1)