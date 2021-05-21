from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

class GeradorPdf:
    def __init__(self, data_jornal):
        self.arquivo = f'pdfs/{data_jornal}.pdf'
        self.pdf = canvas.Canvas(self.arquivo, pagesize=A4)
        self.pdf.setTitle(data_jornal)

    def adiciona_pagina(self, url_imagem):
        imagem = ImageReader(url_imagem)

        self.pdf.drawImage(imagem, 0, 0, 590, 830)
        self.pdf.showPage()

    def adiciona_paginas(self, paginas):
        for pagina in paginas:
            self.adiciona_pagina(pagina)
        
    def salva_pdf(self):
        self.pdf.save()
        os.open(self.arquivo)