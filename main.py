import ply.yacc as yacc
from lexico import tokens, lexer

# Reglas de precedencia para los operadores (de menor a mayor prioridad)
precedence = (
    ('left', 'CONCATENATION', 'CONCATENATION_ASSIGNMENT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
)

# Definición de la gramática

def p_program(p):
    '''
    program : statement_list
    '''
    p[0] = p[1]

def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''
    statement : expression_statement
              | function_declaration
    '''
    p[0] = p[1]

def p_expression_statement(p):
    '''
    expression_statement : expression SEMICOLON
    '''
    p[0] = p[1]

def p_function_declaration(p):
    '''
    function_declaration : FUNCTION IDENTIFIER OPEN_PARENTHESIS parameter_list CLOSE_PARENTHESIS OPEN_CURLY_BRACKET body_statement_list CLOSE_CURLY_BRACKET
    '''
    p[0] = ('function_declaration', p[2], p[4], p[7])  # Nombre de la función, lista de parámetros y cuerpo

def p_body_statement_list(p):
    '''
    body_statement_list : statement_list
                        | empty
    '''

def p_parameter_list(p):
    '''
    parameter_list : parameter
                   | parameter_list COMMA parameter
                   | empty
    '''
    if len(p) == 2:
        if p[1] is None:  # Caso vacío
            p[0] = []
        else:
            p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_parameter(p):
    '''
    parameter : VARIABLE
    '''
    p[0] = p[1]

def p_empty(p):
    '''
    empty :
    '''
    pass  # Regla para representar una lista de parámetros vacía

def p_expression(p):
    '''
    expression : VARIABLE
               | NUMBER
               | STRING
               | BOOLEAN
               | NULL
               | function_call
               | expression PLUS expression
               | expression MINUS expression
               | expression MULTIPLY expression
               | expression DIVIDE expression
               | expression MODULO expression
               | expression CONCATENATION expression
               | expression CONCATENATION_ASSIGNMENT expression
    '''
    # Manejo de diferentes tipos de expresiones y operaciones
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('binary_op', p[2], p[1], p[3])

def p_function_call(p):
    '''
    function_call : IDENTIFIER OPEN_PARENTHESIS CLOSE_PARENTHESIS
    '''
    p[0] = ('function_call', p[1])  # Nombre de la función

# Manejo de errores sintácticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.type}' (valor: {p.value}) en la línea {p.lineno}")
    else:
        print("Error de sintaxis: unexpected end of file")

# Construir el parser
parser = yacc.yacc()

while True:
   try:
       s = input('lp > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)