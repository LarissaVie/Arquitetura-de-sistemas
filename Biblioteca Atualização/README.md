# 📚 Sistema de Biblioteca com FastAPI e Bootstrap

Este projeto é um sistema de gerenciamento de biblioteca desenvolvido com FastAPI (backend), Jinja2 (templates HTML) e Bootstrap (frontend). Ele permite realizar operações CRUD (Create, Read, Update, Delete) para gerenciar livros em uma biblioteca. 📖✨

## 🚀 Funcionalidades

- 📋 **Listar Livros**: Exibe todos os livros cadastrados.
- ➕ **Adicionar Livro**: Permite adicionar um novo livro ao sistema.
- ✏️ **Editar Livro**: Permite editar as informações de um livro existente.
- 🗑️ **Excluir Livro**: Remove um livro do sistema.
- 📱 **Interface Responsiva**: Design moderno e responsivo usando Bootstrap.

## 🛠️ Tecnologias Utilizadas

- 🐍 **FastAPI**: Framework Python para construção de APIs e aplicações web.
- 🎨 **Jinja2**: Mecanismo de templates para renderizar páginas HTML.
- 🎀 **Bootstrap**: Framework CSS para estilização e design responsivo.
- 🖌️ **HTML/CSS**: Para a estrutura e estilos personalizados da interface.
- ⚡ **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.

## 📂 Estrutura do Projeto

biblioteca/
│
├── main.py
├── routers/
│   └── livros.py
├── services/
│   └── livro_service.py
├── models/
│   └── livro_model.py
├── templates/
│   ├── index.html
│   └── form.html
└── static/
    ├── css/
    │   └── styles.css


## 🛠️ Como Executar o Projeto

### Pré-requisitos

- 🐍 Python 3.7 ou superior.
- 📦 Pip (gerenciador de pacotes do Python).

### Passos para Configuração

1. 📥 Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/biblioteca-fastapi.git
    cd biblioteca-fastapi
    ```

2. 🌐 Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. 📦 Instale as dependências:

    ```bash
    pip install fastapi uvicorn
    ```

4. 🚀 Execute o servidor:

    ```bash
    uvicorn main:app --reload
    ```

5. 🌍 Acesse a aplicação:

    Abra o navegador e acesse: `http://127.0.0.1:8000/`

## 🗺️ Rotas da Aplicação

- `GET /`: Página inicial que lista todos os livros. 📋
- `GET /adicionar`: Exibe o formulário para adicionar um novo livro. ➕
- `POST /adicionar`: Processa o formulário e adiciona um novo livro. 📥
- `GET /editar/{livro_id}`: Exibe o formulário para editar um livro existente. ✏️
- `POST /editar/{livro_id}`: Processa o formulário e atualiza o livro. 🔄
- `POST /deletar/{livro_id}`: Remove um livro do sistema. 🗑️

## 🎨 Personalização

### Estilos CSS

Os estilos personalizados estão no arquivo `static/css/styles.css`. Você pode modificar as cores, fontes e outros aspectos visuais conforme necessário. 🎨

### Templates HTML

Os templates estão na pasta `templates/`. Eles são renderizados pelo Jinja2 e podem ser ajustados para incluir novas funcionalidades ou alterar o layout. 🖼️

## 🧑‍💻 Exemplos de Uso

### Adicionar um Livro

1. Acesse `http://127.0.0.1:8000/adicionar`.
2. Preencha o formulário com os detalhes do livro.
3. Clique em "Adicionar".

### Editar um Livro

1. Na página inicial, clique em "Editar" ao lado do livro desejado.
2. Modifique as informações no formulário.
3. Clique em "Atualizar".

### Excluir um Livro

1. Na página inicial, clique em "Excluir" ao lado do livro desejado.
2. Confirme a exclusão.

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## 🙏 Créditos

Desenvolvido por Jhonata Vieira e Larissa Vieira.