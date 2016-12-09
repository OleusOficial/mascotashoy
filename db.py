 
import web 

class DB:
    def __init__(self): 
        self.dba = web.database(dbn='postgres',host='ec2-54-235-72-121.compute-1.amazonaws.com',port=5432,db='d4qioabr5l1v89',user='ywqjeszicwqqrg',pw='lbbQ_-wVX-IJHHrnSEOXui1Waz')
        self.id_user = 0
        self.dba.li


    def validate_user(self, email, password):
        values = dict(e = email) 
        result = self.dba.select('users',values,where="email = $e") 
        for row in result:
            if row.password_p == password:
                self.id_user = row.id_user 
                return True
            else:
                return False 

    def register_user(self, name, email, password): 
        self.dba.insert('users', user_name = name, email = email, password_p = password)

    def delete_user(self,id):  
        self.dba.delete('users',where="id_user=$id",vars = dict(id= id))                    
 
    def get_user_info(self, id_user):
        user = []
        values = dict(id = id_user) 
        result = self.dba.select('users',values, where="id_user=$id") 
        for row in result:
            user.append(dict(row))
        return user