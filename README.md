[Read this page in English](README-en.md)

# Teoria dos Grafos

## Sumário

- [Teoria dos Grafos](#teoria-dos-grafos)
  - [Sumário](#sumário)
  - [Descrição](#descrição)
  - [Para executar o projeto](#para-executar-o-projeto)
  - [Classe Graph](#classe-graph)
    - [Métodos](#métodos)
    - [Verificação de Isomorfismo](#verificação-de-isomorfismo)
    - [Verificação da Similaridade](#verificação-da-similaridade)
  - [Classe Utils](#classe-utils)
    - [Métodos](#métodos-1)
  - [Casos de teste](#casos-de-teste)

## Descrição

Este repositório contém códigos desenvolvidos para a disciplina de Teoria dos Grafos.

## Para executar o projeto

Para executar o projeto, siga os passos abaixo:

1. Verifique se o seu ambiente está configurado para python
2. Clone o repositório: <https://github.com/I-Lima/Theory-of-graphs.git>
3. Importe o projeto em sua IDE preferida.
4. Execute o programa com o seguinte comando:

```
 python main.py
```

## Classe Graph

A classe Graph é uma representação de um grafo não direcionado. Ela contém métodos para manipulação de grafos e para calcular diferentes tipos de similaridade entre dois grafos. A manipulação do grafo é feita através da matriz de adjacência.

### Métodos

- **setAdjacencyMatrix**: Define a matriz de adjacência do grafo.
- **isIsomorphic**: Verifica se dois grafos são isomórficos, ou seja, se eles possuem a mesma estrutura básica.
- **readAdjacencyMatrixFromFile**: Lê uma matriz de adjacência de um arquivo.
- **isSimilar**: Calcula a similaridade entre dois grafos com base em diferentes métricas: cosseno, SimRank e Jaccard.

### Verificação de Isomorfismo

O método `isIsomorphic` é responsável por verificar se dois grafos são isomórficos. Um grafo é isomórfico a outro se houver uma correspondência bijetiva entre seus conjuntos de vértices de modo que a estrutura do grafo (relacionamentos entre os vértices) seja preservada.

Este método utiliza uma abordagem bastante direta e sistemática para verificar o isomorfismo entre dois grafos, garantindo que todos os critérios necessários para a isomorfia sejam verificados de maneira adequada. Ele percorre cada passo essencial para determinar se os grafos são isomórficos e retorna o resultado apropriado com base nesses critérios.

### Verificação da Similaridade

O método `isSimilar` é responsável por calcular a similaridade entre dois grafos, utilizando diferentes métricas: cosseno, SimRank e Jaccard. Cada métrica oferece uma perspectiva sobre a similaridade entre os grafos, considerando diferentes aspectos de sua estrutura e conectividade.

## Classe Utils

A classe Utils fornece métodos auxiliares para realizar a leitura de grafos e selecionar o método de cálculo de similaridade entre eles. Ela permite ao usuário escolher entre inserir os caminhos dos arquivos manualmente ou ler arquivos pré-salvos, além de selecionar o método de similaridade desejado.

### Métodos

- **readGraphs**: Este método permite ao usuário selecionar entre inserir manualmente os caminhos dos arquivos que contêm os grafos ou utilizar caminhos pré-salvos.
- **readSimilarityMethod**: Este método permite ao usuário escolher o método para calcular a similaridade entre os grafos.

## Casos de teste

O projeto dispõe de alguns casos de teste que podem ser executados através do seguinte comando

```
  python testCases.py
```
