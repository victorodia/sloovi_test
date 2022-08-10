from flask import Flask, request, jsonify, make_response
from grpc import StatusCode
from werkzeug.exceptions import HTTPException
from  werkzeug.security import generate_password_hash, check_password_hash
import json
import logging
import datetime
from Database_modules import  query_db 

from Database_modules import create_user 

app = Flask(__name__)
salt ="a.,s.,"



response_pattern =  {
    "code": None,
    "name": "",
    "description": ""
}





@app.errorhandler(Exception)
def handle_exception(e):
 
 
 
    # pass through HTTP errors as json
 
 
 
    if isinstance(e, HTTPException):
        response = e.get_response()
        payload = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.data = f"{payload}\n"
        response.content_type = "application/json"
        return make_response(response, e.code)





@app.route('/register', methods =['POST'])
def signup():
    '''patterns
    first_name : 'lead_test@subi.com',
                last_name : '123456'
                email : 'lead_test@subi.com',
                password : '123456'
              }
    
    
    
    params =  ['first_name' , 'last_name' , 'email' , 'password']'''
    
    
    
    
    global response_pattern
    body = request.json
    
 
 
    try:
        
    
        body = {keY.lower():value for (keY , value) in body.items()  }
    
    except Exception as Argument:
        
        response_pattern['code']=400
        response_pattern["name"]="bad request"
        response_pattern["description"]="Key[s] are of invalid format"
        

        
        return make_response(response_pattern, response_pattern['code'])
 
               
    try:
        
 
        user_instance = create_user.CreateUser(
            body['first_name'],
        body['last_name'],
        body['email'],
        generate_password_hash(salt+body['password'])
      )
        
        response , status_code =user_instance.runner()
        
        
        
        return make_response(response , status_code)
    
    except KeyError:
        

        response_pattern['code']=400
        response_pattern["name"]="bad request"
        response_pattern["description"]="Key[s] are missing or haven't been spelt  correctly"


        return make_response(response_pattern, response_pattern['code'])

@app.route('/login', methods =['POST'])
def login():
    
    try:
        body = request.json
        
        body = {keY.lower():value for (keY , value) in body.items()  }
        email = body['email']
        password =salt+ body['password']
        
        
        
        if email:
            user_result = query_db.query(email )
            
            if user_result["db_fail"]:
                return make_response(user_result["response"])
            else:
                if user_result["user_in_db"]:
                    return "{}".format(check_password_hash("pbkdf2:sha256:260000$TSvT1eMDEekgO4l4$8c0676ee0cbf5456e4af50f06de0a7a35c6d598f36657ece328573b04b035a9ba",password))
                else:
                    response_pattern['code']=400
                    response_pattern["name"]="bad request"
                    response_pattern["description"]="user does not exist"
                    return make_response(response_pattern,response_pattern['code'])

                    
                
            
        else:
            response_pattern['code']=400
            response_pattern["name"]="bad request"
            response_pattern["description"]="Key[s] are missing , check email provided"


            return make_response(response_pattern, response_pattern['code'])

        
        
        
        
        
    
    except KeyError:
        
        

        response_pattern['code']=400
        response_pattern["name"]="bad request"
        response_pattern["description"]="Key[s] are missing or haven't been spelt  correctly"


        return make_response(response_pattern, response_pattern['code'])


if __name__ == "__main__":
    # setting debug to True enables hot reload
    # and also provides a debugger shell
    # if you hit an error while running the server
    app.run(debug = True, port=5000)