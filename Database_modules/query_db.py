from pymongo import MongoClient

def connecT():
    try:
    
        client = MongoClient("mongodb+srv://slooviTestdb:DZzJvtn6RzUuiOiI@sloovitest.dhkofzo.mongodb.net/?retryWrites=true&w=majority")

        db = client['SLOOVITEST']
        return db
    except:
        return "Failled"

response_pattern =  {
        "code": 500,
        "name": "server error",
        "description": "there's an issue on the server"
    }
    
    

def query(email):
    db = connecT()
    
    email = email.lower()
    
    try:
    
    
    
        if db=="Failled":
            print("error......... failled to connect to database")
            db_fail =True
            return db_fail , response_pattern

        
        list_of_items = db.list_collection_names()
        db_fail = False
        
 

        if email in list_of_items:
            User_in_db =True
            
            return {"db_fail":db_fail , "user_in_db":User_in_db}
        else:
            
            User_in_db =False
            return {"db_fail":db_fail , "user_in_db":User_in_db}
    except:
        db_fail = True
        return {"db_fail":db_fail , "response":response_pattern}
    
    
    
        

    #print(db[email])#.find({""}) )

    
    