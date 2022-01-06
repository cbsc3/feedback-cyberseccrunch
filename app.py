from pymongo import MongoClient
from flask import Flask, render_template, session, url_for, redirect, request
import datetime
import os
app = Flask(__name__)

cluster = MongoClient('mongodb+srv://admin:password12345@cluster0.gsfkl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['submissions']
collections = db['submissions']

@app.route('/', methods=['POST', 'GET'])
def home():
  if request.method == "POST":
	  username = request.form.get('username')
	  question = request.form.get('q')
	  time = datetime.datetime.now()

	  if question == "":
		  return render_template("spam.html")
	  if username == "":
		   return render_template("spam.html")
	 



	  post = {"Username":username, "Question":question, "Time Submitted":time}
	  collections.insert_one(post)
	  return render_template('thank.html')


  return render_template('index.html')


if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))
   app.run(debug=True, port=port)