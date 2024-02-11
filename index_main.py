import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication)
from PyQt5 import Qt
from PyQt5.QtGui      import QIcon

from class_universe.variaveis_init import VariaveisInit
from class_universe.exe_qtime import ClassQTime

from app_index.processo_widget.processo_bateria import ProcessoBateria
from app_index.processo_widget.processo_ram import ProcessoRam
from app_index.exe_front import ExeFront
from app_index.exe_beck import ExeIndexBeck
from app_index.processo_widget.processo_bateria1 import Bateria
from app_index.processo_widget.proceso_temperatura import ProcessoTemperatura
from app_index.processo_widget.proceso_processador import ProcessoProcessador
from app_index.processo_widget.processo_cooler  import ProcessadorCoooler
from app_index.processo_widget.processo_disco import ProcessoDisco
from app_index.processo_widget.processo_data import ProcessoData
from janela_key.key import KeyBoard
from Objetos.class_som import Som

class Principal(
    ExeFront,Bateria,ExeIndexBeck,
    KeyBoard,Som, ProcessoTemperatura,
    ClassQTime,ProcessoBateria,ProcessoRam,
    ProcessoProcessador,ProcessadorCoooler,
    ProcessoDisco,ProcessoData,
    
    QMainWindow):

    def __init__(self):
        
        super(Principal, self).__init__()

        self.setAttribute(Qt.Qt.WA_TranslucentBackground, VariaveisInit.TRUE )   
        self.setAttribute(Qt.Qt.WA_NoSystemBackground, VariaveisInit.FALSE)      
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

        self.setGeometry(1580, 100, 300, 510) #j-XY app-XY
        self.setStyleSheet("Principal{background-color: rgba(0,255,255, 20);}") #Aqua / 
        
        self.setWindowIcon   ( QIcon ( VariaveisInit.IMAGEM_ICONE ))   #icone da janela
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = Principal()
    p.show()
    app.exec_()