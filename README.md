# DevQuiz

Api rest para o devquiz

## Features

- Criação de username;
- Alteração do username;
- Tentativa de responder o quiz (questões aleatórias);
- Remover respostas antigas;
- Visualizar o progresso;

## Documentação da API e endpoints

A documentação é servida no endpoint `/docs` da aplicação.

## Execução

Criação do ambiente virtual do python

```sh
python3 -m venv venv
```

### Ativação do venv

- Windows (PowerShell):

```sh
./venv/bin/Activate.ps1
```

- MacOS/Linux:

```sh
source ./venv/bin/activate
```

Instalação das dependências do projeto

```sh
pip install -r requirements.txt
```

### Criação das variáveis de ambiente

**OBS**: Esse passo é obrigatório para o funcionamento da API, leia com atenção!

Criação do arquivo .env para configuração das variáveis de ambiente

Esse comando vai gerar um .env baseado no env.example por comodidade, mas você pode configurar o arquivo com os valores que quiser, respeitando somente os nomes das variáveis

```sh
cat .example.env > .env
```

Iniciando o servidor

```sh
flask run
```

