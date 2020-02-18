import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import json

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

for link in url:
    request = requests.get(link)

    if request.status_code != 200:
        print("Connection Failed -> " + link)
        continue
    
    csv_string = "games_played,team_name,opp_name,result,overtime,points\n"
    points = 0

    page = request.text
    page = bs(page, "html.parser")

    team_name = page.find("h1", {"itemprop": "name"}).span.find_next().text

    game_results = page.find_all("td", {"data-stat": "game_result"})
    teams = page.find_all("td", {"data-stat": "opp_name"})
    overtime = np.array(page.find_all("td", {"data-stat": "overtimes"}))
    
    for i in range(len(teams)):
        if (overtime[i].text != "") == True and game_results[i].text == "L":
            points += 1
        elif game_results[i].text == "W":
            points += 2

        csv_string += str(i) + "," + team_name + "," + teams[i].text + "," \
                    + game_results[i].text + "," + overtime[i].text + "," + str(points) + "\n"

    file.write(csv_string)

file.close()