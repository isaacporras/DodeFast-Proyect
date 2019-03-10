
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A AA AF ALEATORIO COMA CUANDO DAA DAB DCL DEC DEFAULT DESDE DFA DFB DIFERENTE DOSPUNTOS ENCASO ENTONS F FIN FINDESDE FINENCASO FINPROC HAGA HASTA HASTAENCONTRAR IAA IAB ID IFA IFB IGUAL INC INI INICIO INICIOPROC LLAMAR LLAVE_DER LLAVE_IZQ MAYOR MAYORIGUAL MENOR MENORIGUAL MOVER NUMERO PARENTESIS_DER PARENTESIS_IZQ PROC PUNTOCOMA REPITA SINO SUMA\n    Start : code\n          | empty\n    \n    code : INICIO DOSPUNTOS cuerpo FIN PUNTOCOMA procedimiento\n    \n    cuerpo : variable\n            | expresion\n    \n    variable : sinini PUNTOCOMA cuerpo\n            | ini PUNTOCOMA cuerpo\n            | empty empty empty\n    \n    sinini : DCL ID\n    \n    ini : DCL ID IGUAL NUMERO\n    \n    expresion : condicion1 expresion\n            | condicion2 expresion\n            | repita expresion\n            | hacer expresion\n            | funcion expresion\n            | llamarProc expresion\n            | empty empty\n    \n    condicion1 : ENCASO cond1Aux1 FINENCASO PUNTOCOMA\n    \n    cond1Aux1 : cond1Aux2 SINO LLAVE_IZQ expresion LLAVE_DER\n            | empty empty empty empty empty\n    \n    cond1Aux2 : CUANDO ID condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond1Aux2\n            | empty empty empty empty empty empty empty empty empty\n    \n    condicion2 : ENCASO ID cond2Aux1 FINENCASO PUNTOCOMA\n    \n    cond2Aux1 : cond2Aux2 SINO LLAVE_IZQ expresion LLAVE_DER\n                | empty empty empty empty empty\n    \n        cond2Aux2 : CUANDO  condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond2Aux2\n                | empty empty empty empty empty empty empty empty\n        \n    condicion : IGUAL\n              | MAYOR\n              | MENOR\n              | DIFERENTE\n              | MAYORIGUAL\n              | MENORIGUAL\n    \n    sentencia : ID\n               | NUMERO\n    \n     repita : REPITA LLAVE_IZQ expresion LLAVE_DER HASTAENCONTRAR ID condicion sentencia PUNTOCOMA\n    \n    hacer : DESDE ID IGUAL sentencia HASTA sentencia HAGA LLAVE_IZQ expresion LLAVE_DER FINDESDE PUNTOCOMA\n    \n    funcion : Aleatorio\n            | Mover\n            | funcionAlge\n    \n    Aleatorio : ALEATORIO PARENTESIS_IZQ PARENTESIS_DER PUNTOCOMA\n    \n    Mover : MOVER PARENTESIS_IZQ paramMover PARENTESIS_DER PUNTOCOMA\n    \n    paramMover : AF\n                | F\n                | DFA\n                | IFA\n                | DFB\n                | IFB\n                | A\n                | DAA\n                | IAA\n                | DAB\n                | IAB\n                | AA\n    \n    funcionAlge : INC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA\n             | DEC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA\n             | INI PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA\n    \n        procedimiento : PROC ID PARENTESIS_IZQ parametro PARENTESIS_DER INICIOPROC DOSPUNTOS expresion FINPROC PUNTOCOMA procedimiento\n                     | empty empty empty empty empty empty empty empty empty empty empty\n    \n    parametro : ID COMA parametro\n              | ID empty empty\n              | NUMERO COMA parametro\n              | NUMERO empty empty\n\n    \n    llamarProc : LLAMAR ID PARENTESIS_IZQ parametro PARENTESIS_DER PUNTOCOMA\n    \n    empty :\n    '
    
