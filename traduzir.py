from langdetect import detect, LangDetectException
from deep_translator import GoogleTranslator
import textwrap
import sys

# Função para dividir texto em partes menores respeitando o limite
def dividir_texto(texto, limite=4500):
    return textwrap.wrap(texto, width=limite, break_long_words=False, break_on_hyphens=False)

# Função para traduzir texto grande
def traduzirtext(texto, destino="pt"):
    partes = dividir_texto(texto)
    traducao_total = ""
    for parte in partes:
        traducao = GoogleTranslator(source='auto', target=destino).translate(parte)
        traducao_total += traducao + " "
    return traducao_total.strip()

# Função para identificar idioma com tratamento de erro
def identificarlang(texto):
    try:
        return detect(texto)
    except LangDetectException:
        return None

# Entrada multilinha
print("Digite seu texto (pressione Ctrl+Z e depois Enter para terminar):")
texto = sys.stdin.read().strip()

# Verificação se há texto
if not texto:
    print("⚠️ Texto vazio, tente novamente com algo mais.")
else:
    textidioma = identificarlang(texto)
    if not textidioma:
        print("⚠️ Não foi possível identificar o idioma do texto.")
    elif textidioma == "pt":
        print(texto)
    else:
        textoprint = traduzirtext(texto)
        print(textoprint)
