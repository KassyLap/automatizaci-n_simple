import unicodedata

def sanitizar(texto):
    texto = unicodedata.normalize('NFD', texto)
    resultado = ""

    for c in texto:
        if unicodedata.category(c) != 'Mn' and c.isalnum() or c == ' ':
            resultado += c.lower()

    return resultado
