import psutil

from class_universe.variaveis_init import VariaveisInit

class ClassePsutil:

    """              BATERIA                    """
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
    
    def nivel_bateria_sys(self): ## if not
         
        BATERIA_PSUTIL = psutil.sensors_battery()

        return BATERIA_PSUTIL
    
    def nivel_bateria_sys1(self):
        
        BAT = psutil.sensors_battery()
        bater = BAT.percent

        return bater
    
    ###############################################
    """              RAM                        """

    def psutil_ram(self):

        #informações da memoria ram
        informacao           = psutil.virtual_memory ()

        total                = informacao.total
        usada                = informacao.used

        # calcula porcentagm
        calculo_por_centagem      = ( usada * 100 ) / total

        # filtra o float
        calculo_filtro_informacao = round ( calculo_por_centagem, 2 )

        return calculo_filtro_informacao,usada

    def psutil_ram_teste(self):

        informacao = psutil.virtual_memory ()

        return informacao
    
    ###############################################
    """                  temperatura            """

    def temperatura_lib1(self):

        wifi_temp    = psutil.sensors_temperatures()['iwlwifi_1'][0]
        wifi_temp_cur  = wifi_temp.current
        
        return wifi_temp_cur
    
    def temperatura_lib2(self):

        processador_temp = psutil.sensors_temperatures()['acpitz'][0]

        core_temp        = psutil.sensors_temperatures()['coretemp'][0]
        core_temp1       = psutil.sensors_temperatures()['coretemp'][1]
        core_temp2       = psutil.sensors_temperatures()['coretemp'][2]

        processador_temp_cur = processador_temp.current

        core_temp_cur = core_temp.current
        core_temp1_cur = core_temp1.current
        core_temp2_cur = core_temp2.current

        return (processador_temp_cur,core_temp_cur, 
                core_temp1_cur,core_temp2_cur)
        
    ###############################################
    """                  processador            """

    def processador_freq_teste(self):

        teste1x = psutil.cpu_freq ()

        return teste1x
    
    def processador_frequencia(self):
        
        informacao_sistema_1 = psutil.cpu_freq ()

        # puxa as informações e adiciona nas variaveis
        maximo_processador   = informacao_sistema_1.max
        dados_presente       = informacao_sistema_1.current

        # calcula porcentagm
        calculo_processos_dados     = ( dados_presente * 100 ) / maximo_processador       

        # filtra o float
        filtra_calculo_sistema = round ( calculo_processos_dados, 2)

        return filtra_calculo_sistema

    ###############################################
    """                cooler                   """
    def cooler_psutil(self):

        fans_leiint = psutil.sensors_fans()

        return fans_leiint
       
    ###############################################
    """                 disco                   """
    def disco_psutil(self):

        list_maxd = []
        list_usadd = []
        list_particao = []

        particao = psutil.disk_partitions()
        
        for fo in particao:

            li = fo.mountpoint

            list_particao.append(li)

            particao1 = psutil.disk_usage(li)

            list_maxd.append(particao1.total)
            list_usadd.append(particao1.used)
            
        return list_particao,list_maxd,list_usadd