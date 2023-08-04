import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import Qt
from PyQt5.QtGui      import QIcon

from class_universe.variaveis_init import VariaveisInit

from app_index.index_front import WhidgetMain
from app_index.ind_bateria import Bateria

from janela_key.key import KeyBoard

class Principal(
    WhidgetMain,
    KeyBoard,Bateria,
    QMainWindow):

    def __init__(self):
        
        super(Principal, self).__init__()

        self.setAttribute(Qt.Qt.WA_TranslucentBackground, True )   
        self.setAttribute(Qt.Qt.WA_NoSystemBackground, False)      
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

        self.setGeometry(1610, 100, 250, 180) #j-XY app-XY
        self.setStyleSheet("Principal{background-color: rgba(0,255,255, 20);}") #Aqua / 
        
        self.setWindowIcon   ( QIcon ( VariaveisInit.IMAGEM_ICONE ))   #icone da janela
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = Principal()
    p.show()
    app.exec_()