# Algoritmos de Busca em Grafos

Agora, vamos abordar um problema de busca, mas com uma **Busca em Largura (Breadth-First Search, BFS)**, que explora todos os caminhos possíveis em uma "largura" de uma camada de nós (neste caso, cidades) antes de avançar para a próxima camada.

A diferença principal para o algoritmo anterior [Busca de Custo Uniforme](https://github.com/alexmontanha/busca_custo_uniforme) é que o **BFS** não se importa com os custos dos caminhos, mas sim com a quantidade de camadas (níveis) percorridos. Esse método é útil para encontrar o menor número de passos, ou a solução que envolva o menor número de transições entre cidades, independentemente dos custos.

## Explicação

1. **Grafo sem custos**: Diferente do [exemplo anterior](https://github.com/alexmontanha/busca_custo_uniforme) , aqui ignoramos os custos das rotas entre as cidades, focando apenas na conectividade. O grafo é representado por um dicionário onde cada cidade (chave) tem uma lista de vizinhos (valor).

2. **Fila (Queue)**: O BFS utiliza uma fila (FIFO – First In, First Out), aqui implementada com `deque`, para armazenar os caminhos explorados. Ao contrário do UCS que prioriza o menor custo, o BFS trata todos os caminhos igualmente, explorando cada camada de cidades (ou seja, o conjunto de cidades vizinhas) em cada iteração.

3. **Visitados (Visited Set)**: Usamos um conjunto `visited` para evitar explorar cidades repetidas. Quando uma cidade é visitada, ela é adicionada a esse conjunto.

4. **Loop de Busca**
   - O algoritmo remove o primeiro caminho da fila e verifica se a última cidade desse caminho é o destino (meta). Se for, o caminho é retornado.
   - Caso contrário, ele adiciona as cidades vizinhas (que ainda não foram visitadas) à fila como novos caminhos.

5. **Finalização**: Quando o destino é encontrado, o caminho percorrido até ele é retornado e impresso.

## Diferenças e Vantagens da Abordagem BFS

- **Custo Ignorado**: O BFS busca simplesmente o menor número de transições entre cidades, sem considerar custos. É adequado quando os custos entre as ações (movimentos) são uniformes ou irrelevantes.
- **Ideal para encontrar o menor número de passos**: BFS garante encontrar a solução com o menor número de transições, mas pode não ser o caminho mais barato se os custos variam.
- **Aplicação em grafos não ponderados**: O BFS é mais adequado para problemas onde as arestas (caminhos) entre os nós (cidades) não têm pesos, ou quando procuramos uma solução rápida sem considerar otimização de custos.

### Exemplo de Execução

Considerando o grafo da Romênia, o caminho mais curto em termos de transições de Arad até Bucareste pode ser:

```plaintext
Arad → Sibiu → Fagaras → Bucareste
```

Esse caminho envolve 3 passos (ou transições). No entanto, não é necessariamente o caminho de menor custo, pois o algoritmo não considera os valores das distâncias (custos entre as cidades).

## Conclusão

Este exemplo de **Busca em Largura (BFS)** explora de forma diferente o espaço de estados. Ele é ideal para encontrar soluções com o menor número de etapas, mas pode ser ineficiente para problemas que envolvem custos variáveis, ao contrário da Busca de Custo Uniforme, que prioriza caminhos com o menor custo total.

Ambos os algoritmos têm suas vantagens e são adequados para diferentes tipos de problemas.
