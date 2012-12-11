## ITP DWD - Using Remote APIs and Making Sure Your House is Always Clean

Download code. Open code directory in Terminal.

#### #1 Create virtualenv

	virtualenv venv


#### #2 Install requirements

In your code directory run the command below to install new requirements.

	. runpip

or

	. venv/bin/activate
	pip install -r requirements.txt


2 new libraries we're using in this example, Twilio and Requests


#### #3 Start server

Start server

	. start

or 

	. venv/bin/activate
	foreman start

-----------


## Getting Started with Remote APIs


## Twilio demo

demo /twilio

### Getting Twilio Account

* Register [https://www.twilio.com/try-twilio](https://www.twilio.com/try-twilio).
* Verify phone number with access code.
* Pick a phone number.
* Poke around all their API endpoints, make and receive calls, make and receive SMS.

When you are registered locate your your Account SID and Auth Token here,[https://www.twilio.com/user/account](https://www.twilio.com/user/account) and add them to your .env file

**.env**	

	TWILIO_ACCOUNT_SID=xxxxxxxxxxxxxx
	TWILIO_AUTH_TOKEN=xxxxxxxxx
	TWILIO_PHONE_NUMBER=+XXXXXXXXX

Now let's add the Twilio account variables to Heroku.

**In your code directory in Terminal run,**

	heroku config:add TWILIO_ACCOUNT_SID=xxxxxxxxxxxxxx
	heroku config:add TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxx
	heroku config:add TWILIO_PHONE_NUMBER=+XXXXXXXXX


##Setting Up A Roommate Reminder System 

In models.py, create a Roomate Class. We will use this to assign in an initial chore and chore number to 
each roommate, and to also provide each roommate's name and phone number. 

**In models.py**

		name = StringField(required=True, verbose_name="name", unique=True)	
		chorenumber = IntField (required=True, verbose_name="chorenumber")
		phonenumber = StringField(max_length=120, required=True, verbose_name= "phonenumber")
		chore = StringField(required=True)

-----------------

We will use this information in the /setupdb route, which will only be run once in order to
hard code the roommates into the database. 

**In app.py**

		@app.route('/setupdb')
		def db():

	

	tmpRoomie = models.Roommate()
	tmpRoomie.name = "Mimi"
	tmpRoomie.chorenumber = 0
	tmpRoomie.phonenumber = "12345678900"
	tmpRoomie.chore = choreList[tmpRoomie.chorenumber]
	tmpRoomie.save()

	tmpRoomie = models.Roommate()
	tmpRoomie.name = "Dani"
	tmpRoomie.chorenumber = 1
	tmpRoomie.phonenumber = "12345678900"
	tmpRoomie.chore = choreList[tmpRoomie.chorenumber]
	tmpRoomie.save()

	tmpRoomie = models.Roommate()
	tmpRoomie.name = "Schuyler"
	tmpRoomie.chorenumber = 2
	tmpRoomie.phonenumber = "12345678900"
	tmpRoomie.chore = choreList[tmpRoomie.chorenumber]
	tmpRoomie.save()

	tmpRoomie = models.Roommate()
	tmpRoomie.name = "Sara"
	tmpRoomie.chorenumber = 3
	tmpRoomie.phonenumber = "12345678900"
	tmpRoomie.chore = choreList[tmpRoomie.chorenumber]
	tmpRoomie.save()

	return "Roommates created in database."
	
	


