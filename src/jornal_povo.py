import requests


class JornalPovo:
    def __init__(self) -> None:
        self.url_base = 'https://www.jornaldopovo.net/'

    def get_pages(self, date, day):
        keep_looking = True
        pages = []
        counter = 1

        while keep_looking:
            # url = f'{self.url_base}/_app/_files/edicao/{data}/jpg/edicao-{data}-page-{counter}.jpg'
            url = f'{self.url_base}/cliente/img/edicao/{date}/jpg/{day}pg{str(counter).zfill(2)}_copy.jpg'

            try:
                r = requests.get(url, allow_redirects=False, stream=True)
                content_type = r.headers.get('Content-Type')

                if r.status_code == 200 and content_type.startswith('image'):
                    pages.append(url)
                else:
                    keep_looking = False
            except:
                keep_looking = False

            counter = counter + 1
        return pages
