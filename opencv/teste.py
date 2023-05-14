import re

# Dicionário de palavras incorretas e suas correções
corrections = {
    'denuciar': 'denunciar',
    'fassil': 'fácil',
    'deverias': 'deverias',
    # Adicione mais palavras aqui
}

# Expressão regular que identifica as palavras incorretas
pattern = re.compile(r'\b(' + '|'.join(corrections.keys()) + r')\b')

# Função que substitui as palavras incorretas pelas corretas
def correct_words(match):
    return corrections[match.group(0)]

# Texto com palavras incorretas
text = 'Eu vou denuciar aquele fassil de quem deverias cuidar.'

# Substitui as palavras incorretas pelas corretas
corrected_text = pattern.sub(correct_words, text)

# Imprime o texto corrigido
print(corrected_text)
