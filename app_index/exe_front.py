from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel


class ExeFront(QMainWindow):

    def __init__( self ):
    
        super ().__init__() # metodo 

        self.widget_statico_sistema()
        self.widget_statico_informacao()
        self.widget_movel_bateria()
        self.widget_movel_ram()
        self.widget_som()
        self.widget_movel_temperatura()
        self.widget_movel_processador()
        self.widget_movel_cooler()
        self.widget_movel_HD()
        self.widget_movel_crono()
        self.widget_janela()

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
        LABEL_STAT_SIST_2.resize(230,2)
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
        
        LABEL_STAT_SIST_8 = QLabel( self) 
        LABEL_STAT_SIST_8.setGeometry(10, 370,150, 50) 
        LABEL_STAT_SIST_8.setText("Disco")
        LABEL_STAT_SIST_8.setStyleSheet(
            "color: #FFFF00; font: bold; font-size: 20px ")
        
    def widget_statico_informacao(self):
        
        var_ind =480
        
        LABEL_STAT_INFO_1 = QLabel(self)
        LABEL_STAT_INFO_1.setText("Ctrl+Q sair")
        LABEL_STAT_INFO_1.move(5,var_ind)
        LABEL_STAT_INFO_1.resize(50,15)
        LABEL_STAT_INFO_1.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 8px }')

        LABEL_STAT_INFO_2 = QLabel(self)
        LABEL_STAT_INFO_2.setText("Ctrl+O som")
        LABEL_STAT_INFO_2.move(5,var_ind+10)
        LABEL_STAT_INFO_2.resize(50,15)
        LABEL_STAT_INFO_2.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 8px }')

        LABEL_STAT_INFO_3 = QLabel(self)
        LABEL_STAT_INFO_3.setText("vs 2.5")#SISTEMA VAERIAVEL DE VERSOES
        LABEL_STAT_INFO_3.move(70,var_ind+10)
        LABEL_STAT_INFO_3.resize(50,15)
        LABEL_STAT_INFO_3.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 8px }')

        LABEL_STAT_INFO_4 = QLabel(self)
        LABEL_STAT_INFO_4.setText("CODIGO") #SISTEMA VARIAVEL DE VERSOES
        LABEL_STAT_INFO_4.move(110,var_ind+10)
        LABEL_STAT_INFO_4.resize(60,15)
        LABEL_STAT_INFO_4.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 8px }')

    def widget_som(self):

        var_ind2 = 490

        self.LABEL_som = QLabel( self) 
        self.LABEL_som.setGeometry(195, var_ind2,30, 15) 
        self.LABEL_som.setStyleSheet(
            "color: #FF0000; font: bold; font-size: 8px ")

        self.LABEL_som1 = QLabel( self) 
        self.LABEL_som1.setGeometry(225, var_ind2,20, 15) 
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
        
        self.LABEL_RAM1 = QLabel( self)  ##  quantidade ram
        self.LABEL_RAM1.setGeometry(150, 160,150, 50) 
        self.LABEL_RAM1.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 15px ")
                
    def widget_movel_temperatura(self):

        self.LABEL_temp = QLabel( self)  ## temperatura media
        self.LABEL_temp.setGeometry(10, 220,130,50) 
        self.LABEL_temp.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 20px ")
        
        self.LABEL_temp1 = QLabel( self)  ## aviso
        self.LABEL_temp1.setGeometry(180, 190,90, 50) 
        self.LABEL_temp1.setStyleSheet(
            "color: #FF0000; font: bold; font-size: 25px ")
        
        self.LABEL_temp2 = QLabel( self)  ## pico temperatura
        self.LABEL_temp2.setGeometry(180, 225,90, 50) 
        self.LABEL_temp2.setStyleSheet(
            "color: #FF0000; font: bold; font-size: 12px ")
        
    def widget_movel_processador(self):

        self.LABEL_PCC = QLabel( self)  ## nivel PROCESSADOR
        self.LABEL_PCC.setGeometry(10, 280,150, 50) 
        self.LABEL_PCC.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 20px ")
        
    def widget_movel_cooler(self):

        self.LABEL_coo = QLabel( self)  ## nivel coooller
        self.LABEL_coo.setGeometry(10, 340,150, 50) 
        self.LABEL_coo.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 20px ")
        
    def widget_movel_HD(self):
        
        self.LABEL_hd = QLabel( self)  ## nivel coooller
        self.LABEL_hd.setText("100.90 %")
        self.LABEL_hd.setGeometry(10, 400,150, 50) 
        self.LABEL_hd.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 20px ")
        
    def widget_movel_crono(self):

        self.LABEL_data = QLabel( self)  ## nivel coooller
        self.LABEL_data.setText("25.01.23")
        self.LABEL_data.setGeometry(10, 435,100, 50) 
        self.LABEL_data.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 14px ")
        
        self.LABEL_semana = QLabel( self)  ## nivel coooller
        self.LABEL_semana.setText("Segunda")
        self.LABEL_semana.setGeometry(100, 435,100, 50) 
        self.LABEL_semana.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 14px ")
        
        self.LABEL_hora = QLabel( self)  ## nivel coooller
        self.LABEL_hora.setText("12:40")
        self.LABEL_hora.setGeometry(200, 435,100, 50) 
        self.LABEL_hora.setStyleSheet(
            "color: #FFD700; font: bold; font-size: 14px ")
        
    def widget_janela(self):

        self.BUTON_janela = QPushButton( self) 
        self.BUTON_janela.setGeometry(240, 10, 50,50) 
        self.BUTON_janela.setStyleSheet(
            "border-radius : 25;  color: #FFFF00; font: bold; font-size: 12px;border : 3px solid #FFFF00")
        #self.BUTON_janela.clicked.connect(self.J_P)