from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel


class WhidgetMain(QMainWindow):

    def __init__( self ):
    
        super ().__init__() # metodo 

        self.widget_statico()
        self.widget_movel_bateria()
        self.widget_som()

        #QTimer
        self.funcao_qtimer()
        self.funcao_label_som()
       
    def widget_statico(self):

        LABEL_MAIN_1 = QLabel(self)
        LABEL_MAIN_1.setText("HARDWARE")
        LABEL_MAIN_1.move(50,5)
        LABEL_MAIN_1.resize(130,40)
        LABEL_MAIN_1.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 20px}')# YELLOW

        LABEL_MAIN_2 = QLabel(self)
        LABEL_MAIN_2.move(5,40)
        LABEL_MAIN_2.resize(240,2)
        LABEL_MAIN_2.setStyleSheet('QLabel{background-color: #FFFF00}')

        LABEL_MAIN_3 = QLabel(self)
        LABEL_MAIN_3.setText("Ctrl+Q sair")
        LABEL_MAIN_3.move(5,150)
        LABEL_MAIN_3.resize(50,15)
        LABEL_MAIN_3.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 8px }')

        LABEL_MAIN_4 = QLabel(self)
        LABEL_MAIN_4.setText("Ctrl+O som")
        LABEL_MAIN_4.move(5,160)
        LABEL_MAIN_4.resize(50,15)
        LABEL_MAIN_4.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 8px }')

        LABEL_MAIN_5 = QLabel(self)
        LABEL_MAIN_5.setText("vs 2.2")
        LABEL_MAIN_5.move(70,160)
        LABEL_MAIN_5.resize(50,15)
        LABEL_MAIN_5.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 8px }')

        LABEL_MAIN_6 = QLabel(self)
        LABEL_MAIN_6.setText("SOM")
        LABEL_MAIN_6.move(110,160)
        LABEL_MAIN_6.resize(60,15)
        LABEL_MAIN_6.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 8px }')

    def widget_som(self):

        self.LABEL_som = QLabel( self) 
        self.LABEL_som.setGeometry(195, 160,30, 15) 
        self.LABEL_som.setStyleSheet(
            "color: #FF0000; font: bold; font-size: 8px ")

        self.LABEL_som1 = QLabel( self) 
        self.LABEL_som1.setGeometry(225, 160,20, 15) 
        self.LABEL_som1.setStyleSheet(
            "color: #FFFF00; font: bold; font-size: 8px ")
        
    def widget_movel_bateria(self):

        self.LABEL_BAT = QLabel( self) 
        self.LABEL_BAT.setGeometry(10, 60,150, 50) 
        self.LABEL_BAT.setText("Bateria")
        self.LABEL_BAT.setStyleSheet(
            "color: #FFFF00; font: bold; font-size: 20px ")
        
        self.LABEL_BAT3 = QLabel( self) 
        self.LABEL_BAT3.setGeometry(150, 60,90, 50) 
        self.LABEL_BAT3.setStyleSheet(
            "color: #FF0000; font: bold; font-size: 25px ")
        
        self.LABEL_BAT1 = QLabel( self) 
        self.LABEL_BAT1.setGeometry(10, 90,150, 50) 
        self.LABEL_BAT1.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 30px ")
        
        self.LABEL_BAT2 = QLabel( self) 
        self.LABEL_BAT2.setGeometry(120, 95,50, 50) 
        self.LABEL_BAT2.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 15px ")
        
        
