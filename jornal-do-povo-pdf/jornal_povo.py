from PIL import Image
import datetime
import os
import requests

class JornalPovo:
    def __init__(self) -> None:
        pass

    def get_paginas(self, data):
        contador = 1
        continuar_procurando = True

        paginas = []

        while continuar_procurando:
            url = f'http://www.jornaldopovo.com.br/flip/edicoes/{data}/jpg//edicao-{data}-page-{contador:03}.jpg'
            
            try:
                r = requests.get(url, stream=True)

                if r.status_code == 200:
                    paginas.append(url)
            except:
                continuar_procurando = False

            contador = contador + 1
        
        return paginas

    
    def baixa_imagem(self, url):
        arquivo_temporario = 'temp.jpg'
        
        print(datetime.datetime.now())
        r = requests.get(url, stream=True)

        open(arquivo_temporario, 'wb').write(r.content)
        imagem = Image.open(arquivo_temporario)
        print(datetime.datetime.now())
        
        return imagem