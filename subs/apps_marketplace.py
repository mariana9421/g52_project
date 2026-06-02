from flask import Flask, render_template, request, session
from classes.marketplace import Marketplace

prev_option = ""

def apps_marketplace():
    global prev_option
    ulogin=session.get("user")
    
    if (ulogin != None):
        
        butshow = "enable"
        butedit = "disable"
        
        option = request.args.get("option")
        
        if option == "edit":
            butshow, butedit = "disable", "enable"
            
        elif option == "delete":
            obj = Marketplace.current()
            Marketplace.remove(obj.id)
            
            if not Marketplace.previous():
                Marketplace.first()
                
        elif option == "insert":
            butshow, butedit = "disable", "enable"
            
        elif option == 'cancel':
            pass
        
        elif prev_option == 'insert' and option == 'save':
            
            strobj = str(Marketplace.get_id(0))
            strobj = strobj + ';' + request.form["name"] + ';' + \
            request.form["created_date"] + ';' + request.form["category_id"]
            obj = Marketplace.from_string(strobj)
            
            Marketplace.insert(obj.id)
            Marketplace.last()
            
        elif prev_option == 'edit' and option == 'save':
            
            obj = Marketplace.current()
            
            obj.name = request.form["name"]
            obj.created_date = request.form["created_date"]
            obj.category_id = float(request.form["category_id"])
            
            Marketplace.update(obj.id)
            
        elif option == "first":
            Marketplace.first()
            
        elif option == "previous":
            Marketplace.previous()
            
        elif option == "next":
            Marketplace.nextrec()
            
        elif option == "last":
            Marketplace.last()
            
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        
        obj = Marketplace.current()
        
        if option == 'insert' or len(Marketplace.lst) == 0:
            id = 0
            id = Marketplace.get_id(id)
            name = ""
            created_date = ""
            category_id = ""
        else:
            id = obj.id
            name = obj.name
            created_date = obj.created_date
            category_id = obj.category_id
            
        return render_template("marketplace.html", butshow=butshow, butedit=butedit, 
                        id=id,name = name,created_date=created_date,category_id=category_id, 
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

