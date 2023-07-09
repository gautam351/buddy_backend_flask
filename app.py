
from flask import Flask,Blueprint
from flask_mongoengine import MongoEngine
from flask_restful import Api



# initializing app
app=Flask(__name__)


#setting blueprint

api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1/")
api = Api(api_v1_bp)
app.register_blueprint(api_v1_bp)

from Users.routes import initializeRoutes
initializeRoutes(api)





# setting up the database
try:
    app.config['MONGODB_SETTINGS'] = {
    "db": "myapp",
    
    }
    db = MongoEngine(app)
    print("mongodb connected successfully")

except Exception as e:
    print("error in connection",end=" ")
    print(e)








if __name__=="__main__":
    # print(db)
    app.run(debug=True)