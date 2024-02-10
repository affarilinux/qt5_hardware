from class_universe.psutil_py import ClassePsutil
from class_universe.variaveis_init import VariaveisInit

class ProcessoRam(ClassePsutil):

    def funcao_qtimer_ram(self):

        if not self.psutil_ram_teste():

            self.ram_labelr1("S/I")
            
        else:

            nivel_ram = self.psutil_ram()

            self.ram_labelr1(nivel_ram[0])
            
            mm1 = str(nivel_ram[1])
            self.ram_label_memoria(mm1[:-6])

