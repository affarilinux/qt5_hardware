import psutil

class Bateria:

    #def __init__(self) -> None:
        
    
    def bateria_psutil(self):

        BATERIA_PSUTIL = psutil.sensors_battery()

        if not BATERIA_PSUTIL:
             
            self.LABEL_BAT3.setText("S/I")

        else:

            self.carga_bateria(BATERIA_PSUTIL)
            self.estado_bateria()
    
    def carga_bateria(self,BATERIA_PSUTIL):
            # chama o tipo de informação
            nivel_bateria   = BATERIA_PSUTIL.percent

            self.LABEL_BAT1.setText(
                 "{} %".format(int(nivel_bateria)))
            
    def estado_bateria(self):
         
        informacao_bateria = psutil.sensors_battery()

        # puxa uma informação se esta plugado na internet
        informacao_carregamento = informacao_bateria.power_plugged 

        est = None

        if informacao_carregamento   == True :
                
            est = "CA"
                
        elif informacao_carregamento == False :
                est = "DESC"

        self.LABEL_BAT2.setText(est)