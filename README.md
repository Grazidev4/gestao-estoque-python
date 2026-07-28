# 📦 Sistema de Gestão de Estoque

Uma aplicação web leve e funcional para controle e gestão de estoque de produtos. Desenvolvida em **Python** utilizando o micro-framework **Flask**, com renderização de páginas via **Jinja2** e persistência de dados em arquivo **JSON**.

---

## 🎨 Apresentação da Interface

O sistema conta com um layout moderno, responsivo e intuitivo, permitindo a gestão fácil de produtos:

* **Formulário de Cadastro:** Adição de novos itens com nome e preço.
* **Barra de Busca Dinâmica:** Filtragem em tempo real da tabela de produtos.
* **Tabela de Produtos:** Visualização clara com formatação de moeda e botões de ação (Remover).

---

## 🛠️ Tecnologias Utilizadas

* **Back-end:** [Python 3](https://www.python.org/)
* **Framework Web:** [Flask](https://flask.palletsprojects.com/)
* **Template Engine:** [Jinja2](https://jinja.palletsprojects.com/)
* **Front-end:** HTML5 e CSS3 puro (com design responsivo)
* **Persistência de Dados:** JSON (armazenamento local permanente)

---

## Funcionalidades (CRUD + Search)

- [x] **Cadastrar Produtos:** Envio de dados via formulário `POST` com validação de campos.
- [x] **Listar Produtos:** Leitura e exibição dos produtos persistidos no arquivo JSON.
- [x] **Buscar Produtos:** Filtro dinâmico via requisição `GET` diretamente no servidor.
- [x] **Remover Produtos:** Exclusão de itens pelo índice dinâmico na rota da aplicação.
- [x] **Tratamento de Exceções:** Criação automática da estrutura de dados na primeira execução caso o arquivo JSON não exista.

---

## 💻 Como executar o projeto localmente

### Pré-requisitos
* Ter o **Python 3.x** instalado na sua máquina.

### Passo a Passo

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/Grazidev4/gestao-estoque-python.git](https://github.com/Grazidev4/gestao-estoque-python.git)
