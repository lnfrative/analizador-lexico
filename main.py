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
            | condition
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
              | impresion
    '''

def p_assignment(p):
    '''
    assignment : VARIABLE EQUALS expression SEMICOLON
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
       s = input('PHPSemantics -> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)