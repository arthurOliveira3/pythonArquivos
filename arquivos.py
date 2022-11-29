with open('sherlock.txt', encoding='utf8') as file:
  texto = file.read().lower()

def limpaTexto(texto):
    texto_sem_pontuacao = ''
    for c in texto:
        if c.isalpha() or c == ' ':
            texto_sem_pontuacao += c
    return texto_sem_pontuacao    

def listaPalavras(textoLimpo):
    listaPalavras = textoLimpo.split()
    return listaPalavras

def frequenciaPalavras(listaPalavras):
    frequencia_palavras = {}
    for palavra in listaPalavras:
        if palavra not in frequencia_palavras:
            frequencia_palavras[palavra] = 0  
        frequencia_palavras[palavra] += 1
    return frequencia_palavras

print(f'{len(limpaTexto(texto))} caracteres carregadas após limpeza.')
print(f'{len(listaPalavras(limpaTexto(texto)))} palavras carregadas.')
print(f'{len(frequenciaPalavras(listaPalavras(limpaTexto(texto))))} palavras únicas carregadas.')
