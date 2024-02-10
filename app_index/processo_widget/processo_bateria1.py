from class_universe.psutil_py import ClassePsutil

from class_universe.variaveis_init import VariaveisInit

class Bateria(ClassePsutil):
    
    """             BATERIA                     """
    
    def bateria_psutil(self):

        nivel_bateria = self.nivel_bateria_sys1()
        
        self.bateria_labelbat1(int(nivel_bateria))

        if self.estado_bateria_sys() == None:

            self.bateria_labelbat1(VariaveisInit.S_I)
        else:

            self.bateria_label_bat2(self.estado_bateria_sys())
        
        ##soma 1-3
        self.funcao_qtimer_bateria_soma(int(nivel_bateria))
    
   

       
    
    


         
       
        

    
    
                       
    