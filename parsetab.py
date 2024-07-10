
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCONCATENATIONCONCATENATION_EQUALSleftPLUSMINUSleftMULTIPLYDIVIDEMODULOABSTRACT AND AND_EQUALS ARRAY_T AS BOOLEAN BOOLEAN_T BOOL_T BREAK CALLABLE CASE CATCH CLASS CLONE CLOSE_CURLY_BRACKET CLOSE_PARENTHESIS CLOSE_SQUARE_BRACKET CLOSE_TAG COLON COMMA COMMENT CONCATENATION CONCATENATION_EQUALS CONST CONTINUE DECLARE DEFAULT DIE DIVIDE DIVIDE_EQUALS DO DOUBLE_COLON DOUBLE_EQUALS DOUBLE_T ECHO ELSE ELSEIF EMPTY ENDDECLARE ENDFOR ENDFOREACH ENDIF ENDSWITCH ENDWHILE EQUALS EVAL EXIT EXTENDS FINAL FINALLY FLOAT_T FOR FUNCTION GREATER_THAN GREATER_THAN_OR_EQUALS IDENTIFIER IF INTEGER_T INT_T LEFT_SHIFT_EQUALS LESS_THAN LESS_THAN_OR_EQUALS MINUS MINUS_EQUALS MODULO MODULO_EQUALS MULTIPLY MULTIPLY_EQUALS NOT NOT_EQUALS NULL NUMBER OBJECT_T OPEN_CURLY_BRACKET OPEN_PARENTHESIS OPEN_SQUARE_BRACKET OPEN_TAG OPEN_TAG_WITH_ECHO OR OR_EQUALS PLUS PLUS_EQUALS RETURN RIGHT_SHIFT_EQUALS SEMICOLON STRING STRING_T VARIABLE WHILE WHITESPACE XOR_EQUALS\n    program : OPEN_TAG statement_list CLOSE_TAG\n            | condition\n            | math_expression\n    \n    statement_list : statement\n                   | statement_list statement\n                   | empty\n    \n    statement : expression_statement\n              | function_declaration\n              | assignment SEMICOLON\n              | if_statement\n              | while_statement\n              | for_statement\n              | impresion\n    \n    assignment : VARIABLE assignment_operator expression \n              | VARIABLE EQUALS math_expression \n              | VARIABLE EQUALS array_structure \n              | VARIABLE EQUALS condition \n              | VARIABLE PLUS PLUS \n              | VARIABLE assignment_operator list_access\n              | VARIABLE EQUALS casting math_expression\n\n    \n    casting :  OPEN_PARENTHESIS data_type CLOSE_PARENTHESIS\n    \n    data_type : INT_T\n            | INTEGER_T\n            | FLOAT_T\n            | DOUBLE_T\n            | STRING_T\n            | BOOLEAN_T\n            | ARRAY_T\n            | OBJECT_T\n    \n    assignment_operator : PLUS_EQUALS\n                        | MINUS_EQUALS\n                        | MULTIPLY_EQUALS\n                        | DIVIDE_EQUALS\n                        | MODULO_EQUALS\n                        | CONCATENATION_EQUALS\n                        | LEFT_SHIFT_EQUALS\n                        | RIGHT_SHIFT_EQUALS\n                        | AND_EQUALS\n                        | OR_EQUALS\n                        | XOR_EQUALS\n                        | EQUALS\n    \n    expression_statement : expression SEMICOLON\n    \n    function_declaration : FUNCTION IDENTIFIER OPEN_PARENTHESIS parameter_list CLOSE_PARENTHESIS body_statement_list\n    \n    body_statement_list : OPEN_CURLY_BRACKET statement_list CLOSE_CURLY_BRACKET\n                        | OPEN_CURLY_BRACKET empty CLOSE_CURLY_BRACKET\n                        | OPEN_CURLY_BRACKET statement_list RETURN expression SEMICOLON CLOSE_CURLY_BRACKET\n    \n    parameter_list : parameter\n                   | parameter_list COMMA parameter\n                   | empty\n    \n    parameter : VARIABLE\n                | assignment\n                | expression\n    \n    value_parameter_list : value_parameter\n                   | value_parameter_list COMMA value_parameter\n                   | empty\n    \n    value_parameter : expression\n    \n    empty :\n    \n    expression : VARIABLE\n                | NUMBER\n                | STRING\n                | BOOLEAN\n                | NULL\n                | function_call\n                | expression PLUS expression\n                | expression MINUS expression\n                | expression MULTIPLY expression\n                | expression DIVIDE expression\n                | expression MODULO expression\n                | expression CONCATENATION expression\n                | expression CONCATENATION_EQUALS expression\n                \n    \n    function_call : IDENTIFIER OPEN_PARENTHESIS parameter_list CLOSE_PARENTHESIS\n    \n    if_statement : IF OPEN_PARENTHESIS condition CLOSE_PARENTHESIS body_statement_list\n    \n    for_statement : FOR OPEN_PARENTHESIS for_initialization SEMICOLON condition SEMICOLON for_update CLOSE_PARENTHESIS body_statement_list\n    \n    for_initialization : assignment\n                       | empty\n    \n    for_update : assignment\n               | empty\n    \n    while_statement : WHILE OPEN_PARENTHESIS condition CLOSE_PARENTHESIS body_statement_list\n    \n    impresion : ECHO value_parameter_list SEMICOLON\n    \n    condition : expression\n              | condition comparison condition\n              | OPEN_PARENTHESIS condition comparison condition CLOSE_PARENTHESIS\n              | OPEN_PARENTHESIS condition CLOSE_PARENTHESIS comparison condition\n              | condition comparison OPEN_PARENTHESIS condition CLOSE_PARENTHESIS\n              | NOT condition\n    \n    comparison : DOUBLE_EQUALS\n               | NOT_EQUALS\n               | GREATER_THAN\n               | LESS_THAN\n               | GREATER_THAN_OR_EQUALS\n               | LESS_THAN_OR_EQUALS\n               | AND\n               | OR\n    \n    math_operator : PLUS\n                  | DIVIDE\n                  | MINUS\n                  | MULTIPLY\n                  | MODULO\n    \n    math_expression : NUMBER\n                    | math_expression math_operator math_expression\n                    | math_expression math_operator VARIABLE\n                    | VARIABLE math_operator math_expression \n                    | OPEN_PARENTHESIS math_expression math_operator math_expression CLOSE_PARENTHESIS\n                    | OPEN_PARENTHESIS math_expression CLOSE_PARENTHESIS math_operator math_expression\n                    | math_expression math_operator OPEN_PARENTHESIS math_expression CLOSE_PARENTHESIS\n    \n    array_structure : OPEN_SQUARE_BRACKET key_declaration CLOSE_SQUARE_BRACKET\n    \n    key_declaration : expression EQUALS GREATER_THAN expression\n                    | key_declaration COMMA key_declaration\n                    | empty\n    \n    list_access : VARIABLE OPEN_SQUARE_BRACKET expression CLOSE_SQUARE_BRACKET\n    '
    
