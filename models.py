# -*- coding: utf-8 -*-
from mongoengine import *

from flask.ext.mongoengine.wtf import model_form
from datetime import datetime

#make a document for each roommate

class Roommate (Document):
	name = StringField(max_length=120, required=True, verbose_name="name", unique=True)	
	chorenumber = IntField (required=True, verbose_name="chorenumber")
	phonenumber = StringField(max_length=120, required=True, verbose_name= "phonenumber")
	chore = StringField(required=True)

