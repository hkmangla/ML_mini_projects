#!/usr/bin/python

import os
import pickle
import re
import sys
import pickle
sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

def email_text_data(data_dict):
	email_ids = []
	for i in data_dict:
		email_id = data_dict[i]['email_address']
		temp = []
		if email_id != 'NaN':
			temp.append(data_dict[i]['poi'])
			temp.append(email_id)
			email_ids.append(temp)
	from_email_ids = []
	for poi,email_id in email_ids:
		path = 'emails_by_address/from_' + email_id + '.txt'
		try:
			temp = []
			from_email_id = open(path, "r")
			temp.append(from_email_id)
			temp.append(poi)
			temp.append(email_id)
			from_email_ids.append(temp)
		except:
			pass
	word_data = []
	from_data = []
	email_id_data = []
	count = 0
	for from_person,poi,email_id in from_email_ids:
		temp_counter = 0
		full_email_text = ""
		for path in from_person:
			temp_counter += 1
			if temp_counter < 10:
				email = open(path[:-1],"r")
				email_text = parseOutText(email)
				replace_string = ['opportun','kenneth','adjust','lay','easi','entir','skill','contribut','invit']
				for word in replace_string:
					email_text = email_text.replace(word, "")
				full_email_text += email_text
			else:
				break
		word_data.append(full_email_text)
		from_data.append(poi)
		email_id_data.append(email_id)
	return word_data,from_data,email_id_data