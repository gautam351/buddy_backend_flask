
from mongoengine import *
from datetime import datetime
from werkzeug.security import generate_password_hash



# creating the user schema
class users(Document):
    name=StringField(required=True,unique=False,max_length=99)
    email=EmailField(required=True,unique=True,sparse=True)
    password=StringField(required=True)
    role=StringField(required=True)
    created_on=DateTimeField(default=datetime.utcnow())
    isEmailVerfied=BooleanField(default=False)
    pic=StringField(default= "https://icon-library.com/images/anonymous-avatar-icon/anonymous-avatar-icon-25.jpg")
    reset_password_token= StringField(default="")
    # reset_password_expire= DateTimeField(default=datetime.utcnow())




# convert to json
    def to_json(self):
        
        return dict({
            "name":self.name,
            "email":self.email,
            "created_on":self.created_on.strftime("%d-%m-%Y"),
            "is_email_verified":self.isEmailVerfied,
            "pic":self.pic,
            
        })
    


