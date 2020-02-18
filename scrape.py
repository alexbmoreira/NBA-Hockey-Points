import requests
from bs4 import BeautifulSoup as bs
import numpy as np

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
TEAM_FILE = open("hockey_points_team.csv", "w")
POINTS_FILE = open("hockey_points.csv", "w")

def scrape():
    team_csv_header = "games_played,team_name,opp_name,result,overtime,points\n"
    team_csv_string = ""
    points_csv_header = "games_played,team_name,points\n"
    points_csv_string = ""

    for link in URL:
        request = requests.get(link)

        if request.status_code != 200:
            print("Connection Failed -> " + link)
            continue
        
        points = 0
        gp = 0

        page = request.text
        page = bs(page, "html.parser")

        team_name = page.find("h1", {"itemprop": "name"}).span.find_next().text

        game_results = page.find_all("td", {"data-stat": "game_result"})
        teams = page.find_all("td", {"data-stat": "opp_name"})
        overtimes = np.array(page.find_all("td", {"data-stat": "overtimes"}))
        
        for i, (team, game_result, overtime) in enumerate(zip(teams, game_results, overtimes)):
            if game_result.text != "":
                gp += 1
            if (overtime.text != "") == True and game_result.text == "L":
                points += 1
            elif game_result.text == "W":
                points += 2

            team_csv_string += str(i + 1) + "," + team_name + "," + team.text + "," \
                        + game_result.text + "," + overtime.text + "," + str(points) + "\n"

        points_csv_string += str(gp) + "," + team_name + "," + str(points) + "\n"

    POINTS_FILE.write(points_csv_header + points_csv_string)
    TEAM_FILE.write(team_csv_header + team_csv_string)

scrape()
TEAM_FILE.close()
