# IA - Ficha 01

Resolução da Ficha 01 de Inteligência Artificial 2025/2026.

## Formulação do problema

Para formular o problema devemos identificar as seguintes componentes:
- representação de estados
- estado inicial
- estado objetivo
- operações
- custo da solução

Sendo que o problema é determinar um caminho entre dois vértices num grafo, podemos definir que um **estado** é representado por um nodo do grafo.
O **estado inicial** é um vértice do grafo, neste caso o vértice `s`.
O **estado objetivo** é também um vértice, neste caso o vértice `t`.
As **operações** possíveis são transitar de um nodo para outro, caso exista uma aresta entre eles.
O **custo da solução** será o somatório do peso de cada aresta do caminho definido.

## Resultados

Aplicando o algoritmo **Depth-First**, obtemos o seguinte resultado:
- custo: 12
- caminho: `s` -> `a` -> `b` -> `c` -> `d` -> `t`
- nodos visitados: {`s`, `b`, `c`, `a`, `t`, `d`}

Aplicando o algoritmo **Breadth-First**, obtemos o seguinte resultado:
- custo: 11
- caminho: `s` -> `e` -> `f` -> `g` -> `t`
- nodos visitados: {`s`, `b`, `c`, `d`, `a`, `t`, `g`, `e`, `f`}

Podemos verificar que o algoritmo de procura em largura obteu um custo menor, pois a avaliação é feito em relação ao peso de cada aresta.
Se o custo da solução for calculado em relação ao número de nodos visitados, a procura em profundidade prevalece, pois visita menos vértices.
