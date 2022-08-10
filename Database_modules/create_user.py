import re
from pymongo import MongoClient

 
class CreateUser:
    def __init__(self , firstName ,lastName,email  ,password ):
        
        
        self.firstName = firstName
        self.lastName =lastName
        self.email = email.lower()
        self.password = password
        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        self.response_pattern =  {
            "code": None,
            "name": "",
            "description": ""
        }
        self.__client = MongoClient("mongodb+srv://slooviTestdb:DZzJvtn6RzUuiOiI@sloovitest.dhkofzo.mongodb.net/?retryWrites=true&w=majority")

        self.__db = self.__client['SLOOVITEST']


   
    def runner(self):
       result = self.__email_valid()
       return  result
   
    def __email_valid(self):
        try:
 
            if(re.fullmatch(self.regex, self.email)):
                self.__checkUser_exist()
                
                
                return self.response_pattern , self.response_pattern['code']
        
            else:
                    
                self.response_pattern['code']=400
                self.response_pattern["name"]="bad request"
                self.response_pattern["description"]="invalid email address"

                return self.response_pattern ,self.response_pattern['code']
        except:
            
            self.response_pattern['code']=500
            self.response_pattern["name"]="internal server error"
            self.response_pattern["description"]="something went wrong on the server"
            print("errror ........................... the _validateemail  method failed")
            return self.response_pattern , self.response_pattern['code']
            
    # def __validate_email():
    def __checkUser_exist(self):
        try:
            list_of_items = self.__db.list_collection_names()
        
            if self.email in list_of_items:
                self.response_pattern['code']=400
                self.response_pattern["name"]="bad request"
                self.response_pattern["description"]="invalid email address, user already exist with email"
                return self.response_pattern ,self.response_pattern['code']
            else:
                response =  self.__createuser()
                return response
        except:
            self.response_pattern['code']=500
            self.response_pattern["name"]="internal server error"
            self.response_pattern["description"]="something went wrong on the server"
            print("errror ........................... the checkuser_exist method failed")
            return self.response_pattern , self.response_pattern['code']
                
                
    def __createuser(self):
        
        
        try:
            collection = self.__db[self.email]
                
            collection.insert_one(
            {"user_info":{
            "password":self.password,"first_name":self.firstName,"last_name":self.lastName,"Email":self.email,"Templates":{
                        }
            }
                
            }



            )
            
            self.response_pattern['code']=200
            self.response_pattern["name"]="Success"
            self.response_pattern["description"]="User Created "


            return self.response_pattern , self.response_pattern['code']
        except:
            
            self.response_pattern['code']=500
            self.response_pattern["name"]="internal server error"
            self.response_pattern["description"]="something went wrong on the server"
            print("errror ........................... the __create_user method failed")
            return self.response_pattern , self.response_pattern['code']
#print(CreateUser("firstName" ,"lastName","email@hhh.com"  ,"password").runner())