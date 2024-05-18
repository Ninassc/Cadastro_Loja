import time
cores = {'vermelho':('\033[31m'),
         'verde':('\033[32m'),
         'amarelo':('\033[33m'),
         'azul':('\033[34m'),
         'magenta':('\033[35m'),
         'ciano':('\033[36m'),
         'cinza':('\033[37m'),
         'bold':('\033[1m'),
         'limpa':('\033[m')}

def imposto(preco):
    imposto = preco * 0.05
    timposto = preco + imposto
    print(f'O imposto é de {imposto} e preço total é de {timposto}')
    

produtos = {'tablet': 600, 'pc gamer': 15000, 'notbook': 750, 'celular anroid': 1600, 'iphone 15': 13000}

vezes = int(input(f'Quantas {cores['amarelo']}vezes{cores['limpa']} deseja fazer o processo? '))
for vezes in range(vezes):
    produto = str(input(f'Que {cores['amarelo']}produto{cores["limpa"]} deseja verificar no sistema? ')).lower()
    if produto in produtos:
        print(f'{cores["verde"]}Produto disponível na loja{cores["limpa"]}')
        preco = produtos[produto]
        preco = imposto(preco)
    else:
        print(f'{cores["vermelho"]}Produto não disponível na loja{cores["limpa"]}')
    
    remover = str(input(f'Deseja remover algum prouto {cores["bold"]}(sim/não)?{cores["limpa"]}  '))
    if remover == 'sim':
        qremover = str(input(f'Qual produto deseja {cores["amarelo"]}remover{cores["limpa"]}? ')).lower()
        preco_qremover = produtos[qremover]
        produtos.pop(qremover)
        print(f'{cores["magenta"]}Removendo...{cores["limpa"]}')
        time.sleep(0.5)
        print(f'Produto {cores["ciano"]}{qremover}{cores["limpa"]} e o seu preço {cores["ciano"]}{preco_qremover}{cores["limpa"]} foram removidos')
    else:
        print(f'{cores["verde"]}Nenhum produto removido{cores["limpa"]}')

    adicionar = str(input(f'Deseja adicionar algum produto {cores["bold"]}(sim/não){cores["limpa"]}? '))
    if adicionar == 'sim':
        qadicionar = str(input(f'Qual produto deseja {cores["amarelo"]}adicionar{cores["limpa"]}? '))
        qpreco = float(input(f'Que {cores["amarelo"]}preço{cores["limpa"]} deseja adicionar ao produto? '))
        print(f'{cores["magenta"]}Adicionando...{cores["limpa"]}')
        time.sleep(0.5)
        produtos[qadicionar] = qpreco
        print(f'Produto {cores["ciano"]}{qadicionar}{cores["limpa"]} e o seu preço {cores["ciano"]}{qpreco}{cores["limpa"]} foram adicionados')
    else:
        print(f'{cores["vermelho"]}Nenhum produto adicionado{cores["limpa"]}')

print(f'Os produtos disponíveis e seus valores são {produtos}')
    