_lr_action_items = {'INICIO':([0,],[4,]),'$end':([0,1,2,3,56,90,92,121,141,159,171,179,187,196,201,205,206,209,210,],[-65,0,-1,-2,-65,-3,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-58,-59,]),'DOSPUNTOS':([4,178,],[5,186,]),'DCL':([5,32,33,],[18,18,18,]),'FIN':([5,6,7,8,11,12,13,14,15,16,17,22,23,24,32,33,34,35,36,37,38,39,40,41,57,58,59,60,94,115,122,136,152,167,168,169,184,204,],[-65,31,-4,-5,-65,-65,-65,-65,-65,-65,-65,-38,-39,-40,-65,-65,-17,-11,-65,-12,-13,-14,-15,-16,-6,-7,-8,-17,-18,-41,-23,-42,-64,-55,-56,-57,-36,-37,]),'ENCASO':([5,12,13,14,15,16,17,22,23,24,32,33,48,94,105,115,122,123,136,152,162,164,167,168,169,177,184,186,204,],[19,19,19,19,19,19,19,-38,-39,-40,19,19,19,-18,19,-41,-23,19,-42,-64,19,19,-55,-56,-57,19,-36,19,-37,]),'REPITA':([5,12,13,14,15,16,17,22,23,24,32,33,48,94,105,115,122,123,136,152,162,164,167,168,169,177,184,186,204,],[20,20,20,20,20,20,20,-38,-39,-40,20,20,20,-18,20,-41,-23,20,-42,-64,20,20,-55,-56,-57,20,-36,20,-37,]),'DESDE':([5,12,13,14,15,16,17,22,23,24,32,33,48,94,105,115,122,123,136,152,162,164,167,168,169,177,184,186,204,],[21,21,21,21,21,21,21,-38,-39,-40,21,21,21,-18,21,-41,-23,21,-42,-64,21,21,-55,-56,-57,21,-36,21,-37,]),'LLAMAR':([5,12,13,14,15,16,17,22,23,24,32,33,48,94,105,115,122,123,136,152,162,164,167,168,169,177,184,186,204,],[25,25,25,25,25,25,25,-38,-39,-40,25,25,25,-18,25,-41,-23,25,-42,-64,25,25,-55,-56,-57,25,-36,25,-37,]),'ALEATORIO':([5,12,13,14,15,16,17,22,23,24,32,33,48,94,105,115,122,123,136,152,162,164,167,168,169,177,184,186,204,],[26,26,26,26,26,26,26,-38,-39,-40,26,26,26,-18,26,-41,-23,26,-42,-64,26,26,-55,-56,-57,26,-36,26,-37,]),'MOVER':([5,12,13,14,15,16,17,22,23,24,32,33,48,94,105,115,122,123,136,152,162,164,167,168,169,177,184,186,204,],[27,27,27,27,27,27,27,-38,-39,-40,27,27,27,-18,27,-41,-23,27,-42,-64,27,27,-55,-56,-57,27,-36,27,-37,]),'INC':([5,12,13,14,15,16,17,22,23,24,32,33,48,94,105,115,122,123,136,152,162,164,167,168,169,177,184,186,204,],[28,28,28,28,28,28,28,-38,-39,-40,28,28,28,-18,28,-41,-23,28,-42,-64,28,28,-55,-56,-57,28,-36,28,-37,]),'DEC':([5,12,13,14,15,16,17,22,23,24,32,33,48,94,105,115,122,123,136,152,162,164,167,168,169,177,184,186,204,],[29,29,29,29,29,29,29,-38,-39,-40,29,29,29,-18,29,-41,-23,29,-42,-64,29,29,-55,-56,-57,29,-36,29,-37,]),'INI':([5,12,13,14,15,16,17,22,23,24,32,33,48,94,105,115,122,123,136,152,162,164,167,168,169,177,184,186,204,],[30,30,30,30,30,30,30,-38,-39,-40,30,30,30,-18,30,-41,-23,30,-42,-64,30,30,-55,-56,-57,30,-36,30,-37,]),'PUNTOCOMA':([9,10,31,42,62,73,93,95,109,111,116,133,155,156,157,176,199,200,],[32,33,56,-9,94,115,-10,122,-34,-35,136,152,167,168,169,184,204,205,]),'LLAVE_DER':([12,13,14,15,16,17,22,23,24,35,36,37,38,39,40,41,48,60,70,94,105,115,122,123,126,136,142,152,162,164,167,168,169,173,175,177,184,185,204,],[-65,-65,-65,-65,-65,-65,-38,-39,-40,-11,-65,-12,-13,-14,-15,-16,-65,-17,108,-18,-65,-41,-23,-65,145,-42,160,-64,-65,-65,-55,-56,-57,181,183,-65,-36,194,-37,]),'FINPROC':([12,13,14,15,16,17,22,23,24,35,36,37,38,39,40,41,60,94,115,122,136,152,167,168,169,184,186,195,204,],[-65,-65,-65,-65,-65,-65,-38,-39,-40,-11,-65,-12,-13,-14,-15,-16,-17,-18,-41,-23,-42,-64,-55,-56,-57,-36,-65,200,-37,]),'ID':([18,19,21,25,47,53,54,55,71,72,91,98,99,100,101,102,103,104,107,117,118,119,129,130,131,134,140,165,],[42,44,49,50,69,87,88,89,109,112,120,109,-28,-29,-30,-31,-32,-33,109,109,109,109,148,109,112,112,112,109,]),'CUANDO':([19,44,181,183,],[47,66,66,47,]),'FINENCASO':([19,43,44,46,63,65,68,97,106,124,127,143,145,146,160,161,],[-65,62,-65,-65,95,-65,-65,-65,-65,-65,-65,-65,-19,-20,-24,-25,]),'SINO':([19,44,45,46,64,65,68,97,106,124,127,143,146,161,163,172,174,180,181,182,183,188,189,190,191,192,193,197,198,202,203,207,208,211,212,],[-65,-65,67,-65,96,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-27,-26,-65,-22,-21,-65,-65,-65,-65,-65,-65,-65,-65,-65,]),'LLAVE_IZQ':([20,67,96,144,147,166,],[48,105,123,162,164,177,]),'PARENTESIS_IZQ':([26,27,28,29,30,50,120,],[51,52,53,54,55,72,140,]),'IGUAL':([42,49,66,69,148,],[61,71,99,99,99,]),'PARENTESIS_DER':([51,74,75,76,77,78,79,80,81,82,83,84,85,86,109,111,112,113,114,132,135,137,138,139,150,151,153,154,158,],[73,116,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-34,-35,-65,133,-65,-65,-65,155,156,157,-60,-61,-62,-63,170,]),'AF':([52,],[75,]),'F':([52,],[76,]),'DFA':([52,],[77,]),'IFA':([52,],[78,]),'DFB':([52,],[79,]),'IFB':([52,],[80,]),'A':([52,],[81,]),'DAA':([52,],[82,]),'IAA':([52,],[83,]),'DAB':([52,],[84,]),'IAB':([52,],[85,]),'AA':([52,],[86,]),'PROC':([56,205,],[91,91,]),'NUMERO':([61,71,72,98,99,100,101,102,103,104,107,117,118,119,130,131,134,140,165,],[93,111,114,111,-28,-29,-30,-31,-32,-33,111,111,111,111,111,114,114,114,111,]),'MAYOR':([66,69,148,],[100,100,100,]),'MENOR':([66,69,148,],[101,101,101,]),'DIFERENTE':([66,69,148,],[102,102,102,]),'MAYORIGUAL':([66,69,148,],[103,103,103,]),'MENORIGUAL':([66,69,148,],[104,104,104,]),'COMA':([87,88,89,112,114,],[117,118,119,131,134,]),'HASTAENCONTRAR':([108,],[129,]),'HASTA':([109,110,111,],[-34,130,-35,]),'ENTONS':([109,111,125,128,],[-34,-35,144,147,]),'HAGA':([109,111,149,],[-34,-35,166,]),'INICIOPROC':([170,],[178,]),'FINDESDE':([194,],[199,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Start':([0,],[1,]),'code':([0,],[2,]),'empty':([0,5,11,12,13,14,15,16,17,19,32,33,34,36,44,46,48,56,65,68,92,97,105,106,112,114,121,123,124,127,132,135,141,143,146,159,161,162,163,164,171,172,174,177,179,180,181,182,183,186,187,190,193,196,197,198,201,202,203,205,206,207,208,211,212,],[3,11,34,36,36,36,36,36,36,46,11,11,59,60,65,68,36,92,97,106,121,124,36,127,132,135,141,36,143,146,151,154,159,161,163,171,172,36,174,36,179,180,182,36,187,188,190,191,193,36,196,197,198,201,202,203,206,207,208,92,210,211,212,172,163,]),'cuerpo':([5,32,33,],[6,57,58,]),'variable':([5,32,33,],[7,7,7,]),'expresion':([5,12,13,14,15,16,17,32,33,48,105,123,162,164,177,186,],[8,35,37,38,39,40,41,8,8,70,126,142,173,175,185,195,]),'sinini':([5,32,33,],[9,9,9,]),'ini':([5,32,33,],[10,10,10,]),'condicion1':([5,12,13,14,15,16,17,32,33,48,105,123,162,164,177,186,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'condicion2':([5,12,13,14,15,16,17,32,33,48,105,123,162,164,177,186,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'repita':([5,12,13,14,15,16,17,32,33,48,105,123,162,164,177,186,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'hacer':([5,12,13,14,15,16,17,32,33,48,105,123,162,164,177,186,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'funcion':([5,12,13,14,15,16,17,32,33,48,105,123,162,164,177,186,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'llamarProc':([5,12,13,14,15,16,17,32,33,48,105,123,162,164,177,186,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'Aleatorio':([5,12,13,14,15,16,17,32,33,48,105,123,162,164,177,186,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'Mover':([5,12,13,14,15,16,17,32,33,48,105,123,162,164,177,186,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'funcionAlge':([5,12,13,14,15,16,17,32,33,48,105,123,162,164,177,186,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'cond1Aux1':([19,],[43,]),'cond1Aux2':([19,183,],[45,192,]),'cond2Aux1':([44,],[63,]),'cond2Aux2':([44,181,],[64,189,]),'paramMover':([52,],[74,]),'procedimiento':([56,205,],[90,209,]),'condicion':([66,69,148,],[98,107,165,]),'sentencia':([71,98,107,117,118,119,130,165,],[110,125,128,137,138,139,149,176,]),'parametro':([72,131,134,140,],[113,150,153,158,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Start","S'",1,None,None,None),
  ('Start -> code','Start',1,'p_Start','SintacticAnalizer.py',14),
  ('Start -> empty','Start',1,'p_Start','SintacticAnalizer.py',15),
  ('code -> INICIO DOSPUNTOS cuerpo FIN PUNTOCOMA procedimiento','code',6,'p_Code','SintacticAnalizer.py',23),
  ('cuerpo -> variable','cuerpo',1,'p_cuerpo','SintacticAnalizer.py',33),
  ('cuerpo -> expresion','cuerpo',1,'p_cuerpo','SintacticAnalizer.py',34),
  ('variable -> sinini PUNTOCOMA cuerpo','variable',3,'p_Variable','SintacticAnalizer.py',41),
  ('variable -> ini PUNTOCOMA cuerpo','variable',3,'p_Variable','SintacticAnalizer.py',42),
  ('variable -> empty empty empty','variable',3,'p_Variable','SintacticAnalizer.py',43),
  ('sinini -> DCL ID','sinini',2,'p_VariableNoIni','SintacticAnalizer.py',54),
  ('ini -> DCL ID IGUAL NUMERO','ini',4,'p_VariableIni','SintacticAnalizer.py',61),
  ('expresion -> condicion1 expresion','expresion',2,'p_expresion','SintacticAnalizer.py',68),
  ('expresion -> condicion2 expresion','expresion',2,'p_expresion','SintacticAnalizer.py',69),
  ('expresion -> repita expresion','expresion',2,'p_expresion','SintacticAnalizer.py',70),
  ('expresion -> hacer expresion','expresion',2,'p_expresion','SintacticAnalizer.py',71),
  ('expresion -> funcion expresion','expresion',2,'p_expresion','SintacticAnalizer.py',72),
  ('expresion -> llamarProc expresion','expresion',2,'p_expresion','SintacticAnalizer.py',73),
  ('expresion -> empty empty','expresion',2,'p_expresion','SintacticAnalizer.py',74),
  ('condicion1 -> ENCASO cond1Aux1 FINENCASO PUNTOCOMA','condicion1',4,'p_condicion1','SintacticAnalizer.py',84),
  ('cond1Aux1 -> cond1Aux2 SINO LLAVE_IZQ expresion LLAVE_DER','cond1Aux1',5,'p_cond1Aux1','SintacticAnalizer.py',91),
  ('cond1Aux1 -> empty empty empty empty empty','cond1Aux1',5,'p_cond1Aux1','SintacticAnalizer.py',92),
  ('cond1Aux2 -> CUANDO ID condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond1Aux2','cond1Aux2',9,'p_cond1Aux2','SintacticAnalizer.py',102),
  ('cond1Aux2 -> empty empty empty empty empty empty empty empty empty','cond1Aux2',9,'p_cond1Aux2','SintacticAnalizer.py',103),
  ('condicion2 -> ENCASO ID cond2Aux1 FINENCASO PUNTOCOMA','condicion2',5,'p_condicion2','SintacticAnalizer.py',115),
  ('cond2Aux1 -> cond2Aux2 SINO LLAVE_IZQ expresion LLAVE_DER','cond2Aux1',5,'p_cond2Aux1','SintacticAnalizer.py',122),
  ('cond2Aux1 -> empty empty empty empty empty','cond2Aux1',5,'p_cond2Aux1','SintacticAnalizer.py',123),
  ('cond2Aux2 -> CUANDO condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond2Aux2','cond2Aux2',8,'p_cond2Aux2','SintacticAnalizer.py',133),
  ('cond2Aux2 -> empty empty empty empty empty empty empty empty','cond2Aux2',8,'p_cond2Aux2','SintacticAnalizer.py',134),
  ('condicion -> IGUAL','condicion',1,'p_condicion','SintacticAnalizer.py',146),
  ('condicion -> MAYOR','condicion',1,'p_condicion','SintacticAnalizer.py',147),
  ('condicion -> MENOR','condicion',1,'p_condicion','SintacticAnalizer.py',148),
  ('condicion -> DIFERENTE','condicion',1,'p_condicion','SintacticAnalizer.py',149),
  ('condicion -> MAYORIGUAL','condicion',1,'p_condicion','SintacticAnalizer.py',150),
  ('condicion -> MENORIGUAL','condicion',1,'p_condicion','SintacticAnalizer.py',151),
  ('sentencia -> ID','sentencia',1,'p_sentencia','SintacticAnalizer.py',159),
  ('sentencia -> NUMERO','sentencia',1,'p_sentencia','SintacticAnalizer.py',160),
  ('repita -> REPITA LLAVE_IZQ expresion LLAVE_DER HASTAENCONTRAR ID condicion sentencia PUNTOCOMA','repita',9,'p_repita','SintacticAnalizer.py',167),
  ('hacer -> DESDE ID IGUAL sentencia HASTA sentencia HAGA LLAVE_IZQ expresion LLAVE_DER FINDESDE PUNTOCOMA','hacer',12,'p_hacer','SintacticAnalizer.py',174),
  ('funcion -> Aleatorio','funcion',1,'p_funcion','SintacticAnalizer.py',181),
  ('funcion -> Mover','funcion',1,'p_funcion','SintacticAnalizer.py',182),
  ('funcion -> funcionAlge','funcion',1,'p_funcion','SintacticAnalizer.py',183),
  ('Aleatorio -> ALEATORIO PARENTESIS_IZQ PARENTESIS_DER PUNTOCOMA','Aleatorio',4,'p_aleatorio','SintacticAnalizer.py',190),
  ('Mover -> MOVER PARENTESIS_IZQ paramMover PARENTESIS_DER PUNTOCOMA','Mover',5,'p_mover','SintacticAnalizer.py',197),
  ('paramMover -> AF','paramMover',1,'p_ParamMover','SintacticAnalizer.py',204),
  ('paramMover -> F','paramMover',1,'p_ParamMover','SintacticAnalizer.py',205),
  ('paramMover -> DFA','paramMover',1,'p_ParamMover','SintacticAnalizer.py',206),
  ('paramMover -> IFA','paramMover',1,'p_ParamMover','SintacticAnalizer.py',207),
  ('paramMover -> DFB','paramMover',1,'p_ParamMover','SintacticAnalizer.py',208),
  ('paramMover -> IFB','paramMover',1,'p_ParamMover','SintacticAnalizer.py',209),
  ('paramMover -> A','paramMover',1,'p_ParamMover','SintacticAnalizer.py',210),
  ('paramMover -> DAA','paramMover',1,'p_ParamMover','SintacticAnalizer.py',211),
  ('paramMover -> IAA','paramMover',1,'p_ParamMover','SintacticAnalizer.py',212),
  ('paramMover -> DAB','paramMover',1,'p_ParamMover','SintacticAnalizer.py',213),
  ('paramMover -> IAB','paramMover',1,'p_ParamMover','SintacticAnalizer.py',214),
  ('paramMover -> AA','paramMover',1,'p_ParamMover','SintacticAnalizer.py',215),
  ('funcionAlge -> INC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA','funcionAlge',7,'p_funcion_Alge','SintacticAnalizer.py',222),
  ('funcionAlge -> DEC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA','funcionAlge',7,'p_funcion_Alge','SintacticAnalizer.py',223),
  ('funcionAlge -> INI PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA','funcionAlge',7,'p_funcion_Alge','SintacticAnalizer.py',224),
  ('procedimiento -> PROC ID PARENTESIS_IZQ parametro PARENTESIS_DER INICIOPROC DOSPUNTOS expresion FINPROC PUNTOCOMA procedimiento','procedimiento',11,'p_procedimiento','SintacticAnalizer.py',232),
  ('procedimiento -> empty empty empty empty empty empty empty empty empty empty empty','procedimiento',11,'p_procedimiento','SintacticAnalizer.py',233),
  ('parametro -> ID COMA parametro','parametro',3,'p_parametro','SintacticAnalizer.py',245),
  ('parametro -> ID empty empty','parametro',3,'p_parametro','SintacticAnalizer.py',246),
  ('parametro -> NUMERO COMA parametro','parametro',3,'p_parametro','SintacticAnalizer.py',247),
  ('parametro -> NUMERO empty empty','parametro',3,'p_parametro','SintacticAnalizer.py',248),
  ('llamarProc -> LLAMAR ID PARENTESIS_IZQ parametro PARENTESIS_DER PUNTOCOMA','llamarProc',6,'p_llamarProc','SintacticAnalizer.py',261),
  ('empty -> <empty>','empty',0,'p_empty','SintacticAnalizer.py',268),
]
