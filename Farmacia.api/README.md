# API de Gestão de Medicamentos 💊

Esta API, desenvolvida com o framework FastAPI, permite gerenciar uma lista de medicamentos em uma farmácia. A API oferece funcionalidades básicas de CRUD (Criar, Ler, Atualizar, Excluir) para medicamentos, com armazenamento em memória.

## Funcionalidades ✨

- **Listar todos os medicamentos**: Exibe todos os medicamentos cadastrados.
- **Cadastrar um novo medicamento**: Permite adicionar um novo medicamento com nome, descrição, preço e quantidade.
- **Atualizar os dados de um medicamento**: Modifica as informações de um medicamento através do seu ID.
- **Excluir um medicamento**: Remove um medicamento da lista pelo seu ID.

## Endpoints 🌐

### 1. Listar Todos os Medicamentos 📋

**Método**: `GET /medications`

Retorna todos os medicamentos cadastrados na base de dados.

**Exemplo de resposta:**
```json
{
  "status": "success",
  "message": "Medicamentos recuperados com sucesso.",
  "data": [...]
}
```

---

### 2. Cadastrar um Novo Medicamento ➕

**Método**: `POST /medications`

Adiciona um novo medicamento à lista de medicamentos.

**Corpo da requisição (JSON):**
```json
{
  "name": "Paracetamol",
  "description": "Analgésico e antipirético",
  "price": 9.99,
  "quantity": 50
}
```

**Exemplo de resposta:**
```json
{
  "status": "success",
  "message": "Medicamento adicionado com sucesso.",
  "data": {
    "id": 1,
    "name": "Paracetamol",
    "description": "Analgésico e antipirético",
    "price": 9.99,
    "quantity": 50
  }
}
```

---

### 3. Atualizar os Dados de um Medicamento ✏️

**Método**: `PUT /medications/{medication_id}`

Atualiza as informações de um medicamento existente pelo seu ID.

**Corpo da requisição (JSON):**
```json
{
  "name": "Dipirona",
  "description": "Analgésico potente",
  "price": 12.99,
  "quantity": 30
}
```

**Exemplo de resposta:**
```json
{
  "status": "success",
  "message": "Medicamento atualizado com sucesso.",
  "data": {
    "id": 1,
    "name": "Dipirona",
    "description": "Analgésico potente",
    "price": 12.99,
    "quantity": 30
  }
}
```

**Exemplo de resposta (caso não encontrado):**
```json
{
  "status": "error",
  "message": "Medicamento não encontrado."
}
```

---

### 4. Excluir um Medicamento ❌

**Método**: `DELETE /medications/{medication_id}`

Remove um medicamento da lista pelo seu ID.

**Exemplo de resposta:**
```json
{
  "status": "success",
  "message": "Medicamento removido com sucesso.",
  "data": {
    "id": 1,
    "name": "Dipirona",
    "description": "Analgésico potente",
    "price": 12.99,
    "quantity": 30
  }
}
```

**Exemplo de resposta (caso não encontrado):**
```json
{
  "status": "error",
  "message": "Medicamento não encontrado."
}
```

---

## Como Rodar 🚀

### Pré-requisitos

- **Python 3.9+**: Certifique-se de ter o Python instalado na sua máquina.
- **FastAPI e Uvicorn**: Instale as dependências necessárias para rodar a API.

### Passos para Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-repositorio-url.git
   cd seu-repositorio
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

4. Acesse a documentação da API:
   - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Licença 📜

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.