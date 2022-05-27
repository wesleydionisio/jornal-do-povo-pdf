import requests


class JornalPovo:
    def __init__(self) -> None:
        self.url_base = 'https://www.jornaldopovo.net/'

    def get_paginas(self, data):
        continuar_procurando = True
        paginas = []
        contador = 1

        while continuar_procurando:
            url = f'{self.url_base}/_app/_files/edicao/{data}/jpg/edicao-{data}-page-{contador}.jpg'

            try:
                r = requests.get(url, allow_redirects=False, stream=True)
                content_type = r.headers.get('Content-Type')

                if r.status_code == 200 and content_type.startswith('image'):
                    paginas.append(url)
                else:
                    continuar_procurando = False
            except:
                continuar_procurando = False

            contador = contador + 1
        return paginas
