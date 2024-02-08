import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication)
from PyQt5 import Qt
from PyQt5.QtGui      import QIcon

from class_universe.variaveis_init import VariaveisInit
from class_universe.exe_qtime import ClassQTime

from app_index.processo_widget.processo_bateria import QtimerBateria
from app_index.processo_widget.processo_ram import QtimerRam
from app_index.index_front import WhidgetMain
from app_index.exe_front import ExeIndexfront
from app_index.exe_widget import Bateria

from janela_key.key import KeyBoard
from Objetos.class_som import Som

class Principal(
    WhidgetMain,Bateria,ExeIndexfront,
    KeyBoard,Som,
    ClassQTime,QtimerBateria,QtimerRam,
    QMainWindow):

    def __init__(self):
        
        super(Principal, self).__init__()

        self.setAttribute(Qt.Qt.WA_TranslucentBackground, VariaveisInit.TRUE )   
        self.setAttribute(Qt.Qt.WA_NoSystemBackground, VariaveisInit.FALSE)      
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

        self.setGeometry(1580, 100, 300, 400) #j-XY app-XY
        self.setStyleSheet("Principal{background-color: rgba(0,255,255, 20);}") #Aqua / 
        
        self.setWindowIcon   ( QIcon ( VariaveisInit.IMAGEM_ICONE ))   #icone da janela
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = Principal()
    p.show()
    app.exec_()