people = [
    {"name" : "Kuldeep", "House":"Amava"},
    {"name" : "Khushboo", "House":"Bisanda"},
    {"name" : "Malti", "House":"Banda"}
]


people.sort(key =lambda person: person["name"])

print(people)