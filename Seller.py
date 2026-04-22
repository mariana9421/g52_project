# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:46:34 2026

@author: ritam
"""


from gclass import Gclass


class Seller(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    att = ['_id', '_name', '_address']
    
    header = 'Seller'
    
    des = ['Id', 'Name', 'Address']
    
    def __init__(self, id, name, address):
        super().__init__()
        
     
        id = Seller.get_id(id)
        self._id = id
        self._name = name
        self._address = address
       
        

        Seller.obj[id] = self
        
      
        Seller.lst.append(id)
    

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    

    @property
    def address(self):
        return self._address
    

    @address.setter
    def address(self, address):
        self._address = address
    
  
