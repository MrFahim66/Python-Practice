SectionC = ['player1', 'player2', 'player3', 'player4', 'player5']
SectionD = ['player6', 'player7', 'player8', 'player9', 'player10']
SectionE = ['player11', 'player12', 'player13', 'player14', 'player15']
SectionG = ['player16', 'player17', 'player18', 'player19', 'player20']

Team1 = SectionC + SectionD  # Merging 2 lists for team
Team2 = SectionE + SectionG  # Merging 2 lists for team

Team1.pop(-1)  # popping the last element from the list
Team2.pop(-1)  # popping the last element from the list

# Last digit of ID : 4 , index = 4
index = 4

Team1.insert(index, 'NewPlayer1')  # inserting new element to index
Team2.insert(index, 'NewPlayer2')  # inserting new element to index

# printing final lists
print("Modified Teams Are As Followed: ")
print("Team 1:\t", Team1)
print("Team 2:\t", Team2)
