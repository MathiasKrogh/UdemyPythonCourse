my_favourites = {
    "Soda": "Pepsi Twist",
    "Crisps": "Doritos Sweet Chili Pepper"
}

#Get item for dictionary
print(my_favourites["Soda"])

#Add item to dictionary
my_favourites["Noodle"] = "Mama Shrimp"
print(my_favourites)

#Create empty dictionary or clear an existing
empty_dictionary = {}

#Loop through dictionary
for key in my_favourites:
    print(key)
    print(my_favourites[key])

#Nesting list in dictionary
travel_log = {
    "Denmark": ["København", "Aarhus"],
    "Germany": ["Flensburg", "Berlin"]
}

#Nesting dictionary in dictionary
food_list = {
    "noodles": {
        "Mama Shrimp": 3,
        "Yum Yum Shrimp": 28
    }
}

my_list = [
    {
        "country": "Denmark", 
        "cities_visited": ["Aarhus", "Copenhagen"],
        "total_visits": 93
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visits": 21
    }
]