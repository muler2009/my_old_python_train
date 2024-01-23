movies = {
    "name": "Body of lies",
    "date": 2008,
    "mainacator": "Matti Damon",
    "income": 200
}

print(type(movies))
print(len(movies))
print(isinstance(movies, dict))

# Accessig the values 
print(movies['name'])
print(movies['date'])
print(movies.get('name'))

print(movies.keys()) # to get the keys of the dict
print(movies.values()) # to get the values of the dict

print(movies.items()) # key value pair

# changing the value
movies["mainacator"] = "Lenonardo decarpyo" 
print(movies)

movies.update({"name": "Inspection", "firend": 'Rose'})
print(f"Moveis :\n {movies}")

print(f"{movies.popitem()}")
print(movies)

# copying
movies2 = movies.copy()
movies2.update({"age": 57})
print(f"Original movies dict: {movies}")
print(f"Copied movies dict: {movies2}")

# nested dictionaries and how to access it 
movies4 = {
    "action" : {
        "name": "Bourne Ultimetum",
        "relese_date": 2007,
        "actor": "Matti Damn"
    },
    "love" : {
        "name": "The Vow",
        "relese_date": 2005,
        "actor": "Ketty perry"
    },
    "adventure" : {
        "name": "The scorpion ling",
        "relese_date": 1999,
        "actor": "Jason Damn"
    }
    
}
# movies3 = {
#     "action": action,
#     "love": love,
#     "adventure": adventure
# }

print(movies4["action"].get("name"))
print(movies4["action"].keys())
 