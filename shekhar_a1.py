"""
Module for currency exchange
This module provides several string parsing functions to
implement a
simple currency exchange routine using an online currency
service.
The primary function in this module is exchange.
Author: shekhar shrivas
Date: 29-11-2022
"""


def before_space(s):
	"""Returns a copy of s up to, but not including, the first space


	#testing for string return before first white space
	>>> before_space('4 euros')
	'4'
	>>> before_space('4.502 usd')
	'4.502'
	>>> before_space('5.00   INR')
	'5.00'
	>>> before_space(' 5.00 INR')
	''

	Parameter s: the string to slice
	Precondition: s is a string with at least one space
	"""
	end_first=s.find(' ')
	first=s[:end_first]
	return first

# if __name__=='__main__':
# 	import doctest
# 	doctest.testmod()

def after_space(s):
	"""Returns a copy of s after the first space


	#testing for string return after first white space
	>>> after_space('4 euros')
	'euros'
	>>> after_space('4.502 usd')
	'usd'
	>>> after_space('5.00  INR')
	'INR'
	>>> after_space(' 5.00 INR')
	'5.00 INR'
	>>> after_space('5.00INR ')
	''

	Parameter s: the string to slice
	Precondition: s is a string with at least one space
	"""
	end_first=s.find(' ')
	last=s[end_first+1:].strip()
	return last

# if __name__=='__main__':
#  	import doctest
#  	doctest.testmod()

def first_inside_quotes(s):
	"""Returns the first substring of s between two (double) quotes

	A quote character is one that is inside a string, not one that
	delimits it. We typically use single quotes (') to delimit a
	string if we want to use a double quote character (") inside of
	it.
	Examples:
	first_inside_quotes('A "B C" D') returns 'B C'
	first_inside_quotes('A "B C" D "E F" G') returns 'B C',
	because it only picks the first such substring

	#testing for string return the string between two (double) quotes
	>>> first_inside_quotes('a "b" c')
	'b'
	>>> first_inside_quotes('a"b c"d')
	'b c'
	>>> first_inside_quotes('a"bc"d')
	'bc'
	>>> first_inside_quotes('a b "c d" e" f')
	'c d'
	>>> first_inside_quotes('A "B C" D "E F" G')
	'B C'

	Parameter s: a string to search
	Precondition: s is a string containing at least two double
	quotes
	"""
	first_quo=s.find('"')
	secound_quo=s.find('"',first_quo+1)
	str_in_quo=s[first_quo+1:secound_quo]
	return str_in_quo

# if __name__=='__main__':
#  	import doctest
#  	doctest.testmod()

def get_lhs(json):
	"""Returns the lhs value in the response to a currency query

	Given a JSON response to a currency query, this returns the
	string inside double quotes (") immediately following the
	keyword	
	"lhs". For example, if the JSON is
	'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '1 Bitcoin' (not '"1 Bitcoin"').
	This function returns the empty string if the JSON response
	contains an error message.

	#testing for string written in front of lhs
	>>> get_lhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
	'1 Bitcoin'
	>>> get_lhs('{ "lhs" : "2.5 Indian Rupees", "rhs" : "0.80682545635019 Cuban Pesos", "err" : "" }')
	'2.5 Indian Rupees'
	>>> get_lhs('{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }')
	'2.5 United States Dollars'
	>>> get_lhs('{ "lhs" : "", "rhs" : "", "err" : "Source currency code is invalid." }')
	''
	>>> get_lhs('{ "lhs" : "2.5 United States Dollars", "rhs" : "199.4700325 Indian Rupees", "err" : "" }')
	'2.5 United States Dollars'

	Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	"""
	coloun1=json.find(':')+3
	end_quo=json.find('"',coloun1)
	currency1=json[coloun1:end_quo]
	return currency1

# if __name__=='__main__':
#   	import doctest
#   	doctest.testmod()

