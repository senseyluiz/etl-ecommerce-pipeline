import json
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import pandas as pd

# Carrega as variáveis do .env
load_dotenv("../config/.env")

# Configurações do banco
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

# Cria conexão
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
engine = create_engine(DATABASE_URL)

def load_data():
    # Carrega o json
    with open("../data/sales_enriched.json") as json_file:
        sales = json.load(json_file)

    df = pd.DataFrame(sales)
    df.to_sql(
        "sales",
          con=engine,
          index=False,
          if_exists="append" # Adiciona os dados
          )
    print("\33[32m Dados carregados com sucesso \33[m")


if __name__ == "__main__":
    load_data()