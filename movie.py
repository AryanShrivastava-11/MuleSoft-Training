import sqlite3

# Connect to the database
db = sqlite3.connect('Movies.db')
cursor = db.cursor()

movies = [
    {'title': 'Spider-Man: No Way Home', 'year': 2021, 'director': 'Jon Watts', 'actor': 'Tom Holland', 'actress': 'Zendaya'},
    {'title': 'Avengers: Endgame', 'year': 2018, 'director': 'Anthony Russo', 'actor': 'Robert Downey Jr', 'actress': 'Scarlett Johansson'},
    {'title': 'Avengers: Infinity War', 'year': 2018, 'director': 'Anthony Russo', 'actor': 'Robert Downey Jr', 'actress': 'Scarlett Johansson'},
    {'title': 'Iron Man 3', 'year': 2013, 'director': 'Shane Black', 'actor': 'Robert Downey Jr', 'actress': 'Gwyneth Paltrow'},
    {'title': 'Avengers: Age of Ultron', 'year': 2015, 'director': 'Anthony Russo', 'actor': 'Robert Downey Jr', 'actress': 'Scarlett Johansson'}
]

# Create table
cursor.execute("CREATE TABLE Movies1 (title VARCHAR(60), actor VARCHAR(24), actress VARCHAR(24), year INT(4), director VARCHAR(24));")

# Insert data
for movie in movies:
    cursor.execute(f"INSERT INTO Movies1 VALUES (\'{movie['title']}\', \'{movie['actor']}\', \'{movie['actress']}\', {movie['year']}, \'{movie['director']}\');")

# Select data
print("\nSelecting all movies:")
cursor.execute("SELECT * FROM Movies1;")
for i in cursor.fetchall():
    print(i)
print("\n")

# Select all movies with the actor 'Robert Downey Jr'
print("Select all movies with the actor 'Robert Downey Jr':")
cursor.execute("SELECT title, year, director FROM Movies1 WHERE actor='Robert Downey Jr';")
for i in cursor.fetchall():
    print(i)
print("\n")