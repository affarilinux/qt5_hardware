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

        if VariaveisInit.SOM != VariaveisInit.STR_A:

            VariaveisInit.SOM = VariaveisInit.STR_A

        else:

            VariaveisInit.SOM = 0

        self.funcao_label_som()

    def funcao_label_som(self):

        if VariaveisInit.SOM != VariaveisInit.STR_A:

            self.bateria_labelsom(VariaveisInit.STR_SOM)

        else:

            self.bateria_labelsom("S/SOM")
            


