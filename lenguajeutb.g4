grammar lenguajeutb;

start_rule      : principal;
principal       : (comentario)* NOMBRE_EJERCICIO TEXTO bloques;
bloques         : variables flujo;
flujo           : FLUJO (sentencias)* FIN_FLUJO;
variables       : VARIABLES (declaracion)* FIN_VARIABLES;
declaracion     : TIPO (tipo_basico|tipo_lista|tipo_matriz);
tipo_basico     : TIPO_BASICO NOMBRE IDENTIFICADOR (VALOR_INICIAL atom)?;
tipo_lista      : TIPO_COMPUESTO DE TIPO_BASICO NOMBRE IDENTIFICADOR;
tipo_matriz     : TIPO_COMPUESTO DE TIPO_BASICO NOMBRE IDENTIFICADOR DE TAMANO ENTERO EQUIS ENTERO;
sentencias      : (leer|imprimir|comentario|agregar|cambiar_valor);
leer            : LEER IDENTIFICADOR;
imprimir        : MOSTRAR (IDENTIFICADOR|STRING|lista|matriz);
comentario      : NOTA;
agregar         : AGREGAR A IDENTIFICADOR OP_POSC ENTERO;
cambiar_valor   : CAMBIAR VALOR DE IDENTIFICADOR (conversion|cambiar_lista|cambiar_matriz);
conversion      : POR CONVERTIR IDENTIFICADOR A TIPO_BASICO;
cambiar_lista   : POSICION ENTERO EQUIS ENTERO;
cambiar_matriz  : EN_COORDENADA COORDENADA POR ENTERO;
atom            : IDENTIFICADOR|ENTERO|REAL|BOOL|STRING|CHAR;
lista           : IDENTIFICADOR POSICION ENTERO;
matriz          : IDENTIFICADOR EN_COORDENADA COORDENADA;



NOMBRE_EJERCICIO: 'Nombre_del_ejercicio';
NOTA            : 'nota:' ('A'..'Z'|' '|'a'..'z'|'_'|'0'..'9'|'$')+;
VARIABLES       : 'variables';
FIN_VARIABLES   : 'fin_variables';
FLUJO           : 'Flujo';
FIN_FLUJO       : 'fin_flujo';
VALOR           : 'valor';
DE              : 'de';
AGREGAR         : 'agregar';
OP_POSC         : '<-';
CAMBIAR         : 'cambiar';


POSICION        : 'en_la_posicion';
EN_COORDENADA   : 'en_la_coordenada';
COORDENADA      : '('('0'..'9')+','('0'..'9')+')';
POR             : 'por';
CONVERTIR       : 'convertir';
A               : 'a';
LEER            : 'leer';
MOSTRAR         : 'mostrar_en_pantalla';
TIPO            : 'tipo';
TIPO_COMPUESTO  : ('lista'|'matriz');
TIPO_BASICO     : ('entero'|'real'|'texto'|'booleano'|'caracter'|'lista');


NOMBRE          : 'nombre';
VALOR_INICIAL   : 'valor_inicial';
TAMANO          : 'tamano';
EQUIS           : 'x';



ENTERO          : ('-')?('0'..'9')+;
REAL            : ('-')?('0'..'9')+'.'('0'..'9')+;
CHAR            : ('A'..'Z'|'a'..'z');
BOOL            : 'FALSO'|'VERDADERO';
STRING          : '"'('a'..'z'|'A'..'Z'|'0'..'9'|' '|'-'|'_'|'?'|'!'|'$'|'.'|',')*'"';

IDENTIFICADOR   : '$'('A'..'Z'|'a'..'z'|'_'|'0'..'9')+;
TEXTO           : ('A'..'Z'|'a'..'z'|'_'|'0'..'9')+;

WS              : [ \t\r\n]+ -> skip;

//OBSERVACION 1: LOS INDICES DE DEBEN CONVERTIRSE A POSITIVOS
// YA QUE ESTAN CON EL TOKEN 'ENTERO' QUE ADMITE NUMEROS NEGATIVOS
// APLICA PARA: lista, compuesto, tipo_matriz
