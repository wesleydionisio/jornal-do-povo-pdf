import requests


class JornalPovo:
    def __init__(self) -> None:
        self.url_base = 'http://www.jornaldopovo.net'

    def get_pages(self, date, day):
        prefix = '_copy'
        keep_looking = True
        pages = []
        counter = 1
        objetive = 0 #There's definitely a better way to do this.

        while keep_looking:
            url = f'{self.url_base}/cliente/img/edicao/{date}/jpg/{day}pg{str(counter).zfill(2)}{prefix}.jpg'

            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
                r = requests.get(url, allow_redirects=False, stream=True, headers=headers)
                content_type = r.headers.get('Content-Type')

                if r.ok and content_type.startswith('image'):
                    pages.append(url)
                elif r.ok == False and objetive == 0:
                    prefix = ''
                    objetive = 1
                    counter = 0
                else:
                    keep_looking = False
            except:
                keep_looking = False
                
            counter += 1
            
        return pages