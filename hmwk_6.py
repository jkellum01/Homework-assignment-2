'''6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.'''
friend_1 = {'first_name': 'Josh', 'last_name': 'Kellum', 'age': 18, 'city': 'Sugar Grove'}
print(friend_1['first_name'])
print(friend_1['last_name'])
print(friend_1['age'])
print(friend_1['city'])

'''6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.'''
fav_num = {'josh': 176, 'riki': 3, 'sarah': 7, 'ian': 117, 'chad': 69}
print("Josh's favorite number is " + str(fav_num['josh']) + ".")
print("Riki's favorite number is " + str(fav_num['riki']) + ".")
print("Sarah's favorite number is " + str(fav_num['sarah']) + ".")
print("Ian's favorite number is " + str(fav_num['ian']) + ".")
print("Chad's favorite number is " + str(fav_num['chad']) + ".")

'''6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	 Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.'''

words_0 = {'print': 'Prints a statement',
           'For_loop': 'loops through a program',
           'if_statement': 'conditional program',
           'list': 'list of words or values',
           'tuple': 'a more secure list'}
print('Print: ' + str(words_0['print']))
print('For loop: ' + str(words_0['For_loop']))
print('If statement: ' + str(words_0['if_statement']))
print('List: ' + str(words_0['list']))
print('Tuple: ' + str(words_0['tuple']))

'''6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output'''

for term, value in words_0.items():
    print("\nTerm: " + term)
    print("Definition: " + value)

'''6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary'''

rivers = {'nile': 'egypt',
          'mississippi': 'united states',
          'fox': 'chicago',}
for river, place in rivers.items():
    print("\n The " + river +
          " river runs through " + place)

'''6-6. Polling: Use the code in favorite_languages.py (page 104).
•	 Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.'''
print('-------------------------------------------------------')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
poll_ppl = ['jen', 'sarah', 'edward', 'phil', 'tim', 'alex']
for person in poll_ppl:
    if person in favorite_languages:
        print("Thank you for taking the poll")
    else:
        print("Please take our poll!")

'''6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person'''

people = {
    'friend_1': {'first_name': 'Tony',
                'last_name': 'Golbeck',
                'age': 18,
                'city': 'Sugar Grove'
                },
    'family_1': {'first_name': 'Ethan',
                'last_name': 'Kellum',
                'age': 21,
                'city': 'San Jose'
                },
    'friend_2': {'first_name': 'Riki',
                'last_name': 'Sanchez',
                'age': 18,
                'city': 'Aurora'
                },
}


for p, person_info in people.items():
    print("\nName: " + p)
    full_name = person_info['first_name'] + " " + person_info['last_name']
    location = person_info['city']
    age = person_info['age']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

'''6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.'''
print('---------------------------------------')
pets = {
    'pet_1': {'owner_name': 'Tony',
                'kind': 'dog',
                },
    'pet_2': {'owner_name': 'Ethan',
                'kind': 'cat',
                },
    'pet_3': {'owner_name': 'Riki',
                'kind': 'bird',
                },
}


for pet, pet_info in pets.items():
    Owner_name = pet_info['owner_name']
    Kind = pet_info['kind']

    print("\tOwner name: " + Owner_name.title())
    print("\tKind: " + Kind.title())

'''6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.'''

print('---------------------------------------')
favorite_places = {
    'person_1': {'person_name': 'Tony',
                'place': 'chicago',
                },
    'person_2': {'person_name': 'Ethan',
                'place': 'san jose',
                },
    'person_3': {'person_name': 'Riki',
                'place': 'home',
                },
}


for place, place_info in favorite_places.items():
    Person_name = place_info['person_name']
    Place = place_info['place']

    print("\tPerson name: " + Person_name.title())
    print("\tFavorite place: " + Place.title())

