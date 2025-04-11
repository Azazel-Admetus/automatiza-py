import tkinter as tk
from tkinter import filedialog
import ocrmypdf
import os
from time import sleep

root = tk.Tk()
root.withdraw()
entrada = filedialog.askopenfilename(
    title="Selecione o PDF para aplicar o OCR",
    filetypes=[("Arquivos PDF", "*.pdf")]
)
if not entrada:
    print("Nenhum arquivo selecionado. Encerrando o processo...")
    sleep(3)
    exit()

saida = filedialog.asksaveasfilename(
    defaultextension=".pdf",
    filetypes=[("PDF", "*.pdf")],
    title="Salvar PDF com OCR como..."
)

if not saida:
    print("Caminho de saida não definido. Encerrando o processo...")
    sleep(3)
    exit()

try:
    print("Processando OCR, aguarde...")
    ocrmypdf.ocr(
        entrada, 
        saida, 
        language='por',
        deskew=True, 
        force_ocr=True, 
        progress_bar=True
    )
    print(f"\n OCR completo! Arquivo salvo em: {saida}")
except Exception as e:
    print(f"Erro duranter o OCR: {e}")

    