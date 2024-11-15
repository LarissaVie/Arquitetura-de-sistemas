import json

def carregarJson(file):
    conteudo = open(file, 'r')
    conteudo = conteudo.read()
    dados = json.loads(conteudo)
    return dados


def calcularMediaSalarial(dados):
    soma = 0
    media = 0.0
    for item in dados:
        soma+= item["salario"]

    media = soma/len(dados)

    return media
   
   
def calcularMediaIdade(dados):
    soma = 0
    media = 0
    for item in dados:
        soma+= item["idade"]

    media = soma//len(dados)

    return media
   

dados_json = carregarJson("clientes.txt")

media_salarial = calcularMediaSalarial(dados_json)
faixa_etaria_media = calcularMediaIdade(dados_json)

print(f'Média salarial: {media_salarial}')
print(f'Faixa etária média: {faixa_etaria_media}')