from class_universe.psutil_py import ClassePsutil

class ProcessadorCoooler(ClassePsutil):
    
    def leitura_fans(self):
        
        fans_sis = ""

        if not self.cooler_psutil():
            
            fans_sis = "S/I"
        
        else:
            fans_sis = "C/I"
            
        self.cooler_label_ef(fans_sis)
        