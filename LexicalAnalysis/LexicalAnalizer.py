import ply.lex as lex
import ply.yacc as yacc
import re
import codecs
import os
import sys

directorio = os.path.dirname(os.getcwd()) + "/Tests/"
print(directorio)
from pip._vendor.distlib.compat import raw_input

tokens = [
    'COMA', 'PUNTOCOMA', 'DOSPUNTOS', 'LLAVE_IZQ', 'LLAVE_DER', 'IGUAL', 'PARENTESIS_IZQ', 'PARENTESIS_DER',  # SIMBOLOS

    'ID', 'NUMERO',  # IDENTIDFICADOR, NUMERO

    'DIFERENTE', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL', 'SUMA'  # CONDICONES
]

# 'INC', 'DEC', 'INI', 'MOVER', 'ALEATORIO',  # FUNCIONES
# 'PROC', 'INICIO', 'FINAL', 'LLAMAR'  # PROCEDIMIENTOS

reservadas = {
    'DCL': 'DCL', 'DEFAULT': 'DEFAULT', 'Inicio': 'INICIO',
    'EnCaso': 'ENCASO', 'Cuando': 'CUANDO', 'EnTons': 'ENTONS', 'SiNo': 'SINO',
    'Fin-EnCaso': 'FINENCASO', 'Repita': 'REPITA', 'HastaEncontar': 'HASTAENCONTRAR', 'Desde': 'DESDE',
    'Hasta': 'HASTA', 'Haga': 'HAGA', 'Fin-Desde': 'FINDESDE', 'Fin': 'FIN', 'fin': 'FINPROC', 'inicio': 'INICIOPROC',
    'Inc': 'INC', 'Dec': 'DEC', 'Ini': 'INI', 'Mover': 'MOVER', 'Aleatorio': 'ALEATORIO', 'Proc': 'PROC',
    'Llamar': 'LLAMAR'}

movimientos = {'AF': 'AF', 'F': 'F', 'DFA': 'DFA', 'IFA': 'IFA', 'DFB': 'DFB', 'IFB': 'IFB',
               'A': 'A', 'DAA': 'DAA', 'IAA': 'IAA', 'DAB': 'DAB', 'IAB': 'IAB', 'AA': 'AA'}

reservadas.update(movimientos)

tokens = list(reservadas.values()) + tokens

t_ignore = '  \t'

t_COMA = r','
t_PUNTOCOMA = r';'
t_DOSPUNTOS = r':'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_IGUAL = r'='
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_DIFERENTE = r'<>'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_SUMA = r'\+'


def t_InicioProc(t):
    r'inicio'
    t.value = "INICIOPROC"
    t.type = t.value
    return t


def t_FinProc(t):
    r'fin'
    t.value = "FINPROC"
    t.type = t.value
    return t


def t_FinDesde(t):
    r'Fin-Desde'
    t.value = "FINDESDE"
    t.type = "FINDESDE"
    return t


def t_FinEnCaso(t):
    r'Fin-EnCaso'
    print(t.value)
    t.value = "FINENCASO"
    t.type = t.value
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_#@]*'
    if t.value.upper() in reservadas.values():
        t.value = t.value.upper()
        t.type = t.value
    return t


def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded


def buscarFichero(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont) + ". " + file)
        cont += 1

    while respuesta == False:
        numArchivo = raw_input('\n')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break
    print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])

    return files[int(numArchivo) - 1]


archivo = buscarFichero(directorio)
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()
analizador.input(cadena)
'''
while True:
    tok = analizador.token()
    if not tok: break
    print(tok)
'''


# =================================================================================================================== */
#                                        Here Starts the Sintactic Analizer
# =================================================================================================================== */

def p_Start(p):
    '''
    Start : code
          | empty
    '''
    print(p[1])


def p_Code(p):
    '''
    code : INICIO DOSPUNTOS cuerpo FIN PUNTOCOMA procedimiento
    '''
    if (p[6] == '$'):
        p[0] = (p[1], p[3], p[4])
    else:
        p[0] = (p[1], p[3], p[4], p[6])


def p_cuerpo(p):
    '''
    cuerpo : variable
            | expresion
    '''
    p[0] = p[1]


def p_Variable(p):
    '''
    variable : sinini PUNTOCOMA cuerpo
            | ini PUNTOCOMA cuerpo
            | empty empty empty
    '''
    if (p[3] != '$'):

        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]


def p_expresion(p):
    '''
    expresion : condicion1 expresion
            | condicion2 expresion
            | repita expresion
            | hacer expresion
            | funcion expresion
            | llamarProc expresion
            | empty empty
    '''
    if (p[2] != '$'):
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]


