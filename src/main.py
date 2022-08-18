from datetime import date, datetime
from jornal_povo import JornalPovo
from gerador_pdf import GeradorPdf


def main():
    today = date.today()
    print("------------------------------------------------------------------")
    askType = input("Digite 1 para baixar a edição do dia ou 2 para baixar uma versão anterior: ")
    if (askType == '1'):
        today_date = today.strftime("%Y%m%d")
        today_day = today.strftime("%d")
        
    elif (askType == '2'):
        today_date_str = datetime.strptime(input("Digite a Data:F Formato: Dia/Mês/Ano :"), "%d/%m/%Y")
        today_date = today_date_str.strftime("%Y%m%d")
        today_day = date.strftime(today_date_str, "%d")
        
    else:
        print("Digite uma opção válida e pressione Enter.")  
        return main()
    
        
    filename = datetime.strptime(today_date, "%Y%m%d").strftime("%d.%m.%Y")
    print(f'Baixando versão impressa Jornal do Povo'
          + f' - ({filename})...')


    jp = JornalPovo()
    pages = jp.get_pages(today_date, today_day)
    pdf = GeradorPdf(f'Edição {filename}')
    pdf.adiciona_paginas(pages)

    pdf.salva_pdf()


if __name__ == '__main__':
    main()
