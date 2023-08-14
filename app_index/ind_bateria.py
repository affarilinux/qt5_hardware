from app_index.class_sistema.bateria import ClasseBateria

class Bateria(ClasseBateria):
    
    def bateria_psutil(self):

        nivel_bateria = self.nivel_bateria_sys1()
        
        self.bateria_labelbat1(int(nivel_bateria))
                    
        self.bateria_label_bat2(self.estado_bateria_sys())
        
        ##soma 1-3
        self.funcao_qtimer_bateria_soma(int(nivel_bateria))
    
    
         
       
        

    
    
                       
    