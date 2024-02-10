
from class_universe.psutil_py import ClassePsutil

class ProcessoProcessador(ClassePsutil):

    def FC_pcprocessador ( self ):
            
        if not self.processador_freq_teste():
           
            self.processador_label_ef("S/I")
            
        else:

            self.processador_label_ef(self.processador_frequencia())
        
