"""
SOFG1009
Avance 3 - Analizador semántico

Integrantes:
- José Baidal (Paralelo 1)
- Christopher Díaz (Paralelo 2)

Correcciones:
1. Reconocimiento de operaciones con números y variables:
   - Ejemplo: $a = $a + 5;

2. Reconocimiento de comparaciones:
   - Ejemplos: 40 > 30, $var > 1

3. Reconocimiento del token float:
   - Ejemplo: $var = 4.5;

4. Estructura de datos que permita valores enteros:
   - Ejemplo: $arr = ['id' => 20];

Implementación extra if, for, while

"""

import ply.yacc as yacc
import datetime
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
            | condition
            | math_expression
    '''

def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''

def p_statement(p):
    '''
    statement : expression_statement
              | function_declaration
              | assignment
              | if_statement
              | while_statement
              | for_statement
              | impresion
    '''

def p_assignment(p):
    '''
    assignment : VARIABLE EQUALS expression SEMICOLON
              | VARIABLE EQUALS math_expression SEMICOLON
              | VARIABLE EQUALS array_structure SEMICOLON
              | VARIABLE EQUALS condition SEMICOLON
              | VARIABLE PLUS PLUS SEMICOLON

    '''

def p_expression_statement(p):
    '''
    expression_statement : expression SEMICOLON
    '''

def p_function_declaration(p):
    '''
    function_declaration : FUNCTION IDENTIFIER OPEN_PARENTHESIS parameter_list CLOSE_PARENTHESIS body_statement_list
    '''

def p_body_statement_list(p):
    '''
    body_statement_list : OPEN_CURLY_BRACKET statement_list CLOSE_CURLY_BRACKET
                        | OPEN_CURLY_BRACKET empty CLOSE_CURLY_BRACKET
    '''

def p_parameter_list(p):
    '''
    parameter_list : parameter
                   | parameter_list COMMA parameter
                   | empty
    '''

def p_parameter(p):
    '''
    parameter : VARIABLE
    '''

def p_value_parameter_list(p):
    '''
    value_parameter_list : value_parameter
                   | value_parameter_list COMMA value_parameter
                   | empty
    '''

def p_value_parameter(p):
    '''
    value_parameter : expression
    '''

def p_empty(p):
    '''
    empty :
    '''
    pass

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

def p_function_call(p):
    '''
    function_call : IDENTIFIER OPEN_PARENTHESIS CLOSE_PARENTHESIS
    '''

def p_if_statement(p):
    '''
    if_statement : IF OPEN_PARENTHESIS condition CLOSE_PARENTHESIS body_statement_list
    '''

def p_for_statement(p):
    '''
    for_statement : FOR OPEN_PARENTHESIS for_initialization SEMICOLON condition SEMICOLON for_update CLOSE_PARENTHESIS body_statement_list
    '''

def p_for_initialization(p):
    '''
    for_initialization : assignment
                       | empty
    '''

def p_for_update(p):
    '''
    for_update : expression
               | empty
    '''

def p_while_statement(p):
    '''
    while_statement : WHILE OPEN_PARENTHESIS condition CLOSE_PARENTHESIS body_statement_list
    '''

def p_impresion(p):
    '''
    impresion : ECHO OPEN_PARENTHESIS value_parameter_list CLOSE_PARENTHESIS SEMICOLON
    '''

def p_condition(p):
    '''
    condition : expression
              | condition comparison condition
              | OPEN_PARENTHESIS condition comparison condition CLOSE_PARENTHESIS
              | OPEN_PARENTHESIS condition CLOSE_PARENTHESIS comparison condition
              | condition comparison OPEN_PARENTHESIS condition CLOSE_PARENTHESIS
              | NOT condition
    '''

def p_comparison(p):
    '''
    comparison : DOUBLE_EQUALS
               | NOT_EQUALS
               | GREATER_THAN
               | LESS_THAN
               | GREATER_THAN_OR_EQUALS
               | LESS_THAN_OR_EQUALS
               | AND
               | OR
    '''

def p_math_operator(p): 
    '''
    math_operator : PLUS
                  | DIVIDE
                  | MINUS
                  | MULTIPLY
                  | MODULO
    '''

def p_math_expression(p): 
    '''
    math_expression : NUMBER
                    | math_expression math_operator math_expression
                    | math_expression math_operator VARIABLE
                    | VARIABLE math_operator math_expression 
                    | OPEN_PARENTHESIS math_expression math_operator math_expression CLOSE_PARENTHESIS
                    | OPEN_PARENTHESIS math_expression CLOSE_PARENTHESIS math_operator math_expression
                    | math_expression math_operator OPEN_PARENTHESIS math_expression CLOSE_PARENTHESIS
    '''

def p_array_structure(p):
    '''
    array_structure : OPEN_SQUARE_BRACKET key_declaration CLOSE_SQUARE_BRACKET
    '''

def p_key_declaration(p):
    '''
    key_declaration : expression EQUALS GREATER_THAN expression
                    | key_declaration COMMA key_declaration
                    | empty
    '''

# Manejo de errores sintácticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.type}' (valor: {p.value}) en la línea {p.lineno}")
    else:
        print("Error de sintaxis: unexpected end of file")

parser = yacc.yacc()

nombre_usuario = input("Por favor, introduce tu nombre de usuario: ")

fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nombre_archivo = f"log/semantico-{nombre_usuario}-{fecha_hora}.txt"

with open(nombre_archivo, "w") as archivo_salida:
    while True:
        try:
            s = input('PHPSemantics -> ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result) 

        archivo_salida.write(str(result) + "\n") 