_lr_action_items = {'OPEN_TAG':([0,],[2,]),'OPEN_PARENTHESIS':([0,6,7,14,28,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,60,66,68,81,82,89,92,101,103,107,121,122,136,138,144,159,170,],[6,6,58,61,81,82,83,89,-86,-87,-88,-89,-90,-91,-92,-93,92,-94,-95,-96,-97,-98,58,107,114,122,58,58,58,107,89,92,107,107,144,58,107,144,58,-21,]),'NOT':([0,6,7,33,34,35,36,37,38,39,40,41,58,68,81,82,89,101,122,136,144,159,],[7,7,7,7,-86,-87,-88,-89,-90,-91,-92,-93,7,7,7,7,7,7,7,7,7,7,]),'NUMBER':([0,2,6,7,15,16,17,18,19,21,22,23,24,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,60,61,63,64,65,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,89,92,101,103,107,114,121,122,123,131,132,136,138,140,142,144,159,170,172,174,175,176,178,181,182,183,186,187,188,195,196,],[8,32,8,32,32,-4,-6,-7,-8,-10,-11,-12,-13,32,32,-86,-87,-88,-89,-90,-91,-92,-93,93,-94,-95,-96,-97,-98,32,32,32,32,32,32,32,32,93,32,-5,-9,-42,32,8,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,32,32,32,93,32,93,93,32,93,8,32,-79,32,32,93,32,32,8,32,-21,32,-72,32,-78,-43,32,32,-6,-44,32,-45,-73,-46,]),'VARIABLE':([0,2,6,7,15,16,17,18,19,21,22,23,24,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,60,61,63,64,65,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,89,92,101,103,107,114,121,122,123,131,132,136,138,140,142,144,159,170,172,174,175,176,178,181,182,183,184,186,187,188,195,196,],[9,27,9,59,27,-4,-6,-7,-8,-10,-11,-12,-13,59,59,-86,-87,-88,-89,-90,-91,-92,-93,91,-94,-95,-96,-97,-98,59,59,59,59,59,59,59,59,105,111,-5,-9,-42,115,9,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,59,59,130,59,105,59,91,105,111,105,9,59,-79,59,59,105,111,59,9,59,-21,59,-72,27,-78,-43,59,27,-6,130,-44,59,-45,-73,-46,]),'STRING':([0,2,6,7,15,16,17,18,19,21,22,23,24,31,33,34,35,36,37,38,39,40,41,48,49,50,51,52,53,54,58,61,63,64,65,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,89,101,114,122,123,131,132,136,140,142,144,159,172,174,175,176,178,181,182,183,186,187,188,195,196,],[10,10,10,10,10,-4,-6,-7,-8,-10,-11,-12,-13,10,10,-86,-87,-88,-89,-90,-91,-92,-93,10,10,10,10,10,10,10,10,10,-5,-9,-42,10,10,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,10,10,10,10,10,10,10,-79,10,10,10,10,10,10,10,-72,10,-78,-43,10,10,-6,-44,10,-45,-73,-46,]),'BOOLEAN':([0,2,6,7,15,16,17,18,19,21,22,23,24,31,33,34,35,36,37,38,39,40,41,48,49,50,51,52,53,54,58,61,63,64,65,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,89,101,114,122,123,131,132,136,140,142,144,159,172,174,175,176,178,181,182,183,186,187,188,195,196,],[11,11,11,11,11,-4,-6,-7,-8,-10,-11,-12,-13,11,11,-86,-87,-88,-89,-90,-91,-92,-93,11,11,11,11,11,11,11,11,11,-5,-9,-42,11,11,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,11,11,11,11,11,11,11,-79,11,11,11,11,11,11,11,-72,11,-78,-43,11,11,-6,-44,11,-45,-73,-46,]),'NULL':([0,2,6,7,15,16,17,18,19,21,22,23,24,31,33,34,35,36,37,38,39,40,41,48,49,50,51,52,53,54,58,61,63,64,65,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,89,101,114,122,123,131,132,136,140,142,144,159,172,174,175,176,178,181,182,183,186,187,188,195,196,],[12,12,12,12,12,-4,-6,-7,-8,-10,-11,-12,-13,12,12,-86,-87,-88,-89,-90,-91,-92,-93,12,12,12,12,12,12,12,12,12,-5,-9,-42,12,12,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,12,12,12,12,12,12,12,-79,12,12,12,12,12,12,12,-72,12,-78,-43,12,12,-6,-44,12,-45,-73,-46,]),'IDENTIFIER':([0,2,6,7,15,16,17,18,19,21,22,23,24,26,31,33,34,35,36,37,38,39,40,41,48,49,50,51,52,53,54,58,61,63,64,65,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,89,101,114,122,123,131,132,136,140,142,144,159,172,174,175,176,178,181,182,183,186,187,188,195,196,],[14,14,14,14,14,-4,-6,-7,-8,-10,-11,-12,-13,66,14,14,-86,-87,-88,-89,-90,-91,-92,-93,14,14,14,14,14,14,14,14,14,-5,-9,-42,14,14,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,14,14,14,14,14,14,14,-79,14,14,14,14,14,14,14,-72,14,-78,-43,14,14,-6,-44,14,-45,-73,-46,]),'$end':([1,3,4,5,8,9,10,11,12,13,32,57,59,62,88,90,91,93,94,95,96,97,98,99,100,106,139,161,162,163,164,165,166,],[0,-2,-3,-80,-59,-58,-60,-61,-62,-63,-59,-85,-58,-1,-81,-100,-101,-99,-64,-65,-66,-67,-68,-69,-70,-102,-71,-84,-105,-82,-83,-103,-104,]),'CLOSE_TAG':([2,15,16,17,18,19,21,22,23,24,63,64,65,131,174,176,178,186,188,195,196,],[-57,62,-4,-6,-7,-8,-10,-11,-12,-13,-5,-9,-42,-79,-72,-78,-43,-44,-45,-73,-46,]),'FUNCTION':([2,15,16,17,18,19,21,22,23,24,63,64,65,131,174,175,176,178,182,183,186,188,195,196,],[26,26,-4,-6,-7,-8,-10,-11,-12,-13,-5,-9,-42,-79,-72,26,-78,-43,26,-6,-44,-45,-73,-46,]),'IF':([2,15,16,17,18,19,21,22,23,24,63,64,65,131,174,175,176,178,182,183,186,188,195,196,],[28,28,-4,-6,-7,-8,-10,-11,-12,-13,-5,-9,-42,-79,-72,28,-78,-43,28,-6,-44,-45,-73,-46,]),'WHILE':([2,15,16,17,18,19,21,22,23,24,63,64,65,131,174,175,176,178,182,183,186,188,195,196,],[29,29,-4,-6,-7,-8,-10,-11,-12,-13,-5,-9,-42,-79,-72,29,-78,-43,29,-6,-44,-45,-73,-46,]),'FOR':([2,15,16,17,18,19,21,22,23,24,63,64,65,131,174,175,176,178,182,183,186,188,195,196,],[30,30,-4,-6,-7,-8,-10,-11,-12,-13,-5,-9,-42,-79,-72,30,-78,-43,30,-6,-44,-45,-73,-46,]),'ECHO':([2,15,16,17,18,19,21,22,23,24,63,64,65,131,174,175,176,178,182,183,186,188,195,196,],[31,31,-4,-6,-7,-8,-10,-11,-12,-13,-5,-9,-42,-79,-72,31,-78,-43,31,-6,-44,-45,-73,-46,]),'DOUBLE_EQUALS':([3,5,8,9,10,11,12,13,32,55,57,59,88,94,95,96,97,98,99,100,102,120,125,126,133,135,139,161,163,164,177,],[34,-80,-59,-58,-60,-61,-62,-63,-59,34,34,-58,34,-64,-65,-66,-67,-68,-69,-70,34,34,34,34,34,34,-71,34,-82,34,34,]),'NOT_EQUALS':([3,5,8,9,10,11,12,13,32,55,57,59,88,94,95,96,97,98,99,100,102,120,125,126,133,135,139,161,163,164,177,],[35,-80,-59,-58,-60,-61,-62,-63,-59,35,35,-58,35,-64,-65,-66,-67,-68,-69,-70,35,35,35,35,35,35,-71,35,-82,35,35,]),'GREATER_THAN':([3,5,8,9,10,11,12,13,32,55,57,59,88,94,95,96,97,98,99,100,102,120,125,126,133,135,139,161,163,164,173,177,],[36,-80,-59,-58,-60,-61,-62,-63,-59,36,36,-58,36,-64,-65,-66,-67,-68,-69,-70,36,36,36,36,36,36,-71,36,-82,36,181,36,]),'LESS_THAN':([3,5,8,9,10,11,12,13,32,55,57,59,88,94,95,96,97,98,99,100,102,120,125,126,133,135,139,161,163,164,177,],[37,-80,-59,-58,-60,-61,-62,-63,-59,37,37,-58,37,-64,-65,-66,-67,-68,-69,-70,37,37,37,37,37,37,-71,37,-82,37,37,]),'GREATER_THAN_OR_EQUALS':([3,5,8,9,10,11,12,13,32,55,57,59,88,94,95,96,97,98,99,100,102,120,125,126,133,135,139,161,163,164,177,],[38,-80,-59,-58,-60,-61,-62,-63,-59,38,38,-58,38,-64,-65,-66,-67,-68,-69,-70,38,38,38,38,38,38,-71,38,-82,38,38,]),'LESS_THAN_OR_EQUALS':([3,5,8,9,10,11,12,13,32,55,57,59,88,94,95,96,97,98,99,100,102,120,125,126,133,135,139,161,163,164,177,],[39,-80,-59,-58,-60,-61,-62,-63,-59,39,39,-58,39,-64,-65,-66,-67,-68,-69,-70,39,39,39,39,39,39,-71,39,-82,39,39,]),'AND':([3,5,8,9,10,11,12,13,32,55,57,59,88,94,95,96,97,98,99,100,102,120,125,126,133,135,139,161,163,164,177,],[40,-80,-59,-58,-60,-61,-62,-63,-59,40,40,-58,40,-64,-65,-66,-67,-68,-69,-70,40,40,40,40,40,40,-71,40,-82,40,40,]),'OR':([3,5,8,9,10,11,12,13,32,55,57,59,88,94,95,96,97,98,99,100,102,120,125,126,133,135,139,161,163,164,177,],[41,-80,-59,-58,-60,-61,-62,-63,-59,41,41,-58,41,-64,-65,-66,-67,-68,-69,-70,41,41,41,41,41,41,-71,41,-82,41,41,]),'PLUS':([4,5,8,9,10,11,12,13,25,27,32,56,59,69,87,90,91,93,94,95,96,97,98,99,100,104,105,106,111,113,115,116,118,130,134,137,139,143,155,162,165,166,169,185,192,],[43,48,-59,43,-60,-61,-62,-63,48,69,-59,43,-58,124,48,43,43,-99,-64,-65,-66,-67,-68,48,48,43,43,43,69,48,-58,48,43,69,43,43,-71,43,48,43,-103,43,48,48,48,]),'DIVIDE':([4,5,8,9,10,11,12,13,25,27,32,56,59,87,90,91,93,94,95,96,97,98,99,100,104,105,106,111,113,115,116,118,134,137,139,143,155,162,165,166,169,185,192,],[44,51,-59,44,-60,-61,-62,-63,51,-58,-59,44,-58,51,44,44,-99,51,51,-66,-67,-68,51,51,44,44,44,-58,51,-58,51,44,44,44,-71,44,51,44,-103,44,51,51,51,]),'MINUS':([4,5,8,9,10,11,12,13,25,27,32,56,59,87,90,91,93,94,95,96,97,98,99,100,104,105,106,111,113,115,116,118,134,137,139,143,155,162,165,166,169,185,192,],[45,49,-59,45,-60,-61,-62,-63,49,-58,-59,45,-58,49,45,45,-99,-64,-65,-66,-67,-68,49,49,45,45,45,-58,49,-58,49,45,45,45,-71,45,49,45,-103,45,49,49,49,]),'MULTIPLY':([4,5,8,9,10,11,12,13,25,27,32,56,59,87,90,91,93,94,95,96,97,98,99,100,104,105,106,111,113,115,116,118,134,137,139,143,155,162,165,166,169,185,192,],[46,50,-59,46,-60,-61,-62,-63,50,-58,-59,46,-58,50,46,46,-99,50,50,-66,-67,-68,50,50,46,46,46,-58,50,-58,50,46,46,46,-71,46,50,46,-103,46,50,50,50,]),'MODULO':([4,5,8,9,10,11,12,13,25,27,32,56,59,87,90,91,93,94,95,96,97,98,99,100,104,105,106,111,113,115,116,118,134,137,139,143,155,162,165,166,169,185,192,],[47,52,-59,47,-60,-61,-62,-63,52,-58,-59,47,-58,52,47,47,-99,52,52,-66,-67,-68,52,52,47,47,47,-58,52,-58,52,47,47,47,-71,47,52,47,-103,47,52,52,52,]),'CLOSE_PARENTHESIS':([5,8,9,10,11,12,13,32,55,56,57,59,61,88,90,91,93,94,95,96,97,98,99,100,106,108,109,110,111,112,113,114,115,116,117,118,119,120,124,125,126,133,134,135,137,139,141,143,145,146,147,148,149,150,151,152,153,161,162,163,164,165,166,167,171,179,184,189,190,191,],[-80,-59,-58,-60,-61,-62,-63,-59,102,104,-85,-58,-57,-81,-100,-101,-99,-64,-65,-66,-67,-68,-69,-70,-102,139,-47,-49,-50,-51,-52,-57,-58,-14,-19,-15,-16,-17,-18,157,158,161,162,163,165,-71,168,-20,170,-22,-23,-24,-25,-26,-27,-28,-29,-84,-105,-82,-83,-103,-104,-48,-106,-110,-57,193,-76,-77,]),'SEMICOLON':([5,8,9,10,11,12,13,20,25,27,31,32,57,59,83,84,85,86,87,88,90,91,93,94,95,96,97,98,99,100,106,115,116,117,118,119,120,124,127,128,129,139,143,160,161,162,163,164,165,166,171,177,179,192,],[-80,-59,-58,-60,-61,-62,-63,64,65,-58,-57,-59,-85,-58,-57,131,-53,-55,-56,-81,-100,-101,-99,-64,-65,-66,-67,-68,-69,-70,-102,-58,-14,-19,-15,-16,-17,-18,159,-74,-75,-71,-20,-54,-84,-105,-82,-83,-103,-104,-106,184,-110,194,]),'COMMA':([5,8,9,10,11,12,13,31,32,57,59,61,84,85,86,87,88,90,91,93,94,95,96,97,98,99,100,106,108,109,110,111,112,113,114,115,116,117,118,119,120,123,124,139,141,143,154,156,160,161,162,163,164,165,166,167,171,172,179,180,185,],[-80,-59,-58,-60,-61,-62,-63,-57,-59,-85,-58,-57,132,-53,-55,-56,-81,-100,-101,-99,-64,-65,-66,-67,-68,-69,-70,-102,140,-47,-49,-50,-51,-52,-57,-58,-14,-19,-15,-16,-17,-57,-18,-71,140,-20,172,-109,-54,-84,-105,-82,-83,-103,-104,-48,-106,-57,-110,172,-107,]),'CONCATENATION':([5,8,9,10,11,12,13,25,27,32,59,87,94,95,96,97,98,99,100,111,113,115,116,139,155,169,185,192,],[53,-59,-58,-60,-61,-62,-63,53,-58,-59,-58,53,-64,-65,-66,-67,-68,-69,-70,-58,53,-58,53,-71,53,53,53,53,]),'CONCATENATION_EQUALS':([5,8,9,10,11,12,13,25,27,32,59,87,94,95,96,97,98,99,100,111,113,115,116,130,139,155,169,185,192,],[54,-59,-58,-60,-61,-62,-63,54,75,-59,-58,54,-64,-65,-66,-67,-68,-69,-70,75,54,-58,54,75,-71,54,54,54,54,]),'EQUALS':([10,11,12,13,27,32,59,94,95,96,97,98,99,100,111,130,139,155,],[-60,-61,-62,-63,68,-59,-58,-64,-65,-66,-67,-68,-69,-70,68,68,-71,173,]),'CLOSE_SQUARE_BRACKET':([10,11,12,13,32,59,94,95,96,97,98,99,100,123,139,154,156,169,172,180,185,],[-60,-61,-62,-63,-59,-58,-64,-65,-66,-67,-68,-69,-70,-57,-71,171,-109,179,-57,-108,-107,]),'CLOSE_CURLY_BRACKET':([16,18,19,21,22,23,24,63,64,65,131,174,175,176,178,182,183,186,188,194,195,196,],[-4,-7,-8,-10,-11,-12,-13,-5,-9,-42,-79,-72,-57,-78,-43,186,188,-44,-45,196,-73,-46,]),'RETURN':([16,18,19,21,22,23,24,63,64,65,131,174,175,176,178,182,183,186,188,195,196,],[-4,-7,-8,-10,-11,-12,-13,-5,-9,-42,-79,-72,-57,-78,-43,187,-6,-44,-45,-73,-46,]),'PLUS_EQUALS':([27,111,130,],[70,70,70,]),'MINUS_EQUALS':([27,111,130,],[71,71,71,]),'MULTIPLY_EQUALS':([27,111,130,],[72,72,72,]),'DIVIDE_EQUALS':([27,111,130,],[73,73,73,]),'MODULO_EQUALS':([27,111,130,],[74,74,74,]),'LEFT_SHIFT_EQUALS':([27,111,130,],[76,76,76,]),'RIGHT_SHIFT_EQUALS':([27,111,130,],[77,77,77,]),'AND_EQUALS':([27,111,130,],[78,78,78,]),'OR_EQUALS':([27,111,130,],[79,79,79,]),'XOR_EQUALS':([27,111,130,],[80,80,80,]),'OPEN_SQUARE_BRACKET':([68,115,],[123,142,]),'INT_T':([122,],[146,]),'INTEGER_T':([122,],[147,]),'FLOAT_T':([122,],[148,]),'DOUBLE_T':([122,],[149,]),'STRING_T':([122,],[150,]),'BOOLEAN_T':([122,],[151,]),'ARRAY_T':([122,],[152,]),'OBJECT_T':([122,],[153,]),'OPEN_CURLY_BRACKET':([157,158,168,193,],[175,175,175,175,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'condition':([0,6,7,33,58,68,81,82,89,101,122,136,144,159,],[3,55,57,88,55,120,125,126,133,135,55,164,55,177,]),'math_expression':([0,6,42,60,68,92,103,107,121,122,138,144,],[4,56,90,106,118,134,137,56,143,56,166,56,]),'expression':([0,2,6,7,15,31,33,48,49,50,51,52,53,54,58,61,67,68,81,82,89,101,114,122,123,132,136,140,142,144,159,172,175,181,182,187,],[5,25,5,5,25,87,5,94,95,96,97,98,99,100,5,113,116,5,5,5,5,5,113,5,155,87,5,113,169,5,5,155,25,185,25,192,]),'function_call':([0,2,6,7,15,31,33,48,49,50,51,52,53,54,58,61,67,68,81,82,89,101,114,122,123,132,136,140,142,144,159,172,175,181,182,187,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'statement_list':([2,175,],[15,182,]),'statement':([2,15,175,182,],[16,63,16,63,]),'empty':([2,31,61,83,114,123,172,175,184,],[17,86,110,129,110,156,156,183,191,]),'expression_statement':([2,15,175,182,],[18,18,18,18,]),'function_declaration':([2,15,175,182,],[19,19,19,19,]),'assignment':([2,15,61,83,114,140,175,182,184,],[20,20,112,128,112,112,20,20,190,]),'if_statement':([2,15,175,182,],[21,21,21,21,]),'while_statement':([2,15,175,182,],[22,22,22,22,]),'for_statement':([2,15,175,182,],[23,23,23,23,]),'impresion':([2,15,175,182,],[24,24,24,24,]),'comparison':([3,55,57,88,102,120,125,126,133,135,161,164,177,],[33,101,33,33,136,33,33,33,101,33,136,33,33,]),'math_operator':([4,9,56,90,91,104,105,106,118,134,137,143,162,166,],[42,60,103,42,60,138,60,42,42,103,42,42,138,42,]),'assignment_operator':([27,111,130,],[67,67,67,]),'value_parameter_list':([31,],[84,]),'value_parameter':([31,132,],[85,160,]),'parameter_list':([61,114,],[108,141,]),'parameter':([61,114,140,],[109,109,167,]),'list_access':([67,],[117,]),'array_structure':([68,],[119,]),'casting':([68,],[121,]),'for_initialization':([83,],[127,]),'data_type':([122,],[145,]),'key_declaration':([123,172,],[154,180,]),'body_statement_list':([157,158,168,193,],[174,176,178,195,]),'for_update':([184,],[189,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> OPEN_TAG statement_list CLOSE_TAG','program',3,'p_program','main.py',41),
  ('program -> condition','program',1,'p_program','main.py',42),
  ('program -> math_expression','program',1,'p_program','main.py',43),
  ('statement_list -> statement','statement_list',1,'p_statement_list','main.py',48),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','main.py',49),
  ('statement_list -> empty','statement_list',1,'p_statement_list','main.py',50),
  ('statement -> expression_statement','statement',1,'p_statement','main.py',55),
  ('statement -> function_declaration','statement',1,'p_statement','main.py',56),
  ('statement -> assignment SEMICOLON','statement',2,'p_statement','main.py',57),
  ('statement -> if_statement','statement',1,'p_statement','main.py',58),
  ('statement -> while_statement','statement',1,'p_statement','main.py',59),
  ('statement -> for_statement','statement',1,'p_statement','main.py',60),
  ('statement -> impresion','statement',1,'p_statement','main.py',61),
  ('assignment -> VARIABLE assignment_operator expression','assignment',3,'p_assignment','main.py',66),
  ('assignment -> VARIABLE EQUALS math_expression','assignment',3,'p_assignment','main.py',67),
  ('assignment -> VARIABLE EQUALS array_structure','assignment',3,'p_assignment','main.py',68),
  ('assignment -> VARIABLE EQUALS condition','assignment',3,'p_assignment','main.py',69),
  ('assignment -> VARIABLE PLUS PLUS','assignment',3,'p_assignment','main.py',70),
  ('assignment -> VARIABLE assignment_operator list_access','assignment',3,'p_assignment','main.py',71),
  ('assignment -> VARIABLE EQUALS casting math_expression','assignment',4,'p_assignment','main.py',72),
  ('casting -> OPEN_PARENTHESIS data_type CLOSE_PARENTHESIS','casting',3,'p_casting','main.py',78),
  ('data_type -> INT_T','data_type',1,'p_data_type','main.py',83),
  ('data_type -> INTEGER_T','data_type',1,'p_data_type','main.py',84),
  ('data_type -> FLOAT_T','data_type',1,'p_data_type','main.py',85),
  ('data_type -> DOUBLE_T','data_type',1,'p_data_type','main.py',86),
  ('data_type -> STRING_T','data_type',1,'p_data_type','main.py',87),
  ('data_type -> BOOLEAN_T','data_type',1,'p_data_type','main.py',88),
  ('data_type -> ARRAY_T','data_type',1,'p_data_type','main.py',89),
  ('data_type -> OBJECT_T','data_type',1,'p_data_type','main.py',90),
  ('assignment_operator -> PLUS_EQUALS','assignment_operator',1,'p_assignment_operator','main.py',96),
  ('assignment_operator -> MINUS_EQUALS','assignment_operator',1,'p_assignment_operator','main.py',97),
  ('assignment_operator -> MULTIPLY_EQUALS','assignment_operator',1,'p_assignment_operator','main.py',98),
  ('assignment_operator -> DIVIDE_EQUALS','assignment_operator',1,'p_assignment_operator','main.py',99),
  ('assignment_operator -> MODULO_EQUALS','assignment_operator',1,'p_assignment_operator','main.py',100),
  ('assignment_operator -> CONCATENATION_EQUALS','assignment_operator',1,'p_assignment_operator','main.py',101),
  ('assignment_operator -> LEFT_SHIFT_EQUALS','assignment_operator',1,'p_assignment_operator','main.py',102),
  ('assignment_operator -> RIGHT_SHIFT_EQUALS','assignment_operator',1,'p_assignment_operator','main.py',103),
  ('assignment_operator -> AND_EQUALS','assignment_operator',1,'p_assignment_operator','main.py',104),
  ('assignment_operator -> OR_EQUALS','assignment_operator',1,'p_assignment_operator','main.py',105),
  ('assignment_operator -> XOR_EQUALS','assignment_operator',1,'p_assignment_operator','main.py',106),
  ('assignment_operator -> EQUALS','assignment_operator',1,'p_assignment_operator','main.py',107),
  ('expression_statement -> expression SEMICOLON','expression_statement',2,'p_expression_statement','main.py',112),
  ('function_declaration -> FUNCTION IDENTIFIER OPEN_PARENTHESIS parameter_list CLOSE_PARENTHESIS body_statement_list','function_declaration',6,'p_function_declaration','main.py',117),
  ('body_statement_list -> OPEN_CURLY_BRACKET statement_list CLOSE_CURLY_BRACKET','body_statement_list',3,'p_body_statement_list','main.py',122),
  ('body_statement_list -> OPEN_CURLY_BRACKET empty CLOSE_CURLY_BRACKET','body_statement_list',3,'p_body_statement_list','main.py',123),
  ('body_statement_list -> OPEN_CURLY_BRACKET statement_list RETURN expression SEMICOLON CLOSE_CURLY_BRACKET','body_statement_list',6,'p_body_statement_list','main.py',124),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','main.py',129),
  ('parameter_list -> parameter_list COMMA parameter','parameter_list',3,'p_parameter_list','main.py',130),
  ('parameter_list -> empty','parameter_list',1,'p_parameter_list','main.py',131),
  ('parameter -> VARIABLE','parameter',1,'p_parameter','main.py',136),
  ('parameter -> assignment','parameter',1,'p_parameter','main.py',137),
  ('parameter -> expression','parameter',1,'p_parameter','main.py',138),
  ('value_parameter_list -> value_parameter','value_parameter_list',1,'p_value_parameter_list','main.py',143),
  ('value_parameter_list -> value_parameter_list COMMA value_parameter','value_parameter_list',3,'p_value_parameter_list','main.py',144),
  ('value_parameter_list -> empty','value_parameter_list',1,'p_value_parameter_list','main.py',145),
  ('value_parameter -> expression','value_parameter',1,'p_value_parameter','main.py',150),
  ('empty -> <empty>','empty',0,'p_empty','main.py',155),
  ('expression -> VARIABLE','expression',1,'p_expression','main.py',161),
  ('expression -> NUMBER','expression',1,'p_expression','main.py',162),
  ('expression -> STRING','expression',1,'p_expression','main.py',163),
  ('expression -> BOOLEAN','expression',1,'p_expression','main.py',164),
  ('expression -> NULL','expression',1,'p_expression','main.py',165),
  ('expression -> function_call','expression',1,'p_expression','main.py',166),
  ('expression -> expression PLUS expression','expression',3,'p_expression','main.py',167),
  ('expression -> expression MINUS expression','expression',3,'p_expression','main.py',168),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression','main.py',169),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','main.py',170),
  ('expression -> expression MODULO expression','expression',3,'p_expression','main.py',171),
  ('expression -> expression CONCATENATION expression','expression',3,'p_expression','main.py',172),
  ('expression -> expression CONCATENATION_EQUALS expression','expression',3,'p_expression','main.py',173),
  ('function_call -> IDENTIFIER OPEN_PARENTHESIS parameter_list CLOSE_PARENTHESIS','function_call',4,'p_function_call','main.py',179),
  ('if_statement -> IF OPEN_PARENTHESIS condition CLOSE_PARENTHESIS body_statement_list','if_statement',5,'p_if_statement','main.py',184),
  ('for_statement -> FOR OPEN_PARENTHESIS for_initialization SEMICOLON condition SEMICOLON for_update CLOSE_PARENTHESIS body_statement_list','for_statement',9,'p_for_statement','main.py',189),
  ('for_initialization -> assignment','for_initialization',1,'p_for_initialization','main.py',194),
  ('for_initialization -> empty','for_initialization',1,'p_for_initialization','main.py',195),
  ('for_update -> assignment','for_update',1,'p_for_update','main.py',200),
  ('for_update -> empty','for_update',1,'p_for_update','main.py',201),
  ('while_statement -> WHILE OPEN_PARENTHESIS condition CLOSE_PARENTHESIS body_statement_list','while_statement',5,'p_while_statement','main.py',206),
  ('impresion -> ECHO value_parameter_list SEMICOLON','impresion',3,'p_impresion','main.py',211),
  ('condition -> expression','condition',1,'p_condition','main.py',216),
  ('condition -> condition comparison condition','condition',3,'p_condition','main.py',217),
  ('condition -> OPEN_PARENTHESIS condition comparison condition CLOSE_PARENTHESIS','condition',5,'p_condition','main.py',218),
  ('condition -> OPEN_PARENTHESIS condition CLOSE_PARENTHESIS comparison condition','condition',5,'p_condition','main.py',219),
  ('condition -> condition comparison OPEN_PARENTHESIS condition CLOSE_PARENTHESIS','condition',5,'p_condition','main.py',220),
  ('condition -> NOT condition','condition',2,'p_condition','main.py',221),
  ('comparison -> DOUBLE_EQUALS','comparison',1,'p_comparison','main.py',226),
  ('comparison -> NOT_EQUALS','comparison',1,'p_comparison','main.py',227),
  ('comparison -> GREATER_THAN','comparison',1,'p_comparison','main.py',228),
  ('comparison -> LESS_THAN','comparison',1,'p_comparison','main.py',229),
  ('comparison -> GREATER_THAN_OR_EQUALS','comparison',1,'p_comparison','main.py',230),
  ('comparison -> LESS_THAN_OR_EQUALS','comparison',1,'p_comparison','main.py',231),
  ('comparison -> AND','comparison',1,'p_comparison','main.py',232),
  ('comparison -> OR','comparison',1,'p_comparison','main.py',233),
  ('math_operator -> PLUS','math_operator',1,'p_math_operator','main.py',238),
  ('math_operator -> DIVIDE','math_operator',1,'p_math_operator','main.py',239),
  ('math_operator -> MINUS','math_operator',1,'p_math_operator','main.py',240),
  ('math_operator -> MULTIPLY','math_operator',1,'p_math_operator','main.py',241),
  ('math_operator -> MODULO','math_operator',1,'p_math_operator','main.py',242),
  ('math_expression -> NUMBER','math_expression',1,'p_math_expression','main.py',247),
  ('math_expression -> math_expression math_operator math_expression','math_expression',3,'p_math_expression','main.py',248),
  ('math_expression -> math_expression math_operator VARIABLE','math_expression',3,'p_math_expression','main.py',249),
  ('math_expression -> VARIABLE math_operator math_expression','math_expression',3,'p_math_expression','main.py',250),
  ('math_expression -> OPEN_PARENTHESIS math_expression math_operator math_expression CLOSE_PARENTHESIS','math_expression',5,'p_math_expression','main.py',251),
  ('math_expression -> OPEN_PARENTHESIS math_expression CLOSE_PARENTHESIS math_operator math_expression','math_expression',5,'p_math_expression','main.py',252),
  ('math_expression -> math_expression math_operator OPEN_PARENTHESIS math_expression CLOSE_PARENTHESIS','math_expression',5,'p_math_expression','main.py',253),
  ('array_structure -> OPEN_SQUARE_BRACKET key_declaration CLOSE_SQUARE_BRACKET','array_structure',3,'p_array_structure','main.py',258),
  ('key_declaration -> expression EQUALS GREATER_THAN expression','key_declaration',4,'p_key_declaration','main.py',263),
  ('key_declaration -> key_declaration COMMA key_declaration','key_declaration',3,'p_key_declaration','main.py',264),
  ('key_declaration -> empty','key_declaration',1,'p_key_declaration','main.py',265),
  ('list_access -> VARIABLE OPEN_SQUARE_BRACKET expression CLOSE_SQUARE_BRACKET','list_access',4,'p_list_access','main.py',270),
]
