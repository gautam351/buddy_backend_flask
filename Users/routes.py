from flask import Flask,request,Response,jsonify,make_response

from flask_restful import Resource
from .model import users as Users
from bson import json_util
from bcrypt import hashpw,checkpw,gensalt
from pymongo import *
from responseUtil.responseUtil import responseUtil
from helper.jwtHelper import createJwtToekn


class enteryFunction(Resource): 
    def get(self):
        return "Welcome to my first flask app"
    

# sign up function
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
        # if pic is also present
        if (pic is not None):user.pic=pic,
        user.save()
        

#    create jwt ,set cookies, and save the user 
        jsonify_user=user.to_json()
        token=createJwtToekn(jsonify_user.get("_id"))
       
    #    makign response object and setting cookies
        res=make_response(user.to_json())
       
        res.set_cookie("token",token)
        res.status_code=201
       
        
                
        return res
        
# sign up fucntion ended



class login(Resource):
    
    def post(self):
        data=request.get_json()
        email=data.get("email")
        password=data.get("password")
        # check if data is sufficient
        if(  (email is None ) or (password is None)):
            return responseUtil(False,"insufficient details",[]),200
        
        # check if user exists
        user:Users=Users.objects(email=email).first()
        
    
        if(user is None):return responseUtil(success=False,message="user Doesn't exists",data=[]),200
         
        # check if password matches 
        if(checkpw(password=password.encode("utf-8"),hashed_password=user.password.encode("utf-8"))==False):return responseUtil(success=False,message="invalid credentials",data=[]),200
        
        # create token 
        jsonify_user=user.to_json()
        token=createJwtToekn(jsonify_user.get("_id"))

        # create response
        res=make_response(jsonify_user)
        res.set_cookie("token",token)
        res.status_code=201
        return res   
        
    
# # logout route
# class logout(Resource):
#     def get(self):


def initializeRoutes(api):
    api.add_resource(enteryFunction, "/")
    api.add_resource(signup, "/signup")
    api.add_resource(login,"/login")

   
   
            
           
       
    





