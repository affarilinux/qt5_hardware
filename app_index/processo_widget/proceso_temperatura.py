
from class_universe.psutil_py import ClassePsutil

class ProcessoTemperatura(ClassePsutil):
    
    def FC_pt_temperatura(self):

        if not self.temperatura_lib2():

            self.temperatura_label_ef("S/I")
        
        else:
            
            tl2 = sum(self.temperatura_lib2())
            
            try:
               
                tl1 = self.temperatura_lib1()
                
                tl2 = (tl2 + tl1)/5
                
            except KeyError:

                tl2 = tl2/4

                

        self.temperatura_label_ef(round(tl2,2))
        self.temperatura_maxima()
        

    def temperatura_maxima(self,):

        list_max = []

        try:
           
            self.lista_temp_inserir(list_max)
            list_max.append(self.temperatura_lib1())
        
        except KeyError:

            self.lista_temp_inserir(list_max)

        vb = max(list_max)

        self.math_pico_temp(list_max.index(vb),vb)


    def lista_temp_inserir(self,list_max):

        var_ = self.temperatura_lib2()
        for car in var_:

            list_max.append(car)

    def math_pico_temp(self,n1,vb1):

        ## pc = processador
        ## cnº = core
        ##wf = wifi
        
        if vb1 > 80:
            
            match n1:

                case 0:
                    self.temperatura_label_ef_pico(vb1,"pc")

                case 1:
                    self.temperatura_label_ef_pico(vb1,"c0")

                case 2:
                    self.temperatura_label_ef_pico(vb1,"c1")

                case 3:
                    self.temperatura_label_ef_pico(vb1,"c2")

                case 4:
                    self.temperatura_label_ef_pico(vb1,"wf")
            
            self.funcao_som()

            self.temperatura_label_aviso("AVISO")

        else:

            self.temperatura_label_ef_pico_aspa()

            self.temperatura_label_aviso("")