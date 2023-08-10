from PyQt5.QtCore        import QTimer
from PyQt5 import QtCore

from class_universe.variaveis_init import VariaveisInit

from som.class_som import Som

from app_index.class_sistema.bateria import ClasseBateria

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

            VariaveisInit.VAV_QTIME_BATERIA = 0
            self.funcao_vav_qtimer()

        self.som_estado_nivel()
       
    def funcao_vav_qtimer(self):

        if VariaveisInit.SOM != "a":

            VariaveisInit.VAV_QTIMER = 1

    def som_estado_nivel(self):

        if VariaveisInit.VAV_QTIMER == 1:

            sys_bateria = ClasseBateria()

            if int(sys_bateria.nivel_bateria_sys1()) < 20:

                if sys_bateria.estado_bateria_sys() == "DESC":

                    self.ativar_som()

            elif int(sys_bateria.nivel_bateria_sys1()) > 80:

                if sys_bateria.estado_bateria_sys() == "CA":

                    self.ativar_som()

    def ativar_som(self):

        self.LABEL_som1.setText("som")

        som = Som()
        som.funcao_som()

        VariaveisInit.VAV_QTIMER = 0

        QtCore.QTimer.singleShot(3000, self.desativar_labelsom2)

    def desativar_labelsom2(self):

        self.LABEL_som1.setText("")

        