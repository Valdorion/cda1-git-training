""" few functions to say stuff """

def say_something_to_someone(what, to_who):
	return what  + " " + to_who

def say_hello(to_who):
	return say_something_to_someone("Hello", to_who)

def say_hello_world():
	return say_hello("World")

def say_happy_birthday(to_who):
	return say_something_to_someone("Happy Birthday ", to_who)

def say_happy_new_year(to_who):
	return say_something_to_someone("Happy new year", to_who)
