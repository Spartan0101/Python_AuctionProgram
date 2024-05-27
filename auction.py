#Dictionary's and Nesting

#Blind Auction
from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")
bidders = {}
should_continue = True
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n") == "yes"
    clear()

highest_bid = 0
highest_bidder = ""
for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        highest_bidder = bidder
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


'''
#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Hungary": "Budapest",
    "Bulgaria": "Sofia"
}
#Nesting a List in Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "Hungary": ["Budapest", "Debrecen", "Miskolc"],
    "Bulgaria": ["Sofia", "Plovdiv", "Varna"]
}
# Nesting Dictionary in Dictionary
travel_log2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
    "Hungary": {"cities_visited": ["Budapest", "Debrecen", "Miskolc"], "total_visits": 3},
    "Bulgaria": {"cities_visited": ["Sofia", "Plovdiv", "Varna"], "total_visits": 2}
}
#Nesting Dictionary in List
travel_log3 = [
    {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
    {"country": "Hungary", "cities_visited": ["Budapest", "Debrecen", "Miskolc"], "total_visits": 3},
    {"country": "Bulgaria", "cities_visited": ["Sofia", "Plovdiv", "Varna"], "total_visits": 2}
]
'''

'''
print("Secret Auction")
prog_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}
#Retriving Values
print(prog_dictionary["Bug"])
#Adding values
prog_dictionary["Loop"] = "The action of doing something over and over again."
#Editing values
prog_dictionary["Bug"] = "A moth in your computer."
print(prog_dictionary)
#Wipe dictionary
prog_dictionary = {}
#Looping through dictionary
for key in prog_dictionary:
    print(key)
    print(prog_dictionary[key])
'''

'''
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
        student_grades[student] = "Exceeds Expectations"
  elif score > 70:
        student_grades[student] = "Acceptable"
  else:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
'''