def p_procedimiento(p):
    '''
        procedimiento : PROC ID  PARENTESIS_IZQ ID PARENTESIS_DER INICIOPROC DOSPUNTOS expresion FINPROC PUNTOCOMA procedimiento
                     | empty empty empty empty empty empty empty empty empty empty empty
    '''
    if p[11] != '$':
        p[0] = (p[1], p[2], p[4], p[6], p[8], p[9], p[11])
    else:
        p[0] = p[1]


def p_repita(p):
    '''
     repita : REPITA LLAVE_IZQ expresion LLAVE_DER HASTAENCONTRAR ID condicion sentencia PUNTOCOMA
    '''
    p[0] = (p[1], p[3], p[5], p[6], p[7], p[8])


def p_condicion2(p):
    '''
    condicion2 : ENCASO ID cond2Aux1 FINENCASO PUNTOCOMA
    '''
    p[0] = (p[1], p[2], p[3], p[4])


def p_cond2Aux1(p):
    '''
    cond2Aux1 : cond2Aux2 SINO LLAVE_IZQ expresion LLAVE_DER
                | empty empty empty empty empty
    '''
    if (p[5] != '$'):
        p[0] = (p[1], p[2], p[4])
    else:
        p[0] = p[1]


def p_cond2Aux2(p):
    '''
        cond2Aux2 : CUANDO  condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond2Aux2
                | empty empty empty empty empty empty empty empty
        '''
    if p[8] != '$':
        p[0] = (p[1], p[2], p[3], p[4], p[6], p[8])
    elif p[8] == '$' and p[1] != '$':
        p[0] = (p[1], p[2], p[3], p[4], p[6])
    elif p[1] == '$':
        p[0] = p[1]


def p_condicion1(p):
    '''
    condicion1 : ENCASO cond1Aux1 FINENCASO PUNTOCOMA
    '''
    p[0] = (p[1], p[2], p[3])


def p_cond1Aux1(p):
    '''
    cond1Aux1 : cond1Aux2 SINO LLAVE_IZQ expresion LLAVE_DER
            | empty empty empty empty empty
    '''
    if (p[5] != '$'):
        p[0] = (p[1], p[2], p[4])
    else:
        p[0] = p[1]


def p_cond1Aux2(p):
    '''
    cond1Aux2 : CUANDO ID condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond1Aux2
            | empty empty empty empty empty empty empty empty empty
    '''
    if p[9] != '$':
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[7], p[9])
    elif p[9] == '$' and p[1] != '$':
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[7])
    elif p[1] == '$':
        p[0] = p[1]


def p_hacer(p):
    '''
    hacer : DESDE ID IGUAL sentencia HASTA sentencia HAGA LLAVE_IZQ expresion LLAVE_DER FINDESDE PUNTOCOMA
    '''
    p[0] = (p[1], p[2], p[4], p[5], p[6], p[7], p[9], p[11])


def p_funcion(p):
    '''
    funcion : Aleatorio
            | Mover
            | funcionAlge
    '''
    p[0] = p[1]


def p_llamarProc(p):
    '''
    llamarProc : LLAMAR ID PARENTESIS_IZQ parametro PARENTESIS_DER PUNTOCOMA
    '''
    p[0] = (p[1], p[2], p[4])


def p_parametro(p):
    '''
    parametro : ID
              | NUMERO
              | empty
    '''
    p[0] = p[1]


def p_funcion_Alge(p):
    '''
    funcionAlge : INC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA
             | DEC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA
             | INI PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA
    '''

    p[0] = (p[1], p[3], p[4], p[5])


def p_mover(p):
    '''
    Mover : MOVER PARENTESIS_IZQ paramMover PARENTESIS_DER PUNTOCOMA
    '''
    p[0] = (p[1], p[3])


def p_ParamMover(p):
    '''
    paramMover : AF
                | F
                | DFA
                | IFA
                | DFB
                | IFB
                | A
                | DAA
                | IAA
                | DAB
                | IAB
                | AA
    '''
    p[0] = p[1]


def p_aleatorio(p):
    '''
    Aleatorio : ALEATORIO PARENTESIS_IZQ PARENTESIS_DER PUNTOCOMA
    '''
    p[0] = p[1]


def p_condicion(p):
    '''
    condicion : IGUAL
              | MAYOR
              | MENOR
              | DIFERENTE
              | MAYORIGUAL
              | MENORIGUAL
    '''

    p[0] = p[1]


def p_sentencia(p):
    '''
    sentencia : ID
               | NUMERO
    '''
    p[0] = p[1]


def p_VariableIni(p):
    '''
    ini : DCL ID IGUAL NUMERO
    '''
    p[0] = (p[1], p[2], p[4])


def p_VariableNoIni(p):
    '''
    sinini : DCL ID
    '''
    p[0] = (p[1], p[2], 'DEFAULT')


def p_empty(p):
    '''
    empty :
    '''
    p[0] = '$'




parser = yacc.yacc()

parser.parse(cadena)
