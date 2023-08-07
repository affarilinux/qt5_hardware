from pydub import AudioSegment
from pydub.playback import play


class Som:

    def funcao_som(self):

        sound = AudioSegment.from_file(
                file = 'Objetos/jk.wav', format = "wav")
        play(sound)
        
    

