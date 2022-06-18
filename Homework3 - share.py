# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:58:14 2022

@author: Carla Cristina Bailon Rosas
"""
##TASK 1 (Conditional flow)##

###Question 1###

"""
Create a program that tells you whether or not you need an umbrella when you 
leave the house.
The program should:
1. Ask you if it is raining using input().
2. If the input is 'y', it should output 'Take an umbrella'
3. If the input is 'n', it should output 'You don't need an umbrella'

"""
question=input('is it raining? answer with yes(y) or no (n): ')
if question=='y':
    print('Take an umbrella')
elif question=='n':
    print('You don\'t need an umbrella')
  

###Question 2###

"""
I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. 
I've written a program to check that I can afford the cost, but something doesn't 
seem right. Have a look at my program and work out what I've done wrong

my_money = input('How much money do you have? ')
boat cost = 20 + 5

if my_money < boat_cost:
	print('You can afford the boat hire')
else :
	print('You cannot afford the board hire'

"""
#In the code the data type of the input must be a float type,
#the variable boat_cost could be much understandable, and the last print 
#doesn’t have the final bracket. The code must look like the following code:

my_money = float(input('How much money do you have? '))
deposit=5
boat_cost = 20 + deposit

if my_money < boat_cost:
	print('You can afford the boat hire')
else :
	print('You cannot afford the board hire')
    

###Question 3###

"""
Your friend works for an antique book shop that sells books between 1800 and 1950 
and wants to quickly categorise books by the century and decade that they were written. 
Write a program that takes a year (e.g. 1872) and outputs the century and decade 
(e.g. "Eighteenth Century, Seventies")

"""


def category():
    year=int(input('Please insert the year of the book: '))
    decades=(year%100)//10
    options=['noughties','tens','twenties','thirties','forties','fifties','sixties','seventies','eighties','nineties']
    decade=[options[i] for i in range(0,10) if i==decades]
    if year>=1800 and year<1900:
      return 'Nineteenth Century, {}'.format(decade[0])
    elif year>=1900 and year<2000:
      return 'Twentieth Century, {}'.format(decade[0])
  
category()

##TASK 2 (Lists and Dictionaries)##
  
###Question 1###

"""
I have a list of things I need to buy from my supermarket of choice.

shopping_list = [
	"oranges",
	"cat food",
	"sponge cake",
	"long-grain rice",
	"cheese board",
]
print(shopping_list[1])
 
I want to know what the first thing I need to buy is. However, 
when I run the program it shows me a different answer to what I was expecting? 
What is the mistake? How do I fix it.

"""
#A python list start with index 0, so if I want the first item I have to print
#my list calling the index 0. The code will be:
    
shopping_list = [
	"oranges",
	"cat food",
	"sponge cake",
	"long-grain rice",
	"cheese board",
]
print(shopping_list[0])


###Question2###

"""
 I'm setting up my own market stall to sell chocolates. I need a basic till to
 check the prices of different chocolates that I sell. I've started the program
 and included the chocolates and their prices. Finish the program by asking 
 the user to input an item and then output its price.
 
"""


chocolates = {

	'white': 1.50,

	'milk': 1.20,

	'dark': 1.80,

	'vegan': 2.00,

}

chocolate=input("How much is _______ chocolate? ")
while True:
   if chocolate in chocolates:
       print(float(chocolates[chocolate]))
       question=input("Do you want to know another price? yes(y) or no(n) ")
       if question=='y':
          chocolate=input("How much is _______ chocolate? ")
       elif question=='n':
          break
   else: 
       print("\nInsert other type of chocolate")
       question=input("Do you want to know another price? yes(y) or no(n) ")
       if question=='y':
          chocolate=input("How much is _______ chocolate? ")
       elif question=='n':
          break
      
    
###Question 3###

"""
Write a program that simulates a lottery. The program should have a list of seven numbers that represent
a lottery ticket. It should then generate seven random numbers. After comparing the two sets of numbers, 
the program should output a prize based on the number of matches:
•         £20 for three matching numbers
•         £40 for four matching numbers
•         £100 for five matching numbers
•         £10000 for six matching numbers
•         £1000000 for seven matching numbers

"""

#for at least guest three numbers of lottery, the lottery numbers are going 
#to be in a range of 1 to 10.

import random

def lotery():
    ticket=[]
    count=0
    draw=[]
    n=1
    for i in range(0,7):
        number=int(input('write the number '+ str(n) + ' of your lotery ticket: '))
        ticket.append(number)
        draw_number=random.randrange(1,10)
        draw.append(draw_number)
        n+=1
    for i in range(0,7):
        if draw[i] in ticket:
            count+=1
            ticket.remove(draw[i])
    if count==3:
        prize='£20'
    elif count==4:
        prize='£40'
    elif count==5:
        prize='£100'
    elif count==6:
        prize='£10000'
    elif count==7:
        prize='£1000000'
    else:
        prize='£0'
    return 'Your prize is.....: {}'.format(prize)

lotery()

##TASK 3 (Read and Write files)##

###Question1###

"""
You're having coffee/tea/beverage of your choice with a friend that is learning
to program in Python. They're curious about why they would use pip. 
Explain what pip is and one benefit of using pip.

"""

#pip means Package Installer for Python and it is a manager of instalations of 
#libraries, The benefits of use pip are: easy to use,console use,
#command line use,install the latest version,it is possible to install some 
#libraries that are not standard in python, 


###Question2###

"""
This program should save my data to a file, but it doesn't work when I run it.
What is the problem and how do I fix it?

"""

poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file:
	poem_file.write(poem)
    
with open('poem.txt', 'r') as poem_file:
	poem=poem_file.read()
    
print(poem)

###Question3###

"""
Here is a snippet of Elton John’s song “I’m Still Standing”
 
You could never know what it's like
Your blood like winter freezes just like ice
And there's a cold lonely light that shines from you
You'll wind up like the wreck you hide behind that mask you use
 
And did you think this fool could never win?
Well look at me, I'm coming back again
I got a taste of love in a simple way
And if you need to know while I'm still standing, you just fade away
 
Don't you know I'm still standing better than I ever did
Looking like a true survivor, feeling like a little kid
I'm still standing after all this time
Picking up the pieces of my life without you on my mind
 
I'm still standing (Yeah, yeah, yeah)
I'm still standing (Yeah, yeah, yeah)

Tasks:
1.   	Write the lyrics to a new file called song.txt
2.   	Check that a file has been created successfully.
3.   	The read lines from this file and print out ONLY those lines 
that have a word ‘still’ in them. 

"""

elthon=["\nYou could never know what it's like",
        '\nYour blood like winter freezes just like ice', 
        "\nAnd there's a cold lonely light that shines from you",
        "\nYou'll wind up like the wreck you hide behind that mask you use",
        '\nAnd did you think this fool could never win?', 
        "\nWell look at me, I'm coming back again",
        '\nI got a taste of love in a simple way', 
        "\nAnd if you need to know while I'm still standing, you just fade away",
        "\nDon't you know I'm still standing better than I ever did", 
        '\nLooking like a true survivor, feeling like a little kid', 
        "\nI'm still standing after all this time", 
        '\nPicking up the pieces of my life without you on my mind', 
        "\nI'm still standing (Yeah, yeah, yeah)", 
        "\nI'm still standing (Yeah, yeah, yeah)"]


with open('song.txt', 'a') as song_file:
	song_file.writelines(elthon)

with open('song.txt', 'r') as song_file:
	song=song_file.read()
    

print(song)


with open('song.txt', 'r') as song_file:
    content=song_file.readlines()
    for line in content:
      if 'still' in line:
        print(line)
        



##TASK 4 (API)##


###Question1###

"""
In this session you used the Pokémon API to retrieve a single Pokémon.
I want a program that can retrieve multiple Pokémon and save their names and 
moves to a file. Use a list to store about 6 Pokémon IDs. Then in a for loop 
call the API to retrieve the data for each Pokémon. Save their names and moves 
into a file called 'pokemon.txt'


"""

import requests

#Without a function

pokemon_id=[]

for i in range(0,6):#creating pokemon_id list
    id = input("What is the Pokemon's ID? ")
    pokemon_id.append(id)

pokemons={}
for i in range(len(pokemon_id)):#create a dictionary to access better to data
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id[i])
    response = requests.get(url)
    pokemon = response.json()
    moves = pokemon['moves']
    moves=[move['move']['name'] for move in moves]
    pokemons[pokemon['name']]=moves[i:i+4],pokemon['height'],pokemon['weight']

    
    #writing pokemon.txt files:
with open('pokemon.txt', 'a') as pokemon_file:
          for k, v in pokemons.items():
              pokemon_file.write('Pokemon name: '+ str(k) + ' --> '+'Moves: '+ str(v[0]) + ','+'height: '+str(v[1])+','+'weight: '+str(v[2]) + '\n\n')
    #reading the file:
with open('pokemon.txt', 'r') as pokemon_file:
	pok=pokemon_file.read()
    
print(pok)


#with function

def pokemon_file():
    pokemon_id=[]

    for i in range(0,6):
        id = input("What is the Pokemon's ID? ")
        pokemon_id.append(id)
        pokemon_id
            
    def pokemon_desc(pokemon_id):
        pokemons={}
        for i in range(len(pokemon_id)):
            url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id[i])
            response = requests.get(url)
            pokemon = response.json()
            moves = pokemon['moves']
            moves=[move['move']['name'] for move in moves]
            pokemons[pokemon['name']]=(moves[i:i+4],pokemon['height'],pokemon['weight'])
        return pokemons
    
      
    def pokemon_read(pokemons):
        pokemons=pokemon_desc(pokemon_id)
        #writing pokemon.txt file
        with open('pokemon.txt', 'a') as pokemon_file:
          for k, v in pokemons.items():
              pokemon_file.write('Pokemon name: '+ str(k) + ' --> '+'Moves: '+ str(v[0]) + ','+'height: '+str(v[1])+','+'weight: '+str(v[2]) + '\n\n')
        #reading the file 
        with open('pokemon.txt', 'r') as pokemon_file:
            pok=pokemon_file.read()
        print(pok)
        
    return pokemon_read(pokemon_desc(pokemon_id))


pokemon_file()



###Question 2 (optional)###

"""
Here is a link to a really cool API: https://opentdb.com/
Answer the following questions:
"""

"""
1. What is the name of this API?

"""
   
#Open trivia database

"""
2. What does it do?
"""
#It is the access of a database of several questions and answers of different 
#topics, like computer science and cinema.

"""
3. Example URL to make a call to this API?
"""
#I am going to generate an API of easy cinema questions 
#I generated it on the website and I obtain the following link:
#https://opentdb.com/api.php?amount=20&category=11&difficulty=easy

"""
4. Example output?
"""

import requests
endpoint='https://opentdb.com/api.php?amount=20&category=11&difficulty=easy'
response = requests.get(endpoint)

data = response.json()

question={}
result=data['results']

for i in result:
    question[i['question']]=[i['category'],i['difficulty'], i['correct_answer']]

for k,v in question.items():
       print(('question: '+ k + ' --> '+'Category: '+ str(v[0]) + ','+'difficulty: '+str(v[1:-1])+','+'correct_answer: '+str(v[-1]) + '\n\n'))
    

    
