UPDATE player 
SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' 
WHERE first_name = 'Smeagol':| 
DELETE FROM player WHERE first_name = 'Smeagol';
 INSERT INTO player (first_name, last_name, team_id) 
 VALUES ('Smeagol', 'Shire Folk', 1); 
INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1); -- 
DISPLAYING PLAYERS AFTER INSERT 
Player ID: 1 First Name: Thorin Last Name: Oakenshield Team Name: Team Gandalf 
Player ID: 2 First Name: Bilbo Last Name: Baggins Team Name: Team Gandalf 
Player ID: 3 First Name: Frodo Last Name: Baggins Team Name: Team Gandalf 
Player ID: 4 First Name: Saruman Last Name: The White Team Name: Team Sauron 
Player ID: 5 First Name: Angmar Last Name: Witch-king Team Name: Team Sauron 
Player ID: 6 First Name: Azog Last Name: The Defiler Team Name: Team Sauron 
Player ID: 21 First Name: Smeagol Last Name: Shire Folk Team Name: Team Gandalf 
DISPLAYING PLAYERS AFTER UPDATE 
Player ID: 1 First Name: Thorin Last Name: Oakenshield Team Name: Team Gandalf 
Player ID: 2 First Name: Bilbo Last Name: Baggins Team Name: Team Gandalf 
Player ID: 3 First Name: Frodo Last Name: Baggins Team Name: Team Gandalf 
Player ID: 4 First Name: Saruman Last Name: The White Team Name: Team Sauron Player ID: 5 First Name: Angmar Last Name: Witch-king Team Name: Team Sauron 
Player ID: 6 First Name: Azog Last Name: The Defiler Team Name: Team Sauron 
Player ID: 21 First Name: Gollum Last Name: Ring Stealer Team Name: Team Sauron 
DISPLAYING PLAYERS AFTER DELETE 
Player ID: 1 First Name: Thorin Last Name: Oakenshield Team Name: Team Gandalf
 Player ID: 2 First Name: Bilbo Last Name: Baggins Team Name: Team Gandalf Player ID: 3 First Name: Frodo Last Name: Baggins Team Name: Team Gandalf 
Player ID: 4 First Name: Saruman Last Name: The White Team Name: Team Sauron 
Player ID: 5 First Name: Angmar Last Name: Witch-king Team Name: Team Sauron 
Player ID: 6 First Name: Azog Last Name: The Defiler Team Name: Team Sauron Press any key to continue...
