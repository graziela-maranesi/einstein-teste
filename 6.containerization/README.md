## Questão 6

`Containerization (10 pontos) Crie um Dockerfile básico para a API Flask do exercício 3. O contêiner deve ser capaz de rodar a aplicação localmente.
`

### Como estou criando a imagem docker

```
docker build -t graziela-maranesi/api-flask:latest .
```

### Como executar o container local

```
docker run -p 5000:5000 graziela-maranesi/api-flask:latest
```
