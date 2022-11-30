import matplotlib.pyplot as plt
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


def consultaPalavras(frequencia):
    palavra = input('Palavra: ')
    return (f"{palavra} aparece {frequencia.get(palavra,0)} vezes no texto.")


def ordenaPalavras(frequencia):
    from operator import itemgetter
    top_palavras = sorted(frequencia.items(), key=itemgetter(1), reverse=True)
    for palavra, qtde in top_palavras[:30]:
        print(f"{palavra}: {qtde}")


def frequenciaLetras(texto):
    from collections import Counter
    letras = [c for c in texto if c.isalpha()]
    frequencia_letras = Counter(letras)
    return frequencia_letras


textoLimpo = limpaTexto(texto)
palavras = listaPalavras(textoLimpo)
frequencia = frequenciaPalavras(palavras)
frequenciaL = frequenciaLetras(texto)
letrasMaisComum = frequenciaL.most_common(15)
#print(f'{len(textoLimpo)} caracteres carregadas após limpeza.')
#print(f'{len(palavras)} palavras carregadas.')
#print(f'{len(frequencia)} palavras únicas carregadas.')
# print(f'{consultaPalavras(frequencia)}')
# print(f'{ordenaPalavras(frequencia)}')
print(f'{letrasMaisComum}')

rotulos, valores = zip(*letrasMaisComum)
plt.title('Frequência de letras em inglês')
plt.bar(rotulos, valores)
plt.show()
