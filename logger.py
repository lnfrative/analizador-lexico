from datetime import datetime

def logger(lexer): 
    username = input("Por favor, introduce tu nombre de usuario: ")

    now = datetime.now()
    timestamp = now.strftime("%d%m%Y-%Hh%M")

    filename = f"./log/lexico-{username}-{timestamp}.txt"

    with open(filename, 'w') as f:
        while True:
            tok = lexer.token()
            if not tok:
                break
            f.write(str(tok) + '\n')