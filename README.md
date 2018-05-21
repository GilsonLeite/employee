# API REST

# Especificações e Requisitos do Projeto
Desenvolvimento de um projeto para cadastro de funcionarios usando REST para integração.

#### APP Cadastro:
- Nome
- Email
- Departamento
- Ativo

#### API REST deve efetuar as seguintes interações
- Listagem de funcionários
- Detalhes de um Funcionário
- Cadastro de um novo Funcionário
- Atualização de um Funcionário
- Exclusão de um Funcionário

## Tecnologias
Neste projeto foi usado as seguintes tecnologias
Django framework versão 2.0.5,
Django REST Framework versão 3.8.2,
Linguagem de programação Python 3.5.2,
Banco de dados Sqlite3.

## Preparando o Ambiente isolado instalando o projeto e pacotes

**1. Download do projeto, via git clone**:
`$ git clone https://github.com/GilsonLeite/employee`

**2. Criando e ativando o ambiente**:
`$ cd employee` enter,
`$ python3 -m venv` enter,
`$ souce bin/activate` enter,
`cd ../` enter.

**3.Instalar pacotes**:
`(venv)$ python manage.py -r requeriments.txt` enter

**4. Criar bade de dados**:
`(venv)$ python manage.py migrate` enter
`(venv)$ python manage.py createsuperuser` enter
`(venv)$ python manage.py makemigrations cadastro` enter
`(venv)$ python manage.py migrate cadastro` enter

**6. Executando o projeto:**
`python manage.py runserver`

**7. Acessando Admin Cadastro:**
http://127.0.0.1:8000/admin/

**8. Acessando API REST:**
http://127.0.0.1:8000/employee/

### Endpoints
**Método**|**Endpoint**|**Ação**
:--:|:--:|:--:
GET|`http://127.0.0.1:8000/employee/`|lista os funcionários
GET|`http://127.0.0.1:8000/employee/<id>`|Detalhe do funcionário
POST|`http://127.0.0.1:8000/employee/`|cria um novo funcionário
PUT|`http://127.0.0.1:8000/employee/<id>/`|atualiza um funcionário
DELETE|`http://127.0.0.1:8000/employee/<od>/`|deleta um funcionário

**CURL Request lista no terminal**
`curl -H "Content-Type: application/javascript" http://localhost:8000/employee/`

**Response Json**
```json
[
    {
      "id": 1,
      "name": "Gilson Leite",
      "email": "example@gmail.com",
      "department": "Developer",      
  },
  {
        "id": 2,
        "name": "Lucas Leite",
        "email": "example-lucas@gmail.com",
        "department": "Developer"
    }
]
```

**CURL Request detalhe no terminal**
`curl -H "Content-Type: application/javascript" http://localhost:8000/employee/1/`

**Response Json**
```json
[
    {
      "id": 1,
      "name": "Gilson Leite",
      "email": "example@gmail.com",
      "department": "Developer",      
  } 
]
```


**Testes unitários**
`(venv)$ python manage.py test`

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.010s

OK
Destroying test database for alias 'default'...
```
