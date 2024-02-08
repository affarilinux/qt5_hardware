
class ExeIndexfront:

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