'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.'''
print('------------------------------------------------')
fav_num = {'josh': 176, 'riki': 3, 'sarah': 7, 'ian': 117, 'chad': 69}
print("Josh's favorite number is " + str(fav_num['josh']) + ".")
print("Riki's favorite number is " + str(fav_num['riki']) + ".")
print("Sarah's favorite number is " + str(fav_num['sarah']) + ".")
print("Ian's favorite number is " + str(fav_num['ian']) + ".")
print("Chad's favorite number is " + str(fav_num['chad']) + ".")

print("-------------------------------------------------------------------")

'''7-1. Rental Car: Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can find you
a Subaru.”'''

prompt = input('What kind of rental car would you like? ')
print("\nLet me see if I can find you a " + prompt)

'''7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready'''

guests = input('How many guests in your party? ')
guests = int(guests)

if guests >= 8:
    print("\nI'm sorry, you will have to wait for a table.")
else:
    print("\nA table is ready, please wait to be seated. ")

'''7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.'''

num = input('Please enter a number ')
num = int(num)
if num % 10 == 10:
    print("That number is a multiple of 10")
else:
    print("That number is not a multiple of 10")

'''7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.'''

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break

'''7-5. A movie theater charges different ticket prices depending on a person’s age. 
If a person is under the age of 3, the ticket is free; if they are between 3 and 12, 
the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age,
and then tel them the cost of their movie ticket.'''

prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

'''7-8. Make a list called sandwich_orders and fill it with the names of various sandwiches.
 Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders
  and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,
   move it to the list of finished sandwiches. After all the sandwiches have been made, print a message 
   listing each sandwich that was made.'''
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

'''7-10.Write a program that polls users about their dream vacation.
 Write a prompt similar to If you could visit one place in the world, 
 where would you go? Include a block of code that prints the results of the poll.'''

name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")

print('------------------------------------------------------------------------')
'''8-1.Write a function called display_message() that prints one
 sentence telling everyone what you are learning about in this chapter. 
 Call the function, and make sure the message displays correctly.'''
def display_message():
    msg = "I'm learning to store code in functions."
    print(msg)

display_message()

'''8-2.Write a function called favorite_book() that accepts one parameter,
 title. The function should print a message, such as One of my favorite
  books is Alice in Wonderland. Call the function, making sure to include
   a book title as an argument in the function call.'''

def favorite_book(title):
    print(title + " is one of my favorite books.")

favorite_book('The Grinch')

'''8-4.Modify the make_shirt() function so that shirts are large by default 
with a message that reads I love Python. Make a large shirt and a medium shirt 
with the default message, and a shirt of any size with a different message.'''

def make_shirt(size='large', message='I love Python!'):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')

'''8-6. Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this:
“Santiago, Chile”
Call your function with at least three city-country pairs, and print the value that’s returned.'''

def city_country(city, country):
    return(city.title() + ", " + country.title())

city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)

'''8-8. Start with your program from Exercise 8-7. Write a while 
loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the
 user’s input and print the dictionary that’s created. 
 Be sure to include a quit value in the while loop.'''


def make_album(artist, title, tracks=0):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")

'''8-10. Start with a copy of your program from Exercise 8-9. 
Write a function called make_great() that modifies the list of 
magicians by adding the phrase the Great to each magician’s name. 
Call show_magicians() to see that the list has actually been modified.'''

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)

'''8-12. Write a function that accepts a list of items a person 
wants on a sandwich. The function should have one parameter that
 collects as many items as the function call provides, and it should 
 print a summary of the sandiwch that is being ordered. Call the function 
 three tiems, using a different number of arguments each time.'''

def make_sandwich(*items):
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')

'''8-14. Write a function that stores information about a car in a dictionary.
 the function should always receive a manufacturer and a model name.
  It should then accept an arbitrary number of keyword arguments.
   Call the function with the required information and two other name-value pairs, 
   such as a color or an optional feature. Your function should work for a call like this one'''

def make_car(manufacturer, model, **options):
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_accord)

'''8-15. Put the functions for the example printing_models.py in a separate file called printing_functions.py.
 Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.'''


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3d print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)