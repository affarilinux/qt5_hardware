from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel


class WhidgetMain(QMainWindow):

    def __init__( self ):
    
        super ().__init__() # metodo 

        self.widget_statico_sistema()
        self.widget_statico_informacao()
        self.widget_movel_bateria()
        self.widget_movel_ram()
        self.widget_som()
        self.widget_movel_temperatura()

        #QTimer
        self.qtimer_loop5()
        #key
        self.funcao_label_som()
       
    def widget_statico_sistema(self):

        LABEL_STAT_SIST_1 = QLabel(self)
        LABEL_STAT_SIST_1.setText("HARDWARE")
        LABEL_STAT_SIST_1.move(50,5)
        LABEL_STAT_SIST_1.resize(130,40)
        LABEL_STAT_SIST_1.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 20px}')# YELLOW

        LABEL_STAT_SIST_2 = QLabel(self)
        LABEL_STAT_SIST_2.move(5,40)
        LABEL_STAT_SIST_2.resize(240,2)
        LABEL_STAT_SIST_2.setStyleSheet('QLabel{background-color: #FFFF00}')
    
        LABEL_STAT_SIST_3 = QLabel( self) 
        LABEL_STAT_SIST_3.setGeometry(10, 60,150, 50) 
        LABEL_STAT_SIST_3.setText("Bateria")
        LABEL_STAT_SIST_3.setStyleSheet(
            "color: #FFFF00; font: bold; font-size: 20px ")
        
        LABEL_STAT_SIST_4 = QLabel( self) 
        LABEL_STAT_SIST_4.setGeometry(10, 130,150, 50) 
        LABEL_STAT_SIST_4.setText("Ram")
        LABEL_STAT_SIST_4.setStyleSheet(
            "color: #FFFF00; font: bold; font-size: 20px ")
        
        LABEL_STAT_SIST_5 = QLabel( self) 
        LABEL_STAT_SIST_5.setGeometry(10, 190,150, 50) 
        LABEL_STAT_SIST_5.setText("Temperatura")
        LABEL_STAT_SIST_5.setStyleSheet(
            "color: #FFFF00; font: bold; font-size: 20px ")
        
        
        LABEL_STAT_SIST_6 = QLabel( self) 
        LABEL_STAT_SIST_6.setGeometry(10, 250,150, 50) 
        LABEL_STAT_SIST_6.setText("Processador")
        LABEL_STAT_SIST_6.setStyleSheet(
            "color: #FFFF00; font: bold; font-size: 20px ")
        
        LABEL_STAT_SIST_7 = QLabel( self) 
        LABEL_STAT_SIST_7.setGeometry(10, 310,150, 50) 
        LABEL_STAT_SIST_7.setText("Cooler")
        LABEL_STAT_SIST_7.setStyleSheet(
            "color: #FFFF00; font: bold; font-size: 20px ")
        
    def widget_statico_informacao(self):

        LABEL_STAT_INFO_1 = QLabel(self)
        LABEL_STAT_INFO_1.setText("Ctrl+Q sair")
        LABEL_STAT_INFO_1.move(5,380)
        LABEL_STAT_INFO_1.resize(50,15)
        LABEL_STAT_INFO_1.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 8px }')

        LABEL_STAT_INFO_2 = QLabel(self)
        LABEL_STAT_INFO_2.setText("Ctrl+O som")
        LABEL_STAT_INFO_2.move(5,390)
        LABEL_STAT_INFO_2.resize(50,15)
        LABEL_STAT_INFO_2.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 8px }')

        LABEL_STAT_INFO_3 = QLabel(self)
        LABEL_STAT_INFO_3.setText("vs 2.5")#SISTEMA VAERIAVEL DE VERSOES
        LABEL_STAT_INFO_3.move(70,390)
        LABEL_STAT_INFO_3.resize(50,15)
        LABEL_STAT_INFO_3.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 8px }')

        LABEL_STAT_INFO_4 = QLabel(self)
        LABEL_STAT_INFO_4.setText("CODIGO") #SISTEMA VARIAVEL DE VERSOES
        LABEL_STAT_INFO_4.move(110,390)
        LABEL_STAT_INFO_4.resize(60,15)
        LABEL_STAT_INFO_4.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 8px }')

    def widget_som(self):

        self.LABEL_som = QLabel( self) 
        self.LABEL_som.setGeometry(195, 390,30, 15) 
        self.LABEL_som.setStyleSheet(
            "color: #FF0000; font: bold; font-size: 8px ")

        self.LABEL_som1 = QLabel( self) 
        self.LABEL_som1.setGeometry(225, 390,20, 15) 
        self.LABEL_som1.setStyleSheet(
            "color: #FFFF00; font: bold; font-size: 8px ")
        
    def widget_movel_bateria(self):

        self.LABEL_BAT3 = QLabel( self)  ## aviso
        self.LABEL_BAT3.setGeometry(150, 60,90, 50) 
        self.LABEL_BAT3.setStyleSheet(
            "color: #FF0000; font: bold; font-size: 25px ")
        
        self.LABEL_BAT1 = QLabel( self) ##nivel bateria
        self.LABEL_BAT1.setGeometry(10, 90,150, 50) 
        self.LABEL_BAT1.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 30px ")
        
        self.LABEL_BAT2 = QLabel( self) ## estado
        self.LABEL_BAT2.setGeometry(120, 95,50, 50) 
        self.LABEL_BAT2.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 15px ")
        
        self.LABEL_BAT4 = QLabel(self) ##hora
        self.LABEL_BAT4.setText("00.00") 
        self.LABEL_BAT4.move(200,113)
        self.LABEL_BAT4.resize(60,15)
        self.LABEL_BAT4.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 12px }')

    def widget_movel_ram(self):

        self.LABEL_RAM = QLabel( self)  ## nivel ram
        self.LABEL_RAM.setGeometry(10, 160,150, 50) 
        self.LABEL_RAM.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 25px ")
        
        self.LABEL_RAM1 = QLabel( self)  ## aviso
        self.LABEL_RAM1.setText("AVISO")
        self.LABEL_RAM1.setGeometry(180, 130,90, 50) 
        self.LABEL_RAM1.setStyleSheet(
            "color: #FF0000; font: bold; font-size: 25px ")
        
    def widget_movel_temperatura(self):

        self.LABEL_temp1 = QLabel( self)  ## aviso
        self.LABEL_temp1.setText("AVISO")
        self.LABEL_temp1.setGeometry(180, 190,90, 50) 
        self.LABEL_temp1.setStyleSheet(
            "color: #FF0000; font: bold; font-size: 25px ")