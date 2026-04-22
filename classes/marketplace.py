# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:21:10 2026

@author: ritam
"""



from gclass import Gclass
import datetime

class Marketplace(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    att = ['_id', '_name', '_created_date', '_category_id']
    
    header = 'Marketplace'
    
    des = ['Id', 'Name', 'Created Date', 'Category Id']
    
    def __init__(self, id, name, created_date, category_id):
        super().__init__()
        
     
        id = Marketplace.get_id(id)
        self._id = id
        self._name = name
        self._created_date = datetime.date.fromisoformat(created_date)
        self._category_id = category_id
        

        Marketplace.obj[id] = self
        
      
        Marketplace.lst.append(id)
    

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
    def created_date(self):
        return self._created_date
    

    @created_date.setter
    def created_date(self, created_date):
        self._created_date = created_date
    
  
    @property
    def category_id(self):
        return self._category_id
    
    @category_id.setter
    def category_id(self, category_id):
        self._category_id = int(category_id)
