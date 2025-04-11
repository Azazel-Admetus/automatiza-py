import os
from PyPDF2 import PdfMerger
from tkinter import Tk, filedialog, simpledialog
from time import sleep

Tk().withdraw()

print("Selecione os arquivos PDF que deseja juntar")
arquivos = filedialog.askopenfilenames(
    title="Selecione os PDFs",
    filetypes=[("PDF files", "*.pdf")]
)
if not arquivos:
    print("Nenhum arquivo selecionado. Encerrando o processo...")
    sleep(3)
    exit()

nome_arquivo_final = simpledialog.askstring("Nome do Arquivo Final", "Digite o nome do PDF final:")

if not nome_arquivo_final:
    print("Nome inválido. Encerrando processo...")
    sleep(3)
    exit()

nome_arquivo_final += ".pdf"

print("Escolha a pasta para salvar o arquivo final...")
pasta_destino = filedialog.askdirectory(title="Selecione a pasta de destino")

if not pasta_destino:
    print("Nenhuma pasta selecionada. Encerrando o processo")
    sleep(3)
    exit()

caminho_final = os.path.join(pasta_destino, nome_arquivo_final)
unificador = PdfMerger()
for arquivo in arquivos:
    print(f"Adicionando: {os.path.basename(arquivo)}")
    unificador.append(arquivo)

unificador.write(caminho_final)
unificador.close()
print(f"\n Arquivo final salvo com sucesso em : \n{caminho_final}")