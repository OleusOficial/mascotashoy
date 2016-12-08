#!/usr/bin/env python
# -*- coding: utf-8 -*-
from productos_animales import ProductosAnimales
import web 
from db import DB
# Carga de informacion I
# DATABASE 
dba = DB() 
# CSV DATA
pa = ProductosAnimales() 
pa.load_data()  
#WEB 
urls = (
    '/','login',
    '/register','register',
    '/index/(.+)','index' ,
    '/alimentos/(.+)','alimentos',
    '/cuenta/(.+)','cuenta',
    '/eliminaCuenta/(.+)','eliminaCuenta' 
) 
render = web.template.render('templates', base='base')
app = web.application(urls, globals())
# Carga de Informacion F 

class login:
    login_form = web.form.Form(
        web.form.Textbox('Email',web.form.notnull),
        web.form.Password('Password',web.form.notnull)
    )

    def GET(self):
        form = self.login_form()
        return render.login(form)
    
    def POST(self):
        form = self.login_form() 
        if not form.validates(): 
            return render.login(form)
        else:  
            email = form.d.Email
            password = form.d.Password  
            if dba.validate_user(email, password):
                url = '/index/'+ str(dba.id_user)
                raise web.seeother(url) 
            else:
                 return render.login(form) 

class register:
    register_form = web.form.Form(
        web.form.Textbox('Nombre',web.form.notnull),
        web.form.Textbox('Email',web.form.notnull),
        web.form.Password('Password',web.form.notnull)
    )

    def GET(self): 
        form = self.register_form() 
        return render.register(form)        

    def POST(self):
        form = self.register_form() 
        if not form.validates(): 
            return render.register(form)
        else:  
            user_name = form.d.Nombre
            email = form.d.Email
            password = form.d.Password  
            dba.register_user(user_name, email, password) 
            raise web.seeother('/')      

class index:
    def GET(self, id_user): 
        user = dba.get_user_info(id_user)
        return render.index(user)

class alimentos:
    empresas = pa.get_bussiness_list() 
    search_form = web.form.Form(
        web.form.Dropdown('Empresa',empresas) 
    )  

    def GET(self, id_user):   
        form = self.search_form() 
        user = dba.get_user_info(id_user)
        return render.alimentos(form, user, None)
        
    def POST(self,id_user): 
        form = self.search_form()  
        user = dba.get_user_info(id_user)
        if not form.validates(): 
            return render.alimentos(form, user, None)
        else:  
            empresa = form.d.Empresa 
            products = pa.get_product_info_from(empresa)
            return render.alimentos(form, user, products)

class cuenta:
    def GET(self, id_user): 
        user = dba.get_user_info(id_user)
        return render.cuenta(user)

class eliminaCuenta:
    def GET(self, id_user): 
        dba.delete_user(id_user)
        raise web.seeother('/')        

if __name__=='__main__':
    app.run()