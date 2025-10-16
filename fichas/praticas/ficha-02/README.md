# IA - Ficha 02

Resolução da Ficha 02 de Inteligência Artificial 2025/2026.

## Formulação do problema

Para formular o problema devemos identificar as seguintes componentes:
- representação de estados: **nodo** do grafo
- estado inicial: **Elvas**
- estado objetivo: **Lisboa**
- operações: **transitar** de uma cidade para outra, caso exista uma ligação entre elas
- custo da solução: **somatório do peso** de cada aresta do caminho definido.

## Resultados

Aplicando o algoritmo **Greedy**, obtemos o seguinte resultado:
- custo: 267
- caminho: [`elvas`, `alandroal`, `redondo`, `monsaraz`, `barreiro`, `baixadabanheira`, `moita`, `alcochete`, `lisboa`]
- nodos visitados: {`barreiro`, `alcochete`, `moita`, `palmela`, `alandroal`, `redondo`, `borba`, `baixadabanheira`, `monsaraz`, `elvas`, `arraiolos`}

Aplicando o algoritmo **A\***, obtemos o seguinte resultado:
- custo: 155
- caminho: [`elvas`, `borba`, `estremoz`, `evora`, `montemor`, `vendasnovas`, `lisboa`]
- nodos visitados: {`evora`, `barreiro`, `montemor`, `alcochete`, `moita`, `palmela`, `alandroal`, `redondo`, `vendasnovas`, `borba`, `estremoz`, `baixadabanheira`, `monsaraz`, `elvas`, `arraiolos`}

Podemos verificar que o algoritmo de procura A* obteu um custo menor, pois a avaliação tem em consideração tanto a heuristica como o custo da aresta.

## Cenário diferente

No cenário onde possa existir congestionamentos de tráfego, seria necessário alterar a função de heuristica, de forma a obter um resultado orientado a esta.
