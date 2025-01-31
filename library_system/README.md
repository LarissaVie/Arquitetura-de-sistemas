# Sistema de Biblioteca

Este projeto é um sistema de gerenciamento de biblioteca desenvolvido em Python com FastAPI. Ele permite gerenciar livros, usuários e empréstimos de forma eficiente, seguindo os padrões de projeto **Model, View, Controller (MVC)**, **DAO (Data Access Object)** e **Service**.

---

## Funcionalidades Implementadas

### 1. Gerenciamento de Livros

- **Cadastrar livro**: Adicionar um novo livro ao acervo.
- **Listar livros**: Visualizar todos os livros cadastrados.
- **Buscar livro por ID**: Obter detalhes de um livro específico.
- **Atualizar livro**: Modificar informações de um livro existente.
- **Excluir livro**: Remover um livro do sistema.

### 2. Gerenciamento de Usuários

- **Cadastrar usuário**: Adicionar um novo usuário ao sistema.
- **Listar usuários**: Visualizar todos os usuários cadastrados.
- **Buscar usuário por ID**: Obter detalhes de um usuário específico.
- **Excluir usuário**: Remover um usuário do sistema.

### 3. Gerenciamento de Empréstimos

- **Realizar empréstimo**: Registrar o empréstimo de um livro para um usuário.
- **Listar empréstimos**: Visualizar todos os empréstimos registrados.
- **Devolver livro**: Registrar a devolução de um livro emprestado.

---

## Padrões de Projeto Aplicados

### 1. Model

- As classes `Book`, `User` e `Loan` representam as entidades do sistema.
- Elas são definidas no diretório `models/` e utilizam `Pydantic` para validação de dados.

### 2. DAO (Data Access Object)

- As classes `BookDAO`, `UserDAO` e `LoanDAO` são responsáveis pelo acesso aos dados.
- Elas simulam um banco de dados usando listas em memória e estão localizadas no diretório `dao/`.

### 3. Service

- As classes `BookService`, `UserService` e `LoanService` implementam a lógica de negócios.
- Elas validam regras e interagem com a camada DAO. Estão localizadas no diretório `services/`.

### 4. Controller

- Os endpoints da API são definidos nos arquivos `book_controller.py`, `user_controller.py` e `loan_controller.py`.
- Eles estão localizados no diretório `controllers/` e utilizam o FastAPI para expor as funcionalidades do sistema.

### 5. View

- As respostas da API são formatadas em JSON, seguindo as especificações do FastAPI.
- Mensagens de sucesso e erro são padronizadas para facilitar o consumo da API.

---

## Como Executar o Projeto

### Pré-requisitos

- Python 3.8 ou superior.
- FastAPI e Uvicorn instalados.

### Passos para Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-biblioteca.git
   cd sistema-biblioteca
   ```
2. Instale as dependências:
   ```bash
   pip install fastapi uvicorn
   ```
3. Execute o servidor:
   ```bash
   uvicorn main:app --reload
   ```
4. Acesse a API:
   ```bash
    A documentação interativa estará disponível em:
    Swagger UI: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc
   ```

## Como Testar o Sistema

### 1. Usando o Postman

- Importe a coleção do Postman localizada em `tests/postman_collection.json`.
- Teste todas as rotas da API, como:
  - `GET /api/books`: Listar livros.
  - `POST /api/books`: Adicionar livro.
  - `POST /api/loans`: Realizar empréstimo.
  - `PUT /api/loans/{loan_id}/return`: Devolver livro.

### 2. Usando a Documentação Interativa

- Acesse `http://127.0.0.1:8000/docs` para testar as rotas diretamente no navegador.

---

## Estrutura do Projeto

library_system/
├── models/
│ ├── book.py
│ ├── user.py
│ ├── loan.py
├── dao/
│ ├── book_dao.py
│ ├── user_dao.py
│ ├── loan_dao.py
├── services/
│ ├── book_service.py
│ ├── user_service.py
│ ├── loan_service.py
├── controllers/
│ ├── book_controller.py
│ ├── user_controller.py
│ ├── loan_controller.py
├── tests/
│ ├── postman_collection.json
├── main.py
├── README.md

---

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## Vídeo de Demonstração

Assista ao vídeo de demonstração do sistema [Neste Link](https://youtu.be/Jhi5CP-UaWM?feature=shared).
