# 🚀 ETL E-commerce Pipeline

Pipeline de dados completo (ETL) desenvolvido em Python, responsável por extrair dados de uma API pública de e-commerce, transformar esses dados em um modelo analítico e carregá-los em um banco de dados PostgreSQL (Supabase).

---

# 📊 Objetivo

Construir um pipeline de dados de ponta a ponta que:

- Consome dados de uma API pública
- Realiza transformações e enriquecimento
- Calcula métricas de negócio
- Armazena os dados em um banco relacional
- Permite análises via SQL

---

# 🏗️ Arquitetura do Pipeline

API → Extract → JSON (raw) → Transform → JSON (enriched) → Load → PostgreSQL

---

# 🧰 Tecnologias Utilizadas

- Python
- Pandas
- SQLAlchemy
- PostgreSQL (Supabase)
- Requests
- Python-dotenv

---

# 📁 Estrutura do Projeto

<img width="188" height="415" alt="image" src="https://github.com/user-attachments/assets/e9b4e6d9-72b7-4c3a-a3e9-4f2c34db7d24" />

---

# 🔄 Etapas do Pipeline

## 🔹 1. Extract

- Consumo de dados da API de e-commerce
- Extração de:
  - Produtos
  - Carrinhos (vendas)
- Normalização dos dados (flatten)

**Saída:**

- data/products.json
- data/sales.json


---

## 🔹 2. Transform

- JOIN entre produtos e vendas
- Enriquecimento dos dados
- Criação de métricas de negócio

### Métrica criada:
 - revenue = price * quantity

 
**Saída:**
- data/sales_enriched.json


---

## 🔹 3. Load

- Carregamento dos dados no PostgreSQL (Supabase)
- Uso de `pandas.to_sql()` para inserção

**Tabela final:**
- sales


---

# 🗄️ Modelo de Dados

Tabela: `sales`

| Coluna        | Tipo     |
|--------------|----------|
| cart_id      | INT      |
| user_id      | INT      |
| product_id   | INT      |
| product_name | TEXT     |
| category     | TEXT     |
| price        | NUMERIC  |
| quantity     | INT      |
| date         | DATE     |
| revenue      | NUMERIC  |

---

# 📊 Análises (SQL)

Exemplos disponíveis em `sql/analytics.sql`:

- Receita por produto
- Receita por categoria
- Vendas por dia
- Produtos mais vendidos

---

# ⚙️ Como Executar o Projeto

## 1. Clonar repositório

```git clone https://github.com/seu-usuario/etl-ecommerce-pipeline.git```

```cd etl-ecommerce-pipeline```

---

## 2. Criar ambiente Virtual

 ```python -m venv .venv```
 
.venv\Scripts\activate # Windows

## 3. Instatlar dependencias
- ```pip install -r requirements.txt```

## 4. Configurar variáveis de ambiente
- Criar Arquivo:
  - config/.env
    - exemplo:
    - <img width="146" height="104" alt="image" src="https://github.com/user-attachments/assets/bf653b13-96a6-4691-b32d-882769ed6a6c" />

## 5. Executar pipeline
- Extração:

```python scripts/transform.py```

- Transformação:

  ```python scripts/transform.py```

- Carga:

  ```python scripts/load.py```
---

## 👨‍💻 Autor

Luis Henrique

Projeto desenvolvido para portfólio de Engenharia de Dados




