import os
import mysql.connector

# Function that I found online to cleare the screen. Makes the command line nicer
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function that prints all of the data stored in your database
def printGame():
    cursor.execute("SELECT * FROM video_games;")
    games = cursor.fetchall()
    
    if games:
        print("\nVideo Game Collection:")
        print("-" * 50)
        for game in games:
            print(f"{game[1]} ({game[2]}) | Year: {game[3]} | Rating: {game[4]}")
        print("-" * 50)
    else:
        print("No games found!")
    a = input()
    clear_screen()

# Function that adds games into your data base. The user will input data and change the SQL table
def addGame():
    title = input("Enter game title: ")
    platform = input("Enter platform: ")
    release_year = input("Enter release year: ")
    rating = input("Enter rating: ")

    try:
        cursor.execute('''
            INSERT INTO video_games (title, platform, release_year, rating)
            VALUES (%s, %s, %s, %s);
        ''', (title, platform, release_year, rating))
        conn.commit()
        print(f"{title} added successfully!")
    except mysql.connector.errors.IntegrityError:
        print("This game already exists in the database.")
    a = input()
    clear_screen()

# Function that removes games from the table. Allows users to manipulate data and removes data
def removeGame():
    title = input("Enter the title of the game to remove: ")
    platform = input("Enter the platform: ")

    cursor.execute('''
        DELETE FROM video_games WHERE title = %s AND platform = %s;
    ''', (title, platform))
    
    if cursor.rowcount > 0:
        conn.commit()
        print(f"{title} removed successfully!")
    else:
        print("Game not found!")
    a = input()
    clear_screen()

# Function that changes data stores in the table. Allows users to manupulate and change data in the table
def updateGame():
    title = input("Enter the title of the game to update: ")
    platform = input("Enter the platform: ")

    cursor.execute('''
        SELECT * FROM video_games WHERE title = %s AND platform = %s;
    ''', (title, platform))
    
    if cursor.fetchone():
        new_title = input("Enter new title (or press Enter to skip): ")
        new_platform = input("Enter new platform (or press Enter to skip): ")
        new_year = input("Enter new release year (or press Enter to skip): ")
        new_rating = input("Enter new rating (or press Enter to skip): ")

        if new_title or new_platform:
            try:
                if not new_title:
                    new_title = title
                if not new_platform:
                    new_platform = platform
                
                cursor.execute('''
                    UPDATE video_games 
                    SET title = %s, platform = %s 
                    WHERE title = %s AND platform = %s;
                ''', (new_title, new_platform, title, platform))
                
                title, platform = new_title, new_platform  # Update reference for next queries
            except mysql.connector.errors.IntegrityError:
                print("A game with this title and platform already exists!")
                return

        if new_year:
            cursor.execute('''
                UPDATE video_games SET release_year = %s WHERE title = %s AND platform = %s;
            ''', (new_year, title, platform))

        if new_rating:
            cursor.execute('''
                UPDATE video_games SET rating = %s WHERE title = %s AND platform = %s;
            ''', (new_rating, title, platform))

        conn.commit()
        print(f"{title} updated successfully!")
    else:
        print("Game not found!")
    a = input()
    clear_screen()

# The Main function of the program starts here

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost", # Replace with your host (localhost by default)
    user="root", # Replace with your user (root by default)
    password="-----", # Replace this with your password
    database="video_game_db" # Replace this with your database
)

cursor = conn.cursor()

# Creates a table if there is none already created
cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS video_games (
               id INT AUTO_INCREMENT PRIMARY KEY,
               title VARCHAR(100) NOT NULL,
               platform VARCHAR(50) NOT NULL,
               release_year INT,
               rating FLOAT
               );
               ''')

loop = True
clear_screen()

while(loop) :
    # Command line interface for user inputs
    print("Here are your actions:")
    print("0. Show Table")
    print("1. Add")
    print("2. Remove")
    print("3. Update")
    print("4. Exit")

    action = input("What would you like to do: ")
    if isinstance(action, str):  # Ensure i is a string
        action = action.lower()  # Convert to lowercase
    
    # Switch satements for each user
    match action:
        case "show table" :
            printGame()
        case "0" :
            printGame()

        case "add" :
            print()
            addGame()
        case "1" :
            print()
            addGame()

        case "remove" :
            print()
            removeGame()
        case "2" :
            print()
            removeGame()

        case "update" :
            print()
            updateGame()
        case "3" :
            print()
            updateGame()

        case "exit" :
            print()
            loop = False
        case "4" :
            print()
            loop = False
        case _ : 
            print("That is not a valid command. Either write a valid number or command name.")
            a = input()
            clear_screen()

# Commits changes that the users made
conn.commit()

# Closes the MySQL
conn.close()
