## Dictionaries in python

programming_dictionary = {
    "Bug": "An error in a program",
    "Function": "A piece of code",
}

# Retrieveing items from  Dictionary
print(programming_dictionary["Function"])

# Adding a new item in Dictionary
programming_dictionary["Loop"] = "The action of doing somthing over and over again"

# Creating a new Dictionary
empty_dictionary = {}

# Wipe an existing Dictinary
#programming_dictionary = {}

# Edit an existing item in adictionary
programming_dictionary["Bug"] = "A moth in a computer"
print(programming_dictionary["Bug"])

# Looping a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#######Neating in a dictionary########

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Dictionary ina Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijion"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# Dictionary in a list

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijion"],
        "total_visits":12
    },
    {
        "country": "France",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5
    },
]
print(travel_log[1])
