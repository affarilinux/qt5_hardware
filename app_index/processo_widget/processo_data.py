from class_universe.data import Data

class ProcessoData(Data):

    """           data                         """
    def data_processo(self):

        vd = self.data_dia()

        self.data_label(vd[0],vd[1],vd[2])

    """             hora                        """
    def hora_processo(self):

        hr = self.hora_dia()
        
        self.hora_label(hr[0],hr[1])

    def semana_processo(self):

        self.semana_label_(self.semana_dia())


