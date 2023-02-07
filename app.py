from flask import Flask, render_template,request
# from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb+srv://aniket:CollegPlace107@cluster0.8opd5.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient("mongodb+srv://aniket:CollegePlace107@cluster0.8opd5.mongodb.net/?retryWrites=true&w=majority")
# db = client.test

# mongo = PyMongo(app)
# db = mongo.db

db = client["users"]
collection = db["userdata"]
add_user_collection = db["new_users"]

food = client["food"]
food_data = db["food_data"]
@app.route("/")
def index():
    
    return render_template("home.html")

@app.route('/hotel',methods=['post'])
def hotel():
    msg = "Wrong email or password"
    if request.method == "POST":
        email = request.form['email']
        entered_password = request.form['password']
        
        item = add_user_collection.find({"email":email})
        for i in item:
            print(i)
            if i['password'] == entered_password:
                
                
                return render_template("hotel.html")
    return render_template("home.html",msg = msg)
            
@app.route('/register',methods=['post'])
def register():
    return render_template("register.html")

@app.route('/addUser',methods=['post'])
def addUser():
    
    # hotel name
    # phone
    # email
    # pass 
    # location
    
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        contact = request.form['contact']
        email = request.form['email']
        org = request.form['org']
        password = request.form['password']
        add = {"name":name, "address":address,"contact":contact,"email":email,"org":org, "password":password}
        
        add_user_collection.insert_one(add)
    
    
    return render_template("home.html")


if __name__ == '__main__':
   app.run(debug=True)


# from flask import Flask
# from flask_pymongo import PyMongo

# app = Flask(__name__)

# app.config['MONGO_URI'] = 'mongodb+srv://aniket:<password>@cluster0.8opd5.mongodb.net/?retryWrites=true&w=majority'

# mongo = PyMongo(app)

# @app.route('/')
# def index():
    # user_collection = mongo.db.users
    # users = user_collection.find({})
#     return str(users)

# if __name__ == '__main__':
#     app.run()
