import psutil

from class_universe.variaveis_init import VariaveisInit

class ClasseBateria:

    def estado_bateria_sys(self):

        informacao_bateria = psutil.sensors_battery()

        # puxa uma informação se esta plugado na internet
        informacao_carregamento = informacao_bateria.power_plugged 

        est = None

        if informacao_carregamento   == VariaveisInit.TRUE :
                
            est = VariaveisInit.BATERIA_CARREGANDO
                
        elif informacao_carregamento == VariaveisInit.FALSE :
                est = VariaveisInit.BATERIA_DESCARREGANDO

        return est
    
    def nivel_bateria_sys(self):
         
        BATERIA_PSUTIL = psutil.sensors_battery()

        return BATERIA_PSUTIL
    
    def nivel_bateria_sys1(self):
        
        BAT = psutil.sensors_battery()
        bater = BAT.percent

        return bater