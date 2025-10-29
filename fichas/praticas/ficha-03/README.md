# IA - Ficha 03

Resolução da Ficha 03 de Inteligência Artificial 2025/2026.

## Formulação do problema

Para formular o problema devemos identificar as seguintes componentes:
- representação de estados: tuplo com a quantidade de liquido em cada balde (e.g.: `(0,0)`)
- estado inicial: `(0,0)`
- estado objetivo: `(0,2)` e `(2,0)` 
- operações:
  - esvaziar balde A (pré: balde A tem de ter conteúdo)
  - esvaziar balde B (pré: balde B tem de ter conteúdo)
  - encher balde A (pré: balde A não está cheio)
  - encher balde B (pré: balde B não está cheio)
  - transferir conteúdo do balde A para o balde B (pré: balde A tem água e B não está cheio)
  - transferir conteúdo do balde B para o balde A (pré: balde B tem água e A não está cheio)
- custo da solução: número de operações realizadas

