from jornal_povo import JornalPovo
from gerador_pdf import GeradorPdf

data_jornal = '20210521'

jp = JornalPovo()
paginas = jp.get_paginas(data_jornal)

pdf = GeradorPdf(data_jornal)
pdf.adiciona_paginas(paginas)

pdf.salva_pdf()