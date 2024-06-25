"""
SOFG1009
Avance 1 - Analizador Léxico

Integrantes:
- José Baidal (Paralelo 1)
- Christopher Díaz (Paralelo 2)
"""

import ply.lex as lex
from logger import logger

# Palabras reservadas en PHP - José Baidal
palabras_reservadas = {
    'abstract': 'ABSTRACT',
    'and': 'AND',
    'array': 'ARRAY',
    'as': 'AS',
    'break': 'BREAK',
    'callable': 'CALLABLE',
    'case': 'CASE',
    'catch': 'CATCH',
    'class': 'CLASS',
    'clone': 'CLONE',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'declare': 'DECLARE',
    'default': 'DEFAULT',
    'die': 'DIE',
    'do': 'DO',
    'echo': 'ECHO',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'empty': 'EMPTY',
    'enddeclare': 'ENDDECLARE',
    'endfor': 'ENDFOR',
    'endforeach': 'ENDFOREACH',
    'endif': 'ENDIF',
    'endswitch': 'ENDSWITCH',
    'endwhile': 'ENDWHILE',
    'eval': 'EVAL',
    'exit': 'EXIT',
    'extends': 'EXTENDS',
    'final': 'FINAL',
    'finally': 'FINALLY',
    'return': 'RETURN',
    'function': 'FUNCTION'
}

# Lista de tokens - Christopher Díaz
tokens = (
    'NUMBER',
    'STRING',
    'BOOLEAN',
    'NULL',
    'IDENTIFIER',
    'VARIABLE',
    'OPEN_TAG',
    'CLOSE_TAG',
    'OPEN_TAG_WITH_ECHO',
    'WHITESPACE',
    'EQUALS',
    'OPEN_PARENTHESIS',
    'CLOSE_PARENTHESIS',
    'OPEN_CURLY_BRACKET',
    'CLOSE_CURLY_BRACKET',
    'OPEN_SQUARE_BRACKET',
    'CLOSE_SQUARE_BRACKET',
    'SEMICOLON',
    'COMMA',
    'COLON',
    'DOUBLE_COLON',
    'DOUBLE_EQUALS',
    'NOT_EQUALS',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_THAN_OR_EQUALS',
    'GREATER_THAN_OR_EQUALS',
    'PLUS',
    'DIVIDE',
    'MINUS',
    'MULTIPLY',
    'MODULO',
    'COMMENT',
    'CONCATENATION_ASSIGNMENT',
    'CONCATENATION'
) + tuple(palabras_reservadas.values())

# Expresiones regulares para tokens simples
t_EQUALS = r'='
t_OPEN_PARENTHESIS = r'\('
t_CLOSE_PARENTHESIS = r'\)'
t_OPEN_CURLY_BRACKET = r'\{'
t_CLOSE_CURLY_BRACKET = r'\}'
t_OPEN_SQUARE_BRACKET = r'\['
t_CLOSE_SQUARE_BRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','
t_COLON = r':'
t_DOUBLE_COLON = r'::'
t_DOUBLE_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_THAN_OR_EQUALS = r'<='
t_GREATER_THAN_OR_EQUALS = r'>='
t_PLUS = r'\+'
t_DIVIDE = r'/'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_MODULO = r'%'
t_ignore_WHITESPACE = r'\s+'
t_CONCATENATION_ASSIGNMENT = r'\.='
t_CONCATENATION = r'\.'

# Expresiones regulares para tokens más complejos
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\'(?:\\.|[^\\\'])*\' | \"(?:\\.|[^\\\"])*\"'
    t.value = t.value[1:-1]
    return t

def t_BOOLEAN(t):
    r'true|false'
    t.value = (t.value == 'true')
    return t

def t_NULL(t):
    r'null'
    t.value = None
    return t

def t_VARIABLE(t):
    r'\$[a-zA-Z_ñÑ][a-zA-Z0-9_ñÑ]*'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_ñÑ][a-zA-Z0-9_ñÑ]*'
    t.type = palabras_reservadas.get(t.value, 'IDENTIFIER') 
    return t

def t_OPEN_TAG(t):
    r'<\?php'
    return t

def t_CLOSE_TAG(t):
    r'\?>'
    return t

def t_OPEN_TAG_WITH_ECHO(t):
    r'<\?='
    return t

def t_RETURN(t):
    r'return'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_COMMENT(t):
    r'\/\/.*[ñÑ]*.*'
    pass

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

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


// Función para verificar si un número es primo - José Baidal
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

// Función para obtener la suma de los dígitos de un número
function sumaDigitos($numero) {
    $suma = 0;
    while ($numero > 0) {
        $suma += $numero % 10;
        $numero = (int) $numero / 10;
    }
    return $suma;
}

// Función para verificar si la suma de los dígitos es un número primo
function sumaDigitosEsPrimo($numero) {
    $suma = sumaDigitos($numero);
    return esPrimo($suma);
}

// Ejemplo de uso 1
$num = 12345;
$suma = sumaDigitos($num);
if (sumaDigitosEsPrimo($num)) {
    echo "La suma de los dígitos de {$num} es {$suma}, que es un número primo.";
} else {
    echo "La suma de los dígitos de {$num} es {$suma}, que no es un número primo.";
}

// Ejemplo de uso 2
$longitudDeseada = 12; // Puedes cambiar la longitud de la contraseña aquí
$contraseña = generarContrasena($longitudDeseada);
echo "Contraseña generada: " . $contraseña;

?>

'''

lexer.input(data)

# Ejecutar el lexer y mostrar los tokens
logger(lexer)
