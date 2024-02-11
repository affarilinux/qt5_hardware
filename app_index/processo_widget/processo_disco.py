from class_universe.psutil_py import ClassePsutil

class ProcessoDisco(ClassePsutil):

    def disco_processo(self):

        if not self.disco_psutil():

            print("sem")

        else:

            list_max_ = self.disco_psutil()[1]
            list_sistema = self.disco_psutil()[0]
            list_usada_ = self.disco_psutil()[2]

            cal_por = (sum(list_usada_) * 100)/ sum(list_max_)

            cal_por1 = round(cal_por,2)
            
            self.disco_label_ef(cal_por1)

            str_usada = str(sum(list_usada_))
            str_usada1 = str_usada[:-6]
    
            self.disco_label_ef_mb(str_usada1)

            self.disco_label_usada(list_sistema,
                list_max_,list_usada_)

    def disco_label_usada(self,ls,lmax,luse):

        list_porcento = []

        for lis in range(len(ls)):

            calc = (luse[lis] * 100)/lmax[lis]

            list_porcento.append(int(calc))
        
        max_particao = max(list_porcento)

        if max_particao > 90:

            ind = list_porcento.index(max_particao)

            str_particao = ls[ind]
            str_particao1 = str_particao[-4:]

            self.disco_label_ef_if(str_particao1,max_particao)
            

