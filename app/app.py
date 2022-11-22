import os
from flask import Flask
from flask_pymongo import PyMongo
from flask import request,Flask,render_template,redirect,jsonify, request, make_response, url_for
from bson.objectid import ObjectId
import datetime
from prometheus_flask_exporter import PrometheusMetrics
import status

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://username:password@host:port/db_name?authSource=admin"

app.config["MONGO_URI"] = "mongodb://root:pass@mongodb:27017/Users?authSource=admin"

# app.config["MONGO_URI"] = "mongodb://mongodb:27017/Users"

mongodb_client = PyMongo(app)
db = mongodb_client.db
metrics = PrometheusMetrics(app)


metrics.info("app_info", "App Info, app Healthy", version="1.0.0")

@app.route("/health")
def health():
    """Health Status"""
    return jsonify(dict(status="OK")), 200

@app.route("/" ,methods=['GET','POST'])
def home():
    # get the Users from the database
    users = list(db.users.find({}).sort("createdAt",-1));
    nbr_users = len(users)
    # render a view
    if(request.method == "POST"):
        return jsonify(dict(nbr_users=nbr_users))

    return render_template("/pages/User_grid.html",users=users,status_code = 200)


@app.route("/add-user", methods=['GET','POST'])
def addNote():
    if(request.method == "GET"):
        return render_template("pages/add-user.html")
    elif (request.method == "POST"):
        # get the fields data
        title = request.form['name']
        role = request.form['role']
        createdAt = datetime.datetime.now()
        # save the record to the database
        db.users.insert_one({"name":title,"role":role,"createdAt":createdAt})
        # redirect to home page
    return redirect('/')

@app.route('/edit-user', methods = ['GET','POST'])
def editNote():

    if request.method == "GET":

        # get the id of the note to edit
        userId = request.args.get('form')
        # get the note details from the db
        user = dict(db.users.find_one({'_id': ObjectId(userId)}))
        # direct to edit note page
        return render_template('pages/edit-user.html',user=user)

    elif request.method == "POST":

        #get the data of the note
        userId = request.form['_id']
        title = request.form['name']
        role = request.form['role']

        # update the data in the db
        db.users.update_one({"_id":ObjectId(userId)},{"$set":{"name":title,"role":role}})

        # redirect to home page
        return redirect("/")


@app.route('/delete-user', methods=['POST','DELETE'])
def deleteNote():
    userId = request.form.get('_id')
    # delete from the database
    db.users.delete_one({ "_id": ObjectId(userId)})
    return redirect("/")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)