# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:34:42 2026

@author: ritam
"""

import csv

from Category import Category
from Marketplace import Marketplace
from Seller import Seller
from Transaction import Transaction

def load_data(filename):
    Category.reset()
    Marketplace.reset()
    Seller.reset()
    Transaction.reset()

    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")

        for row in reader:
            
            category_id = int(row["category_id"])
            if category_id not in Category.obj:
                Category(
                    row["category_id"],
                    row["category_name"],
                    row["category_comments"]
                )

            
            marketplace_id = int(row["marketplace_id"])
            if marketplace_id not in Marketplace.obj:
                Marketplace(
                    row["marketplace_id"],
                    row["marketplace_name"],
                    row["mkt_created_date"],
                    row["category_id"]
                )

            
            seller_id = int(row["seller_id"])
            if seller_id not in Seller.obj:
                Seller(
                    row["seller_id"],
                    row["seller_name"],
                    row["seller_address"]
                )

            
            Transaction(
                0,
                row["transaction_date"],
                row["transaction_value"],
                row["seller_id"],
                row["marketplace_id"]
            )


def show_summary():
    print("=== RESUMO DOS DADOS ===")
    print(f"Categorias: {len(Category.obj)}")
    print(f"Marketplaces: {len(Marketplace.obj)}")
    print(f"Sellers: {len(Seller.obj)}")
    print(f"Transactions: {len(Transaction.obj)}")


def main():
    filename = "G52_data (1).csv"
    load_data(filename)
    show_summary()


if __name__ == "__main__":
    main()