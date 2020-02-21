class Team():

    def __init__(self):
        self.standing = 0
        self.name = ""
        self.gp = 0
        self.wins = 0
        self.losses = 0
        self.ot_losses = 0
        self.points = 0
        self.reg_wins = 0
        self.ppg = 0
    
    def __str__(self):
        #gp = str(self.gp).rjust(2, ' ')
        #name = ("'" + self.name + "'").rjust(25, ' ')
        #wins = str(self.wins).rjust(2, ' ')
        #losses = str(self.losses).rjust(2, ' ')
        #ot_losses = str(self.ot_losses).rjust(2, ' ')
        #points = str(self.points).rjust(3, ' ')
        #reg_wins = str(self.reg_wins).rjust(2, ' ')

        arr = [self.standing, self.name, self.gp, self.wins, self.losses, self.ot_losses, self.points, self.reg_wins, self.ppg]
        return ",".join(str(item) for item in arr)

    def points_per_game(self):
        self.ppg =  int(self.points / self.gp * 1000) / 1000
