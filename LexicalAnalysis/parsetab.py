
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMA CUANDO DCL DEFAULT DESDE DIFERENTE DOSPUNTOS ENCASO ENTONS FIN FINDESDE FINENCASO FINPROC HAGA HASTA HASTAENCONTRAR ID IGUAL INICIO INICIOPROC LLAVE_DER LLAVE_IZQ MAYOR MAYORIGUAL MENOR MENORIGUAL NUMERO PARENTECIS_DER PARENTECIS_IZQ PUNTOCOMA REPITA SINO SUMA\n    Start : code\n          | empty\n    \n    code : INICIO DOSPUNTOS cuerpo FIN PUNTOCOMA procedimiento\n\n    \n        procedimiento : ID\n                     | empty\n    \n    variable : sinini PUNTOCOMA cuerpo\n            | ini PUNTOCOMA cuerpo\n            | empty empty empty\n    \n    cuerpo : variable\n            | expresion\n    \n    expresion : condicion1 expresion\n            | condicion2 expresion\n            | repita expresion\n            | empty empty\n\n    \n     repita : REPITA LLAVE_IZQ expresion LLAVE_DER HASTAENCONTRAR ID condicion sentencia PUNTOCOMA\n\n    \n    condicion2 : ENCASO ID cond2Aux2 FINENCASO PUNTOCOMA\n\n    \n    cond2Aux2 : CUANDO condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER SINO LLAVE_IZQ expresion LLAVE_DER\n\n    \n    condicion1 : ENCASO cond1Aux FINENCASO PUNTOCOMA\n\n    \n    cond1Aux : CUANDO ID condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER SINO LLAVE_IZQ expresion LLAVE_DER\n\n    \n    condicion : IGUAL\n              | MAYOR\n              | MENOR\n              | DIFERENTE\n              | MAYORIGUAL\n              | MENORIGUAL\n\n    \n    sentencia : ID\n               | NUMERO\n\n    \n    ini : DCL ID IGUAL NUMERO\n\n    \n    sinini : DCL ID\n\n    \n    empty :\n    '
    
