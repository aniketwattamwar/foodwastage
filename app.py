from flask import Flask, render_template
# from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("home.html")

@app.route('/hotel',methods=['post'])
def hotel():
    return render_template("hotel.html")

@app.route('/register',methods=['post'])
def register():
    return render_template("register.html")

if __name__ == '__main__':
   app.run(debug=True)


# from flask import Flask
# from flask_pymongo import PyMongo

# app = Flask(__name__)

# app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydb'

# mongo = PyMongo(app)

# @app.route('/')
# def index():
#     user_collection = mongo.db.users
#     users = user_collection.find({})
#     return str(users)

# if __name__ == '__main__':
#     app.run()
