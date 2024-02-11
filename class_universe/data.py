from datetime import datetime as DT

class Data:

    """                data                     """
    def data_dia(self):

        dia = DT.now()

        return dia.day,dia.month,dia.year
    
    """                  hora                   """

    def hora_dia(self):

        hora = DT.now()

        return hora.hour,hora.minute,hora.second
    
    """                  semana                 """

    def semana_dia(self):

        sem =DT.now()

        return sem.strftime("%A")