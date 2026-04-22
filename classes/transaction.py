# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:42:44 2026

@author: ritam
"""

from gclass import Gclass
import datetime

class Transaction(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    att = ['_id','_date', '_transactions','_seller_id','_marketplace_id']
    
    header = 'Transaction'
    
    des = ['Id','Date', "Transactions",'Seller Id','Marketplace Id']
    
    def __init__(self,id, date, transactions, seller_id, marketplace_id):
        super().__init__()
        
        id= Transaction.get_id(id)
        self._id= id
        self._date = datetime.date.fromisoformat(date)
        self._transactions = float(transactions)        
        self._seller_id = int (seller_id)
        self._marketplace_id= int (marketplace_id)
        
        Transaction.obj[id]=self
        Transaction.lst.append (id)

    @property
    def id(self):
        return self._id
    

    @id.setter
    def id(self, id):
        self._id = id
    

    @property
    def date(self):
        return self._date
    

    @date.setter
    def date(self, date):
        self._date = date
    
    
    @property
    def transactions(self):
        return self._transactions
    

    @transactions.setter
    def transactions(self, transactions):
        self._transactions = transactions
  
    
    @property
    def seller_id(self):
        return self._seller_id
    
    @seller_id.setter
    def seller_id(self, seller_id):
        self._seller_id = int(seller_id)
    
    @property
    def marketplace_id(self):
        return self._marketplace_id
    
    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        self._marketplace_id = int(marketplace_id)  
