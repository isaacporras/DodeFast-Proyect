def runSemanticAnalizer(parse):
    try:
        inicio(parse[1])
        procedimientos(parse[3])
    except:
        print('error de estructura')


def inicio(cuerpo):
    print(cuerpo)
    print(1)
    for i in cuerpo:
        print(i)
        print('\n')
    print(2)


def procedimientos(cuerpo):
    print(cuerpo)
