from flask import Flask,request,Response,jsonify

from flask_restful import Resource
from .model import users as Users
from bson import json_util
from bcrypt import hashpw,checkpw,gensalt
from pymongo import *
from responseUtil.responseUtil import responseUtil



class enteryFunction(Resource): 
    def get(self):
        return "Welcome to my first flask app"
    

class signup(Resource):
    
    def post(self):
        
# check if data is missing 
        data=request.get_json()

        username=data.get("username")
        email=data.get("email")
        password=data.get("password")
        role=data.get("role")
        pic=data.get("pic")
        if((username is None) or (email is None) or (password is None) or (role is None) ):
           
            return responseUtil(success=False,message="insufficient details",data=[]),200
#    check if the user already exists or not 
        check_user=Users.objects(email=email)
        if(len(check_user)>0):return responseUtil(success=False,message="user already exists",data=[]),200
        
      
        user=Users(
            name=username,
            email=email,
            role=role,
            password=hashpw(data["password"].encode("utf-8"), gensalt()),
            
        )
        if (pic is not None):user.pic=pic,
        user.save()
        data=[]
        data.append(user.to_json())
#  create jwt ,set cookies, and save the user 
        
        # return response,200
        

         
        
    


def initializeRoutes(api):
    api.add_resource(enteryFunction, "/")
    api.add_resource(signup, "/signup")

   
   
            
           
       
    





