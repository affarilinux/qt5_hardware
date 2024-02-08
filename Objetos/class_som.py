from pydub import AudioSegment
from pydub.playback import play
from class_universe.variaveis_init import VariaveisInit
from PyQt5 import QtCore

class Som:

    def ativar_som(self):

        self.bateria_labelsom1(VariaveisInit.STR_SOM)

        self.funcao_som()

        QtCore.QTimer.singleShot(3000, self.desativar_labelsom2)

    def desativar_labelsom2(self):

        self.bateria_labelsom1(VariaveisInit.ASPAS)

    def funcao_som(self):

        sound = AudioSegment.from_file(
                file = "/home/waghtom/Downloads/CTRL-C/envs/hardware/qt_hard/Objetos/jk.wav", format = "wav")
        play(sound)
        
    

