import requests
from bs4 import BeautifulSoup as bs
import numpy as np
from team import NbaTeam

URL = ["https://www.basketball-reference.com/teams/ATL/2020_games.html", \
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

FILE = open("hockey_points.csv", "w")

def scrape():
    points_csv_header = "gp, team name, wins, losses, ot_losses, points, reg_wins\n"
    points_csv_string = ""
    teams = []

    for link in URL:
        request = requests.get(link)

        if request.status_code != 200:
            print("Connection Failed -> " + link)
            continue

        page = request.text
        page = bs(page, "html.parser")

        team = Team()
        team.name = page.find("h1", {"itemprop": "name"}).span.find_next().text
        
        game_results = page.find_all("td", {"data-stat": "game_result"})
        teams = page.find_all("td", {"data-stat": "opp_name"})
        overtimes = page.find_all("td", {"data-stat": "overtimes"})
        
        for i, (team, game_result, overtime) in enumerate(zip(teams, game_results, overtimes)):
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

            points_csv_string += str(team) + "\n"

    FILE.write(points_csv_header + points_csv_string)

scrape()
