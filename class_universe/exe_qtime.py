from PyQt5.QtCore        import QTimer

from class_universe.variaveis_init import VariaveisInit

class ClassQTime:

    def __init__( self ):
    
        super ().__init__() # metodo

        qtimer_1 = QTimer        ( self )

        qtimer_1.setInterval     ( 5000 )
        qtimer_1.start           ()

        #chamada de funçãO
        qtimer_1.timeout.connect ( self.qtimer_loop5 )

    """
        front end
    """
    def qtimer_loop5(self):

        ## whideget
        self.funcao_qtimer_bateria()
        self.funcao_qtimer_ram()
        self.FC_pt_temperatura()
        self.FC_pcprocessador()
        self.leitura_fans()
        self.disco_processo()

        ##datetime
        self.data_processo()
        self.hora_processo()
        self.semana_processo()
        
    """
        execusao som
    """
    def funcao_vav_qtimer(self):

        if VariaveisInit.SOM != VariaveisInit.STR_A:

            VariaveisInit.VAV_QTIMER = 1
            
    

    
        