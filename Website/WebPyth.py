from flask import Flask
from flask import Flask, Blueprint, flash, redirect, render_template, request, session, abort, url_for
import os
from sqlalchemy.orm import sessionmaker, load_only
from tabledef import *
from random import choice
import string
import validators
import requests
import json
from wtforms import Form, BooleanField, StringField, PasswordField, validators


engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False}, echo=True)

app = Flask(__name__)
app.secret_key = "secret key"

Session = sessionmaker(bind=engine)
dbsession = Session()

# piece1 = Clothing("Funky Candles 4 Pack", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum", "12", "/static/t1.jpg", "/static/t2.jpg", "/static/t3.jpg", "2", "4", "3", "clothing/1")
# dbsession.add(piece1)

# piece2 = Clothing("Baby Yoda/Grogu Rug", "Description of Item Two", "40", "/static/t3.jpg", "/static/t4.jpg", "/static/t6.jpg", "1", "4", "2", "clothing/2")
# dbsession.add(piece2)

# piece3 = Clothing("Troll Spoon", "Description of Item Three", "10", "/static/t5.jpg", "/static/t6.jpg", "/static/t9.jpg", "2", "6", "3", "clothing/3")
# dbsession.add(piece3)

# piece4 = Clothing("Item4", "Description of Item Four", "26", "/static/t7.jpg", "/static/t8.jpg", "/static/t12.jpg", "6", "3", "8", "clothing/4")
# dbsession.add(piece4)

# piece5 = Clothing("Item5", "Description of Item Five", "26", "/static/t9.jpg", "/static/t10.jpg", "/static/t12.jpg", "6", "3", "8", "clothing/5")
# dbsession.add(piece5)

# piece6 = Clothing("Item6", "Description of Item Six", "26", "/static/t11.jpg", "/static/t12.jpg", "/static/t12.jpg", "6", "3", "8", "clothing/6")
# dbsession.add(piece6)

# piece7 = Clothing("Item7", "Description of Item Seven", "26", "/static/t13.jpg", "/static/t14.jpg", "/static/t12.jpg", "6", "3", "8", "clothing/7")
# dbsession.add(piece7)

# piece8 = Clothing("Item8", "Description of Item Eight", "26", "/static/t15.jpg", "/static/t16.jpg", "/static/t12.jpg", "6", "3", "8", "clothing/8")
# dbsession.add(piece8)

# piece9 = Clothing("Item9", "Description of Item Nine", "26", "/static/t17.jpg", "/static/t18.jpg", "/static/t12.jpg", "6", "3", "8", "clothing/9")
# dbsession.add(piece9)

# dbsession.commit()





@app.route('/home', methods=["GET", "POST"])
def home():
	pieces = dbsession.query(Clothing)
	return render_template('homepage.html', pieces=pieces)



@app.route('/clothing/<int:id>', methods=["GET", "POST"])
def clothing(id):
	pieces = dbsession.query(Clothing)
	return render_template('clothes.html', idVar=dbsession.query(Clothing).get(id).id, nameVar=dbsession.query(Clothing).get(id).name, priceVar=dbsession.query(Clothing).get(id).price, descVar=dbsession.query(Clothing).get(id).description, img1Var=dbsession.query(Clothing).get(id).image, img2Var=dbsession.query(Clothing).get(id).image2, img3Var=dbsession.query(Clothing).get(id).image3, ext=dbsession.query(Clothing).get(id).ext)


@app.route('/cart')
def cart():

	if 'theOrder' not in session:
		session['theOrder'] = []

	the_order = session['theOrder']

	session['theOrder'] = the_order


	return render_template('cart.html', items=session['theOrder'])



@app.route('/addtocart/<int:id>/<string:size>/<int:quantity>', methods=['GET', 'POST'])
def addtocart(id, size, quantity):


	# session.clear()


	if 'theOrder' not in session:
		session['theOrder'] = []

	the_order = session['theOrder']

	nameV = dbsession.query(Clothing).get(id).name
	imageV = dbsession.query(Clothing).get(id).image
	priceV = dbsession.query(Clothing).get(id).price


	boo = 0

	# for i = 0, enumerate the first dimension
	for i, order in enumerate(the_order):
		# for j = 0, enumerate the second dimension
		for j, oD in enumerate(order):
			# if "id01" in the dimension
			if str(nameV) in oD:
				# set P to the value of the quantity
				if str(size) == the_order[i][2]:
					p = the_order[i][3];
					the_order[i][3] = str(int(p)+1);
					session['theOrder'] = the_order
					boo = 1;
					#peu = the_order[i][2];


	if boo == 0:
		new_list = [str(id), str(nameV), str(size), str(quantity), str(imageV), str(priceV)]
		# the_order.append(str(id) + "," dbsession.query(Clothing).get(id).name + "," + str(size) + "," + str(quantity) + "," + dbsession.query(Clothing).get(id).image + "," dbsession.query(Clothing).get(id).price)
		the_order.append(new_list)

		session['theOrder'] = the_order


	flash("Added To Cart")

	return redirect(url_for('clothing', id=id))



@app.route('/removefromcart/<int:id>', methods=['GET', 'POST'])
def removefromcart(id):

	the_order = session['theOrder']

	del the_order[id];

	session['theOrder'] = the_order

	return redirect(url_for('cart'))





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
