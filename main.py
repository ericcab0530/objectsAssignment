class Players:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        return f"{self.playerName} - {self.playerPosition}"


class NFLTeam:
    def __init__(self, teamName, playersList):
        self.teamName = teamName
        self.playerList = playersList

    def showTeam(self):
        print(f"Team Name: {self.teamName}")
        print("Players:")
        print(self.playerList[0])
        print(self.playerList[1])
        print(self.playerList[2])
        print(self.playerList[3])

player1 = Players("Joe Montana", "QB")
player2 = Players("Barry Sanders", "RB")
player3 = Players("Jerry Rice", "WR")
player4 = Players("Graham Gano", "K")

playersList = [player1, player2, player3, player4]

team = NFLTeam("New York Giants", playersList)

team.showTeam()