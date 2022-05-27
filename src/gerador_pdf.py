from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os


class GeradorPdf:
    def __init__(self, data_jornal):
        self.arquivo = f'{data_jornal}.pdf'
        self.pdf = canvas.Canvas(self.arquivo, pagesize=A4)
        self.pdf.setTitle(data_jornal)

    def adiciona_pagina(self, url_imagem):
        imagem = ImageReader(url_imagem)

        self.pdf.drawImage(imagem, 0, 0, 595, 842)
        self.pdf.showPage()

    def adiciona_paginas(self, paginas):
        for pagina, url_imagem in enumerate(paginas, start=1):

            print(f'Adicionando página {pagina} de {len(paginas)}...')
            self.adiciona_pagina(url_imagem)

    def salva_pdf(self):
        self.pdf.save()

        caminho_completo = f'{os.getcwd()}/{self.arquivo}'
        os.startfile(caminho_completo)
