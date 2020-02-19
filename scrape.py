import requests
from bs4 import BeautifulSoup as bs
import numpy as np
from team import Team
from operator import attrgetter

def nba_scrape(url):
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

def nhl_scrape(url):
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
        
        game_results = page.find_all("td", {"data-stat": "game_outcome"})
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

def sort(teams):
    s = sorted(teams, key = attrgetter("reg_wins"), reverse = True)
    s = sorted(s, key = attrgetter("gp"))
    return sorted(s, key = attrgetter("points"), reverse = True)

if __name__ == "__main__":
    nba_url = ["https://www.basketball-reference.com/teams/ATL/2020_games.html", \
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
    nhl_url = ["https://www.hockey-reference.com/teams/ANA/2020_games.html", \
               "https://www.hockey-reference.com/teams/ARI/2020_games.html", \
               "https://www.hockey-reference.com/teams/BOS/2020_games.html", \
               "https://www.hockey-reference.com/teams/BUF/2020_games.html", \
               "https://www.hockey-reference.com/teams/CGY/2020_games.html", \
               "https://www.hockey-reference.com/teams/CAR/2020_games.html", \
               "https://www.hockey-reference.com/teams/CHI/2020_games.html", \
               "https://www.hockey-reference.com/teams/COL/2020_games.html", \
               "https://www.hockey-reference.com/teams/CBJ/2020_games.html", \
               "https://www.hockey-reference.com/teams/DAL/2020_games.html", \
               "https://www.hockey-reference.com/teams/DET/2020_games.html", \
               "https://www.hockey-reference.com/teams/EDM/2020_games.html", \
               "https://www.hockey-reference.com/teams/FLA/2020_games.html", \
               "https://www.hockey-reference.com/teams/LAK/2020_games.html", \
               "https://www.hockey-reference.com/teams/MIN/2020_games.html", \
               "https://www.hockey-reference.com/teams/MTL/2020_games.html", \
               "https://www.hockey-reference.com/teams/NSH/2020_games.html", \
               "https://www.hockey-reference.com/teams/NJD/2020_games.html", \
               "https://www.hockey-reference.com/teams/NYI/2020_games.html", \
               "https://www.hockey-reference.com/teams/NYR/2020_games.html", \
               "https://www.hockey-reference.com/teams/OTT/2020_games.html", \
               "https://www.hockey-reference.com/teams/PHI/2020_games.html", \
               "https://www.hockey-reference.com/teams/PIT/2020_games.html", \
               "https://www.hockey-reference.com/teams/SJS/2020_games.html", \
               "https://www.hockey-reference.com/teams/STL/2020_games.html", \
               "https://www.hockey-reference.com/teams/TBL/2020_games.html", \
               "https://www.hockey-reference.com/teams/TOR/2020_games.html", \
               "https://www.hockey-reference.com/teams/VAN/2020_games.html", \
               "https://www.hockey-reference.com/teams/VEG/2020_games.html", \
               "https://www.hockey-reference.com/teams/WSH/2020_games.html", \
               "https://www.hockey-reference.com/teams/WPG/2020_games.html", \
               ]
    file = open("hockey_points.csv", "w")
    points_csv_header = "gp, team name, wins, losses, ot_losses, points, reg_wins\n"
    points_csv_string = ""

    teams = nhl_scrape(nhl_url)
    teams.extend(nba_scrape(nba_url))
    teams = sort(teams)
    for team in teams:
        points_csv_string += str(team) + "\n"
    file.write(points_csv_header + points_csv_string)
    file.close()
