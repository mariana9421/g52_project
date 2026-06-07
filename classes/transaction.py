# -*- coding: utf-8 -*-
from classes.seller import Seller
from classes.marketplace import Marketplace

# Import the generic class
from classes.gclass import Gclass


class Transaction(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    # class attributes, identifier id, attribute must be the first on the list
    # _seller_id tem de estar em segundo lugar para funcionar no subform Seller_Transaction
    att = ['_id', '_marketplace_id', '_seller_id', '_date', '_transactions']

    # Class header title
    header = 'Transactions'

    # field description for use in, for example, input form
    des = ['Id', 'Marketplace_id','Seller_id', 'Date', 'Transactions']

    # Constructor: Called when an object is instantiated
    def __init__(self, id, marketplace_id, seller_id, date, transactions):
        super().__init__()

        # Check seller and marketplace referential integrity
        seller_id = int(seller_id)
        marketplace_id = int(marketplace_id)
        
        if marketplace_id in Marketplace.lst:
            if seller_id in Seller.lst:
            
                id = Transaction.get_id(id)

                self._id = id
                self._seller_id = seller_id
                self._marketplace_id = marketplace_id
                self._date = date
                self._transactions = float(transactions)
                

                # Add the new object to the Transaction list
                Transaction.obj[id] = self
                Transaction.lst.append(id)
            else:
                print('Marketplace ', marketplace_id, ' not found')
        else:
            print('Seller ', seller_id, ' not found')

    # Object properties

    @property
    def id(self):
        return self._id

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
        self._transactions = float(transactions)

