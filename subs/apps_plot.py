

from flask import render_template, session
from classes.seller import Seller
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import io
import base64


def apps_plot():
    # Liga à base de dados do teu projeto
    engine = create_engine('sqlite:///' + filename + 'Marketplace.db')

    # Lê a tabela Transaction
    df_transaction = pd.read_sql_query('SELECT * FROM "Transaction"', con=engine)

    # Soma o valor das transações por seller
    result = df_transaction.groupby('seller_id')['transactions'].sum()

    # Vai buscar os nomes dos sellers
    seller_ids = result.index
    seller_names = []

    for seller_id in seller_ids:
        seller_obj = Seller.obj[int(seller_id)]
        seller_names.append(seller_obj.name)

    total_transactions = result.values

    # Cria gráfico de barras
    df_plot = pd.DataFrame({
        "Seller": seller_names,
        "Total Transactions": total_transactions
    })

    # Mostra apenas os 10 sellers com mais transactions
    df_plot = df_plot.sort_values("Total Transactions", ascending=False).head(10)
    
    # Cria gráfico horizontal
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.barh(df_plot["Seller"], df_plot["Total Transactions"])
    
    ax.set_xlabel("Total Transactions")
    ax.set_ylabel("Seller")
    ax.set_title("Top 10 sellers by total transactions")
    
    # Coloca o maior em cima
    ax.invert_yaxis()
    
    plt.tight_layout()

    # Converte o gráfico para imagem
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)

    buf.seek(0)
    image = base64.b64encode(buf.getvalue()).decode('utf-8')

    return render_template("plot.html", image=image, ulogin=session.get("user"))