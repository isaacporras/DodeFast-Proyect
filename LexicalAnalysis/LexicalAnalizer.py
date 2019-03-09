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
    'COMA', 'PUNTOCOMA', 'DOSPUNTOS', 'LLAVE_IZQ', 'LLAVE_DER', 'IGUAL', 'PARENTECIS_IZQ', 'PARENTECIS_DER',  # SIMBOLOS

    'ID', 'NUMERO',  # IDENTIDFICADOR, NUMERO

    'DIFERENTE', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL','SUMA'  # CONDICONES
]

# 'INC', 'DEC', 'INI', 'MOVER', 'ALEATORIO',  # FUNCIONES
# 'PROC', 'INICIO', 'FINAL', 'LLAMAR'  # PROCEDIMIENTOS

reservadas = {
    'DCL': 'DCL', 'DEFAULT': 'DEFAULT','Inicio':'INICIO',
    'EnCaso': 'ENCASO', 'Cuando': 'CUANDO', 'EnTons': 'ENTONS', 'SiNo': 'SINO',
    'Fin-EnCaso': 'FINENCASO','Repita': 'REPITA', 'HastaEncontar': 'HASTAENCONTRAR', 'Desde': 'DESDE',
    'Hasta': 'HASTA', 'Haga': 'HAGA','Fin-Desde': 'FINDESDE','Fin':'FIN','fin':'FINPROC', 'inicio':'INICIOPROC'}

tokens =list(reservadas.values()) + tokens

t_ignore = '  \t'


t_COMA = r','
t_PUNTOCOMA = r';'
t_DOSPUNTOS = r':'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_IGUAL = r'='
t_PARENTECIS_IZQ = r'\('
t_PARENTECIS_DER = r'\)'
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
    t.value = "fin"
    t.type = "FINPROC"
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
    if(p[6] == '$'):
        p[0] = (p[1], p[3], p[4])
    else:
        p[0] = (p[1], p[3], p[4], p[6])

def p_procedimiento(p):
    '''
        procedimiento : ID
                     | empty
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




def p_cuerpo(p):


    '''
    cuerpo : variable
            | expresion
    '''
    p[0] = p[1]

def p_expresion(p):
    '''
    expresion : condicion1 expresion
            | condicion2 expresion
            | repita expresion
            | empty empty

    '''
    if(p[2] != '$'):
        p[0] = (p[1],p[2])
    else:
        p[0] = p[1]

def p_repita(p):
    '''
     repita : REPITA LLAVE_IZQ expresion LLAVE_DER HASTAENCONTRAR ID condicion sentencia PUNTOCOMA

    '''
    p[0] = (p[1],p[3],p[5],p[6],p[7],p[8])

def p_condicion2(p):
    '''
    condicion2 : ENCASO ID cond2Aux2 FINENCASO PUNTOCOMA

    '''
    p[0] = (p[1], p[2], p[3], p[4])

def p_cond2Aux(p):
    '''
    cond2Aux2 : CUANDO condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER SINO LLAVE_IZQ expresion LLAVE_DER

    '''

    p[0] = (p[1],p[2],p[3],p[4], p[6],p[8],p[10])

def p_condicion1(p):
    '''
    condicion1 : ENCASO cond1Aux FINENCASO PUNTOCOMA

    '''
    p[0] = (p[1], p[2], p[3])

def p_cond1Aux(p):
    '''
    cond1Aux : CUANDO ID condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER SINO LLAVE_IZQ expresion LLAVE_DER

    '''

    p[0] = (p[1],p[2],p[3],p[4], p[5],p[7],p[9], p[11])

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