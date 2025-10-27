
# IA - Ficha Teórico-Prática 03

Resolução da Ficha Teórico-Prática 03 de Inteligência Artificial 2025/2026.


## Exercício 1

Formulação do jogo:
- **Tipo de problema**: deterministico e de estado único.
- **Estado Inicial**: estação do Aeroporto.
- **Estado final**: estação Lumiar.
- **Operadores**: 
    - transitar de uma estação para outra (caso seja adjacente)
    - mudar de linha (caso exista interseção de linhas)
- **Custo**: tempo de transporte entre estações.


## Exercício 2

Formulação do jogo:
- **Tipo de problema**: deterministico e de estado único.
- **Representação de estados**: lista de (torre, lista de discos) (e.g.: `(B, [D1, D2])`).
- **Estado Inicial**: `[(A, []), (B, []), (C, [D1, D2, D3, D4])]`.
- **Estado final**: `[(A, [D1, D2, D3, D4]), (B, []), (C, [])]`.
- **Operadores**: 
    - mover um disco para outra torre (caso a torre destino esteja vazia, ou os discos lá colocados são maiores)
- **Custo**: número de movimentos.