def get_rhs(json):
	"""Returns the rhs value in the response to a currency query

	Given a JSON response to a currency query, this returns the
	string inside double quotes (") immediately following the
	keyword
	"rhs". For example, if the JSON is
	'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '19995.85429186 Euros' (not
	'"38781.518240835 Euros"').
	This function returns the empty string if the JSON response
	contains an error message.

	#testing for string written in front of rhs
	>>> get_rhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
	'19995.85429186 Euros'
	>>> get_rhs('{ "lhs" : "", "rhs" : "", "err" : "Source currency code is invalid." }')
	''

	Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	"""

	rhs=json.find('"rhs"')+5
	quo_start=json.find('"',rhs)+1
	quo_end=json.find('"',quo_start)
	currency2=json[quo_start:quo_end]
	return currency2

# if __name__=='__main__':
#    	import doctest
#    	doctest.testmod()

def has_error(json):
	"""Returns True if the query has an error; False otherwise.

	Given a JSON response to a currency query, this returns True if
	there
	is an error message. For example, if the JSON is
	'{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
	then the query is not valid, so this function returns True (It
	does NOT return the message 'Currency amount is invalid.').

	#testing for the function get_lhs(json) is geting the empty string or not
	>>> has_error('{ "lhs" : "", "rhs" : "", "err" : "Source currency code is invalid." }')
	True
	>>> has_error('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
	False

	Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	"""
	return get_lhs(json)==''

# if __name__=='__main__':
#     import doctest
#     doctest.testmod()

import requests
def query_website(old,new,amt):
	"""Returns a JSON string that is a response to a currency query.

	A currency query converts amt money in currency old to the
	currency new. The response should be a string of the form
	'{ "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'
	where the values old-amount and new-amount contain the value
	and name for the old and new currencies. If the query is
	invalid, both old-amount and new-amount will be empty, while
	"err" will have an error message.

	#testin for return the json string
	>>> query_website('USD','CUP',2.5)
	'{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }'
	>>> query_website('USD','INR',2.5)
	'{ "lhs" : "2.5 United States Dollars", "rhs" : "199.4700325 Indian Rupees", "err" : "" }'
	>>> query_website('USD','PSD',3.5)
	'{ "lhs" : "", "rhs" : "", "err" : "Exchange currency code is invalid." }'

	Parameter old: the currency on hand
	Precondition: old is a string with no spaces or non-letters
	Parameter new: the currency to convert to
	Precondition: new is a string with no spaces or non-letters
	Parameter amt: amount of currency to convert
	Precondition: amt is a float
	"""
	json = (requests.get('http://cs1110.cs.cornell.edu/2022fa/a1?old={0}&new={1}&amt={2}'.format(old,new,amt))).text
	return json

# if __name__=='__main__':
#     import doctest
#     doctest.testmod()

def is_currency(code):
	"""Returns: True if code is a valid (3 letter code for a) currency
	It returns False otherwise.

	#testing for the code is valid or not
	>>> is_currency('INR')
	True
	>>> is_currency('PSD')
	False

	Parameter code: the currency code to verify
	Precondition: code is a string with no spaces or non-letters.
	"""
	
	return has_error(query_website(code,'USD',2.5))==False

# if __name__=='__main__':
#     import doctest
#     doctest.testmod()

def exchange(old,new,amt):
	"""Returns the amount of currency received in the given exchange.

	In this exchange, the user is changing amt money in currency
	old to the currency new. The value returned represents the
	amount in currency new.

	The value returned has type float.
	
	#testing for the old currency convert into new currency
	>>> exchange('USD','CUP',2.5)
	'64.375'
	>>> exchange('USD','INR',2.5)
	'199.4700325'

	Parameter old: the currency on hand
	Precondition: old is a string for a valid currency code
	Parameter new: the currency to convert to
	Precondition: new is a string for a valid currency code
	Parameter amt: amount of currency to convert
	Precondition: amt is a float
	"""
	json=query_website(old,new,amt)
	exchange_amount=get_rhs(json)
	return before_space(exchange_amount)

# if __name__=='__main__':
#     import doctest
#     doctest.testmod()
