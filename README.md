# DevQuiz

Api rest para o devquiz

## Features

- Criação de username;
- Alteração do username;
- Tentativa de responder o quiz (questões aleatórias);
- Remover respostas antigas;
- Visualizar o progresso;

## Execução

Para executar o projeto, primeiro faça o build da imagem docker

```sh
docker build . -t devquiz-backend
```

Com a imagem pronta, suba o container (por padrão na porta 8080)

```bash
docker run -d devquiz-backend -p 8080:8080 devquiz-backend
```

## Documentação da API e endpoints

A documentação é servida no endpoint `/docs` da aplicação.

### Criação das variáveis de ambiente

**OBS**: Esse passo é obrigatório para o funcionamento da API, leia com atenção!

Criação do arquivo .env para configuração das variáveis de ambiente

Esse comando vai gerar um .env baseado no env.example por comodidade, mas você pode configurar o arquivo com os valores que quiser, respeitando somente os nomes das variáveis

```sh
cat .example.env > .env
```
