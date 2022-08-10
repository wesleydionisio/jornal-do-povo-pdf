from datetime import date
from jornal_povo import JornalPovo
from gerador_pdf import GeradorPdf


def main():
    today = date.today()
    today_date = today.strftime("%Y%m%d")
    today_day = today.strftime("%d")

    print(f'Baixando versão impressa Jornal do Povo'
          + f' - ({today.strftime("%d/%m/%Y")})...')

    jp = JornalPovo()
    pages = jp.get_pages(today_date, today_day)

    pdf = GeradorPdf(today_date)
    pdf.adiciona_paginas(pages)

    pdf.salva_pdf()


if __name__ == '__main__':
    main()
