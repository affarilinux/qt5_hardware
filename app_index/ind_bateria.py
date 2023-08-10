import psutil

from class_universe.variaveis_init import VariaveisInit
from app_index.class_sistema.bateria import ClasseBateria

class Bateria:
    
    def bateria_psutil(self):

        bateria_class1 = ClasseBateria()
        
        if not bateria_class1.nivel_bateria_sys:
             
            self.bateria_pt("S/I")

        else:
            
            #nivel_bateria   = BATERIA_PSUTIL.percent
            nivel_bateria = bateria_class1.nivel_bateria_sys1()

            self.LABEL_BAT1.setText(
                 "{} %".format(int(nivel_bateria)))
            
            #funcoes
            self.estado_bateria()
            self.processo_qtime_bateria(int(nivel_bateria))
    
    def estado_bateria(self):
         
        bateria_class = ClasseBateria()
        estado = bateria_class.estado_bateria_sys()

        self.LABEL_BAT2.setText(estado)

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