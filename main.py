import ply.lex as lex
import ply.yacc as yacc

from logger import logger

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
}

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
)

tokens = tokens + tuple(palabras_reservadas.values())

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

# Expresiones regulares para tokens más complejos
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # Remover las comillas alrededor de la cadena
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
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = palabras_reservadas.get(t.value, 'IDENTIFIER')  # Verificar palabras reservadas
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

def t_COMMENT(t):
    r'(//.*|/\*[\s\S]*?\*/)'
    pass  # Ignorar los comentarios

# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Prueba del lexer
data = '''
<?php
function generarContrasena($longitud = 12) {
    // Caracteres permitidos en la contraseña
    $letrasMayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $letrasMinusculas = 'abcdefghijklmnopqrstuvwxyz';
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

// Ejemplo de uso
$longitudDeseada = 12; // Puedes cambiar la longitud de la contraseña aquí
$contraseña = generarContrasena($longitudDeseada);
echo "Contraseña generada: " . $contraseña;
?>

'''

lexer.input(data)

logger(lexer)