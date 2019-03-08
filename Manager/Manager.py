
from  LexicalAnalysis.LexicalAnalizer import *

class Manager:
    def startCompile(self):
       lexical_analizer = LexicalAnalizer.analize(self)



manager = Manager()
manager.startCompile()