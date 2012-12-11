# -*- coding: utf-8 -*-
import os, datetime
import re
from unidecode import unidecode

from flask import Flask, request, render_template, redirect, abort, jsonify
import requests

# import all of mongoengine
from mongoengine import *
from flask.ext.mongoengine import mongoengine


# import data models
import models

# Twilio
from twilio.rest import TwilioRestClient

# create Flask app
app = Flask(__name__)   # create our flask app


# --------- Database Connection ---------
# MongoDB connection to MongoLab's database
mongoengine.connect('mydata', host=os.environ.get('MONGOLAB_URI'))
app.logger.debug("Connecting to MongoLabs")





choreList = ['Kitchen','Bathroom', 'Floors','Misc']


# --------- Routes ----------
#@app.route('/')
#def main():
#	return render_template('index.html')


## We just use this route to add the roomies into the database. 

@app.route('/setupdb')
def db():

	

	tmpRoomie = models.Roommate()
	tmpRoomie.name = "mimi"
	tmpRoomie.chorenumber = 0
	tmpRoomie.phonenumber = "12817340266"
	tmpRoomie.chore = choreList[tmpRoomie.chorenumber]
	tmpRoomie.save()

	tmpRoomie = models.Roommate()
	tmpRoomie.name = "roomietwo"
	tmpRoomie.chorenumber = 1
	tmpRoomie.phonenumber = "12345678900"
	tmpRoomie.chore = choreList[tmpRoomie.chorenumber]
	tmpRoomie.save()

	tmpRoomie = models.Roommate()
	tmpRoomie.name = "roomiethree"
	tmpRoomie.chorenumber = 2
	tmpRoomie.phonenumber = "23456789011"
	tmpRoomie.chore = choreList[tmpRoomie.chorenumber]
	tmpRoomie.save()

	tmpRoomie = models.Roommate()
	tmpRoomie.name = "roomiefour"
	tmpRoomie.chorenumber = 3
	tmpRoomie.phonenumber = "34567891234"
	tmpRoomie.chore = choreList[tmpRoomie.chorenumber]
	tmpRoomie.save()

	return "Roommates created in database."

@app.route('/updatechores')
def chores():

	# get all roomies
	roommates = models.Roommate.objects()

	# loop all roomies + increment chore number
	for r in roommates:		

		# get the new chore name
		if r.chorenumber == len(choreList)-1:
			r.chorenumber = 0   # choreList[0]  or  choreList[r.chorenumber] (write this!x)

		else:
			r.chorenumber += 1

		r.chore = choreList[r.chorenumber]

		# save r
		r.save()
	return redirect('/')

		# send sms (write the code for this)

	

@app.route('/', methods=['GET','POST'])
def twilio():

	roommates = models.Roommate.objects()

	templateData = {
			'chores' : choreList,
			'roommates' : roommates
		}

	if request.method == "GET":
		return render_template('twilio.html', **templateData)

	elif request.method == "POST":

		telephone = request.form.get('telephone')
		sms_text = request.form.get('sms_text')
		person = request.form.get ('person_text')

		# prepare telephone number. regex, only numbers
		##telephone_num = re.sub("\D", "", telephone)
		##if len(telephone_num) != 11:
		##	return "Your target phone number must be 11 digits. Try again."
		##else:
		to_number = "+" + str(12817340266) #US country only now

		
		# trim message to 120
		#if len(sms_text) > 120:
		#	sms_text = sms_text[0:119]

		account = os.environ.get('TWILIO_ACCOUNT_SID')
		token = os.environ.get('TWILIO_AUTH_TOKEN')

		client = TwilioRestClient(account, token)

		from_telephone = os.environ.get('TWILIO_PHONE_NUMBER') # format +19171234567

		message = client.sms.messages.create(to=to_number, from_=from_telephone,
	                                     body="Chore Reminder: ")


		#return "message '%s' sent" % sms_text 
		return render_template('twilio.html', **templateData)

@app.route('/text/<roommate>')
def text():

	


#@app.route('/choresheet')
#def choresheet_display():




@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



# --------- Server On ----------
# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	