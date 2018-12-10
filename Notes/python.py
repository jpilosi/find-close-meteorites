Python

Python has dynamic typing

Checks:
	and, or, not

Types:
int, float, list, string, boolian, bytes, 

Conversions:
  list(), int(), float(), str()
  
  Lists:
	["x",x,x,x]
	
	
Int = 1
float = 2.0

can add lists: list1 + list2

Compairisons all true:
5 == 5
'a' == 'a'
'A' != 'a'
"apple" in "pineapple"     (substring check)
5 in [1,2,3,5,6]			*in is only for itterables (strings,list)


IF"s
----------------------------------------
if "key" in "monkey" : print("ook") 

if name <  "Robin":
	print ("ok")
elif name == "Robin":
	print ("Great name")
else:
	print("not")
	
name = ""   #empty variable is always false

if name and len(name) > 2:
	print("hello" + name)
else:
	print("enter name")
	
	
	
Exctracting:
	sentance = "The quick brown fox"
	sentance[0]  #this will return T
	sentance.find('qu') #would return 5
	"There are {0} items in your car.".format(5)
	
	sorted(abradadba) #will print in alphabetical order
	reversed
	list(reversed(sorted("abracabra"))) #reverses, sorts, and splits into a list 
	
	colors = ["blue", "red", "green", "yellow"]
	colors[1]   #this will return reduce
	colors[1:4] # returns 1-3
	colors[1:]   #returns after 1
	colors[1] = "black" #updates 1 to black
	
	a_list = 'This is a long string'.split("")
	sentance.split(' ') #split sentance into a list
	"-".join(colors)    #joins the list with - between words
	colors.pop()   #takes last value out of list 
	colors.append("valu") #add another thing to list 
	colors2 = colors.copy   #this will copy a list
	
	haystack = ["hey"] * 20		#loads 20 hey's 
	haystack[6] = "needle"		#changes 6th element
	
	sum([1,2,3])
	max([1,2,3])
	min([1,2,3])
	

loops
	for c in colors: 
		for m in modifiers:
			print(m + " " + c)
	
	while countdown >= 0:
		print(str(countdown))
		countdown -= 1

	
	break   #kills loop
	continue	#allows loop to skip and continue 

		

Functions:
	def product(numbers): 
		#print("hello, {0}".format(name))
		p = 1
		for n in numbers:
			p *= n
		return p
	

	
None:
	if my_data is None:
		print("not set")
		
		

		
Dictionaries:   #unordered aka hash table, key s are unique 
	cats = {}
	cats["Robin"] = 5
	cats["Bren"] = 2
	cats["tom"] = 10
	or
	{"Robin": 5, "bren": 3}
	
	cats["bren"]			#gets values
	cats.get("robin")		#gets values
	"Robin" in cats			#checks if Robin is in a dict
	
	for name in cats:
		print("{0} has {1} cats(s)".format(name, cats[name]))
		
	for name in cats.keys():			#gets keys 
	for num_cats in cats.values():		#gets values 
	
	for (person, num_cats) in cats.items():	#grabs key and value
	del cats["Robin"]	#removes robin
	cats.pop("Bilbo") #will return value and remove 
	
	examples:
		cond = "Cloudy"
		weather = {"Rainy": "rain.png", "Cloudy": "clouds.png"}
		thumbnail = weather.get(cond)
		
		users = {1: {"name": "joe", "email": "joe@example.com"}, 2: {"name": "liz", "email": "liz@example.com"}}    #Nested hashs
		
		
bytes:
	b = bytes()
	greeting = b"Hello, world!"   #set greeting to bytes and load it.
	for c in greeting: print(c)    #prints each byte 
	
	data = bytearray()		#operates like a list by byte array
	

tuple #is immutable, a list you can't modify

set #elements in a set are unique  

frozenset #a set you can't modify


pulling data:
	for i in ["a", "list", "of", "strings": print(i)	#loops through list created
	for (f,v) in zip(fruits, vegetables): print(f,v)	#loops through both lists, stops when 1 runs out
	
	


input:
	name = input()    #grabs user data
	name = input("Enter your name: ")	#prompt for input
	
	
try:											#try code
	inp = input("Enter a number: ")
	inp_int = int(inp)
	
except ValueError:								#catches a ValueError	
	inp_int = None
	print("That's not a number I know about!")
except NameError as e:							#e catches value of error
	print("Something went wrong with my code")
	print(e)									#print actual error
	raise e										#Raise error											
except:
	print("I have no idea what went wrong!")
else:											#will get executed if no errors
	print("No errors raised")					

finally:										#runs last if all code is done
	print("all done")
	
	
Files:
	with open("C:/recipe.txt") as input_file:						#read file
		for line in input_file
			line = line.strip()
			if len(line) < 4: continue
			if line[0] == "o" and line[3] == 'y' : print(line)
			
	
	with open('c:/writeme.txt", 'w') as output_file:			#write file 
		for word in wors:
			output_file.write(word _ "\n")
			
Moduels:
	import math			#imports whole module set 
	import random
	from random import shuffle #imports just shuffle function 
	import itertools
	import time
	import datetime
	import gzip
	import zipfile
	import csv
	import os
	import sys
	import re     #regular expressions 
	
	
https://pypi.org/

pip3 install requests    # install python 3 packages

Grabbing data from websites:
	4 scrapping the sight (grabbing the html response)
	3 jason/xml
	2 API
	1 library or service
	
type(meteor_data)    #shows type of data


for meteor in meteor_data:
    if not ('reclat' in meteor and 'reclong' in meteor): continue
	meteor['distance'] = calc_dist(float(meteor['reclat']), float(meteor['reclong']), my_loc[0], my_loc[1])
	
	



		
		
	
	
	



