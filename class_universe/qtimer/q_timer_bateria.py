from class_universe.variaveis_init import VariaveisInit
from app_index.class_sistema.bateria import ClasseBateria

from PyQt5 import QtCore

from som.class_som import Som

class QtimerBateria(ClasseBateria):

    def funcao_qtimer_bateria(self):

        if not self.nivel_bateria_sys:
             
            self.bateria_labelbat3("S/I")

        else:
            # funcoes init
            self.bateria_psutil()

            #qtimer
            self.funcao_qtimer_bateria_se3()

    def funcao_qtimer_bateria_soma(self,NB):

        if NB < VariaveisInit.BATERIA_MINIMA or (
             NB > VariaveisInit.BATERIA_MAXIMA):

            VariaveisInit.VAV_QTIME_BATERIA = (
             VariaveisInit.VAV_QTIME_BATERIA + 1)
            
    def funcao_qtimer_bateria_se3(self):
        
        if VariaveisInit.VAV_QTIME_BATERIA == 3:
          
            VariaveisInit.VAV_QTIME_BATERIA = 0
            self.funcao_vav_qtimer()

        self.som_estado_nivel()
        VariaveisInit.VAV_QTIMER = 0

    def som_estado_nivel(self):

        if VariaveisInit.VAV_QTIMER == 1:

            if int(self.nivel_bateria_sys1()) < (
                VariaveisInit.BATERIA_MINIMA
                ):
                
                if self.estado_bateria_sys() == (
                    VariaveisInit.BATERIA_DESCARREGANDO
                ):
    
                    self.bateria_labelbat3(VariaveisInit.AVISO)
                    self.ativar_som()

                else:
                    
                    self.bateria_labelbat3(VariaveisInit.ASPAS)
                
            elif int(self.nivel_bateria_sys1()) > (
                VariaveisInit.BATERIA_MAXIMA
            ):

                if self.estado_bateria_sys() == (
                    VariaveisInit.BATERIA_CARREGANDO
                ):
                    
                    self.bateria_labelbat3(VariaveisInit.AVISO)
                    self.ativar_som()
                    
                else:
                 
                    self.bateria_labelbat3(VariaveisInit.ASPAS)

    def ativar_som(self):

        self.bateria_labelsom1(VariaveisInit.STR_SOM)

        som = Som()
        som.funcao_som()

        QtCore.QTimer.singleShot(3000, self.desativar_labelsom2)

    def desativar_labelsom2(self):

        self.bateria_labelsom1(VariaveisInit.ASPAS)
