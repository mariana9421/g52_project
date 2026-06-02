# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:13:57 2026

@author: ritam
"""



import sqlite3
import datetime


class Gclass:
    dbfile = "data/Marketplace.db"

    def __init__(self):
        pass

    @classmethod
    def get_id(cls, id):
        if id == 0 or id == "0" or id == "" or id is None:
            if len(cls.lst) == 0:
                id = 1
            else:
                id = max(cls.lst) + 1
        else:
            id = int(id)
        return id

    @classmethod
    def from_string(cls, str_data):
        str_list = str_data.split(";")
        strarg = "cls(str_list[0]"
        for i in range(1, len(str_list)):
            strarg += ", str_list[" + str(i) + "]"
        strarg += ")"
        return eval(strarg)

    @classmethod
    def reset(cls):
        cls.obj = dict()
        cls.lst = list()
        cls.pos = 0

    @classmethod
    def nextrec(cls):
        cls.pos += 1
        return cls.current()

    @classmethod
    def previous(cls):
        cls.pos -= 1
        return cls.current()

    @classmethod
    def current(cls, code=None):
        if code in cls.lst:
            cls.pos = cls.lst.index(code)

        if cls.pos < 0:
            cls.pos = 0
            return None

        elif cls.pos >= len(cls.lst):
            cls.pos = len(cls.lst) - 1
            return None

        else:
            code = cls.lst[cls.pos]
            return cls.obj[code]

    @classmethod
    def first(cls):
        cls.pos = 0
        return cls.current()

    @classmethod
    def last(cls):
        cls.pos = len(cls.lst) - 1
        return cls.current()

    @classmethod
    def orderfunc(cls, e):
        return getattr(cls.obj[e], cls.sortkey)

    @classmethod
    def sort(cls, att, reverse=False):
        cls.sortkey = att
        cls.lst.sort(key=cls.orderfunc, reverse=reverse)
        
        
    @classmethod
    def getlines(cls, att, value):
        lines = []
    
        for obj_id in cls.lst:
            obj = cls.obj[obj_id]
    
            if getattr(obj, att) == value:
                lines.append(obj_id)
    
        return lines

    @classmethod
    def find(cls, value, att):
        lobj = cls.obj.values()
        return [obj for obj in lobj if getattr(obj, att) == value]

    @classmethod
    def set_filter(cls, f_dic={}):
        if f_dic:
            code = cls.att[0]
            lobj = cls.obj.values()
            s = set()

            for att, listf in f_dic.items():
                s1 = set(
                    [getattr(obj, code) for obj in lobj if getattr(obj, att) in listf]
                )
                s = s.union(s1)

            if len(s) > 0:
                cls.lst = list(s)
                cls.pos = 0

        else:
            obj = cls.current()
            cls.lst = list(cls.obj.keys())
            code = cls.att[0]

            if obj is not None:
                cls.current(getattr(obj, code))

    @classmethod
    def getatlist(cls, att):
        return [getattr(obj, att) for obj in list(cls.obj.values())]

    # --------------------------------------------------
    # Funções auxiliares para SQLite
    # --------------------------------------------------

    @classmethod
    def column_names(cls):
        """
        Converte:
            ['_id', '_name', '_comments']
        em:
            ['id', 'name', 'comments']
        """
        return [
            att[1:] if att.startswith("_") else att
            for att in cls.att
        ]

    @classmethod
    def object_values(cls, obj):
        """
        Obtém os valores do objeto numa forma que o SQLite consiga guardar.
        As datas são guardadas como texto no formato YYYY-MM-DD.
        """
        values = []

        for att in cls.att:
            value = getattr(obj, att)

            if isinstance(value, datetime.date):
                value = value.isoformat()

            values.append(value)

        return values

    # --------------------------------------------------
    # Ler dados da base de dados SQLite
    # --------------------------------------------------

    @classmethod
    def read(cls, dbfile="data/Marketplace.db"):
        cls.reset()
        cls.dbfile = dbfile

        try:
            connection = sqlite3.connect(dbfile)
            cursor = connection.cursor()

            table = cls.__name__

            cursor.execute(f'SELECT * FROM "{table}"')
            rows = cursor.fetchall()

            connection.close()

            for row in rows:
                values = [
                    "" if value is None else str(value)
                    for value in row
                ]

                cls(*values)

        except sqlite3.Error as err:
            print(f"Erro ao ler a tabela {cls.__name__}: {err}")

    # --------------------------------------------------
    # Inserir um novo registo na base de dados
    # --------------------------------------------------

    @classmethod
    def insert(cls, code):
        try:
            obj = cls.obj[code]

            columns = cls.column_names()
            values = cls.object_values(obj)

            table = cls.__name__

            columns_sql = ", ".join([f'"{column}"' for column in columns])
            questions = ", ".join(["?"] * len(columns))

            sql = f'INSERT INTO "{table}" ({columns_sql}) VALUES ({questions})'

            connection = sqlite3.connect(cls.dbfile)
            cursor = connection.cursor()

            cursor.execute(sql, values)

            connection.commit()
            connection.close()

        except sqlite3.Error as err:
            print(f"Erro ao inserir na tabela {cls.__name__}: {err}")

    # --------------------------------------------------
    # Atualizar um registo já existente
    # --------------------------------------------------

    @classmethod
    def update(cls, code):
        try:
            obj = cls.obj[code]

            columns = cls.column_names()
            values = cls.object_values(obj)

            table = cls.__name__

            updates = ", ".join(
                [f'"{column}" = ?' for column in columns[1:]]
            )

            sql = (
                f'UPDATE "{table}" '
                f'SET {updates} '
                f'WHERE "{columns[0]}" = ?'
            )

            parameters = values[1:] + [values[0]]

            connection = sqlite3.connect(cls.dbfile)
            cursor = connection.cursor()

            cursor.execute(sql, parameters)

            connection.commit()
            connection.close()

        except sqlite3.Error as err:
            print(f"Erro ao atualizar a tabela {cls.__name__}: {err}")

    # --------------------------------------------------
    # Apagar um registo da base de dados
    # --------------------------------------------------

    @classmethod
    def remove(cls, code):
        try:
            table = cls.__name__
            id_column = cls.column_names()[0]

            sql = f'DELETE FROM "{table}" WHERE "{id_column}" = ?'

            connection = sqlite3.connect(cls.dbfile)
            cursor = connection.cursor()

            cursor.execute(sql, (code,))

            connection.commit()
            connection.close()

            cls.lst.remove(code)
            del cls.obj[code]

        except sqlite3.Error as err:
            print(f"Erro ao apagar da tabela {cls.__name__}: {err}")

    def __str__(self):
        strprint = "f'"

        for att in type(self).att:
            strprint += "{self." + att + "};"

        strprint = strprint[:-1] + "'"

        return eval(strprint)