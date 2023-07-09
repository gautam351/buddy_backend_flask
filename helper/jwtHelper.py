import jwt
from config import SECRET_KEY


def createJwtToekn(id:str)->str:
    return jwt.encode({"user_id":id},SECRET_KEY,algorithm="HS256")

def decodeJwtToken(token:str)->str:
    return jwt.decode(token,SECRET_KEY,algorithms="HS256")