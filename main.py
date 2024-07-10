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
    ('left', 'CONCATENATION', 'CONCATENATION_EQUALS'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
)

# Definición de la gramática

def p_program(p):
    '''
    program : OPEN_TAG statement_list CLOSE_TAG
            | condition
            | math_expression
    '''

def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
                   | empty
    '''

def p_statement(p):
    '''
    statement : expression_statement
              | function_declaration
              | assignment SEMICOLON
              | if_statement
              | while_statement
              | for_statement
              | impresion
    '''

def p_assignment(p):
    '''
    assignment : VARIABLE assignment_operator expression 
              | VARIABLE EQUALS math_expression 
              | VARIABLE EQUALS array_structure 
              | VARIABLE EQUALS condition 
              | VARIABLE PLUS PLUS 
              | VARIABLE assignment_operator list_access
              | VARIABLE EQUALS casting math_expression

    '''

def p_casting(p):
    '''
    casting :  OPEN_PARENTHESIS data_type CLOSE_PARENTHESIS
    '''

def p_data_type(p):
    '''
    data_type : INT_T
            | INTEGER_T
            | FLOAT_T
            | DOUBLE_T
            | STRING_T
            | BOOLEAN_T
            | ARRAY_T
            | OBJECT_T
    '''
    p[0] = p[1]

def p_assignment_operator(p):
    '''
    assignment_operator : PLUS_EQUALS
                        | MINUS_EQUALS
                        | MULTIPLY_EQUALS
                        | DIVIDE_EQUALS
                        | MODULO_EQUALS
                        | CONCATENATION_EQUALS
                        | LEFT_SHIFT_EQUALS
                        | RIGHT_SHIFT_EQUALS
                        | AND_EQUALS
                        | OR_EQUALS
                        | XOR_EQUALS
                        | EQUALS
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
                        | OPEN_CURLY_BRACKET statement_list RETURN expression SEMICOLON CLOSE_CURLY_BRACKET
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
                | assignment
                | expression
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
                | expression CONCATENATION_EQUALS expression
                
    '''

def p_function_call(p):
    '''
    function_call : IDENTIFIER OPEN_PARENTHESIS parameter_list CLOSE_PARENTHESIS
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
    for_update : assignment
               | empty
    '''

def p_while_statement(p):
    '''
    while_statement : WHILE OPEN_PARENTHESIS condition CLOSE_PARENTHESIS body_statement_list
    '''

def p_impresion(p):
    '''
    impresion : ECHO value_parameter_list SEMICOLON
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

def p_list_access(p):
    '''
    list_access : VARIABLE OPEN_SQUARE_BRACKET expression CLOSE_SQUARE_BRACKET
    '''

# Manejo de errores sintácticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.type}' (valor: {p.value}) en la línea {p.lineno}")
    else:
        print("Error de sintaxis: unexpected end of file")

parser = yacc.yacc()

# nombre_usuario = input("Por favor, introduce tu nombre de usuario: ")

# fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# nombre_archivo = f"log/semantico-{nombre_usuario}-{fecha_hora}.txt"

data = '''
<?php

// Algoritmo para generar contraseñas - Christopher Díaz
function generarContrasena($longitud = 12) {
    // Caracteres permitidos en la contraseña
    $letrasMayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $letrasMinusculas = 'abcdefghijklmnopqrstuvwxyz';
    $meee = 'deñdllde';
    $numeros = '0123456789';
    $caracteresEspeciales = '!@#$%^&*()-_[]{}<>~`+=,.;:/?|';
    
    // Combinar todos los caracteres
    $todosLosCaracteres = $letrasMayusculas . $letrasMinusculas . $numeros . $caracteresEspeciales;
    
    // Asegurarse de que la contraseña contenga al menos uno de cada tipo de caracter
    $contraseña = '';
    $contraseña .= $letrasMayusculas[rand(0, strlen($letrasMayusculas) - 1)];
    $contraseña .= $letrasMinusculas[rand(0, strlen($letrasMinusculas) - 1)];
    $contraseña .= $numeros[rand(0, strlen($numeros) - 1)];
    $contraseña .= $caracteresEspeciales[rand(0, strlen($caracteresEspeciales) - 1)];
    
    // Completar la longitud de la contraseña con caracteres aleatorios
    for ($i = 4; $i < $longitud; $i++) {
        $contraseña .= $todosLosCaracteres[rand(0, strlen($todosLosCaracteres) - 1)];
    }
    
    // Mezclar la contraseña para evitar patrones predecibles
    $contraseña = str_shuffle($contraseña);
    
    return $contraseña;
}

function esPrimo($numero) {
    if ($numero <= 1) {
        return false;
    }

    for ($i = 2; $i <= sqrt($numero); $i++) {
        if ($numero % $i == 0) {
            return false;
        }
    }
    return true;
}

function sumaDigitos($numero) {
    $suma = 0;
    while ($numero > 0) {
        $suma += $numero % 10;
        $numero = (int) $numero / 10;
    }
    return $suma;
}

function sumaDigitosEsPrimo($numero) {
    $suma = sumaDigitos($numero);
    return esPrimo($suma);
}

$num = 12345;
$suma = sumaDigitos($num);
if (sumaDigitosEsPrimo($num)) {
    echo "La suma de los dígitos de {$num} es {$suma}, que es un número primo.";
} else {
    echo "La suma de los dígitos de {$num} es {$suma}, que no es un número primo.";
}

?>

'''

post_data = '''

// Función para verificar si la suma de los dígitos es un número primo


// Ejemplo de uso 1


// Ejemplo de uso 2
$longitudDeseada = 12; // Puedes cambiar la longitud de la contraseña aquí
$contraseña = generarContrasena($longitudDeseada);
echo "Contraseña generada: " . $contraseña;
'''

result = parser.parse(data)
print(result) 

# with open(nombre_archivo, "w") as archivo_salida:
#     while True:
#         try:
#             s = input('PHPSemantics -> ')
#         except EOFError:
#             break
#         if not s:
#             continue
#         result = parser.parse(s)
#         print(result) 

#         archivo_salida.write(str(result) + "\n") 