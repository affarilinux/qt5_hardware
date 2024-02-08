from class_universe.psutil_py import ClassePsutil
from class_universe.variaveis_init import VariaveisInit

class QtimerRam(ClassePsutil):

    def funcao_qtimer_ram(self):

        if not self.psutil_ram_teste():

            print("certo")

        else:

            self.ram_psutil() ## ram

    
    def FC_qtimer_ram_soma(self,NR):

        if NR >= 90:

            VariaveisInit.VAV_QTIME_RAM = (
                VariaveisInit.VAV_QTIME_RAM +1)
            
    def FC_qtimer_ram_soma3(self):

        if VariaveisInit.VAV_QTIME_RAM == 3:

            VariaveisInit.VAV_QTIME_RAM = 0