import requests
from bs4 import BeautifulSoup as bs
import numpy as np
from team import Team
from operator import attrgetter

def scrape(url):
    points_csv_header = "gp, team name, wins, losses, ot_losses, points, reg_wins\n"
    points_csv_string = ""
    teams = []

    for link in url:
        request = requests.get(link)

        if request.status_code != 200:
            print("Connection Failed -> " + link)
            continue

        page = request.text
        page = bs(page, "html.parser")

        team = Team()
        team.name = page.find("h1", {"itemprop": "name"}).span.find_next().text
        
        game_results = page.find_all("td", {"data-stat": "game_result"})
        overtimes = page.find_all("td", {"data-stat": "overtimes"})
        
        for i, (game_result, overtime) in enumerate(zip(game_results, overtimes)):
            if game_result.text != "":
                team.gp += 1
            
            if game_result.text == "L":
                if overtime.text != "":
                    team.points += 1
                    team.ot_losses += 1
                else:
                    team.losses += 1
            elif game_result.text == "W":
                team.points += 2
                team.wins += 1
                if overtime.text == "":
                    team.reg_wins += 1

        teams.append(team)

    return teams

def compare(team_a, team_b):
    if team_a.points != team_b.points:
        return team_a.points - team_b.points
    else:
        if team_a.gp != team_b.gp:
            return team_b.gp - team_a.gp
        else:
            return team_a.reg_wins - team_b.reg_wins

def sort(teams):
    s = sorted(teams, key = attrgetter("points"), reverse = True)
    s = sorted(s, key = attrgetter("gp"))
    return sorted(s, key = attrgetter("reg_wins"), reverse = True)

if __name__ == "__main__":
    url = ["https://www.basketball-reference.com/teams/ATL/2020_games.html", \
       "https://www.basketball-reference.com/teams/BOS/2020_games.html", \
       "https://www.basketball-reference.com/teams/BRK/2020_games.html", \
       "https://www.basketball-reference.com/teams/CHO/2020_games.html", \
       "https://www.basketball-reference.com/teams/CHI/2020_games.html", \
       "https://www.basketball-reference.com/teams/CLE/2020_games.html", \
       "https://www.basketball-reference.com/teams/DAL/2020_games.html", \
       "https://www.basketball-reference.com/teams/DEN/2020_games.html", \
       "https://www.basketball-reference.com/teams/DET/2020_games.html", \
       "https://www.basketball-reference.com/teams/GSW/2020_games.html", \
       "https://www.basketball-reference.com/teams/HOU/2020_games.html", \
       "https://www.basketball-reference.com/teams/IND/2020_games.html", \
       "https://www.basketball-reference.com/teams/LAC/2020_games.html", \
       "https://www.basketball-reference.com/teams/LAL/2020_games.html", \
       "https://www.basketball-reference.com/teams/MEM/2020_games.html", \
       "https://www.basketball-reference.com/teams/MIA/2020_games.html", \
       "https://www.basketball-reference.com/teams/MIL/2020_games.html", \
       "https://www.basketball-reference.com/teams/MIN/2020_games.html", \
       "https://www.basketball-reference.com/teams/NOP/2020_games.html", \
       "https://www.basketball-reference.com/teams/NYK/2020_games.html", \
       "https://www.basketball-reference.com/teams/OKC/2020_games.html", \
       "https://www.basketball-reference.com/teams/ORL/2020_games.html", \
       "https://www.basketball-reference.com/teams/PHI/2020_games.html", \
       "https://www.basketball-reference.com/teams/PHO/2020_games.html", \
       "https://www.basketball-reference.com/teams/POR/2020_games.html", \
       "https://www.basketball-reference.com/teams/SAC/2020_games.html", \
       "https://www.basketball-reference.com/teams/SAS/2020_games.html", \
       "https://www.basketball-reference.com/teams/TOR/2020_games.html", \
       "https://www.basketball-reference.com/teams/UTA/2020_games.html", \
       "https://www.basketball-reference.com/teams/WAS/2020_games.html", \
       ]
    file = open("hockey_points.csv", "w")
    string = ""
    teams = sort(scrape(url))
    for team in teams:
        string += str(team) + "\n"
    file.write(string)
    file.close()
