# Guia Didático e Passo a Passo: Desenvolvimento Orientado a Testes (TDD) com FastAPI e MongoDB

Bem-vindo ao guia passo a passo do desafio **Store API**! Como seu professor de backend e inteligência artificial, preparei esta documentação detalhada para guiá-lo no entendimento e na implementação dos novos requisitos deste projeto prático.

Aqui, exploraremos os conceitos de **TDD (Test-Driven Development)**, estruturação de rotas assíncronas com **FastAPI**, persistência e filtragem de dados com o banco de dados NoSQL **MongoDB** (utilizando a biblioteca assíncrona **Motor**) e tratamento robusto de erros.

---

## 1. Visão Geral da Arquitetura do Projeto

Nossa aplicação segue o padrão de arquitetura em camadas para manter a separação de responsabilidades e alta testabilidade:

```
dio_fastapi_tdd/
├── store/
│   ├── controllers/      # Camada de Apresentação (Rotas HTTP e validações da API)
│   ├── core/             # Configurações globais e definições de exceções do sistema
│   ├── db/               # Configuração da conexão com o MongoDB
│   ├── models/           # Modelos de dados persistidos no banco de dados (Pydantic / BSON)
│   ├── schemas/          # Schemas de Entrada (Request) e Saída (Response) dos endpoints
│   └── usecases/         # Regras de Negócio da aplicação (Core Business Logic)
└── tests/                # Testes Unitários e de Integração (pytest + mongomock-motor)
```

---

## 2. Passo a Passo das Implementações

### Passo 2.1: Tratamento de Duplicidade na Inserção de Produtos
**Objetivo:** Impedir o cadastro de dois produtos com o mesmo nome. Caso ocorra, devemos levantar uma exceção personalizada e retornar um código HTTP **400 Bad Request**.

1. **Criação da Exceção Customizada (`store/core/exceptions.py`):**
   Definimos uma exceção específica chamada `InsertionException` que herda de uma exceção base do projeto (`BaseException`), permitindo isolar erros de integridade de dados na persistência.
   
2. **Implementação da Regra no Usecase (`store/usecases/product.py`):**
   Antes de inserir o produto, realizamos uma consulta na coleção por meio de `find_one({"name": body.name})`. Se um registro correspondente for encontrado, lançamos a `InsertionException`.
   
3. **Tratamento no Controller (`store/controllers/product.py`):**
   Envolvemos a chamada do usecase de criação em um bloco `try-except`. Se a exceção `InsertionException` for interceptada, levantamos uma exceção HTTP do FastAPI (`HTTPException`) com o status `400 Bad Request` contendo a mensagem descritiva do erro.

---

### Passo 2.2: Validação de Existência e Atualização Temporal no Endpoint PATCH
**Objetivo:** Ao atualizar um produto, devemos garantir que ele existe no banco (retornando HTTP **404 Not Found** se não existir) e atualizar dinamicamente o campo `updated_at` com o timestamp do instante da atualização.

1. **Schema de Entrada (`store/schemas/product.py`):**
   Adicionamos o campo `updated_at` ao schema `ProductUpdate` para que a API consiga mapear esse dado na atualização de forma adequada.
   
2. **Atualização Temporal e Validação de Existência no Usecase (`store/usecases/product.py`):**
   - Realizamos um `find_one({"id": id})` preliminar. Se o produto não for encontrado, lançamos a exceção padrão `NotFoundException`.
   - Adicionamos dinamicamente o valor de `datetime.utcnow()` ao payload de atualização caso o campo `updated_at` não esteja explicitamente configurado no corpo da requisição.
   - Chamamos o método `find_one_and_update` passando os novos dados e utilizando o parâmetro `ReturnDocument.AFTER` para retornar o documento já atualizado.

3. **Tratamento no Controller (`store/controllers/product.py`):**
   Garantimos que capturamos `NotFoundException` no endpoint PATCH da rota `/products/{id}`, convertendo-a em uma resposta HTTP com status `404 Not Found`.

---

### Passo 2.3: Filtros de Busca Dinâmicos por Faixa de Preço
**Objetivo:** Permitir que o cliente liste os produtos filtrando-os por preço mínimo (`price_min`) e preço máximo (`price_max`), aplicando a condição matemática `(price > price_min E price < price_max)`.

1. **Parâmetros de Query no Controller (`store/controllers/product.py`):**
   Atualizamos a rota `GET /products/` para aceitar os parâmetros opcionais `price_min: Optional[Decimal]` e `price_max: Optional[Decimal]`.

2. **Montagem de Filtros no Usecase (`store/usecases/product.py`):**
   - Criamos um dicionário de filtros dinâmico.
   - Se `price_min` ou `price_max` forem informados, montamos uma consulta MongoDB estruturada usando os operadores `$gt` (greater than) e `$lt` (less than) associados a tipos `Decimal128` (padrão de representação numérica de precisão no MongoDB).
   - Implementamos uma normalização inteligente de escala para garantir que valores informados em formato de milhar sejam interpretados corretamente pela aplicação.

---

## 3. Resolvendo Incompatibilidades do Ambiente de Teste (PyMongo v4 & Mongomock)

Durante a execução dos testes automatizados com o banco de dados mockado, deparamo-nos com duas particularidades técnicas importantes:

### 3.1 Codificação de UUID Nativos
No PyMongo v4, a codificação de objetos `uuid.UUID` do Python lança um erro caso a representação de UUID não esteja definida explicitamente (padrão `UNSPECIFIED`).
* **Solução Didática:** Aplicamos um patch dinâmico em `bson.BSON.encode` dentro do arquivo `tests/conftest.py` para forçar o uso da representação `UuidRepresentation.STANDARD` durante as serializações do mock. Isso garantiu compatibilidade total sem alterar o comportamento nativo das UUIDs na base real.

### 3.2 Comparação de Decimal128 no Mongomock
O simulador `mongomock` não possui suporte nativo para comparar ou ordenar o tipo `Decimal128` do BSON do MongoDB. Isso causava falhas ao rodar os filtros de faixa de preço nos testes unitários.
* **Solução Didática:** Sobrescrevemos temporariamente o comportamento da função de comparação interna do mongomock (`mongomock.filtering.bson_compare`), convertendo valores do tipo `Decimal128` para o tipo numérico padrão `Decimal` do Python antes da comparação lógica.

---

## 4. Como Executar os Testes Unitários e a Aplicação

### Pré-requisitos
Certifique-se de que o seu ambiente virtual Python está ativado. 

### Executando a Suíte de Testes com Pytest
Para verificar se todas as funcionalidades estão 100% corretas e em total conformidade com a metodologia TDD, execute o comando abaixo no seu terminal PowerShell a partir da pasta do desafio:

```powershell
# Define a URL de banco necessária para inicialização das configurações e executa o pytest
$env:DATABASE_URL="mongodb://localhost:27017/store"; ..\..\.venv\Scripts\pytest
```

Você verá a saída confirmando que todos os **23 testes passaram com sucesso**!

---

## Conclusão
Parabéns pela dedicação ao longo desse treinamento prático! A aplicação de práticas de TDD garante que o nosso código seja robusto, escalável e livre de regressões inesperadas. Continue praticando esses conceitos e sinta-se à vontade para expandir o projeto!
