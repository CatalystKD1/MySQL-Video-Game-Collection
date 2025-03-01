# MySQL-Video-Game-Collection
A SQL project that uses MySQL to make a database for a video game collection

This is a small project made right before a CS251 midterm. It uses Python and MySQL to create a table for a video game collection.
This project allows you to document all of the games you own by Title, System, Year and Rating.

Before running this program, there are a couple of steps you must do first:
  1. Download MySQL onto your local system: https://dev.mysql.com/downloads/mysql/
  3. Install the mysql-connector-python package using this command in your command line:

    pip install mysql-connector-python


Make sure to create a new database using the MySQL Command Line using this command:

    CREATE DATABASE video_game_db;

Note: You can replace video_game_db with any name, however you will need to change the Python code to now work with your new command.

If you download the file or copy the code, make sure to change these lines of code so the Python Program can properly link yo your MySQL account:

![image](https://github.com/user-attachments/assets/a2b6d0ae-6b5d-437e-8d77-f0be6008c43e)

Once you have changed the User, Password, Host and Databse (Password is the only required change) you can run the program!

Commands and what they do:

  ![image](https://github.com/user-attachments/assets/d9ce8e01-cbc3-4076-87e5-8511356e6e19)

  0. Print:
    The print command will print out the Title, System, Year of Release and Rating of all the games in the table

      ![image](https://github.com/user-attachments/assets/083929a1-b441-4ac8-b843-856ce90a0b83)

  2. Add:
      The add command will allow the user to add a games to their collection
     
      ![image](https://github.com/user-attachments/assets/371cd347-3567-40be-ac5b-ec79f1bf498d)
     
  3. Remove:
       This command allows the user to remove a game from their collection
     
      ![image](https://github.com/user-attachments/assets/49bb39fe-403f-4c17-8f21-a1ddfe6116f7)

  5. Update:
       This command allows the user to change data of a game, incase they inputed it incorrectly
     
      ![image](https://github.com/user-attachments/assets/47d9fc62-0706-4702-898a-301adf791397)
  
  7. Exit:
       This command allows the user to update their database changes, close MySQL and close the program

This code can be change to be a database of anything, such as: Movies, Books, Posters, Albums, Posters. I made it video games because I collect them.
I hope you like my program!


