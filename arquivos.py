with open('sherlock.txt', encoding='utf8') as file:
    textoSherlock = file.read().lower()
    
with open('machado.txt', encoding='utf8') as file:
    textoMachado = file.read().lower()

with open('cervantes.txt', encoding='utf8') as file:
    textoCervantes = file.read().lower()


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


#print(f'{len(textoLimpo)} caracteres carregadas após limpeza.')
#print(f'{len(palavras)} palavras carregadas.')
#print(f'{len(frequencia)} palavras únicas carregadas.')
#print(f'{consultaPalavras(frequencia)}')
#print(f'{ordenaPalavras(frequencia)}')
#textoLimpo = limpaTexto(texto)
#palavras = listaPalavras(textoLimpo)
#frequencia = frequenciaPalavras(palavras)


qtdePalavras = 5
frequenciaLetraSherlock = frequenciaLetras(textoSherlock)
letrasMaisComumSherlock  = frequenciaLetraSherlock.most_common(qtdePalavras)
frequenciaLetraMachado = frequenciaLetras(textoMachado)
letrasMaisComumMachado = frequenciaLetraMachado.most_common(qtdePalavras)
frequenciaLetraCervantes = frequenciaLetras(textoCervantes)
letrasMaisComumCervantes = frequenciaLetraCervantes.most_common(qtdePalavras)

print(f'{letrasMaisComumMachado}, \n {letrasMaisComumSherlock}, \n {letrasMaisComumCervantes}')


import matplotlib.pyplot as plt
import numpy as np

rotulosS, valoresS = zip(*letrasMaisComumSherlock)
rotulosM, valoresM = zip(*letrasMaisComumMachado)
rotulosC, valoresC = zip(*letrasMaisComumCervantes)
labels = [str('      '+rotulosM[n]+'    '+rotulosS[n]+'    '+rotulosC[n]) for n in range(qtdePalavras)]
x = np.arange(len(labels))
width = 0.25
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, valoresS, width, label='Inglês')
rects2 = ax.bar(x + width/2, valoresM, width, label='Português')
rects3 = ax.bar(x + width/2 + 0.25, valoresC, width, label='Espanhol')

ax.set_ylabel('Quantidade')
ax.set_title('Mais Comuns')
ax.set_xticks(x, labels)
ax.legend()
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)
fig.tight_layout()
plt.show()