
class ExeIndexBeck:

    """
        EXECUÇÃO DOS FRONT DE VARIAVEIS
        BATERIA
    """
    ##widget_movel_bateria
    def bateria_labelbat1(self,nivbat):

        self.LABEL_BAT1.setText("{} %".format(nivbat))
        
    def bateria_label_bat2(self,estado):

        self.LABEL_BAT2.setText(estado)

    def bateria_labelbat3(self,pt_bateria):
         
        self.LABEL_BAT3.setText("{}".format(pt_bateria))

    """
        EXECUÇÃO DOS FRONT DE VARIAVEIS
        SOM
    """
    #widget_som
    def bateria_labelsom(self,som):
    
        self.LABEL_som.setText(som)
        
    def bateria_labelsom1(self,som1):
          
        self.LABEL_som1.setText("{}".format(som1))

    """
        EXECUÇÃO DOS FRONT DE VARIAVEIS
        RAM
    """
    def ram_labelr1(self,nivram):

        self.LABEL_RAM.setText("{} %".format(nivram))

    def ram_label_memoria(self,mm):

        self.LABEL_RAM1.setText("{} mb".format(mm))

    """
        EXECUÇÃO DOS FRONT DE VARIAVEIS
        TEMPERATURA
    """
    def temperatura_label_ef(self,th):

        self.LABEL_temp.setText("{} ºC".format(th))

    def temperatura_label_ef_pico(self,pic,ttx):

        self.LABEL_temp2.setText("{} ºC {}".format(pic,ttx))

    def temperatura_label_ef_pico_aspa(self):

        self.LABEL_temp2.setText("")

    def temperatura_label_aviso(self,avis):

        self.LABEL_temp1.setText("{}".format(avis))

    """
        EXECUÇÃO DOS FRONT DE VARIAVEIS
        PROCESSADOR
    """
    def processador_label_ef(self,md):

        self.LABEL_PCC.setText("{} %".format(md))

    """
        EXECUÇÃO DOS FRONT DE VARIAVEIS
        COOLER
    """
    def cooler_label_ef(self,fans_sis1):

        self.LABEL_coo.setText("{}".format(fans_sis1))


                
