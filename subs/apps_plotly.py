
from flask import render_template, session
from classes.seller import Seller
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px


def apps_plotly():
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

        # Cria gráfico interativo
    df_plot = pd.DataFrame({
        "Seller": seller_names,
        "Total Transactions": total_transactions
    })

    # Mostra apenas os 10 sellers com mais transactions
    df_plot = df_plot.sort_values("Total Transactions", ascending=False).head(10)
    
    # Cria gráfico horizontal interativo
    fig = px.bar(
        df_plot,
        x="Total Transactions",
        y="Seller",
        orientation="h",
        title="Top 10 sellers by total transactions",
        labels={
            "Total Transactions": "Total Transactions",
            "Seller": "Seller"
        }
    )
    
    fig.update_layout(
        yaxis={
            "categoryorder": "total ascending"
        }
    )
    plot_div = fig.to_html(full_html=False, div_id='my-plot')

    return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"))