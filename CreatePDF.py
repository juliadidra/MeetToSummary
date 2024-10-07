import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

class CreatePDF:
    def create_doc_pdf(texto, filename):

        diretorio = "files"
        
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print(f"Pasta '{diretorio}' criada com sucesso.")
        else:
            print(f"Pasta '{diretorio}' já existe.")

        caminho_arquivo = os.path.join(diretorio, f"{filename}.pdf")

        # Crie um arquivo PDF em branco
        doc = canvas.Canvas(caminho_arquivo, pagesize=letter)
        doc.setTitle("Resumo")


        # Definir posição inicial para o texto
        x = 100
        y = 750

        fonte_padrao = "Helvetica"
        fonte_negrito = "Helvetica-Bold"
        tamanho_fonte_titulo = 20
        tamanho_fonte_texto = 14
        cor_fonte = colors.black
        cor_titulo = colors.darkblue

        # Estilo para título
        doc.setFont(fonte_negrito, tamanho_fonte_titulo)
        doc.setFillColor(cor_titulo)
        doc.drawCentredString(300, y, "Resumo")
        y -= 40  # Posição vertical para começar o texto

        # Aplicar estilo para o texto normal
        doc.setFont(fonte_padrao, tamanho_fonte_texto)
        doc.setFillColor(cor_fonte)

        # Largura máxima do texto antes de quebrar a linha
        max_width = 450  # Largura máxima da linha, ajustável conforme necessário
        
        # Divide o texto em múltiplas linhas conforme o tamanho máximo
        lines = []
        for line in texto.split('\n'):  # Mantém as quebras de linha manuais
            while len(line) > 0:
                if doc.stringWidth(line, fonte_padrao, tamanho_fonte_texto) > max_width:
                    # Se o texto exceder a largura, corte-o
                    split_index = len(line)
                    while doc.stringWidth(line[:split_index], fonte_padrao, tamanho_fonte_texto) > max_width:
                        split_index -= 1
                    lines.append(line[:split_index])  # Adiciona a linha quebrada
                    line = line[split_index:].lstrip()  # Continua a partir do restante
                else:
                    lines.append(line)
                    break

        # Aumentar o espaçamento entre linhas
        espacamento_linhas = 18  # Define o espaçamento entre linhas (pode ajustar)

        # Função auxiliar para desenhar texto em negrito ou normal
        def desenha_texto_com_negrito(doc, texto, x, y):
            partes = texto.split('**')
            for i, parte in enumerate(partes):
                if i % 2 == 0:
                    # Texto normal
                    doc.setFont(fonte_padrao, tamanho_fonte_texto)
                else:
                    # Texto em negrito
                    doc.setFont(fonte_negrito, tamanho_fonte_texto)
                
                doc.drawString(x, y, parte)
                x += doc.stringWidth(parte, doc._fontname, tamanho_fonte_texto)

        # Desenha o texto linha por linha no PDF
        for line in lines:
            desenha_texto_com_negrito(doc, line, x, y)
            y -= espacamento_linhas  # Ajuste para mover o texto para a linha de baixo
        
        # Adiciona um rodapé (exemplo)
        doc.setFont(fonte_padrao, 10)
        doc.setFillColor(colors.grey)
        doc.drawCentredString(300, 50, "Rodapé - Página 1")

        doc.showPage()
        doc.save()
        print("PDF criado com sucesso.")

        print('caminho:', caminho_arquivo)

        return caminho_arquivo