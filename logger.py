import os
from datetime import datetime

def logger(lexer):
    username = input("Por favor, introduzca su nombre de usuario GitHub: ")

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
            print(str(tok))