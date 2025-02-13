# API de Vendas

## Descrição do Projeto
Esta é uma API desenvolvida em Python para gerenciar uma aplicação de vendas. O objetivo é fornecer um sistema eficiente para cadastrar vendedores, clientes, itens disponíveis para compra e registrar as vendas realizadas.

## Tecnologias Utilizadas
- **Python**
- **FastAPI**
- **PostgreSQL**
- **Docker**
- **Amazon EC2**

## Funcionalidades
- **Cadastro de Vendedores**: Cada venda precisa estar associada a um vendedor.
- **Cadastro de Clientes**: Armazena informações sobre os compradores.
- **Cadastro de Itens**: Mantém a lista de produtos disponíveis para venda.
- **Registro de Vendas**: Permite registrar vendas associadas a um vendedor e cliente.
- **Consulta de Vendas**: Permite buscar histórico de vendas por vendedor, cliente ou data.

## Como Executar o Projeto
### Requisitos
- Python 3.8+
- Banco de Dados PostgreSQL (ou SQLite para testes)
- Dependências do projeto (listadas em `requirements.txt`)

### Instalação e Execução
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Configure as variáveis de ambiente no arquivo `.env`.
4. Execute a aplicação:
   ```bash
   uvicorn app.main:app --reload
   ```

## Endpoints
### Exemplo de Endpoints Disponíveis
- `POST /vendedores/` - Cadastrar um novo vendedor
- `POST /clientes/` - Cadastrar um novo cliente
- `POST /itens/` - Cadastrar um novo item
- `POST /vendas/` - Registrar uma nova venda
- `GET /vendas/` - Listar todas as vendas
- `GET /vendas/{id}` - Consultar detalhes de uma venda específica

## Contribuição
Se deseja contribuir, faça um fork do repositório, crie uma branch para sua feature e envie um pull request.

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo `LICENSE` para mais detalhes.

