from PyQt5.QtCore        import QTimer

from class_universe.variaveis_init import VariaveisInit

from som.class_som import Som

class ClassQTime:

    def __init__( self ):
    
        super ().__init__() # metodo

        qtimer_1 = QTimer        ( self )

        qtimer_1.setInterval     ( 5000 )
        qtimer_1.start           ()

        #chamada de funçãO
        qtimer_1.timeout.connect ( self.funcao_qtimer )

        qtimer_2 = QTimer        ( self )

        qtimer_2.setInterval     ( 15000 )
        qtimer_2.start           ()

        #chamada de funçãO
        qtimer_2.timeout.connect ( self.funcao_qtimer1 )

    """
        front end
    """
    def funcao_qtimer(self):

        self.bateria_psutil()

    """som
    """
    def funcao_qtimer1(self):
        
        if VariaveisInit.VAV_QTIME_BATERIA == 3:

            self.funcao_vav_qtimer()
            VariaveisInit.VAV_QTIME_BATERIA = 0

        self.ativar_som()
       
    def funcao_vav_qtimer(self):

        if VariaveisInit.SOM != "a":

            VariaveisInit.VAV_QTIMER = 1

    def ativar_som(self):

        if VariaveisInit.VAV_QTIMER == 1:

            som = Som()
            som.funcao_som()

            VariaveisInit.VAV_QTIMER = 0

    

        