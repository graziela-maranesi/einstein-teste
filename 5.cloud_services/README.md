## Questão 5

`Cloud Services (10 pontos) Descreva como você faria o deploy da API Flask criada anteriormente usando Docker e AWS (EC2 ou Fargate). Explique as etapas principais.
`

### Passo a Passo

- Criaria um dockerfile para poder executar a API independente do sistema operacional
- Criaria uma imagem a partir deste dockerfile localmente
- Subiria esta imagem para o dockerhub ou um container registrty privado como o executar
- Subiria uma instancia no EC2 e instalaria o dockerfile
- Baixaria a imagem docker (pull) dentro na EC2
- Precisaria criar as regras de network para habilitar o acesso da porta para API. Confesso que este passo eu tenho mais dificuldade e possivelmente precisaria de ajuda.

### Pontos de Atenção

- Nunca utilizei o Fargate
