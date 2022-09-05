from calendar import week
from http.client import OK
import requests
from datetime import datetime


class JornalPovo:
    def __init__(self) -> None:
        self.url_base = 'https://www.jornaldopovo.net'

    def get_pages(self, date, day):
        day_str = date[6:8]
        month_str = date[4:6]
        year_str = date[0:4]
        date_str = f'{day_str}/{month_str}/{year_str}'
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        if date_obj.weekday() == 5:
            day = int(day) + 1
            day = str(day).rjust(2, '0')
        if date_obj.weekday() == 6:
            day_str = int(day) - 1
            date_obj = date_obj.replace(day=day_str)
            date = date_obj.strftime("%Y%m%d")
        prefix = [".jpg", "copy.jpg", "_copy.jpg", "_copyjpg", "copyjpg"]
        counterPrefix = 0
        keep_looking = True
        pages = []
        counter = 1
        objetive = False

        while keep_looking:
            url = f'{self.url_base}/cliente/img/edicao/{date}/jpg/{day}pg{str(counter).zfill(2)}{prefix[counterPrefix]}'
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
                r = requests.get(url, allow_redirects=False, stream=True, headers=headers)
                content_type = r.headers.get('Content-Type')

                if r.ok and content_type.startswith('image'):
                    pages.append(url)
                    objetive = True
                    
                elif r.ok == False and objetive == False:
                    if counterPrefix < len(prefix):
                        counterPrefix += 1
                    counter = 0
                    
                else:
                    keep_looking = False
            except:
                keep_looking = False
                
            counter += 1
            
        return pages