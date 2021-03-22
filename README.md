# Lugares a ir rede social
Link: (futuramente)
Criado por mim mesmo **Fabricio Patrocinio**
Usando Python com Flask

## Ideia
A ideia é criar um rede social onde as pessoas possam adicionar fotos de paisagens ou lugares de lazer, descrição e endereço do local.

### Principais recursos
- Tema free do bootstrap.
- Todos os recursos do python estão em requirements.txt
- Para gerar imagens aleatórias estou usando lorem ipsum imagens.
- No slide das imagens estou usando framework Glider.js

### Dependências usadas
As dependências que usei se encontram no requirements.txt. Para instalar use o comando:
```
pip install -r requirements.txt
```

### Banco de dados
No banco de dados estou usando SQLAlchemy com Migrate. E todos os dados do banco se encotra na pasta _migrations_.
Crie um banco de dados com nome **lugares_a_ir** e rode no terminal esse comando:
```
flask db upgrade
```
Caso não consiga criar o banco de dados, apague a pasta migrations e use:
```
flask db init
flask db migrate
flask db upgrade
```
Feito isso ele irá criar todas as tabelas no seu banco.

### Rodar o projeto
Dentro da pasta raiz rode esse comando:
```
flask run (Para rodar o servidor)
```

### Outros recursos usados
- Tema free do Mashup Template/Unsplash.
- Gliter para criar os carousels.
- Banco de dados com todas cidades e estados do Brasil, com tabelas relacionais.
