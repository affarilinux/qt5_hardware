import psutil

from class_universe.variaveis_init import VariaveisInit

class Bateria:
          
    def bateria_psutil(self):

        BATERIA_PSUTIL = psutil.sensors_battery()

        if not BATERIA_PSUTIL:
             
            self.bateria_pt("S/I")

        else:
            
            nivel_bateria   = BATERIA_PSUTIL.percent
            #funcoes
            self.carga_bateria(int(nivel_bateria))
            self.estado_bateria()
            self.processo_qtime_bateria(int(nivel_bateria))
    
    def carga_bateria(self,nivel_bateria):
            
            # chama o tipo de informação
            self.LABEL_BAT1.setText(
                 "{} %".format(nivel_bateria))
            
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

    ##QTIMER#############################################################
    def processo_qtime_bateria(self,NB):

        if NB < 20 or NB > 80:

            VariaveisInit.VAV_QTIME_BATERIA = (
             VariaveisInit.VAV_QTIME_BATERIA + 1)
            
            self.bateria_pt("AVISO")

        else:
             
             self.bateria_pt("")
            
    def bateria_pt(self,pt_bateria):
         
          self.LABEL_BAT3.setText("{}".format(pt_bateria))