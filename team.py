class NbaTeam():

    def __init__(self):
        self.gp = 0
        self.name = ""
        self.wins = 0
        self.losses = 0
        self.ot_losses = 0
        self.points = 0
        self.reg_wins = 0
    
    def __str__(self):
        arr = [self.gp, self.name, self.wins, self.losses, self.ot_losses, self.points, self.reg_wins]
        return ",".join(arr)

    def calc_points(self):
        return self.wins * 2 + self.ot_losses