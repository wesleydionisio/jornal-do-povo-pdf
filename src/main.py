from datetime import date
from jornal_povo import JornalPovo
from gerador_pdf import GeradorPdf


def main():
    today = date.today()
    data_jornal = today.strftime("%Y%m%d")

    print(f'Baixando versão impressa Jornal do Povo'
          + f' - ({today.strftime("%d/%m/%Y")})...')

    jp = JornalPovo()
    paginas = jp.get_paginas(data_jornal)

    pdf = GeradorPdf(data_jornal)
    pdf.adiciona_paginas(paginas)

    pdf.salva_pdf()


if __name__ == '__main__':
    main()