_lr_action_items = {'INICIO':([0,],[4,]),'$end':([0,1,2,3,31,42,43,44,],[-30,0,-1,-2,-30,-3,-4,-5,]),'DOSPUNTOS':([4,],[5,]),'DCL':([5,19,20,],[15,15,15,]),'FIN':([5,6,7,8,11,12,13,14,19,20,21,22,23,24,25,32,33,34,35,46,57,74,],[-30,18,-9,-10,-30,-30,-30,-30,-30,-30,-14,-11,-30,-12,-13,-6,-7,-8,-14,-18,-16,-15,]),'ENCASO':([5,12,13,14,19,20,30,46,57,66,67,74,77,78,],[16,16,16,16,16,16,16,-18,-16,16,16,-15,16,16,]),'REPITA':([5,12,13,14,19,20,30,46,57,66,67,74,77,78,],[17,17,17,17,17,17,17,-18,-16,17,17,-15,17,17,]),'PUNTOCOMA':([9,10,18,26,37,45,47,59,60,71,],[19,20,31,-29,46,-28,57,-26,-27,74,]),'LLAVE_DER':([12,13,14,22,23,24,25,30,35,41,46,57,66,67,69,70,74,77,78,79,80,],[-30,-30,-30,-11,-30,-12,-13,-30,-14,56,-18,-16,-30,-30,72,73,-15,-30,-30,81,82,]),'ID':([15,16,29,31,48,49,50,51,52,53,54,55,62,68,],[26,28,40,43,59,-20,-21,-22,-23,-24,-25,59,65,59,]),'CUANDO':([16,28,],[29,39,]),'LLAVE_IZQ':([17,63,64,75,76,],[30,66,67,77,78,]),'IGUAL':([26,39,40,65,],[36,49,49,49,]),'FINENCASO':([27,38,81,82,],[37,47,-17,-19,]),'NUMERO':([36,48,49,50,51,52,53,54,55,68,],[45,60,-20,-21,-22,-23,-24,-25,60,60,]),'MAYOR':([39,40,65,],[50,50,50,]),'MENOR':([39,40,65,],[51,51,51,]),'DIFERENTE':([39,40,65,],[52,52,52,]),'MAYORIGUAL':([39,40,65,],[53,53,53,]),'MENORIGUAL':([39,40,65,],[54,54,54,]),'HASTAENCONTRAR':([56,],[62,]),'ENTONS':([58,59,60,61,],[63,-26,-27,64,]),'SINO':([72,73,],[75,76,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Start':([0,],[1,]),'code':([0,],[2,]),'empty':([0,5,11,12,13,14,19,20,21,23,30,31,66,67,77,78,],[3,11,21,23,23,23,11,11,34,35,23,44,23,23,23,23,]),'cuerpo':([5,19,20,],[6,32,33,]),'variable':([5,19,20,],[7,7,7,]),'expresion':([5,12,13,14,19,20,30,66,67,77,78,],[8,22,24,25,8,8,41,69,70,79,80,]),'sinini':([5,19,20,],[9,9,9,]),'ini':([5,19,20,],[10,10,10,]),'condicion1':([5,12,13,14,19,20,30,66,67,77,78,],[12,12,12,12,12,12,12,12,12,12,12,]),'condicion2':([5,12,13,14,19,20,30,66,67,77,78,],[13,13,13,13,13,13,13,13,13,13,13,]),'repita':([5,12,13,14,19,20,30,66,67,77,78,],[14,14,14,14,14,14,14,14,14,14,14,]),'cond1Aux':([16,],[27,]),'cond2Aux2':([28,],[38,]),'procedimiento':([31,],[42,]),'condicion':([39,40,65,],[48,55,68,]),'sentencia':([48,55,68,],[58,61,71,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Start","S'",1,None,None,None),
  ('Start -> code','Start',1,'p_Start','LexicalAnalizer.py',149),
  ('Start -> empty','Start',1,'p_Start','LexicalAnalizer.py',150),
  ('code -> INICIO DOSPUNTOS cuerpo FIN PUNTOCOMA procedimiento','code',6,'p_Code','LexicalAnalizer.py',157),
  ('procedimiento -> ID','procedimiento',1,'p_procedimiento','LexicalAnalizer.py',167),
  ('procedimiento -> empty','procedimiento',1,'p_procedimiento','LexicalAnalizer.py',168),
  ('variable -> sinini PUNTOCOMA cuerpo','variable',3,'p_Variable','LexicalAnalizer.py',176),
  ('variable -> ini PUNTOCOMA cuerpo','variable',3,'p_Variable','LexicalAnalizer.py',177),
  ('variable -> empty empty empty','variable',3,'p_Variable','LexicalAnalizer.py',178),
  ('cuerpo -> variable','cuerpo',1,'p_cuerpo','LexicalAnalizer.py',190),
  ('cuerpo -> expresion','cuerpo',1,'p_cuerpo','LexicalAnalizer.py',191),
  ('expresion -> condicion1 expresion','expresion',2,'p_expresion','LexicalAnalizer.py',199),
  ('expresion -> condicion2 expresion','expresion',2,'p_expresion','LexicalAnalizer.py',200),
  ('expresion -> repita expresion','expresion',2,'p_expresion','LexicalAnalizer.py',201),
  ('expresion -> empty empty','expresion',2,'p_expresion','LexicalAnalizer.py',202),
  ('repita -> REPITA LLAVE_IZQ expresion LLAVE_DER HASTAENCONTRAR ID condicion sentencia PUNTOCOMA','repita',9,'p_repita','LexicalAnalizer.py',212),
  ('condicion2 -> ENCASO ID cond2Aux2 FINENCASO PUNTOCOMA','condicion2',5,'p_condicion2','LexicalAnalizer.py',219),
  ('cond2Aux2 -> CUANDO condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER SINO LLAVE_IZQ expresion LLAVE_DER','cond2Aux2',11,'p_cond2Aux','LexicalAnalizer.py',226),
  ('condicion1 -> ENCASO cond1Aux FINENCASO PUNTOCOMA','condicion1',4,'p_condicion1','LexicalAnalizer.py',234),
  ('cond1Aux -> CUANDO ID condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER SINO LLAVE_IZQ expresion LLAVE_DER','cond1Aux',12,'p_cond1Aux','LexicalAnalizer.py',241),
  ('condicion -> IGUAL','condicion',1,'p_condicion','LexicalAnalizer.py',249),
  ('condicion -> MAYOR','condicion',1,'p_condicion','LexicalAnalizer.py',250),
  ('condicion -> MENOR','condicion',1,'p_condicion','LexicalAnalizer.py',251),
  ('condicion -> DIFERENTE','condicion',1,'p_condicion','LexicalAnalizer.py',252),
  ('condicion -> MAYORIGUAL','condicion',1,'p_condicion','LexicalAnalizer.py',253),
  ('condicion -> MENORIGUAL','condicion',1,'p_condicion','LexicalAnalizer.py',254),
  ('sentencia -> ID','sentencia',1,'p_sentencia','LexicalAnalizer.py',262),
  ('sentencia -> NUMERO','sentencia',1,'p_sentencia','LexicalAnalizer.py',263),
  ('ini -> DCL ID IGUAL NUMERO','ini',4,'p_VariableIni','LexicalAnalizer.py',270),
  ('sinini -> DCL ID','sinini',2,'p_VariableNoIni','LexicalAnalizer.py',277),
  ('empty -> <empty>','empty',0,'p_empty','LexicalAnalizer.py',287),
]
