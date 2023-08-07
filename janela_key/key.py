from PyQt5.QtWidgets import QMainWindow, QShortcut

from PyQt5.QtGui import QKeySequence

from class_universe.variaveis_init import VariaveisInit

class KeyBoard(QMainWindow):
    
    def __init__( self ):
    
        super ().__init__() # metodo 

        self.shortcut_close = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcut_close.activated.connect(self.closeApp)

        self.shortcut_close = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcut_close.activated.connect(self.key_som)

    def closeApp(self):

        self.close()

    def key_som(self):

        if VariaveisInit.SOM != "a":

            VariaveisInit.SOM = "a"

        else:

            VariaveisInit.SOM = 0

        

