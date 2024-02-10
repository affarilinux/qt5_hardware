from class_universe.variaveis_init import VariaveisInit
from class_universe.psutil_py import ClassePsutil

class ProcessoBateria(ClassePsutil):

    def funcao_qtimer_bateria(self):

        if not self.nivel_bateria_sys:
             
            self.bateria_labelbat3(VariaveisInit.S_I)

        else:
            # funcoes init
            self.bateria_psutil()

            #qtimer
            self.funcao_qtimer_bateria_se3()

    def funcao_qtimer_bateria_soma(self,NB):

        if NB <= VariaveisInit.BATERIA_MINIMA or (
             NB >= VariaveisInit.BATERIA_MAXIMA):

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

            if int(self.nivel_bateria_sys1()) <= (
                VariaveisInit.BATERIA_MINIMA
                ):
                
                if self.estado_bateria_sys() == (
                    VariaveisInit.BATERIA_DESCARREGANDO
                ):
    
                    self.bateria_labelbat3(VariaveisInit.AVISO)
                    self.ativar_som()

                else:
                    
                    self.bateria_labelbat3(VariaveisInit.ASPAS)

            elif int(self.nivel_bateria_sys1()) >= (
                VariaveisInit.BATERIA_MAXIMA
            ):
                #print("ok",self.estado_bateria_sys()) 
                ###### falta o none, pois esta havendo problema com relacao a isso
                #acima de 85%
                if self.estado_bateria_sys() == (
                    VariaveisInit.BATERIA_CARREGANDO
                ):
                   
                    self.bateria_labelbat3(VariaveisInit.AVISO)
                    self.ativar_som()
                    
                else:
                 
                    self.bateria_labelbat3(VariaveisInit.ASPAS)

    
