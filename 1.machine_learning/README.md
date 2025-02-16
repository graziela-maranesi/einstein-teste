## Questão 1

`Machine Learning (10 pontos) Explique com suas palavras qual seria o impacto de um dataset desbalanceado em um modelo de classificação e proponha uma solução para mitigar esse problema.`

Um dataset desbalanceado pode gerar vícios no modelo por falta de dados. Uma possível solução seria re-treinar o modelo com mais exemplos da categoria com menor quantidade de dados. Se não for possível, também poderíamos modificar o peso de cada parâmetro dentro do treinamento, se tivermos convicção de que aquele parâmetro qualifica os dados de maneira mais assertiva.
